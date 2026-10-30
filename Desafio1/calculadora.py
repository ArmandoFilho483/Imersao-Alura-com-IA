"""
Calculadora Simples em Python
Desafio 1 - Alura: Criando sua primeira aplicação com IA
"""
import sys

# Garante compatibilidade de caracteres em terminais Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a: float, b: float) -> float:
    """Retorna a subtração entre dois números."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números."""
    return a * b

def dividir(a: float, b: float) -> float:
    """Retorna a divisão do primeiro número pelo segundo."""
    if b == 0:
        raise ZeroDivisionError("Erro: Não é possível dividir um número por zero.")
    return a / b

def exibir_menu() -> None:
    """Exibe o menu de opções para o usuário."""
    print("\n" + "=" * 30)
    print("      CALCULADORA EM PYTHON")
    print("=" * 30)
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Sair")
    print("=" * 30)

def obter_numero(mensagem: str) -> float:
    """Lê um número float do teclado com validação contra entradas inválidas."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

def main() -> None:
    """Fluxo principal da calculadora."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "5":
            print("\nEncerrando a calculadora. Até mais!")
            break

        if opcao not in {"1", "2", "3", "4"}:
            print("\nOpção inválida! Escolha um número entre 1 e 5.")
            continue

        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        try:
            if opcao == "1":
                resultado = somar(num1, num2)
                operador = "+"
            elif opcao == "2":
                resultado = subtrair(num1, num2)
                operador = "-"
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                operador = "*"
            elif opcao == "4":
                resultado = dividir(num1, num2)
                operador = "/"

            print(f"\nResultado: {num1} {operador} {num2} = {resultado}")

        except ZeroDivisionError as erro:
            print(f"\n{erro}")

if __name__ == "__main__":
    main()
