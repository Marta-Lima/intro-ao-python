from datetime import datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro

niver = input ("Qual a data do seu aniversário no formato brasileiro ?" ) 

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele

quantidade_de_dias = datetime.strptime(aniversario, '%d/%m/%Y') - datetime.now()
print(f"Faltam {quantidade_de_dias.days} dias para o seu aniversário")

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta

gostar = input("Você gosta de aniversários?")


# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta

festa = input("Você vai fazer festa?")


# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.

if gosta == 'sim' and festa == 'sim':
    print("\n Você ganhará presente!")
else:
    print("\nEntão você não ganhará presente!")