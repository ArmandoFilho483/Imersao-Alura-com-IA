# Plano de Testes e Matriz de Cobertura (Desafio 3)

Este documento especifica os casos de teste, regras de negócio e critérios de aceitação da Lista de Tarefas desenvolvida no **Desafio 3 da Imersão Alura com IA**.

---

## 1. Matriz de Requisitos vs. Casos de Teste

| ID Requisito | Funcionalidade | Cenário Avaliado | Critério de Aceitação | Status |
| :---: | :--- | :--- | :--- | :---: |
| **RF-01** | Adicionar Tarefa | Adição com texto válido | Tarefa criada com ID único e status `concluida = false`. | **Aprovado** |
| **RF-02** | Validação de Entrada | Tentativa de adicionar texto vazio | Sistema recusa com mensagem de erro amigável. | **Aprovado** |
| **RF-03** | Validação de Entrada | Tentativa com apenas espaços | Espaços são cortados (`trim`) e a tarefa é rejeitada. | **Aprovado** |
| **RF-04** | Concluir Tarefa | Marcar tarefa pendente como concluída | Status alterado para `concluida = true`. Estilo visual atualizado. | **Aprovado** |
| **RF-05** | Desmarcar Tarefa | Alternar tarefa já concluída | Status revertido para `concluida = false`. | **Aprovado** |
| **RF-06** | Remover Tarefa | Exclusão de tarefa pelo ID | Tarefa é removida da memória e do storage. | **Aprovado** |
| **RF-07** | Integridade do ID | Remover/alternar ID inexistente | Lança exceção controlada sem quebrar a aplicação. | **Aprovado** |
| **RF-08** | Filtros | Filtrar por Pendentes e Concluídas | Retorna apenas os registros condizentes com o filtro. | **Aprovado** |
| **RF-09** | Estatísticas | Cálculo dinâmico de contadores | Informa com precisão o total, pendentes e concluídas. | **Aprovado** |
| **RF-10** | Distinção Visual | Tarefa concluída na interface | Aplica texto tachado, cor atenuada e selo de concluída. | **Aprovado** |

---

## 2. Estratégia de Teste

A arquitetura separa estritamente a **Regra de Negócio** (`todo_core.js`) da **Apresentação Visual / DOM** (`app.js`). Isso permitiu:

1. **Testes Unitários Automatizados de Alta Velocidade:** Executados nativamente via Node.js Test Runner sem dependência de browser ou emuladores.
2. **Testes Visuais Interativos:** Verificação de clique, hover, transição CSS e renderização nos navegadores Chrome e Edge e via Tkinter em Python.

---

## 3. Como Reproduzir os Testes

Para rodar os testes automatizados da lógica:

```bash
node --test test_todo.js
```
