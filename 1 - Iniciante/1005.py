#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

def read_float():
  try:
    return float(raw_input())
  except NameError:
    return float(input())

N1 = read_float()
N2 = read_float()
MEDIA = (((N1 * 3.5) + (N2 * 7.5)) / 11)
print("MEDIA = %s" % '{0:.5f}'.format(MEDIA))
