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

---

## 👤 Autor

Desenvolvido por **Armando Patrício** ([@ArmandoFilho483](https://github.com/ArmandoFilho483))  
Participante da **Imersão Alura com Inteligência Artificial**.
