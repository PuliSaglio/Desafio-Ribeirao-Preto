#QUESTAO 2) 
# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci():
    ultimo = 1
    penultimo = 1
    termo = ultimo + penultimo
    cont = 3
    fib = False

    num = int(input("Informe o número que voce quer conferir se está na sequencia de fibonacci: "))

    if num==0 or num == 1 or num == 2:
        print(f'o número {num} pertence a sequencia de fibonacci')

    while num >= cont:
        if num == termo:
            print(f'o número {num} pertence a sequencia de fibonacci')
            fib = True
            break
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        cont += 1

    if fib == False and not 2:
        print(f'o número {num} nao pertence a sequencia de fibonacci')

           
fibonacci()