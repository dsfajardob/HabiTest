# Autor: David Santiago Fajardo Barrrera

## Requisitos para ejecuar:
-Python 3.x


## Modo de uso:
Los datos seran leidos por consola en el formato que se indicaba en el problema, para ejecutarlo
se debe ejecuar el archivo main.py, en caso tal de querer ver las pruebas unitarias se puede ejecuar
el archivo test_numberdisplay.py donde se encuentran diferentes pruebas y comparaciones con los valores
que se tenian de ejemplo en el problema

```bash
python3 main.py
python3 test_numberdisplay.py
```

## Archivos:
* main.py: Desde este se ejecuta el problema y se ve la impresion de los valores en el formato solicitado

* test_numberdisplay.py: Desde este se ejecutan las pruebas unitarias, es importante recalcar que no se veran impresiones por consola mas alla de las propias del modulo unittest de la ibreria estandar de python 3.x

* numberdisplay.py: este archivo simula una pantalla LCD de 7 segmentos y hace el mapeo de los numeros del 0,9 

* segments.py: este archivo contiene funciones las cuales sirven para "llenar los segmentos" de una pantalla LCD de 7 segmentos, es importante ya que el archivo numberdisplay.py lo usa para poder llenar los numeros segun corresponde en una matris de size*2+3 filas y size + 2 columnas