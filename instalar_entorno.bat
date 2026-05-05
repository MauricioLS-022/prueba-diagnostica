@echo off
echo ==============================================
echo Instalando entorno para la Prueba Diagnostica
echo ==============================================

echo Verificando instalacion de Python...
python --version

echo Instalando dependencias desde requirements.txt...
pip install -r requirements.txt

echo ==============================================
echo Instalacion finalizada. Entorno listo.
echo ==============================================
pause