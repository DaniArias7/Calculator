# Calculadora de hipoteca inversa.

El proyecto consiste en desarrollar una aplicación en Python
que permita calcular la cuota mensual que un banco le pagaría 
a una persona que ha adquirido una hipoteca inversa.

## Integrantes del grupo:
- Diego Sanabria Gómez.
- Andrés Julián Murillo.

## Estructura del proyecto:
- src: En esta carpeta se encuentra la lógica de negocio (model), la interfaz de usuario (view) y el controlador (controller).
- tests: En esta carpeta se encuentran las pruebas unitarias del aplicativo, ya sea del controlador o del modelo.

## Dependencias: 
- Asegurese de tener instalado Python en su unidad.
- Para el funcionamiento de la interfaz gráfica por consola instale la librería kivy. Use el siguiente comando: `pip install Kivy`

## ¿Cómo se usa?
Para hacer uso del aplicativo asegurese de tener instalado las dependencias necesarias. Una vez tenga las dependencias necesarias prosiga con las instrucciones:

1. Clone el repositorio en su unidad y abra la consola de comandos.
2. Ubiquese en la raiz de la carpeta clonada. Use el comando `cd [ruta de la carpeta]`.
3. Si desea correr las pruebas unitarias del modelo del aplicativo:
    - Ubiquese en la carpeta 'tests' de la ruta clonada.
    - Ejecute el siguiente comando: `python tests.py`.
4. Si desea ejecutar las pruebas del controlador:
    - Ubiquese en la carpeta 'tests' de la ruta clonada.
    - Ejecute el siguiente comando: `python controller_tests.py`
5. Si desea ejecutar la interfaz por consola:
    - Ubiquese en la siguiente ruta 'src/view/console'.
    - Ejecute el siguiente comando: `python controller_console.py`
6. Si desea ejecutar la interfaz gráfica de usuario (gui):
    - Ubiquese en la siguiente ruta: 'src/view/interface'.
    - Ejecute el siguiente comando: `python interface.py`.


