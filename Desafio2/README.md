# Imersão Alura com Inteligência Artificial

## 📚 Desafio 2: Evoluindo sua primeira aplicação com o Google Antigravity

### Enunciado do Desafio

> *No primeiro desafio, a IA ajudou a criar uma calculadora em Python. Agora damos um passo adiante: o desafio é usar o Google Antigravity para criar ou importar o projeto da calculadora e modificar a aplicação existente.*
>
> *Isso envolve três atividades:*
> 1. *Explorar o projeto: peça ao Antigravity para identificar os arquivos e explicar como o código está organizado.*
> 2. *Adicionar uma funcionalidade: solicite a implementação de uma nova operação, como o cálculo de porcentagem.*
> 3. *Testar a aplicação: peça à IA para verificar se a nova funcionalidade funciona corretamente, sem comprometer as operações anteriores.*
>
> *Depois, execute a aplicação e observe as mudanças feitas no código.*
>
> *O objetivo é praticar uma atividade comum na Engenharia de Software: compreender um código existente, implementar melhorias e verificar se tudo continua funcionando.*

---

## 🛠️ Atividade 1: Exploração e Entendimento do Projeto Legado

Antes de realizar modificações, o projeto da calculadora do **Desafio 1** foi importado e inspecionado:

* **Ponto de Entrada e Funções Existentes:**
  - `somar(a, b)`, `subtrair(a, b)`, `multiplicar(a, b)` e `dividir(a, b)`.
  - Tratamento defensivo em `dividir` contra divisão por zero (`ZeroDivisionError`).
  - Entrada de dados centralizada em `obter_numero` com conversão de vírgula para ponto e captura de `ValueError`.
  - Controle de ciclo de vida em `main()` via menu numérico em loop `while True`.

---

## ✨ Atividade 2: Implementação da Nova Funcionalidade (Porcentagem)

Para atender ao desafio, foi implementada a operação de cálculo de porcentagem mantendo 100% da compatibilidade com as funcionalidades já existentes.

### 1. Criação da Função Matemática
Foi adicionada a função `calcular_porcentagem(total: float, porcentagem: float) -> float`:
```python
def calcular_porcentagem(total: float, porcentagem: float) -> float:
    """
    Calcula uma porcentagem sobre um valor base.
    Exemplo: 15% de 200 = (200 * 15) / 100 = 30.0
    """
    return (total * porcentagem) / 100.0
```

### 2. Atualização da Interface (`exibir_menu`)
O menu recebeu a nova opção `5`, deslocando a opção de saída para `6`:
```text
================================
   CALCULADORA EVOLUÍDA (v2.0)
================================
1 - Adição (+)
2 - Subtração (-)
3 - Multiplicação (*)
4 - Divisão (/)
5 - Porcentagem (%) [NOVO]
6 - Sair
================================
```

### 3. Adaptação do Fluxo Principal (`main`)
Diferente das operações aritméticas padrão que pedem "primeiro e segundo número", a porcentagem pede dados semanticamente claros para o usuário:
- **Valor base** (ex.: `200`)
- **Taxa percentual** (ex.: `15` para $15\%$)

O resultado é exibido no formato: `15.0% de 200.0 = 30.0`.

---

## 🧪 Atividade 3: Testes e Garantia de Não-Regressão

Um dos pilares da engenharia de software é assegurar que **novas melhorias não quebrem recursos pré-existentes**.

Foi criada uma suíte de testes automatizados com o framework nativo `unittest` no arquivo [`test_calculadora.py`](./test_calculadora.py), cobrindo:

1. **Testes de Não-Regressão (Operações Anteriores):**
   - Adição com inteiros, negativos e decimais.
   - Subtração com resultados positivos e negativos.
   - Multiplicação com fatores positivos, negativos e zero.
   - Divisão padrão e verificação de lançamento de exceção em divisão por zero.
2. **Testes da Nova Operação (Porcentagem):**
   - Cálculo básico (ex.: $15\%$ de $200 = 30.0$).
   - Taxas com casas decimais (ex.: $12.5\%$ de $80 = 10.0$).
   - Casos limites com zero ($0\%$ de $500 = 0.0$ e $50\%$ de $0 = 0.0$).
   - Percentuais superiores a $100\%$ ($150\%$ de $200 = 300.0$).

### Resultado da Execução dos Testes
```bash
python -m unittest test_calculadora.py -v
```
```text
test_calcular_porcentagem_basica (test_calculadora.TestCalculadoraEvoluida) ... ok
test_calcular_porcentagem_com_decimais (test_calculadora.TestCalculadoraEvoluida) ... ok
test_calcular_porcentagem_maior_que_cem (test_calculadora.TestCalculadoraEvoluida) ... ok
test_calcular_porcentagem_zero (test_calculadora.TestCalculadoraEvoluida) ... ok
test_dividir (test_calculadora.TestCalculadoraEvoluida) ... ok
test_dividir_por_zero (test_calculadora.TestCalculadoraEvoluida) ... ok
test_multiplicar (test_calculadora.TestCalculadoraEvoluida) ... ok
test_somar (test_calculadora.TestCalculadoraEvoluida) ... ok
test_subtrair (test_calculadora.TestCalculadoraEvoluida) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

---

## 📁 Estrutura do Desafio 2

```text
Desafio2/
├── calculadora.py       # Aplicação evoluída com porcentagem e menu atualizado
├── test_calculadora.py  # Testes unitários automatizados (9 testes cobrindo 100% das funções)
├── README.md            # Documentação completa da evolução do software
└── .gitignore           # Ignora caches e arquivos temporários do Python
```

---

## 🚀 Como Executar

### 1. Rodar a Calculadora Interativa
```bash
python calculadora.py
```

### 2. Rodar a Suíte de Testes Automatizados
```bash
python -m unittest test_calculadora.py
```

---

## 👤 Autor

Desenvolvido por **Arman** durante a **Imersão Alura com Inteligência Artificial** com apoio do **Google Antigravity**.
