/**
 * Suíte de Testes Automatizados para a Lista de Tarefas (Desafio 3)
 * Executado nativamente pelo Node.js Test Runner: `node --test`
 */

const test = require('node:test');
const assert = require('node:assert/strict');
const { GerenciadorTarefas } = require('./todo_core.js');

test('Suíte de Testes - Gerenciador de Tarefas', async (t) => {
  await t.test('1. Deve adicionar uma nova tarefa com status inicial pendente', () => {
    const gerenciador = new GerenciadorTarefas();
    const tarefa = gerenciador.adicionarTarefa('Estudar Python e IA');

    assert.equal(gerenciador.tarefas.length, 1);
    assert.equal(tarefa.texto, 'Estudar Python e IA');
    assert.equal(tarefa.concluida, false);
    assert.ok(tarefa.id);
  });

  await t.test('2. Não deve permitir adicionar tarefas vazias ou só com espaços', () => {
    const gerenciador = new GerenciadorTarefas();

    assert.throws(() => gerenciador.adicionarTarefa(''), /A tarefa não pode estar vazia/);
    assert.throws(() => gerenciador.adicionarTarefa('   '), /A tarefa não pode estar vazia/);
    assert.throws(() => gerenciador.adicionarTarefa(null), /O texto da tarefa é obrigatório/);
  });

  await t.test('3. Deve marcar uma tarefa pendente como concluída', () => {
    const gerenciador = new GerenciadorTarefas();
    const tarefa = gerenciador.adicionarTarefa('Criar projeto no Antigravity');

    const atualizada = gerenciador.alternarConclusao(tarefa.id);
    assert.equal(atualizada.concluida, true);
  });

  await t.test('4. Deve alternar de concluída de volta para pendente ao clicar novamente', () => {
    const gerenciador = new GerenciadorTarefas();
    const tarefa = gerenciador.adicionarTarefa('Revisar código');

    gerenciador.alternarConclusao(tarefa.id); // vira true
    const desmarcada = gerenciador.alternarConclusao(tarefa.id); // volta para false
    assert.equal(desmarcada.concluida, false);
  });

  await t.test('5. Deve remover uma tarefa existente pelo ID', () => {
    const gerenciador = new GerenciadorTarefas();
    const t1 = gerenciador.adicionarTarefa('Tarefa 1');
    const t2 = gerenciador.adicionarTarefa('Tarefa 2');

    const removida = gerenciador.removerTarefa(t1.id);
    assert.equal(removida.id, t1.id);
    assert.equal(gerenciador.tarefas.length, 1);
    assert.equal(gerenciador.tarefas[0].id, t2.id);
  });

  await t.test('6. Deve lançar erro ao tentar remover ou alternar tarefa com ID inexistente', () => {
    const gerenciador = new GerenciadorTarefas();
    assert.throws(() => gerenciador.removerTarefa('id-inexistente'), /não encontrada/);
    assert.throws(() => gerenciador.alternarConclusao('id-inexistente'), /não encontrada/);
  });

  await t.test('7. Deve filtrar tarefas por status (todas, pendentes e concluídas)', () => {
    const gerenciador = new GerenciadorTarefas();
    const t1 = gerenciador.adicionarTarefa('Tarefa Pendente');
    const t2 = gerenciador.adicionarTarefa('Tarefa Concluída');
    gerenciador.alternarConclusao(t2.id);

    assert.equal(gerenciador.filtrarTarefas('todas').length, 2);
    assert.equal(gerenciador.filtrarTarefas('pendentes').length, 1);
    assert.equal(gerenciador.filtrarTarefas('pendentes')[0].id, t1.id);
    assert.equal(gerenciador.filtrarTarefas('concluidas').length, 1);
    assert.equal(gerenciador.filtrarTarefas('concluidas')[0].id, t2.id);
  });

  await t.test('8. Deve calcular corretamente as estatísticas de tarefas', () => {
    const gerenciador = new GerenciadorTarefas();
    const t1 = gerenciador.adicionarTarefa('T1');
    const t2 = gerenciador.adicionarTarefa('T2');
    const t3 = gerenciador.adicionarTarefa('T3');
    gerenciador.alternarConclusao(t1.id);

    const stats = gerenciador.obterEstatisticas();
    assert.equal(stats.total, 3);
    assert.equal(stats.concluidas, 1);
    assert.equal(stats.pendentes, 2);
  });
});
