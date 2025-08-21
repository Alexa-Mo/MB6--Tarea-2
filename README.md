## MB6-Tarea 2-TDD SOLUCION

 RETO 5 — Calcular descuento simple


## ¿Para que sirve?

Este reto sirve para calcular el precio final con un descuento. Como cliente necesito saber cuánto voy a pagar después de aplicar un porcentaje

## Contexto

1. **Rojo (test que falla)**  
   Se escribieron pruebas para dos casos:  

   - aplicar_descuento(100, 10) → 90  
   - aplicar_descuento(200, 0) → 200  

   Al inicio no había función, por lo que falló.

2. **Verde (código mínimo)**  
   Se implementó la función:
    ```python
   precio_final = precio - (precio * descuento / 100) # codigo minimo
    return precio_final

## Descripción

Este proyecto corresponde al Reto 5: Calcular descuento simple, aplicado con la metodología TDD (Test Driven Development) en Python.

El desarrollo se hizo siguiendo las fases de TDD:

Rojo: primero se escribieron pruebas unitarias que fallaron al no existir la función.
Verde: se implementó el código mínimo que hace pasar las pruebas.
Refactor: se agregó entrada de usuario y documentación para mejorar la comprensión del proyecto.

Este ejercicio demuestra cómo TDD ayuda a evitar errores comunes en la lógica del cálculo y garantiza que los resultados sean los esperados antes de pasar a producción.

