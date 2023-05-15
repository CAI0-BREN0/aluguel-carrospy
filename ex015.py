dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('quantos km foi rodado? '))
print('juntando os {} dias e os {} km rodados o total a  pagar ficara {:.2f} '.format(dias,km,(dias*60)+(km*0.15)))