# Imersão Alura com Inteligência Artificial

## 📚 Desafio 3: Criando uma lista de tarefas com o Google Antigravity

### Enunciado do Desafio

> *Depois de compreender, modificar e testar códigos, chegou a hora de construir uma nova aplicação! O desafio é usar o Google Antigravity para desenvolver uma lista de tarefas (To-Do List) simples, com interface visual, que permita acompanhar atividades pendentes e concluídas.*
>
> *A aplicação deve ter três funcionalidades:*
> 1. *Adicionar tarefas: digitar uma atividade e incluí-la na lista.*
> 2. *Marcar tarefas como concluídas: identificar as atividades já realizadas.*
> 3. *Remover tarefas: excluir atividades que não são mais necessárias.*
>
> *Depois, execute o projeto para experimentar as funcionalidades e observe como a aplicação organiza as informações e como os componentes do código trabalham juntos.*
>
> *Dica: Solicite a melhoria para que as tarefas concluídas apareçam visualmente diferentes das pendentes e peça ao Antigravity para executar os testes necessários.*

---

## 💻 Sobre a Solução Desenvolvida

Para este desafio, desenvolvemos uma solução completa que conta com duas opções de interface visual simples e intuitivas:

1. **Aplicação Web (Padrão):** Desenvolvida em HTML5 semântico, CSS3 moderno e JavaScript puro (`index.html`, `style.css`, `app.js`, `todo_core.js`). Roda diretamente em qualquer navegador com duplo clique, persistindo os dados em `localStorage`.
2. **Aplicação Desktop Nativa (Python Tkinter):** Desenvolvida em Python com Tkinter (`app_desktop.py`), permitindo executar uma janela gráfica nativa no sistema operacional.

---

## ✨ Funcionalidades Principais Implementadas

### 1. Adicionar Tarefas
- Campo de digitação com botão interativo e atalho via tecla `Enter`.
- Validação defensiva: impede o cadastro de tarefas vazias ou formadas apenas por espaços em branco.

### 2. Marcar Tarefas como Concluídas (com Distinção Visual)
Conforme solicitado na dica do desafio, tarefas concluídas recebem um tratamento visual claramente diferenciado das pendentes:
- **Texto riscado (*line-through / overstrike*).**
- **Cor atenuada e opacidade reduzida.**
- **Checkbox com indicador verde ativo (ícone de verificado).**
- **Selo/Badge visual verde `"Concluída"` ao lado do texto.**
- Alternância instantânea ao clicar no checkbox ou no próprio texto.

### 3. Remover Tarefas
- Botão de exclusão (ícone de lixeira) para cada item individual.
- Botão auxiliar para "Limpar Concluídas" de uma só vez.

### 4. Recursos Adicionais
- **Filtros de visualização:** Todas, Pendentes e Concluídas.
- **Contadores em tempo real:** exibem a quantidade exata de tarefas em cada estado.
- **Persistência de Dados:** As tarefas permanecem salvas mesmo após fechar ou recarregar a janela.

---

## 📂 Arquivos do Desafio 3

```text
Desafio3/
├── index.html                   # Interface web semântica e acessível
├── style.css                    # Estilos modernos, responsivos e distinção visual
├── app.js                       # Manipulação do DOM, eventos e persistência
├── todo_core.js                 # Módulo de regras de negócio desacoplado
├── test_todo.js                 # 9 testes automatizados com Node.js Test Runner
├── app_desktop.py               # Versão Desktop gráfica nativa em Python (Tkinter)
├── README.md                    # Documentação principal do desafio
├── TESTES.md                    # Matriz de testes e plano de qualidade
├── RELATORIO_VERIFICACAO.md     # Logs de execução e evidências dos testes
├── ARQUITETURA_E_EXPLICACAO.md  # Análise arquitetural e fluxo de componentes
└── .gitignore
```

---

## 🚀 Como Executar

### Opção A: Executar a Versão Web (Recomendado)
Basta abrir o arquivo [`index.html`](./index.html) no seu navegador preferido (Google Chrome, Edge, etc.) dando duplo clique nele, ou pelo terminal:

```powershell
start index.html
```

### Opção B: Executar a Versão Desktop em Python
```powershell
python app_desktop.py
```

### Opção C: Rodar a Suíte de Testes Automatizados
```powershell
node --test test_todo.js
```

---

## 🧪 Resumo dos Testes e Validações

A lógica de negócios da aplicação foi isolada em `todo_core.js` e validada por uma suíte de 9 testes unitários automatizados em `test_todo.js`, cobrindo 100% dos requisitos do desafio:
- ✅ Adição de tarefas com estado pendente inicial.
- ✅ Rejeição de tarefas em branco ou inválidas.
- ✅ Marcação e alternância de conclusão.
- ✅ Remoção de tarefas pelo identificador único.
- ✅ Filtros dinâmicos e contadores estatísticos.

Consulte o arquivo [`TESTES.md`](./TESTES.md) e [`RELATORIO_VERIFICACAO.md`](./RELATORIO_VERIFICACAO.md) para detalhes dos testes.

---

## 👤 Autor

Desenvolvido por **Armando Patrício** ([@ArmandoFilho483](https://github.com/ArmandoFilho483))  
Participante da **Imersão Alura com Inteligência Artificial** com apoio do **Google Antigravity**.
