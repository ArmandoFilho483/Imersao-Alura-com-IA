"""
Calculadora Evoluída em Python
Desafio 2 - Alura: Evoluindo sua primeira aplicação com o Google Antigravity
Funcionalidade adicionada: Cálculo de Porcentagem (%)
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

def calcular_porcentagem(total: float, porcentagem: float) -> float:
    """
    Calcula uma porcentagem sobre um valor base.
    Exemplo: 15% de 200 = (200 * 15) / 100 = 30.0
    """
    return (total * porcentagem) / 100.0

def exibir_menu() -> None:
    """Exibe o menu de opções atualizado."""
    print("\n" + "=" * 32)
    print("   CALCULADORA EVOLUÍDA (v2.0)")
    print("=" * 32)
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Porcentagem (%) [NOVO]")
    print("6 - Sair")
    print("=" * 32)

def obter_numero(mensagem: str) -> float:
    """Lê um número float do teclado com validação contra entradas inválidas."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

def main() -> None:
    """Fluxo principal da calculadora com suporte a porcentagem."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "6":
            print("\nEncerrando a calculadora. Até mais!")
            break

        if opcao not in {"1", "2", "3", "4", "5"}:
            print("\nOpção inválida! Escolha um número entre 1 e 6.")
            continue

        try:
            if opcao == "5":
                total = obter_numero("Digite o valor base (ex: 200): ")
                taxa = obter_numero("Digite a taxa percentual (ex: 15 para 15%): ")
                resultado = calcular_porcentagem(total, taxa)
                print(f"\nResultado: {taxa}% de {total} = {resultado}")
            else:
                num1 = obter_numero("Digite o primeiro número: ")
                num2 = obter_numero("Digite o segundo número: ")

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
