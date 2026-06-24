print('bem-vindo ao app racha-conta.')
conta_total = float(input('valor total da conta?: '))
# já tinha deixado float por costume 
pessoas_mesa = int(input('quantas pessoas na mesa?: '))

garcom = conta_total * 0.10
valor_basico = conta_total / pessoas_mesa

print(f'Cada pessoa deve pagar: R$ {valor_basico:.2f}')
print(f'Valor do garcom: R$ {garcom:.2f}')



