# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora

cidade = input("Em qual cidade você mora? ")
estado = input("Em qual estado você mora? ")

# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.

print(f"Você mora em {cidade.upper()}.")

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.

estado_maiusculo = estado.upper()
print(f"Você mora no estado {estado_maiusculo}.")