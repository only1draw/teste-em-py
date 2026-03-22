l=input('\nqual o nome do eletrodomésticos:\n')
w=float(input('\nqual a potencia desse aparelhon(em watts):\n'))
h=float(input('\nquantas horas esse aparelho esta funcionando em media por dia:\n'))
cal=((w*h*30)/1000)
v=cal*0.75
print('\no eletrodomésticos {} \n tem o consumo estimado de {} kWh/mês\n custando un total estimado de {:.2f} reais'.format(l, cal, v))