print('bem-vindo ao app racha-conta.')
conta_total = float(input('valor total da conta?: '))
# já tinha deixado float por costume 
pessoas_mesa = int(input('quantas pessoas na mesa?: '))

garcom_total = conta_total * 0.10 
conta_com_gorjeta = conta_total + garcom_total 
valor_final_por_pessoa = conta_com_gorjeta / pessoas_mesa

print(f'Valor total do garçom (mesa): R$ {garcom_total:.2f}')
print(f'Valor final para cada pessoa: R$ {valor_final_por_pessoa:.2f}')