#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1001

def read_integer():
  try:
    return int(raw_input())
  except NameError:
    return int(input())

A = read_integer()
B = read_integer()
X = A + B
print(str("X = ") + str(X))
