print('lojas SILVA')
valor = float(input('Qual o Valor das compras?:'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''') 
escolha = int(input('Qual a forma de pagamento?:'))
if escolha == 1:
    c1 = (valor * 10) / 100
    c2 = valor - c1 
    print('Pagando á Vista no dinheiro/cheque você ganhou um desconto de 10%. O valor total a pagar é de R$:{:.2f}'.format(c2))
elif escolha == 2:
    c1 = (valor * 5) / 100
    c2 = valor - c1 
    print('Pagando á vista no cartão você ganhou um desconto de 5%. O valor total a pagar é de R$:{:.2f}'.format(c2))
elif escolha == 3: 
    c1 = valor / 2 
    print('Pagando em Duas vezes á parcela fica em torno R$:{:.2f}'.format(c1))
else:
    parcelas = int(input('Qual o número de parcelas?:'))
    c1 = valor + (valor * 20/ 100)
    c2 = c1 / parcelas
    print('Por conta do número, o de parcelas terá um acréscimo de 20% de juros. As parcelas ficaram no valor R$:{:.2f} durante {} meses'.format(c2,parcelas))