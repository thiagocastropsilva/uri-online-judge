#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1004


def read_integer():
  try:
    return int(raw_input())
  except NameError:
    return int(input())

A = read_integer()
B = read_integer()
PROD = A * B
print(str("PROD = ") + str(PROD))