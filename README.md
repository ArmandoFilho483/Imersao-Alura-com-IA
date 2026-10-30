# 🚀 Imersão Alura com Inteligência Artificial

Bem-vindo ao repositório oficial das atividades e desafios desenvolvidos durante a **Imersão Alura com IA**. Este projeto reúne a criação, evolução e documentação técnica de aplicações desenvolvidas em parceria com Inteligência Artificial Generativa (**Google AI Studio** e **Google Antigravity**).

---

## 📂 Estrutura do Repositório

```text
Imersao-Alura-com-IA/
│
├── Desafio1/                         # 📚 Desafio 1: Criando sua primeira aplicação com IA
│   ├── calculadora.py                # Calculadora em terminal com as 4 operações básicas
│   ├── README.md                     # Documentação com respostas às perguntas do Desafio 1
│   ├── TESTES.md                     # Matriz de testes manuais e casos de borda
│   └── .gitignore
│
├── Desafio2/                         # 📚 Desafio 2: Evoluindo a aplicação com Google Antigravity
│   ├── calculadora.py                # Calculadora expandida com cálculo de porcentagem (%)
│   ├── test_calculadora.py           # 9 testes unitários automatizados com unittest
│   ├── README.md                     # Documentação da evolução e atividades do Desafio 2
│   ├── TESTES.md                     # Plano de testes e matriz de rastreabilidade
│   ├── RELATORIO_VERIFICACAO.md      # Evidências de execução e logs dos testes automatizados
│   ├── ARQUITETURA_E_EVOLUCAO.md     # Análise de engenharia de software e diagramas de fluxo
│   └── .gitignore
│
├── Desafio3/                         # 📚 Desafio 3: Criando uma Lista de Tarefas com Google Antigravity
│   ├── index.html                    # Interface Web semântica e responsiva
│   ├── style.css                     # Estilos, distinção visual e efeito tachado
│   ├── app.js                        # Controlador de interface e persistência localStorage
│   ├── todo_core.js                  # Lógica de negócio e regras de domínio desacopladas
│   ├── test_todo.js                  # 9 testes unitários automatizados com Node.js
│   ├── app_desktop.py                # Versão desktop gráfica nativa em Python (Tkinter)
│   ├── README.md                     # Documentação e relatório do Desafio 3
│   ├── TESTES.md                     # Plano de testes e matriz de requisitos
│   ├── RELATORIO_VERIFICACAO.md      # Evidências de execução e logs dos testes
│   ├── ARQUITETURA_E_EXPLICACAO.md   # Desenho de arquitetura e diagramas mermaid
│   └── .gitignore
│
├── .gitignore                        # Regras de exclusão de artefatos temporários Python
└── README.md                         # Índice geral do repositório
```

---

## 🎯 Resumo dos Desafios

### [Desafio 1: Criando sua primeira aplicação com IA](./Desafio1/README.md)
* **Objetivo:** Compreender instruções, variáveis, funções e condicionais construindo uma calculadora simples em Python.
* **Funcionalidades:** Adição, subtração, multiplicação e divisão com tratamento de divisão por zero.
* **Documentos:**
  - [`Desafio1/README.md`](./Desafio1/README.md): Detalhamento dos componentes, identificação das operações e lógica de programação.
  - [`Desafio1/TESTES.md`](./Desafio1/TESTES.md): Matriz de testes práticos validados.

### [Desafio 2: Evoluindo sua aplicação com Google Antigravity](./Desafio2/README.md)
* **Objetivo:** Praticar atividades clássicas de Engenharia de Software: entender código existente, implementar melhorias e validar não-regressão.
* **Funcionalidades adicionadas:** Nova operação de cálculo de porcentagem (`calcular_porcentagem`), menu contextual e suíte de testes automatizados com `unittest`.
* **Documentos e Relatórios Técnicos:**
  - [`Desafio2/README.md`](./Desafio2/README.md): Relatório da evolução e passo a passo.
  - [`Desafio2/TESTES.md`](./Desafio2/TESTES.md): Matriz de testes automatizados e critérios de aceitação.
  - [`Desafio2/RELATORIO_VERIFICACAO.md`](./Desafio2/RELATORIO_VERIFICACAO.md): Evidências reais de execução com 100% de aprovação nos testes.
  - [`Desafio2/ARQUITETURA_E_EVOLUCAO.md`](./Desafio2/ARQUITETURA_E_EVOLUCAO.md): Diagrama de fluxo (`mermaid`), análise de complexidade e boas práticas (SRP, Clean Code e programação defensiva).

### [Desafio 3: Criando uma Lista de Tarefas com Google Antigravity](./Desafio3/README.md)
* **Objetivo:** Construir do zero uma aplicação To-Do List visual completa com as 3 funcionalidades fundamentais: adicionar, concluir (com distinção visual evidente) e remover tarefas.
* **Funcionalidades:** Suporte a versão Web e Desktop (Python Tkinter), filtros dinâmicos, contadores em tempo real e persistência.
* **Documentos e Relatórios Técnicos:**
  - [`Desafio3/README.md`](./Desafio3/README.md): Visão geral do desafio e recursos.
  - [`Desafio3/TESTES.md`](./Desafio3/TESTES.md): Matriz de requisitos e cenários de teste.
  - [`Desafio3/RELATORIO_VERIFICACAO.md`](./Desafio3/RELATORIO_VERIFICACAO.md): Logs de teste e evidências práticas.
  - [`Desafio3/ARQUITETURA_E_EXPLICACAO.md`](./Desafio3/ARQUITETURA_E_EXPLICACAO.md): Desenho arquitetural, diagramas de fluxo e separação em camadas.

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.12+
- **Testes Automatizados:** `unittest` (Standard Library)
- **Ferramentas de IA:** Google AI Studio, Google Antigravity
- **Versionamento:** Git & GitHub

---

## ⚡ Como Executar os Projetos Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/ArmandoFilho483/Imersao-Alura-com-IA.git
cd Imersao-Alura-com-IA
```

### 2. Executar o Desafio 1
```bash
cd Desafio1
python calculadora.py
```

### 3. Executar o Desafio 2
```bash
cd ../Desafio2
python calculadora.py
```

### 4. Executar os Testes Automatizados do Desafio 2
```bash
cd ../Desafio2
python -m unittest test_calculadora.py -v
```

### 5. Executar o Desafio 3 (Lista de Tarefas)
- **Versão Web:** Abra o arquivo `Desafio3/index.html` em qualquer navegador.
- **Versão Desktop (Python):**
  ```bash
  cd ../Desafio3
  python app_desktop.py
  ```
- **Testes Automatizados do Desafio 3:**
  ```bash
  cd ../Desafio3
  node --test test_todo.js
  ```

---

## 👤 Autor

Desenvolvido por **Armando Patrício** ([@ArmandoFilho483](https://github.com/ArmandoFilho483))  
Participante da **Imersão Alura com Inteligência Artificial**.
