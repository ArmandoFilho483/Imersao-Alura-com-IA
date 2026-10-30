/**
 * Módulo de Regras de Negócio da Lista de Tarefas (To-Do List)
 * Desafio 3 - Imersão Alura com IA & Google Antigravity
 */

class GerenciadorTarefas {
  constructor(tarefasIniciais = []) {
    this.tarefas = [...tarefasIniciais];
  }

  /**
   * Adiciona uma nova tarefa à lista.
   * Valida se o texto não está vazio ou composto apenas de espaços.
   */
  adicionarTarefa(texto) {
    if (texto === undefined || texto === null || typeof texto !== 'string') {
      throw new Error('O texto da tarefa é obrigatório.');
    }

    const textoFormatado = texto.trim();
    if (textoFormatado.length === 0) {
      throw new Error('A tarefa não pode estar vazia.');
    }

    const novaTarefa = {
      id: Date.now().toString() + Math.random().toString(36).substring(2, 7),
      texto: textoFormatado,
      concluida: false,
      criadaEm: new Date().toISOString()
    };

    this.tarefas.push(novaTarefa);
    return novaTarefa;
  }

  /**
   * Alterna o estado de conclusão de uma tarefa (pendente <-> concluída).
   */
  alternarConclusao(id) {
    const tarefa = this.tarefas.find(t => t.id === id);
    if (!tarefa) {
      throw new Error(`Tarefa com ID ${id} não encontrada.`);
    }

    tarefa.concluida = !tarefa.concluida;
    return tarefa;
  }

  /**
   * Remove uma tarefa da lista pelo ID.
   */
  removerTarefa(id) {
    const indice = this.tarefas.findIndex(t => t.id === id);
    if (indice === -1) {
      throw new Error(`Tarefa com ID ${id} não encontrada.`);
    }

    const [removida] = this.tarefas.splice(indice, 1);
    return removida;
  }

  /**
   * Filtra tarefas por status ('todas', 'pendentes', 'concluidas').
   */
  filtrarTarefas(filtro = 'todas') {
    switch (filtro) {
      case 'pendentes':
        return this.tarefas.filter(t => !t.concluida);
      case 'concluidas':
        return this.tarefas.filter(t => t.concluida);
      case 'todas':
      default:
        return [...this.tarefas];
    }
  }

  /**
   * Retorna estatísticas da lista de tarefas.
   */
  obterEstatisticas() {
    const total = this.tarefas.length;
    const concluidas = this.tarefas.filter(t => t.concluida).length;
    const pendentes = total - concluidas;
    return { total, concluidas, pendentes };
  }
}

// Suporte tanto para módulos CommonJS/Node quanto navegador global
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { GerenciadorTarefas };
}
