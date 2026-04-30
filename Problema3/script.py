def collatz_intervalo(p, q):
  # Valida que la regla q >= 100p se cúmpla
  if q < 100 * p:
    print(f"Error: No se cumple la regla q >= 100p (q={q}, 100p={100*p})")
    return

  print(f'Demostrando conjetura de Collatz para intervalo [{p}, {q}]')

  for n_inicial in range(p, q + 1):

    n = n_inicial
    secuencia = [str(n)]

    while n != 1:
      if n % 2 == 0:
        n = n / 2
      else:
        n = 3*n + 1
      secuencia.append(str(int(n)))
    #se imprimen en pantalla los primeros 5 y los ultimos 5 del intervalo
    if n_inicial <= p + 4 or n_inicial >= q - 4:
      print(f'n={n_inicial}: {' -> '.join(secuencia)}\n')
  print('Demostrado para todo el intervalo')

#collatz_intervalo(1,100)
# collatz_intervalo(2,250)
# collatz_intervalo(5,100)
collatz_intervalo(3,300)