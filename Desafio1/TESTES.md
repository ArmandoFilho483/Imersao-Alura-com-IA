# Verificações e Testes da Aplicação (Desafio 1)

Este documento registra a matriz de testes manuais e a validação de comportamento da calculadora básica desenvolvida no Desafio 1.

---

## 1. Casos de Teste Executados

| ID | Operação | Entradas | Saída Obtida | Status |
| :---: | :--- | :--- | :--- | :---: |
| **CT01** | Adição | `10` e `5` | `Resultado: 10.0 + 5.0 = 15.0` | **Aprovado** |
| **CT02** | Subtração | `10` e `4` | `Resultado: 10.0 - 4.0 = 6.0` | **Aprovado** |
| **CT03** | Multiplicação | `7` e `8` | `Resultado: 7.0 * 8.0 = 56.0` | **Aprovado** |
| **CT04** | Divisão | `20` e `4` | `Resultado: 20.0 / 4.0 = 5.0` | **Aprovado** |
| **CT05** | Divisão por Zero | `10` e `0` | `Erro: Não é possível dividir um número por zero.` | **Aprovado** |
| **CT06** | Entrada Inválida | `texto` | `Entrada inválida! Por favor, digite um número válido.` | **Aprovado** |
| **CT07** | Vírgula Decimal | `10,5` e `2` | `Resultado: 10.5 + 2.0 = 12.5` | **Aprovado** |

---

## 2. Como Reproduzir os Testes

Execute no terminal:
```bash
python calculadora.py
```
Insira os dados indicados em cada caso de teste acima para validar os resultados.
