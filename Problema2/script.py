def validar_fen(fen):
	partes = fen.split(" ")
	if len(partes) != 6:
		return False, "La cadena no tiene 6 partes separadas por espacio."
	
	tablero, turno, enroque, al_paso, medio_mov, num_mov = partes
	
	# 1. Validar tablero (8 filas separadas por '/')
	filas = tablero.split('/')
	if len(filas) != 8:
		return False, "El tablero no tiene 8 filas."
	for fila in filas:
		casillas = 0
		for char in fila:
			if char in '12345678':
				casillas += int(char)
			elif char in 'pnbrqkPNBRQK':
				casillas += 1
			else:
				return False, f"Carácter inválido en tablero: {char}"
		if casillas != 8:
			return False, "Una fila no suma 8 casillas."
			
	# 2. Validar turno
	if turno not in ['w', 'b']:
		return False, "El turno debe ser 'w' o 'b'."
		
	# 3. Validar enroque
	if enroque != '-':
		if not all(c in 'KQkq' for c in enroque) or len(enroque) > 4:
			return False, "Enroque inválido."
		
	# 4. Validar peón al paso
	if al_paso != '-':
		if len(al_paso) != 2 or al_paso[0] not in 'abcdefgh' or al_paso[1] not in '36':
			return False, "Casilla al paso inválida."
		
	# 5 y 6. Validar contadores
	if not medio_mov.isdigit() or not num_mov.isdigit():
		return False, "Los movimientos deben ser numéricos."
	
	return True, "La cadena FEN es VÁLIDA."

# Ejemplo de uso con la posición inicial
fen_valida = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen_valida1 = "4k3/8/8/8/8/8/4P3/4K3 w - - 5 39"
fen_valida2 = "rnbqkbnr/pppppppp/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen_valida3 = "rnbqkbnr/pppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

valido, msj = validar_fen(fen_valida)
valido1, msj1 = validar_fen(fen_valida1)
valido2, msj2 = validar_fen(fen_valida2)
valido3, msj3 = validar_fen(fen_valida3)
print(msj)
print(msj1)
print(msj2)
print(msj3)