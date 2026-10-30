# Imersão Alura com Inteligência Artificial

Repositório dedicado aos projetos, experimentos e desafios desenvolvidos durante a **Imersão Alura com IA**. O objetivo desta jornada é explorar como a Inteligência Artificial Generativa pode atuar como copiloto no ciclo de desenvolvimento de software, acelerando a prototipagem, a resolução de problemas e o aprendizado de novas linguagens e paradigmas de programação.

---

## 📚 Desafio 1: Criando sua primeira aplicação com IA

### Enunciado do Desafio

> *Agora que você conheceu algumas possibilidades da Inteligência Artificial no desenvolvimento de software, chegou a hora de colocar a mão na massa! O desafio é usar o Google AI Studio para gerar uma calculadora em Python com as quatro operações básicas (adição, subtração, multiplicação e divisão) e entender como a aplicação funciona.*
>
> *Depois de gerar o código, explore a solução com a ajuda da IA e procure responder:*
> 1. *Quais são os principais componentes do código gerado?*
> 2. *Como a aplicação recebe os números e identifica a operação escolhida?*
> 3. *Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?*
>
> *Experimente também realizar diferentes operações e observar como a aplicação se comporta.*
>
> *O objetivo não é dominar Python de imediato, e sim começar a compreender como instruções, variáveis e condições são utilizadas na construção de um software.*

---

## 💻 Sobre a Aplicação: Calculadora em Python

A aplicação desenvolvida em [`calculadora.py`](./calculadora.py) é uma calculadora de terminal interativa, construída de ponta a ponta com boas práticas de engenharia de software: código modular, tipagem estática (*type hints*), validação defensiva de dados e tratamento seguro de exceções (como divisão por zero).

### Estrutura de Arquivos

```text
├── calculadora.py    # Código-fonte principal da aplicação
├── README.md         # Documentação completa do projeto e do desafio
└── .gitignore        # Arquivos ignorados pelo controle de versão
```

---

## 🔍 Análise e Respostas do Desafio

### 1. Quais são os principais componentes do código gerado?

O código foi arquitetado em componentes com responsabilidade única:

* **Funções de Operações Matemáticas (`somar`, `subtrair`, `multiplicar`, `dividir`):**
  Funções puras que recebem dois argumentos numéricos (`a` e `b`) e retornam o valor calculado. A função `dividir` inclui uma verificação explícita que lança a exceção `ZeroDivisionError` quando o divisor for igual a zero, protegendo a integridade da execução.
* **Função de Interface e Apresentação (`exibir_menu`):**
  Centraliza o texto exibido no terminal, facilitando a navegação do usuário através de um menu numerado.
* **Função de Validação e Entrada (`obter_numero`):**
  Implementa um laço defensivo com `try / except ValueError`. Aceita separadores decimais tanto no formato brasileiro (vírgula `,`) quanto no padrão internacional (ponto `.`), evitando que caracteres inválidos quebrem a execução.
* **Orquestrador de Fluxo (`main`):**
  Mantém a aplicação ativa em um laço `while True` até que o usuário solicite explicitamente a saída (opção `5`), controlando a chamada das funções e a exibição amigável de erros.

---

### 2. Como a aplicação recebe os números e identifica a operação escolhida?

1. **Seleção da Opção:**
   - A função `input("Escolha uma opção (1-5): ")` captura a entrada como string.
   - O código valida se a opção está no conjunto permitido `{"1", "2", "3", "4", "5"}` antes de solicitar qualquer dado adicional.
   - Caso o usuário digite `5`, o comando `break` finaliza o laço imediatamente.
2. **Coleta e Conversão dos Números:**
   - Com uma opção válida selecionada (1 a 4), a função `obter_numero` solicita o primeiro e o segundo operando.
   - O texto digitado é tratado com `.strip().replace(",", ".")` e convertido para ponto flutuante (`float`), armazenado nas variáveis `num1` e `num2`.

---

### 3. Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?

* **Controle de Fluxo e Condicionais (`if / elif`):**
  Avalia a variável `opcao` para decidir qual função executar e qual símbolo matemático associar à saída:
  - `opcao == "1"` $\rightarrow$ `somar(num1, num2)` e operador `+`
  - `opcao == "2"` $\rightarrow$ `subtrair(num1, num2)` e operador `-`
  - `opcao == "3"` $\rightarrow$ `multiplicar(num1, num2)` e operador `*`
  - `opcao == "4"` $\rightarrow$ `dividir(num1, num2)` e operador `/`
* **Tratamento Seguro de Exceções (`try / except`):**
  A chamada do cálculo está envolvida em um bloco defensivo. Se ocorrer divisão por zero, a exceção é capturada e exibe uma mensagem de orientação ao usuário, sem abortar a aplicação.
* **Interpolação de Saída (*f-strings*):**
  O resultado é apresentado de forma legível por meio de formatação direta de strings em Python:
  ```python
  print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
  ```

---

## 🚀 Como Executar a Aplicação

### Pré-requisitos
- Ter o **Python 3.10+** instalado.

### Passo a Passo

1. Abra o terminal no diretório da aplicação:
   ```bash
   cd c:\Users\arman\Documents\MeusProjetos\Alura\Desafio1
   ```

2. Execute o script:
   ```bash
   python calculadora.py
   ```

3. Exemplo de uso no terminal:
   ```text
   ==============================
         CALCULADORA EM PYTHON
   ==============================
   1 - Adição (+)
   2 - Subtração (-)
   3 - Multiplicação (*)
   4 - Divisão (/)
   5 - Sair
   ==============================
   Escolha uma opção (1-5): 1
   Digite o primeiro número: 15.5
   Digite o segundo número: 4.5

   Resultado: 15.5 + 4.5 = 20.0
   ```

---

## 🧪 Casos de Teste Validados

| Operação | Entrada 1 | Entrada 2 | Comportamento Esperado |
| :--- | :---: | :---: | :--- |
| **Adição** | `10` | `5` | Retorna `15.0` |
| **Subtração** | `20` | `8` | Retorna `12.0` |
| **Multiplicação** | `6` | `7` | Retorna `42.0` |
| **Divisão** | `25` | `4` | Retorna `6.25` |
| **Divisão por Zero** | `10` | `0` | Exibe mensagem de erro defensiva sem travar |
| **Entrada Inválida** | `abc` | `10` | Solicita novamente até receber número válido |
| **Vírgula Decimal** | `5,5` | `2,5` | Converte para `5.5` e `2.5` e calcula normalmente |

---

## 👤 Autor

Desenvolvido por **Arman** durante a **Imersão Alura com Inteligência Artificial**.
