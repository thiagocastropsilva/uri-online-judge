#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1003

def read_integer():
  try:
    return int(raw_input())
  except NameError:
    return int(input())

A = read_integer()
B = read_integer()
SOMA = A + B
print(str("SOMA = ") + str(SOMA))