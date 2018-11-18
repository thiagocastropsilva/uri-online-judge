#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

def read_string():
  try:
    return str(raw_input())
  except NameError:
    return str(input())

def read_float():
  try:
    return float(raw_input())
  except NameError:
    return float(input())

N = read_string()
V = read_float()
V2 = read_float()
B = V2 * 0.15
S = V + B
print("TOTAL = R$ %s" % '{0:.2f}'.format(S))