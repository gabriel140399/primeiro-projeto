#Definindo a função de cada operação
def soma(a, b):
   return a + b

def subtracao(a, b):
   return a - b

def multiplicacao(a, b):
   return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Não é possivel realizar divisão por '0'"

#Função principal da calculadora
def calculadora():
    while True:
        #Mostra o menu de opções
        print("\n Escolha a operação desejada: ")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

#escolha do usuario
        escolha = input("Digite a opção desejada: ")

        if escolha == '0':
            print("Encerrando a calculadora!")
            break
        elif escolha in ('1','2','3','4'):

#Solicite o numero para realizar a operação
            num1 = int(input("Digite o primeiro número para operação"))
            num2 = int(input("Digite o segundo número para operação"))

#fazendo calculo conforme escoha

            if escolha == '1':
                print("Resultado = ",soma (num1, num2))

            elif escolha == '2':
                print("Resultado = ", subtracao(num1, num2))

            elif escolha == '3':
                print("Resultado = ", multiplicacao(num1, num2))

            elif escolha == '4':
                print("Resultado = ", divisao(num1, num2))

        else:
            print("Opção invalida tente novamente")

# Chamada da função principal para executar a calculadora
calculadora()


