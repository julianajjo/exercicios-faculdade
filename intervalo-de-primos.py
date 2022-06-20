inicio = int(input())
fim = int(input())
primos = 0

for i in range(inicio, fim+1):
  if i > 1:
    for n in range(2, i):
      if (i % n == 0):
        break
    else:
      print(i)
      primos += 1

print(f'primos: {primos}')