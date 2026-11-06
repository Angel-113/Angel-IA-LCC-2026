# Descripción PEAS de agentes inteligentes

## 1. Asistente virtual de voz

- **Performance.** No tengo muy claro cómo establecer una métrica de rendimiento.
  Al menos no sin incluir directamente la participación del usuario final.
  Podríamos crear una función del sistema que permita evaluar, para cada
  instrucción, si el agente realizó correctamente lo que se solicitó.
  Tal vez pedir detalles sobre la instrucción y lo que
  el agente (y su herramienta de interpretación de voz) infirieron,
  para así entender lo que interpretaron. En ese sentido,
  una métrica de rendimiento podría ser cuántas instrucciones se ejecutaron correctamente.

- **Environment.** El ambiente son simplemente las señales de audio a procesar.
  Pueden contener ruido. Ello implica que no es un ambiente
  discreto y tampoco es un ambiente determinista. Uno nunca
  sabe cómo, cuándo o por qué surge el ruido.
  Y no es discreto porque las señales de audio
  (el hecho de procesar la voz) necesitan categorías continuas: ondas.
  El entorno es, por tanto, continuo y probabilístico.

- **Actuators.** Los actuadores pueden ser instrucciones específicas: `mover`, `copiar`,
  `crear`, `buscar`. Y en base a eso, crear concatenaciones
  de instrucciones en base a instrucciones monolíticas.

- **Sensors.** Los sensores son simplemente micrófonos.

## 2. Robot aspirador doméstico

- **Performance.** En este caso parece más sencillo establecer una métrica
  de rendimiento. Podríamos considerar la cantidad de superficie que
  el agente logró limpiar y la cantidad de suciedad
  que logró retirar. Sin embargo, no bastaría con medir
  cuánto tiempo estuvo funcionando, porque ello no necesariamente implica
  que haya realizado una limpieza adecuada. También habría que
  considerar el consumo energético y si logró evitar obstáculos
  sin dañar los objetos que se encuentran en el ambiente.
  En ese sentido, una métrica de rendimiento podría combinar
  la calidad de limpieza, el tiempo empleado y los recursos consumidos.

- **Environment.** El ambiente es simplemente el espacio físico en el
  que se encuentra el robot. Puede contener muebles, paredes,
  personas, mascotas y distintos tipos de superficies. Además,
  los obstáculos pueden cambiar de posición mientras el agente
  realiza su tarea. Ello implica que no es un
  ambiente completamente observable, porque el robot no necesariamente conoce
  todo lo que sucede a su alrededor. Tampoco es
  determinista, ya que no siempre puede predecir qué encontrará
  al desplazarse. El ambiente es, por tanto, parcialmente observable,
  dinámico y probabilístico. El espacio es continuo, aunque podríamos
  representarlo mediante una distribución discreta de habitaciones o coordenadas.

- **Actuators.** Los actuadores son principalmente los motores que permiten desplazar
  el robot y modificar su dirección. También podemos incluir
  los mecanismos de succión y los cepillos que permiten
  recoger la suciedad. Podríamos expresar estas acciones mediante instrucciones
  como `desplazar`, `girar`, `aspirar`, `cepillar` y `detener`.
  En ese sentido, el agente puede combinar varias instrucciones
  para completar las operaciones necesarias de limpieza.

- **Sensors.** Los sensores pueden ser cámaras, sensores infrarrojos, ultrasónicos
  o de proximidad. También podría contar con sensores para
  detectar suciedad, desniveles y colisiones. En conjunto, estos permiten
  que el agente obtenga información sobre su posición y
  sobre los elementos que lo rodean.

## 3. Sistema de recomendación de streaming

- **Performance.** No tengo muy claro si podríamos establecer una métrica
  de rendimiento sin considerar directamente la satisfacción del usuario.
  Podríamos utilizar la cantidad de contenido reproducido, el tiempo
  que permanece viendo una película o serie y la
  frecuencia con la que el usuario interactúa con las recomendaciones.
  Sin embargo, estas métricas no necesariamente indican que el
  contenido recomendado sea de su agrado. Tal vez una
  persona permanezca viendo algo simplemente porque no encontró otra cosa.
  En ese sentido, podríamos incluir valoraciones, reproducciones completadas y
  la frecuencia con la que el usuario decide consumir
  una recomendación. Una métrica de rendimiento podría ser, por
  tanto, la capacidad del agente para recomendar contenido
  que corresponda con los intereses del usuario.

- **Environment.** El ambiente está compuesto principalmente por el catálogo de
  contenido disponible y los usuarios que interactúan con él.
  También podemos incluir las preferencias, el historial de reproducciones
  y el contexto en el que se consume el contenido.
  No es un ambiente completamente observable porque el agente
  no conoce directamente los gustos del usuario; solamente puede
  inferirlos a partir de sus interacciones. Además, las preferencias
  pueden cambiar con el tiempo y el catálogo también
  puede modificarse. Ello implica que es un ambiente dinámico
  y parcialmente observable. Por otra parte, el comportamiento
  de los usuarios no siempre es predecible, así que
  también es probabilístico.

- **Actuators.** Los actuadores son las recomendaciones que el agente muestra
  al usuario. Podrían ser películas, series o cualquier otro
  contenido disponible dentro de la plataforma. También podemos incluir
  el orden en el que se presentan las recomendaciones,
  las notificaciones y la reproducción automática del siguiente contenido.
  Podríamos expresar estas acciones mediante instrucciones como `buscar`, `filtrar`,
  `recomendar`, `ordenar`, `notificar` y `reproducir`. En ese sentido,
  el agente no solamente selecciona qué contenido recomendar, sino
  que también puede determinar cómo y cuándo presentarlo.

- **Sensors.** Los sensores son principalmente los registros de interacción del
  usuario. Podemos considerar las búsquedas, las reproducciones, el tiempo
  de visualización, los contenidos abandonados y las valoraciones.
  También podría utilizar información sobre el dispositivo o el
  momento en el que se consume el contenido.

## 4. Vehículo autónomo en ciudad

- **Performance.** La métrica de rendimiento parece estar bastante relacionada con
  la seguridad y la capacidad del agente para llegar
  a su destino. Podríamos considerar si logró completar el
  recorrido sin accidentes, respetando las señales de tránsito y
  evitando situaciones que pongan en peligro a los peatones
  o a otros conductores. También habría que considerar el
  tiempo empleado y el consumo energético. En ese sentido,
  no bastaría con que el agente encuentre el camino
  más corto, porque podría tratarse de una ruta más peligrosa.
  Una métrica de rendimiento tendría que considerar principalmente la
  seguridad, el cumplimiento de las normas de tránsito y
  la eficiencia del recorrido.

- **Environment.** El ambiente es la ciudad y todos los elementos
  con los que el vehículo puede interactuar. Esto incluye
  las calles, los semáforos, los peatones, otros vehículos,
  las señales de tránsito y las condiciones meteorológicas. Es
  un ambiente dinámico porque los elementos pueden cambiar de
  posición constantemente. También es parcialmente observable, ya que el
  vehículo no puede conocer con certeza todo lo que
  sucede a su alrededor. Por ejemplo, no siempre puede
  anticipar las decisiones de un peatón o de otro conductor.
  Ello implica que tampoco es determinista. Además, es un
  ambiente continuo, porque tanto el movimiento del vehículo como
  el de los demás elementos ocurre dentro de un
  espacio y un tiempo continuos. Es también multiagente,
  porque existen otros agentes que toman decisiones dentro del mismo entorno.

- **Actuators.** Los actuadores son los mecanismos que permiten controlar el
  vehículo. Principalmente, el volante, los frenos y el acelerador.
  También podemos incluir las luces direccionales, los faros y
  otros mecanismos que permiten comunicar las intenciones del vehículo
  a los demás conductores. Podríamos expresar estas acciones mediante
  instrucciones como `acelerar`, `frenar`, `girar`, `detener` y `señalizar`.
  En conjunto, estos permiten que el agente modifique su
  movimiento y actúe sobre el ambiente.

- **Sensors.** Los sensores pueden ser cámaras, radares, sensores LiDAR
  y sensores ultrasónicos. También podemos incluir el GPS y
  los sensores que permiten conocer la velocidad, aceleración y
  orientación del vehículo. Cada uno proporciona información distinta sobre
  el ambiente y sobre el propio estado del vehículo.

## 5. Agente de trading algorítmico en bolsa

- **Performance.** Una métrica de rendimiento podría ser la rentabilidad obtenida
  por el agente durante un periodo determinado. Sin embargo,
  no creo que sea suficiente considerar únicamente cuánto dinero
  ganó, porque también habría que considerar el riesgo que
  asumió para obtener esa rentabilidad. Podríamos incluir las pérdidas
  máximas, los costos de transacción y la comparación con
  algún índice de referencia. En ese sentido, una métrica
  de rendimiento tendría que considerar tanto los beneficios obtenidos
  como el riesgo y los recursos necesarios para conseguirlos.

- **Environment.** El ambiente es el mercado financiero y todos los
  elementos que participan en él. Esto incluye los activos
  disponibles, los precios, las órdenes de compra y venta,
  los demás participantes del mercado y la información económica
  que puede influir en los precios. Es un ambiente dinámico
  porque los precios y las condiciones del mercado cambian
  constantemente. También es parcialmente observable, porque el agente no
  conoce todas las intenciones de los participantes ni puede
  anticipar con certeza sus decisiones. Ello implica que es
  un ambiente probabilístico y multiagente. Además, aunque algunas
  acciones del agente son discretas, como comprar o vender,
  los precios y las cantidades involucradas pueden representarse mediante
  valores continuos.

- **Actuators.** Los actuadores son principalmente las órdenes de compra y
  venta que el agente puede enviar al mercado. También
  podemos incluir la modificación o cancelación de órdenes existentes,
  así como la selección de los activos y las
  cantidades que desea negociar. Podríamos expresar estas acciones mediante
  instrucciones como `comprar`, `vender`, `establecer_orden`, `modificar_orden`
  y `cancelar_orden`. En ese sentido, sus acciones permiten
  intervenir directamente en el mercado y modificar la composición
  de su cartera.

- **Sensors.** Los sensores son las fuentes de información financiera que
  recibe el agente. Podemos considerar los precios históricos y actuales,
  el volumen de negociación, el libro de órdenes y
  las transacciones realizadas. También podría recibir información económica,
  noticias y datos sobre el estado de su propia cartera.

## 6. Sistema de diagnóstico médico asistido por IA

- **Performance.** La métrica de rendimiento podría estar relacionada con
  la precisión de los diagnósticos que realiza el agente.
  Sin embargo, no bastaría con considerar cuántas veces acertó,
  porque también habría que distinguir entre los distintos tipos
  de errores que puede cometer. Por ejemplo, no es
  lo mismo identificar una enfermedad que no está presente
  que no detectar una enfermedad que sí lo está.
  Podríamos considerar la sensibilidad, la especificidad y la frecuencia con
  la que sus recomendaciones coinciden con los diagnósticos confirmados.
  En ese sentido, una métrica de rendimiento tendría que
  considerar la precisión del diagnóstico, la seguridad del paciente
  y la utilidad de las recomendaciones para el personal médico.

- **Environment.** El ambiente está compuesto principalmente por los pacientes, su
  historial médico y la información clínica disponible. También podemos
  incluir los hospitales, los laboratorios y el personal médico
  que interactúa con el agente. No es un ambiente
  completamente observable porque el sistema no puede conocer directamente
  el estado de salud del paciente; solamente puede inferirlo
  a partir de los síntomas, estudios y demás información
  que recibe. Además, las condiciones médicas pueden cambiar con
  el tiempo. Ello implica que es un ambiente dinámico,
  parcialmente observable y probabilístico. También puede contener información continua,
  como los valores de presión arterial o temperatura, e
  información discreta, como los resultados de determinadas pruebas.

- **Actuators.** Los actuadores son principalmente las recomendaciones que el agente
  presenta al personal médico. Podría sugerir posibles diagnósticos, señalar
  inconsistencias en los resultados de laboratorio o recomendar estudios adicionales.
  También puede generar alertas cuando detecta valores que requieren
  atención. Podríamos expresar estas acciones mediante instrucciones como
  `sugerir_diagnóstico`, `recomendar_estudio`, `emitir_alerta` y `solicitar_revisión`.
  En ese sentido, sus acciones no necesariamente tienen que
  modificar directamente el estado del paciente; pueden limitarse a
  proporcionar información que permita tomar mejores decisiones clínicas.

- **Sensors.** Los sensores son las fuentes de información médica que
  recibe el agente. Podemos incluir historiales clínicos, síntomas reportados
  por los pacientes, resultados de laboratorio, imágenes médicas y
  mediciones de dispositivos médicos. También podría recibir información de
  equipos que monitorean constantemente los signos vitales del paciente.

## 7. Dron de inspección de infraestructura

- **Performance.** Una métrica de rendimiento podría considerar la cantidad de
  infraestructura que el agente logró inspeccionar y su capacidad
  para identificar defectos o anomalías. Sin embargo, no bastaría
  con medir la superficie recorrida, porque el objetivo no
  es simplemente desplazarse, sino obtener información útil sobre el
  estado de la infraestructura. Podríamos considerar la precisión con
  la que detecta fisuras, deformaciones o daños, así como
  la calidad de las imágenes obtenidas. También habría que
  considerar el tiempo empleado y el consumo de batería.
  En ese sentido, una métrica de rendimiento podría combinar
  la cobertura de inspección, la precisión de detección y
  la eficiencia del recorrido.

- **Environment.** El ambiente está compuesto por la infraestructura que el
  dron necesita inspeccionar y el espacio físico que la rodea.
  Esto puede incluir puentes, edificios, torres o instalaciones industriales.
  También podemos considerar obstáculos, corrientes de aire, condiciones meteorológicas
  y variaciones en la iluminación. Es un ambiente dinámico
  porque las condiciones pueden cambiar mientras el dron realiza
  la inspección. Además, es parcialmente observable, ya que el
  agente no necesariamente conoce la totalidad de los obstáculos
  o las condiciones de la infraestructura antes de comenzar.
  Ello implica que también es probabilístico. El ambiente es
  continuo porque el movimiento del dron ocurre en un
  espacio tridimensional.

- **Actuators.** Los actuadores son principalmente los motores y las hélices
  que permiten controlar el movimiento del dron. También podemos
  incluir los mecanismos que permiten modificar la orientación de
  la cámara o estabilizarla mientras el agente se desplaza.
  Podríamos expresar estas acciones mediante instrucciones como `despegar`, `desplazar`,
  `girar`, `orientar_cámara`, `capturar_imagen` y `aterrizar`. En ese
  sentido, sus acciones no solamente consisten en moverse hacia
  una posición determinada, sino también en orientar sus instrumentos
  para obtener información de la infraestructura.

- **Sensors.** Los sensores pueden ser cámaras, cámaras térmicas, sensores
  LiDAR y sensores de proximidad. También podemos incluir el
  GPS, los acelerómetros y los giroscopios, que permiten conocer
  la posición y orientación del dron. Estos proporcionan información
  tanto sobre el ambiente como sobre el propio estado del agente.

## 8. Agente jugador de ajedrez

- **Performance.** En este caso la métrica de rendimiento es
  bastante sencilla. El objetivo del agente es ganar la
  partida, por lo que podríamos considerar si logró dar
  jaque mate al oponente. También podemos considerar los empates
  y las derrotas como resultados posibles. En ese sentido,
  una métrica de rendimiento podría ser la cantidad de partidas
  ganadas en relación con el total de partidas jugadas.
  También podríamos considerar el tiempo empleado para realizar los
  movimientos, especialmente cuando se juega con un límite de tiempo.

- **Environment.** El ambiente es simplemente el tablero de ajedrez y
  las piezas que se encuentran sobre él. También debemos
  considerar al oponente y las reglas que determinan los
  movimientos permitidos. A diferencia de otros ejemplos, este es
  un ambiente completamente observable, porque el agente puede conocer
  la posición de todas las piezas en cualquier momento
  de la partida. Es determinista porque las consecuencias de
  cada movimiento están establecidas por las reglas del juego.
  Sin embargo, es multiagente, ya que el oponente también
  toma decisiones y sus acciones afectan directamente al estado
  del ambiente. Además, es discreto, porque el tablero,
  las piezas y los movimientos posibles pueden representarse mediante
  un conjunto finito de estados y acciones.

- **Actuators.** Los actuadores son simplemente los movimientos que el agente
  puede realizar con las piezas. Cada movimiento modifica la
  posición de una o varias piezas dentro del tablero,
  de acuerdo con las reglas del juego. Podríamos expresar
  estas acciones mediante instrucciones como `mover`, `capturar`, `enrocar`,
  `promover` y `ofrecer_tablas`. En ese sentido, las acciones
  del agente están restringidas por el estado actual del
  tablero y por los movimientos permitidos.

- **Sensors.** Los sensores son la información que recibe el agente
  sobre el estado del tablero. Esto incluye la posición
  de todas las piezas, los movimientos realizados por el oponente
  y el tiempo disponible para jugar. En este caso,
  no necesariamente necesitamos sensores físicos, porque la información puede
  recibirse directamente mediante una representación digital del tablero.
