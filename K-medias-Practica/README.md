# Reporte de Ejercicio 01 Clustering K-medias

1. En los datos de Géron, ¿por qué el codo “prefiere” (k = 4) si make_blobs usó 5 centros?

Porque hay dos blobs que están muy juntos. De manera muy resumida, esto hace que una de las medias tienda a estar en el
"punto medio" de estos dos blobs y, por tanto, al momento de crear una nueva categoría de clasificación, el algoritmo
no logre separarlos, considerandolos a ambos dentro de la misma.

El capítulo dedicado a clustering y k-medias precisamente habla sobre este problema. Menciona que el algoritmo converge pero
que no asegura que la solución a la que lo hace sea la adecuada. Al final da varias heurísticas para mejorar la inicialización
y menciona que si se tiene una idea de dónde deben estar ubicadas las medias, es una buena idea incluirlas en el método como
una lista de puntos. 

2. Con tus blobs separados, ¿el codo y la silueta coinciden en el mismo (k)? ¿Ese (k) es 5?

Si, al separar los blobs, logre que el $k$ sea 5. Justamente se logra al separar los blobs que están muy pegados en la sección
de abajo a la izquierda del plano. 

3. Si el codo sigue en 4, ¿qué te falta mover (distancia entre centros vs. blob_std)?

Dos de los blobs de la izquierda están a solo 0.5 de distancia con σ = 0.1, así que con k = 4 un solo centroide
queda justo en su punto medio y los trata como un grupo. Separar los blobs lo arregla: con k = 5 cada nube recibe su propio centroide.
Que es mas o menos lo mismo que se entiende en las primeras dos preguntas.
