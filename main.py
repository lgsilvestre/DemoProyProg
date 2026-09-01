Luis = 1
Allan = '+'
Balta = 3

def calcular(n1, n2, op):
  if op == '+':
    return n1 + n2
  elif op == '-':
    return n1 - n2
  elif op == '*':
    return n1 * n2
  elif op == '/':
    if n2 == 0:
      return 'Error: División por cero'
    return n1 / n2
  else:
    return 'Operador no válido'


# Ejemplo de uso:
resultado = calcular(Luis,Balta,Allan)
print(resultado)  # Muestra 15


calcular(Luis,Balta,Allan)