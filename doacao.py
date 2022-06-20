total_doacao = 0
doacao = float(input())

while doacao != -1.0:
  total_doacao += doacao
  doacao = float(input())
print(f'VC$ {total_doacao:.2f}')
print(f'R$ {total_doacao * 2.5:.2f}')