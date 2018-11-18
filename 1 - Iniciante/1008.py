#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

def read_integer():
  try:
    return int(raw_input())
  except NameError:
    return int(input())

def read_float():
  try:
    return float(raw_input())
  except NameError:
    return float(input())

N = read_integer()
V = read_integer()
H = read_float()
S = V * H
print(str("NUMBER = ") + str(N))
print("SALARY = U$ %s" % '{0:.2f}'.format(S))
