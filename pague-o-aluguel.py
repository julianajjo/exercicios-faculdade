divida = int(input())
pag_mensal = int(input())
parcela = 1

while divida > 0:
    if divida >= pag_mensal:
      print(f'pagamento: {parcela}')
      print(f'antes = {divida}')
      print(f'depois = {divida - pag_mensal}')
      print("-----")
      parcela += 1
      divida = divida - pag_mensal
    else:
      print(f'pagamento: {parcela}')
      print(f'antes = {divida}')
      print(f'depois = {divida - divida}')
      print("-----")
      break