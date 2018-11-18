#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1002


def read_float():
  try:
    return float(raw_input())
  except NameError:
    return float(input())

P = 3.14159
A = round(read_float(),2)
area = P * (A**2)
print("A=%s" % '{0:.4f}'.format(area))