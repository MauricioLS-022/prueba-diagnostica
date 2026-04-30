# Prueba Diagnóstica — Instrucciones para ejecutar los scripts

Este repositorio contiene tres problemas con scripts en Python dentro de las carpetas `Problema1`, `Problema2` y `Problema3`.

**Requisitos**

- Python 3.8 o superior instalado.

**Cómo ejecutar los scripts**

1. Abrir una terminal en la carpeta raíz del proyecto (la que contiene este `README.md`).

2. Ejecutar cada script por separado:
   - Ejecutar el script del Problema 1:

     ```bash
     python Problema1/script.py
     ```

   - Ejecutar el script del Problema 2:

     ```bash
     python Problema2/script.py
     ```

   - Ejecutar el script del Problema 3:

     ```bash
     python Problema3/script.py
     ```

**Descripción breve de los scripts y cómo probarlos**

- Problema1: [Problema1/script.py](Problema1/script.py)
  - Función: analizador aritmético (tokeniza números, identificadores, operadores y paréntesis).
  - Pruebas incluidas: el archivo contiene ejemplos (`ejemplo`, `ejemplo1`, `ejemplo2`, `ejemplo3`) que se imprimen al ejecutar el script.

- Problema2: [Problema2/script.py](Problema2/script.py)
  - Función: valida cadenas FEN de ajedrez.
  - Pruebas incluidas: varias cadenas `fen_valida*` se validan y se imprimen los resultados al ejecutar el script.

- Problema3: [Problema3/script.py](Problema3/script.py)
  - Función: recorre un intervalo y muestra las secuencias de Collatz para los valores; imprime los primeros y últimos 5 del intervalo.
  - Prueba incluida: la llamada `collatz_intervalo(3,300)` se ejecuta por defecto en el archivo.

**Salida esperada (resumen)**

- `Problema1/script.py`: imprimirá textos con tokens y, si hay paréntesis, un indicador de paréntesis balanceados/no balanceados.
- `Problema2/script.py`: imprimirá mensajes indicando si cada FEN es válida o no.
- `Problema3/script.py`: imprimirá las secuencias Collatz (primero/últimos ítems según el intervalo).

**Link al repositorio de GitHub**

https://github.com/MauricioLS-022/prueba-diagnostica
