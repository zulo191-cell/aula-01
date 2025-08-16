faturamento= int(input('Quanto que você ganho \n'))
gasto= int(input('Quanto você gasto \n'))

lucro = (faturamento - gasto)

print(lucro)

if lucro >= 0:
    print( f'você lucrou '.upper())

else:
    print( f'você teve prejuizo'.upper())
