# Reporte

## 1. ¿Por qué el camino de 13 pasos es óptimo?

Con γ = 1 y recompensa de −1 en cada paso ordinario,
el retorno es el negativo del número de pasos.
Maximizar el retorno es llegar a G en la menor cantidad
de pasos posible, sin pisar el acantilado.

Desde S no puedo avanzar al este, porque (3, 1) es acantilado.
Tampoco puedo caminar por la fila 3 hasta llegar a G.
Entonces el primer paso tiene que ser al norte, y al final
tengo que bajar a la fila 3 para entrar a G.
Eso da 1 + 11 + 1 = 13 pasos como mínimo, y la única
forma de lograrlo es N, once veces E y una vez S.

Es el camino que va pegado al borde porque la fila 2
es la más cercana al acantilado. Cualquier camino por
las filas 1 o 0 necesita más pasos, así que rinde menos.
Q-learning lo aprende aunque explore, porque su blanco usa
el máximo de Q(s', ·) y no la acción que se ejecuta.

## 2. ¿Por qué la curva queda por debajo de −13?

En el entrenamiento el agente sigue ε-greedy con ε = 0.1.
Eso significa que la acción S sale por azar con
probabilidad 0.1 × 1/4 = 0.025 en cada paso.
Sobre la fila 2, entre las columnas 1 y 10, esa acción
es una caída: cuesta −100 y me regresa a S.

Son 10 casillas expuestas, así que, aun siguiendo el camino
óptimo, hay una caída en alrededor del 22 % de los
episodios (1 − 0.975^10). Además, cada acción aleatoria extra
alarga el recorrido. Por eso la curva se queda por debajo
de −13, aunque la política greedy ya sea óptima.
En mi corrida con semilla 42, la media de los últimos
100 episodios fue de −46.1. El −13 solo se mide
en la evaluación con ε = 0.

## 3. ¿Cuál es s' al caer y por qué no es terminal?

Cuando el agente cae, el siguiente estado s' es S = (3, 0)
y la recompensa es −100. El blanco queda así:
−100 + γ max_a' Q(S, a').

No trato el acantilado como estado terminal porque el
episodio no termina al caer. El agente reaparece en S
y sigue actuando, así que lo que pase desde ahí
también cuenta en el retorno. Por eso el máximo futuro
es max_a' Q(S, a') y no 0.

Con γ = 1, ese máximo converge a −13, así que la caída
vale −100 + (−13) = −113. En mi corrida con semilla 42,
Q(S, E) quedó exactamente en −113. Si lo marcara como terminal,
el blanco sería solo −100 y la caída parecería más barata,
porque ignoraría los 13 pasos para volver a recorrer el camino.
