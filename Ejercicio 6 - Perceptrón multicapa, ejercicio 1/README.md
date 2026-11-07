# Reporte

## 1. ¿Bajó más el error al agregar dos capas?

No. En las cuatro corridas, la red de cinco capas
(4 x 3 x 3 x 3 x 3) terminó peor que la original.
Pasó tanto en NumPy como en Keras, aunque no igual.

En NumPy, el error final subió de 0.0645 a 0.1981,
casi el triple. La red profunda se quedó en una meseta
de aproximadamente 0.67 durante unas 300 épocas.
Solo después empezó a bajar, y a la época 500
todavía seguía bajando, así que no alcanzó a converger.

En Keras, la pérdida subió de 0.1859 a 0.2221.
La curva quedó plana desde cerca de la época 200.
Además, la predicción de ejemplo fue casi 1/3 para
las tres clases (0.337, 0.335, 0.336). Es decir,
la red no aprendió a distinguirlas.

En tiempo, NumPy pasó de 9 s a 13.6 s.
En Keras casi no cambió: 37 s contra 36.5 s.

Debo aclarar que cada configuración se ejecutó una sola vez,
sin semilla fija. El mismo Keras de 4 x 3 x 3
terminó en 0.2202 en una ejecución y en 0.1859 en otra.
Esa diferencia es comparable a la que hay entre
la red original y la profunda. La dirección se mantuvo
(la profunda es peor), pero la magnitud no es confiable
con una sola corrida.

## 2. ¿Se parecen las curvas de NumPy y de Keras?

No. Con la misma topología, el error en NumPy baja
hasta 0.06, mientras que la pérdida de Keras
casi no baja de 0.19. Creo que se debe
a varias diferencias de implementación:

- **Escala:** NumPy suma los errores cuadráticos de las tres
  salidas y Keras los promedia, un factor de 3.
- **Actualizaciones:** NumPy actualiza con cada muestra,
  150 veces por época. Keras usa lotes de 32
  y da solo 5 pasos por época. En 500 épocas
  son 75 000 actualizaciones contra 2 500.
- **Orden de los datos:** en NumPy recorro Iris en orden,
  sin barajar. Keras lo baraja en cada época.
- **Inicialización:** uniforme entre -0.5 y 0.5 en NumPy,
  y Glorot en Keras.
- **Backprop del notebook 04 original:** tiene los índices
  de los pesos transpuestos. Lo corregí en la versión profunda.

## 3. ¿Tiene sentido que una red más profunda no aprenda mejor?

Sí. Iris es un problema pequeño y la red de 4 x 3 x 3
ya tiene capacidad de sobra. El problema de la red profunda
no es de capacidad, sino de optimización.

Con sigmoides apiladas, cada capa multiplica el δ por h(1 − h),
que nunca pasa de 0.25, y por pesos pequeños.
Medí el |δ| promedio al inicio en 300 inicializaciones.
De la salida a la primera capa pasa de 0.12 a 0.0001,
aproximadamente una milésima parte. En la red de dos capas
esa proporción es de una dieciochoava parte.
Con el mismo η = 0.03, las primeras capas casi no se mueven.
