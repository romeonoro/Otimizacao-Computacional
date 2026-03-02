def funcao(a,b,x0,x1):
  result = []
  for x in range(x0,x1+1): #segundo parametro soma 1 para alcançar
    result.append((a*x)+b)
  return result

# simulando
r = funcao(-5, -11, -2, 5)
print(r)
