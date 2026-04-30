import re

def analizador_aritmetico(expresion): 
  patrones = [
    ('NUMERO', r'\d+(\.\d+)?'),
    ('OPERANDO', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('OPERADOR', r'[\+\-\*\/]'),
    ('PAREN_IZQ', r'\('),
    ('PAREN_DER', r'\)'),
    ('ESPACIO', r'\s+'),
    ('ERROR', r'.')
  ]

  patron_regex = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in patrones)

  balance_parentesis = 0
  tiene_parentesis = False
  resultados = []

  for match in re.finditer(patron_regex, expresion):
    tipo = match.lastgroup
    valor = match.group()

    if tipo == 'ESPACIO': 
      continue
    
    if tipo == 'PAREN_IZQ':
      balance_parentesis += 1
      tiene_parentesis = True
    elif tipo == 'PAREN_DER':
      balance_parentesis -= 1
      tiene_parentesis = True

    resultados.append(f'{tipo} {valor}')

    estado_parentesis = 'PARÉNTESIS BALANCEADOS' if balance_parentesis == 0 else 'PARÉNTESIS NO BALANCEADOS'


  return ' '.join(resultados) + f' {estado_parentesis if tiene_parentesis else ''}'

ejemplo = "12 + 3 * ( 4 )"
ejemplo1 = "100 $ 20"
ejemplo2 = "45.5 * A + ( 2 - VALOR )"
ejemplo3 = "( 10 / 2 ))"

print("Salida:", analizador_aritmetico(ejemplo))
print("Salida:", analizador_aritmetico(ejemplo1))
print("Salida:", analizador_aritmetico(ejemplo2))
print("Salida:", analizador_aritmetico(ejemplo3))