#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1007

def read_integer():
  try:
    return int(raw_input())
  except NameError:
    return int(input())

A = read_integer()
B = read_integer()
C = read_integer()
D = read_integer()

DIFERENCA = ((A * B) - (C * D))
print(str("DIFERENCA = ") + str(DIFERENCA))