# Relatório de Verificação e Evidências de Execução

Este relatório consolida as evidências práticas dos testes realizados na versão evoluída da Calculadora Python, atestando a qualidade do software e a integridade de todas as operações.

---

## 1. Resumo Executivo

- **Ambiente de Teste:** Windows 11 / Python 3.12.x
- **Framework de Testes:** Python `unittest` (Standard Library)
- **Total de Testes Automatizados:** 9 testes
- **Taxa de Sucesso:** 100% (9 aprovados, 0 falhas, 0 erros)
- **Tempo de Execução:** < 0.001s

---

## 2. Evidência do Log de Execução dos Testes Unitários

Comando executado:
```bash
python -m unittest test_calculadora.py -v
```

Log oficial de saída:
```text
test_calcular_porcentagem_basica (test_calculadora.TestCalculadoraEvoluida.test_calcular_porcentagem_basica) ... ok
test_calcular_porcentagem_com_decimais (test_calculadora.TestCalculadoraEvoluida.test_calcular_porcentagem_com_decimais) ... ok
test_calcular_porcentagem_maior_que_cem (test_calculadora.TestCalculadoraEvoluida.test_calcular_porcentagem_maior_que_cem) ... ok
test_calcular_porcentagem_zero (test_calculadora.TestCalculadoraEvoluida.test_calcular_porcentagem_zero) ... ok
test_dividir (test_calculadora.TestCalculadoraEvoluida.test_dividir) ... ok
test_dividir_por_zero (test_calculadora.TestCalculadoraEvoluida.test_dividir_por_zero) ... ok
test_multiplicar (test_calculadora.TestCalculadoraEvoluida.test_multiplicar) ... ok
test_somar (test_calculadora.TestCalculadoraEvoluida.test_somar) ... ok
test_subtrair (test_calculadora.TestCalculadoraEvoluida.test_subtrair) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

---

## 3. Verificação Interativa de Casos de Borda (Edge Cases)

Além dos testes unitários isolados, foram verificadas as entradas de terminal para assegurar que a experiência de uso (UX) e o tratamento de erros continuam impecáveis.

### Teste de Borda 1: Divisão por Zero
* **Ação do Usuário:** Escolhe opção `4` (Divisão), informa numerador `50` e denominador `0`.
* **Resultado Obtido:**
  ```text
  Erro: Não é possível dividir um número por zero.
  ```
* **Avaliação:** O programa não sofreu encerramento inesperado (*crash*). O erro foi tratado de forma defensiva e o menu foi reapresentado.

### Teste de Borda 2: Cálculo de Porcentagem Decimais
* **Ação do Usuário:** Escolhe opção `5` (Porcentagem), informa base `80` e taxa `12.5`.
* **Resultado Obtido:**
  ```text
  Resultado: 12.5% de 80.0 = 10.0
  ```
* **Avaliação:** Cálculo exato respeitando a precisão do ponto flutuante.

### Teste de Borda 3: Entrada com Vírgula Decimal Brasileira
* **Ação do Usuário:** Digita `15,5` quando o sistema solicita um número.
* **Resultado Obtido:** O sistema converteu automaticamente para `15.5` sem disparar `ValueError`.
* **Avaliação:** Validação ergonômica e tolerante a formatos regionais.

### Teste de Borda 4: Digitação de Caracteres Alfanuméricos Inválidos
* **Ação do Usuário:** Digita `cem` em vez de `100`.
* **Resultado Obtido:**
  ```text
  Entrada inválida! Por favor, digite um número válido.
  ```
* **Avaliação:** O loop solicita o valor novamente sem interromper o fluxo da aplicação.

---

## 4. Conclusão da Verificação

A evolução do software atendeu a todos os critérios de aceitação do **Desafio 2**:
1. O código legado permaneceu intacto em seu comportamento original.
2. A nova funcionalidade de porcentagem foi integrada com harmonia à arquitetura existente.
3. Não foram identificados vazamentos de exceção nem falhas de tipo em nenhuma das operações.
