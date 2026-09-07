#!/usr/bin/env python3
"""Calculadora simples executada pelo terminal."""


def ler_numero(mensagem):
    """Solicita um número até que o usuário informe um valor válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido.")


def main():
    nome = input("Digite seu nome: ").strip()
    print(f"Olá, {nome}, vamos começar!\n")

    primeiro_numero = ler_numero("Digite um número: ")
    segundo_numero = ler_numero("Digite um número: ")

    print(
        "\nEscolha a operação:\n"
        "1 - soma\n"
        "2 - subtração\n"
        "3 - multiplicação\n"
        "4 - divisão\n"
    )
    operacao = input("Digite o número da operação desejada: ").strip()

    if operacao == "1":
        resultado = primeiro_numero + segundo_numero
        nome_operacao = "soma"
    elif operacao == "2":
        resultado = primeiro_numero - segundo_numero
        nome_operacao = "subtração"
    elif operacao == "3":
        resultado = primeiro_numero * segundo_numero
        nome_operacao = "multiplicação"
    elif operacao == "4":
        if segundo_numero == 0:
            print("\nNão é possível dividir por zero.")
            return
        resultado = primeiro_numero / segundo_numero
        nome_operacao = "divisão"
    else:
        print("\nOperação inválida.")
        return

    print(f"\nO resultado da {nome_operacao} é: {resultado}")


if __name__ == "__main__":
    main()
