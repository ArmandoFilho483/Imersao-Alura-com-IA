# Plano de Testes e Estratégia de Verificação (Desafio 2)

Este documento descreve a metodologia, a matriz de cobertura de requisitos e os cenários de teste aplicados na evolução da Calculadora em Python (Desafio 2 da Imersão Alura com IA).

---

## 1. Objetivos dos Testes

1. **Garantia de Não-Regressão:** Assegurar que a introdução do cálculo de porcentagem não degrade nem altere o comportamento das quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`).
2. **Validação da Nova Operação:** Certificar que a função `calcular_porcentagem` execute cálculos exatos para valores inteiros, fracionários, limites (zero) e taxas superiores a $100\%$.
3. **Robustez e Engenharia Defensiva:** Validar o tratamento de exceções (divisão por zero) e a resiliência contra entradas não numéricas.

---

## 2. Tipos de Teste Aplicados

| Tipo | Ferramenta / Técnica | Escopo |
| :--- | :--- | :--- |
| **Testes Unitários Automatizados** | `unittest` (módulo nativo do Python) | Teste individual de cada função matemática isolada. |
| **Testes de Integração de Fluxo** | Simulação via subprocesso e I/O de terminal | Validação do fluxo do menu (`main`) e interação do usuário. |
| **Testes de Casos de Borda (Edge Cases)** | Casos limítrofes manuais e unitários | Divisão por zero, porcentagem zero, taxas maiores que $100\%$ e números negativos. |

---

## 3. Matriz de Rastreabilidade de Testes

| ID do Caso | Componente | Cenário Avaliado | Dados de Entrada | Resultado Esperado | Status |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **CT-01** | `somar` | Soma de dois inteiros positivos | `a = 10, b = 5` | Retornar `15.0` | **Aprovado** |
| **CT-02** | `somar` | Soma envolvendo número negativo | `a = -2, b = 5` | Retornar `3.0` | **Aprovado** |
| **CT-03** | `somar` | Soma de números de ponto flutuante | `a = 1.5, b = 2.3` | Retornar `3.8` | **Aprovado** |
| **CT-04** | `subtrair` | Subtração simples com resultado positivo | `a = 10, b = 4` | Retornar `6.0` | **Aprovado** |
| **CT-05** | `subtrair` | Subtração resultando em negativo | `a = 5, b = 10` | Retornar `-5.0` | **Aprovado** |
| **CT-06** | `multiplicar` | Multiplicação simples | `a = 6, b = 7` | Retornar `42.0` | **Aprovado** |
| **CT-07** | `multiplicar` | Multiplicação com fator negativo | `a = -3, b = 4` | Retornar `-12.0` | **Aprovado** |
| **CT-08** | `multiplicar` | Multiplicação por elemento nulo | `a = 10, b = 0` | Retornar `0.0` | **Aprovado** |
| **CT-09** | `dividir` | Divisão exata | `a = 20, b = 4` | Retornar `5.0` | **Aprovado** |
| **CT-10** | `dividir` | Divisão fracionária | `a = 7, b = 2` | Retornar `3.5` | **Aprovado** |
| **CT-11** | `dividir` | **Caso Crítico:** Divisão por zero | `a = 10, b = 0` | Lançar `ZeroDivisionError` | **Aprovado** |
| **CT-12** | `calcular_porcentagem` | Cálculo padrão de porcentagem | `total = 200, taxa = 15` | Retornar `30.0` | **Aprovado** |
| **CT-13** | `calcular_porcentagem` | Taxa percentual com casas decimais | `total = 80, taxa = 12.5` | Retornar `10.0` | **Aprovado** |
| **CT-14** | `calcular_porcentagem` | **Caso Limite:** Taxa zero sobre valor | `total = 500, taxa = 0` | Retornar `0.0` | **Aprovado** |
| **CT-15** | `calcular_porcentagem` | **Caso Limite:** Taxa sobre base zero | `total = 0, taxa = 50` | Retornar `0.0` | **Aprovado** |
| **CT-16** | `calcular_porcentagem` | Taxa percentual superior a 100% | `total = 200, taxa = 150` | Retornar `300.0` | **Aprovado** |

---

## 4. Instruções para Reprodução

Para executar toda a bateria de testes unitários:

```bash
python -m unittest test_calculadora.py -v
```
