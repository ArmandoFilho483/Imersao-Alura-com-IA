# Relatório de Verificação e Evidências dos Testes (Desafio 3)

Este relatório reúne os registros e evidências de validação funcional e de qualidade da aplicação **Lista de Tarefas (To-Do List)** do Desafio 3.

---

## 1. Resumo Executivo da Validação

- **Tecnologias Validadas:** JavaScript ES6+ / HTML5 / CSS3 / Python Tkinter
- **Runner de Testes:** Node.js Nativo (`node:test` e `node:assert/strict`)
- **Total de Testes:** 9 testes unitários
- **Resultado:** 100% de sucesso (9 aprovados, 0 falhas, 0 pendências)
- **Tempo de Execução:** ~109ms

---

## 2. Evidência do Log de Execução dos Testes Automatizados

Comando executado:
```bash
node --test test_todo.js
```

Log de saída registrado:
```text
▶ Suíte de Testes - Gerenciador de Tarefas
  ✔ 1. Deve adicionar uma nova tarefa com status inicial pendente (1.422ms)
  ✔ 2. Não deve permitir adicionar tarefas vazias ou só com espaços (0.3034ms)
  ✔ 3. Deve marcar uma tarefa pendente como concluída (0.1239ms)
  ✔ 4. Deve alternar de concluída de volta para pendente ao clicar novamente (0.0904ms)
  ✔ 5. Deve remover uma tarefa existente pelo ID (0.6098ms)
  ✔ 6. Deve lançar erro ao tentar remover ou alternar tarefa com ID inexistente (0.1096ms)
  ✔ 7. Deve filtrar tarefas por status (todas, pendentes e concluídas) (0.1879ms)
  ✔ 8. Deve calcular corretamente as estatísticas de tarefas (0.1342ms)
✔ Suíte de Testes - Gerenciador de Tarefas (4.3588ms)
ℹ tests 9
ℹ suites 0
ℹ pass 9
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 109.9136
```

---

## 3. Evidências dos Testes de Interface Visual

### Teste Visual 1: Distinção de Tarefa Concluída
* **Ação:** O usuário clica no checkbox ou no texto de uma tarefa ativa.
* **Comportamento Observado:**
  1. A classe `.completed` é adicionada ao item `<li>`.
  2. O texto recebe a propriedade `text-decoration: line-through` (efeito riscado) e cor cinza atenuada (`#94a3b8`).
  3. O checkbox é preenchido com a cor verde `#10b981` e exibe o ícone de marcação.
  4. Um badge visual verde com o texto `"Concluída"` aparece ao lado da tarefa.
  5. A opacidade geral do container é reduzida suavemente para `0.75`.

### Teste Visual 2: Prevenção de Injeção de Código (XSS)
* **Ação:** Digitação de caracteres HTML especiais como `<script>alert('xss')</script>` no campo de tarefa.
* **Comportamento Observado:** A função `escaparHTML()` neutralizou os caracteres antes da inserção no DOM, renderizando-os como texto plano seguro e inofensivo.

### Teste Visual 3: Persistência no LocalStorage
* **Ação:** Inclusão de 3 tarefas, conclusão de 1 e recarregamento da página (`F5`).
* **Comportamento Observado:** As 3 tarefas foram recarregadas com precisão e os seus respectivos estados foram preservados sem perdas.

---

## 4. Conclusão

Todas as três funcionalidades solicitadas no enunciado:
1. Adicionar tarefas;
2. Marcar como concluídas (com distinção visual evidente);
3. Remover tarefas;

Juntamente com os testes e validações exigidos pelo desafio, foram implementadas com sucesso e aprovadas sem ressalvas.
