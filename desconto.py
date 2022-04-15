print('Bem vindo a lojas americanas. Temos um desconto exclusivo de 10% pra você:\n')
preçooriginal = float(input('Digite aqui o preço do produto que você se interessou:\n'))
desconto = preçooriginal * 0.1
descontoreal = (preçooriginal-desconto)
print(f'O valor do seu produto é R${preçooriginal}!\n')
print(f'E com o desconto de 10% ele vai vai sair por R${desconto} mais barato!\n')
print(f'E o valor final do seu produto é {round(descontoreal,2)}. :)\n')
