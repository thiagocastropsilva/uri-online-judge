#Problema https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

V = []
def read_string():
  try:
    return str(raw_input())
  except NameError:
    return str(input())

for i in range(2):
    N = read_string().split(' ')
    T = int(N[1]) * float(N[2])
    N.insert(3,T)
    V.insert(i,N)
r = 0.00
for i in V:
    r = r + float(i[3])

print("VALOR A PAGAR: R$ %s" % '{0:.2f}'.format(r))    