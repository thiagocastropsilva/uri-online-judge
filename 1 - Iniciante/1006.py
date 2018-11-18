#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1006

def read_float():
  try:
    return float(raw_input())
  except NameError:
    return float(input())

N1 = read_float()
N2 = read_float()
N3 = read_float()
MEDIA = (((N1 * 2) + (N2 * 3) + (N3 * 5)) / 10)
print("MEDIA = %s" % '{0:.1f}'.format(MEDIA))
