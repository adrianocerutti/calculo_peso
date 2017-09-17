#Exibe uma mensagem na tela
print("Cálculo de peso ideal")
#Recupera o valor digitado pelo usuário e armazena em uma variável
altura = float(input("Digite sua altura: "))
#Realiza o cálculo e armazena o resultado em uma variável
peso = (72.7 * altura) - 58
#Exibe o resultado na tela e arredonda o valor para 2 casas
print("Seu peso ideal é",round(peso,2),"Kg.")
