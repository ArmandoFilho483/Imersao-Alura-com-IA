/**
 * Controlador de Interface da Lista de Tarefas (DOM & Eventos)
 * Desafio 3 - Imersão Alura com IA & Google Antigravity
 */

// Chave para persistência no localStorage
const STORAGE_KEY = 'imersao_alura_todo_tasks';

// Inicializa o gerenciador com dados salvos no localStorage (se houver)
function carregarTarefasSalvas() {
  try {
    const dados = localStorage.getItem(STORAGE_KEY);
    return dados ? JSON.parse(dados) : [];
  } catch (erro) {
    console.error('Erro ao ler tarefas do localStorage:', erro);
    return [];
  }
}

function salvarTarefas(tarefas) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tarefas));
  } catch (erro) {
    console.error('Erro ao salvar tarefas no localStorage:', erro);
  }
}

// Instância do Gerenciador de Tarefas
const gerenciador = new GerenciadorTarefas(carregarTarefasSalvas());

// Estado de filtro ativo: 'todas' | 'pendentes' | 'concluidas'
let filtroAtual = 'todas';

// Elementos do DOM
const formTarefa = document.getElementById('form-tarefa');
const inputTarefa = document.getElementById('input-tarefa');
const mensagemValidacao = document.getElementById('mensagem-validacao');
const listaTarefas = document.getElementById('lista-tarefas');
const estadoVazio = document.getElementById('estado-vazio');
const countTodas = document.getElementById('count-todas');
const countPendentes = document.getElementById('count-pendentes');
const countConcluidas = document.getElementById('count-concluidas');
const botoesFiltro = document.querySelectorAll('.filter-btn');
const btnLimparConcluidas = document.getElementById('btn-limpar-concluidas');

/**
 * Atualiza os contadores numéricos de tarefas.
 */
function atualizarContadores() {
  const stats = gerenciador.obterEstatisticas();
  countTodas.textContent = stats.total;
  countPendentes.textContent = stats.pendentes;
  countConcluidas.textContent = stats.concluidas;
}

/**
 * Renderiza a lista de tarefas no DOM de acordo com o filtro selecionado.
 */
function renderizarTarefas() {
  const tarefasFiltradas = gerenciador.filtrarTarefas(filtroAtual);
  listaTarefas.innerHTML = '';

  if (tarefasFiltradas.length === 0) {
    estadoVazio.classList.remove('hidden');
  } else {
    estadoVazio.classList.add('hidden');

    tarefasFiltradas.forEach(tarefa => {
      const li = document.createElement('li');
      li.className = `task-item ${tarefa.concluida ? 'completed' : ''}`;
      li.dataset.id = tarefa.id;

      li.innerHTML = `
        <div class="task-left">
          <button 
            type="button" 
            class="custom-checkbox" 
            aria-label="${tarefa.concluida ? 'Marcar como pendente' : 'Marcar como concluída'}"
            title="${tarefa.concluida ? 'Marcar como pendente' : 'Marcar como concluída'}"
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </button>
          <span class="task-text">${escaparHTML(tarefa.texto)}</span>
          ${tarefa.concluida ? '<span class="status-badge">Concluída</span>' : ''}
        </div>
        <button 
          type="button" 
          class="btn-delete" 
          aria-label="Excluir tarefa" 
          title="Excluir tarefa"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="3 6 5 6 21 6"></polyline>
            <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            <line x1="10" y1="11" x2="10" y2="17"></line>
            <line x1="14" y1="11" x2="14" y2="17"></line>
          </svg>
        </button>
      `;

      // Evento de concluir/alternar ao clicar no checkbox ou texto
      const btnCheck = li.querySelector('.custom-checkbox');
      const taskText = li.querySelector('.task-text');
      
      const toggle = () => {
        gerenciador.alternarConclusao(tarefa.id);
        salvarTarefas(gerenciador.tarefas);
        renderizarTarefas();
        atualizarContadores();
      };

      btnCheck.addEventListener('click', toggle);
      taskText.addEventListener('click', toggle);

      // Evento de remover ao clicar no botão de lixeira
      const btnDelete = li.querySelector('.btn-delete');
      btnDelete.addEventListener('click', () => {
        gerenciador.removerTarefa(tarefa.id);
        salvarTarefas(gerenciador.tarefas);
        renderizarTarefas();
        atualizarContadores();
      });

      listaTarefas.appendChild(li);
    });
  }

  atualizarContadores();
}

/**
 * Função utilitária para evitar injeções de script (XSS).
 */
function escaparHTML(texto) {
  const div = document.createElement('div');
  div.textContent = texto;
  return div.innerHTML;
}

// 1. Evento de Adicionar Tarefa pelo Formulário
formTarefa.addEventListener('submit', (e) => {
  e.preventDefault();
  mensagemValidacao.textContent = '';

  try {
    const texto = inputTarefa.value;
    gerenciador.adicionarTarefa(texto);
    salvarTarefas(gerenciador.tarefas);
    
    inputTarefa.value = '';
    inputTarefa.focus();
    renderizarTarefas();
  } catch (erro) {
    mensagemValidacao.textContent = erro.message;
  }
});

// Limpa mensagem de validação ao digitar
inputTarefa.addEventListener('input', () => {
  if (mensagemValidacao.textContent) {
    mensagemValidacao.textContent = '';
  }
});

// 2. Eventos dos Filtros de Visualização
botoesFiltro.forEach(btn => {
  btn.addEventListener('click', () => {
    botoesFiltro.forEach(b => {
      b.classList.remove('active');
      b.setAttribute('aria-selected', 'false');
    });
    btn.classList.add('active');
    btn.setAttribute('aria-selected', 'true');

    filtroAtual = btn.dataset.filter;
    renderizarTarefas();
  });
});

// 3. Evento para Limpar Tarefas Concluídas
btnLimparConcluidas.addEventListener('click', () => {
  const concluidas = gerenciador.filtrarTarefas('concluidas');
  if (concluidas.length === 0) return;

  concluidas.forEach(t => gerenciador.removerTarefa(t.id));
  salvarTarefas(gerenciador.tarefas);
  renderizarTarefas();
});

// Inicialização da tela ao carregar o script
renderizarTarefas();
