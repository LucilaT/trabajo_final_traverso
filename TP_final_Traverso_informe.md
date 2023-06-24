# Trabajo Final: Manejo de Datos en Biología Computacional - Herramientas de Estadística

## Descripción del sistema y de las variables estudiadas

Se diseñó un experimento con el fin de estudiar un posible rol del gen codificante para el neuropéotido ITG-like en el insecto triatomino _Rhodnius prolixus_. Para ello, se utilizó la técnica de RNA de interferencia para tratar hembras de la especie y se comprobó que la expresión del gen cayó significativamente en los insectos “itg” respecto a los insectos control (“blac”), interferidos para el gen inespecífico B-lactamasa. Los insectos fueron mantenidos en condiciones de cría idénticas, individualizados mediante marcación con pintura acrílica no tóxica.

Con los dos grupos de insectos interferidos se realizó un ensayo de alimentación y análisis de oviposición para evaluar el papel del gen ITG-like en estos procesos fisiológicos. Los insectos utilizados para el ensayo fueron mantenidos en condiciones de cría durante 75 días posteriores al experimento. Durante ese tiempo se registró el número de huevos ovipuestos por cada hembra. El índice de fecundidad (IF) se calculó mediante la fórmula (Ruegg & Davey 1979, doi: 10.1080/01651269.1979.10553294):


> IF= número de huevos ÷ (peso de la hembra en ayunas (mg) × peso de la sangre ingerida (mg) × 1000)


El peso de la sangre ingerida se estimó pesando a la hembra antes e inmediatamente después de la alimentación. Los individuos del grupo control se denominan con el prefijo “blac” y los del grupo tratado con el prefijo “itg”.


## Representación gráfica de las variables estudiadas

A continuación, se muestran los histogramas de las variables estudiadas.

<img src=./peso_sin_alim_histograma.png
     width="50%" 
     height=auto />

<img src=./peso_sing_histograma.png
     width="50%" 
     height=auto />

<img src=./huevos_puestos_histograma.png
     width="50%" 
     height=auto />

<img src=./IF_histograma.png
     width="50%" 
     height=auto />


Dado que el número de individuos en cada grupo es pequeño, no queda graficada de forma clara la distribución de las variables estudiadas.


## Análisis de las medidas características de cada distribución

Dado que las variables medidas son cuantitativas, pueden calcularse una serie de medidas de centralización y dispersión con el fin de obtener una caracterización rápida de la distribución de los datos. Dado que el número de individuos incluidos en el experimento es bajo, la utilidad de estas medidas es limitada.

### Medidas de centralización

#### Media, mediana y moda


En las siguientes tablas se muestran la media, mediana y moda para cada grupo y variable. Para hacer más preciso el cálculo de la moda, se decide redondear los números a dos decimales, a excepción del índice de fecundidad en donde se decide eliminar los decimales para lograr un dato aproximado. En el caso de que no haya una única moda, se muestran todos los valores separados por “;”:

***Peso sin alimentar***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Media |0.090878 |0.0916 |0.0903|
|Mediana |0.0912 |0.092 |0.09|
|Moda |0.09 |0.09 |0.09;0.10|


> La media del peso de los insectos utilizados para el estudio es de 0.09 mg, mientras que no parece haber una diferencia importante entre las medias de los insectos separados por grupo experimental. Si bien la media nos indica el valor central de los datos, la observación de una mediana similar nos indica ausencia de valores extremos. La moda es consistente con este resultado, ya que los valores más abundantes son 0.09 a 0.1 mg.


***Sangre ingerida***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Media |0.148778 |0.138275 |0.15718 |
|Mediana |0.1454 |0.14465 |0.1483 |
|Moda |0.14;0.15 |0.15 |0.14;0.18 |


> La media del peso del volumen ingerido por ambos grupos es 0.14 mg. Al igual que para la variable anterior, la mediana indica que no hay influencia de valores extremos en ese número. Al observar las medias y modas de los grupos por separados, podría observarse una tendencia de los insectos interferidos a ingerir más volumen de sangre.


***Cantidad de huevos***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Media |35.111111 |41.75 |29.8 |
|Mediana |36.0 |45.0 |30.0 |
|Moda |21;22;25;30;36;37;43;47;55 |22;43;47;55 |21;25;30;36;37 |


> En promedio, los insectos en su conjunto ponen 35,1 huevos. Sin embargo, al evaluar las medias de cada grupo por separado, se observa que los insectos del grupo control tienen una media más alta que este número, mientras que los insectos interferidos muestran un valor menor para esta característica. La mediana es similar a la media en el caso de todos los insectos en su conjunto y en el caso del grupo interferido. En el caso de los insectos control, la mediana es mayor, lo que podría indicar la existencia de valores en el extremo inferior.


***Índice de fecundidad***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Media |2.652516 |3.287904 |2.144205 |
|Mediana |2.408478 |3.412443 |2.361922 |
|Moda |2 |3 |2 |


> Al igual que para el número de huevos puestos, la media del índice de fecundidad calculado para los insectos interferidos es menor que la calculada para los insectos en su conjunto, mientras que la media de los insectos control es mayor. La mediana es similar a la media en todos los casos.


#### Cálculo de percentiles
No se realiza el cálculo de percentiles porque se cuenta con un bajo número de individuos en el experimento y el resultado no sería informativo.


### Medidas de dispersión

Las medidas de dispersión se calculan para analizar la variabilidad de los datos, lo que nos ayuda a evaluar la representatividad de las medidas de centralización. Tal como se aclaró anteriormente la utilidad de estas medidas es limitada debido al bajo número de individuos utilizados en el experimento.


#### Rango, recorrido intercuartilo (RI), desviación estándar (SD) y varianza

En las siguientes tablas se muestran el rango, recorrido intercuartilo (RI), desviación estándar (SD) y varianza para cada grupo y variable:


***Peso sin alimentar***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Rango |0.0300 |0.0300 |0.0200 |
|RI |0.0100 |0.0100 |0.0100 |
|SD |0.0095 |0.0126 |0.0077 |
|Varianza |0.0001 |0.0002 |0.0001 |


> En el caso de esta variable, en consistencia con lo observado para las medidas de centralización no se observa una gran influencia de valores extremos: el rango y el recorrido intercuartilo presentan un valor bajo en todos los casos. La desviación estándar es más alta en los insectos control; dado que en este caso no hay una gran influencia de valores extremos es un estadístico válido para evaluar dispersión. La varianza nos indica que en todos los casos existe muy poca variabilidad de los datos con respecto a la media calculada.


***Sangre ingerida***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Rango |0.0700 | 0.0500 |0.0500 |
|RI |0.0200 |0.0100 |0.0400 |
|SD |0.0226 |0.0198 |0.0230 |
|Varianza |0.0005 |0.0004 |0.0005 |


> En el caso de esta variable, se observa una dispersión un poco mayor que para el caso anterior, tal como puede observarse con el rango y la desviación estándar calculados.


***Huevos puestos***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Rango |34.0000 | 33.0000 |15.0000 |
|RI |18.0000 |11.2500 |11.0000 |
|SD |11.7414 |14.0801 |6.9065 |
|Varianza |137.8611 |198.2500 |47.7000 |


> En el caso de huevos puestos, se observa una menor dispersión de los datos del grupo interferido en todas las medidas calculadas.


***Indice de fecundidad***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Rango |3.1000 |2.2900 |1.2900 |
|RI |1.1000 |0.6800 |0.1700 |
|SD |0.9173 |0.9488 |0.5303 |
|Varianza |0.8415 |0.9002 |0.2812 |


> En el caso del índice de fecundidad, similar a lo observado para la variable analizada anteriormente, se observa una menor dispersión de los datos del grupo interferido en todas las medidas calculadas.


#### Coeficientes de variación, asimetría y curtosis

***Coeficientes de variación para cada grupo y variable***

Para analizar la dispersión de manera comparativa (independientemente de la unidad de medida de la variable), se calculó el coeficiente de variación de Pearson.

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Peso sin alimentar |0.1042 |0.1375 |0.0853 |
|Sangre ingerida |0.1518 |0.1432 |0.1462 |
|Huevos puestos |0.3344 |0.3372 |0.2318 |
|Índice de fecundidad |0.3458 |0.2886 |0.2473 |


> Se observa una manor variación en el caso del grupo interferido, especialmente para Huevos puestos e Índice de fecundidad.


Para estudiar la simetría de los datos y su concentración con respecto a la medida central, se complementan los análisis anteriores con el calculo de coeficientes de asimetría y curtosis. Sin embargo, tal como se observó en los histogramas graficados, el número de individuos analizado es bajo lo que compromete la utilidad de estos coeficientes.


***Coeficientes de asimetría para cada grupo y variable***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Peso sin alimentar |-0.2356 |-0.1892 |-1.1824 |
|Sangre ingerida |0.1183 |-1.6611 |0.4572 |
|Huevos puestos |0.3788 |-1.2493 |-0.2283 |
|Índice de fecundidad |0.4345 |-0.7636 |-2.0583 |


> En el caso de peso sin alimentar, se observa una asimetría a la izquierda (es decir, hacia los valores más bajos de la distribución), especialmente para el grupo interferido. En el caso de la sangre ingerida, los valores de asimetría difieren entre los grupos: se observa una asimetria hacia la derecha para ambos grupos y para el grupo interferido, mientras que ocurre lo contrario para el grupo control. En el caso de huevos puestos e índice de fecundidad, la asimentría es hacia la izquierda para ambos grupos experimentales.


***Coeficientes de curtosis para cada grupo y variable***

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Peso sin alimentar |0.1860 |1.4398 |1.4266 |
|Sangre ingerida |0.4569 |3.1187 |-2.9980 |
|Huevos puestos |-0.8976 |2.0826 |-2.1256 |
|Índice de fecundidad |0.2569 |1.7243 |4.3544 |


> En el caso de peso sin alimentar, los coeficientes indican una distribución leptocúrtica (mayoría de datos alrededor del valor central). En el caso de la sangre ingerida y huevos puestos, se observa distribución leptocúrtica para el grupo control, mientras que el grupo interferido presenta distribución platicúrtica. La variable índice de fecundidad presenta distribución leptocúrtica en ambos grupos.


## Estimación de intervalos de confianza

Para realizar la estimación de los intervalos de confianza se utilizará la distribución T de student porque la varianza poblacional es desconocida y el n < 30. En la siguiente tabla se muestran los Intervalos de Confianza (95%) estimados en base a cada grupo y variable:

|Característica |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Peso sin alimentar |[0.08, 0.1] |[0.07, 0.11] |[0.08, 0.1] |
|Sangre ingerida |[0.13, 0.17] |[0.11, 0.17] |[0.13, 0.19] |
|Huevos puestos |[26.09, 44.14] |[19.35, 64.15] |[21.22, 38.38] |
|Índice de fecundidad |[1.95, 3.36] |[1.78, 4.8] |[1.49, 2.8] |


> Estos datos nos muestran que existe un 95% de probabilidad de que los intervalos calculados contengan el valor real de esa variable en la población.


## Determinación del tamaño de la muestra


Con el fin de determinar si la cantidad de individuos que forman parte del ensayo son suficientes para abordar el análisis de las variables de interés, se realizó una determinación del tamaño de la muestra utilizando la función _TTestIndPower_ de la librería _statsmodels.stats.power_.
              
El tamaño muestral necesario para Peso sin alimentar es: 751

El tamaño muestral necesario para Peso sangre ingerida es: 21

El tamaño muestral necesario para Huevos puestos es: 15

El tamaño muestral necesario para Índice de fecundidad es: 751


> Con los resultados puede concluirse que el número de individuos incluidos en el diseño experimental es muy insuficiente. Si no se hallan diferencias significativas en las comparaciones de medias, los resultados no pueden tomarse como representativos de las poblaciones ya que podrían modificarse (es decir, podrían hallarse diferencias significativas) utilizando un número de individuos mayor.


## Ensayos de hipótesis

### Comparación de medias

Para poder testear la hipótesis de si que el gen ITG-like tiene un rol en la reproducción de la especie estudiada, se planea comparar las medias de las variables analizadas utilizando la prueba de T de student. Para aplicar esta prueba, deben comprobarse una serie de supuestos que se detallan y evalúan a continuación.


***Tipo de datos, independencia de las muestras y número de individuos y grupos analizados***

Se trata de un set de datos cuantitativos, con un tamaño muestral < 30 compuesto por dos grupos de muestras independientes. Estas características son apropiadas para un análisis de comparación de medias por T de student.


***Homocedasticidad***

La homocedasticidad se chequea mediante el test de Levene, planteando las siguientes hipótesis:

H0: Las varianzas de los grupos comparados son homogéneas
H1: Las varianzas de los grupos comparados no son homogéneas

En este caso, se compara para cada variable el grupo control y el interferido. En la siguiente tabla se muestra el resultado del test para cada variable:

|Peso sin alimentar |Sangre ingerida |Huevos puestos |Índice de fecundidad |
|--------------- |------------- |------------- |------------------ |
|[0.416, 0.539] |[0.356, 0.569] |[0.678, 0.437] |[0.701, 0.429] |

> Las varianzas son homogéneas en todos los casos (p > 0.05) por lo que se acepta la hipótesis nula, cumpliéndose este supuesto en todos los casos.


***Normalidad de los datos***

La normalidad se chequea mediante el test de Shapiro-Wilk, planteando las siguientes hipótesis:


H0: La variable se distribuye normalmente
H1: La variable no se distribuye normalmente

Este test se aplica tanto para los grupos por separado, como para los grupos en su conjunto y para cada variable analizada. En la siguiente tabla se muestra el estadístico resultante del test en cada caso, y su correspondiente valor p.

|Variable |Ambos grupos |Grupo control |Grupo interferido |
|---------------|-------------|------------- |------------------|
|Peso sin alimentar |[0.936, 0.548] |[0.964, 0.808] |[0.860, 0.229] |
|Sangre ingerida |[0.934, 0.522] |[0.826, 0.158] |[0.839, 0.163] |
|Huevos puestos |[0.949, 0.680] |[0.916, 0.516] |[0.925, 0.566] |
|Índice de fecundidad |[0.952, 0.713] |[0.947, 0.698] |[0.719, 0.015] |

> A excepción del índice de fecundidad, las variables se distribuyen normalmente (p > 0.05), por lo que se acepta la hipótesis nula. En el caso del IF la hipótesis nula se rechaza con un p = 0.015. Esto puede deberse a que la muestra es muy pequeña: como ya se determinó, el tamaño muestral necesario para analizar esta variable es 751. Para este caso, se realizará una prueba de T y también un test no paramétrico para evaluar los resultados.


#### Prueba de T

Para cada variable, se plantean las siguientes hipótesis:

H0: Las medias de los grupos analizados no son diferentes
H1: Las medias de los grupos analizados son diferentes

Los resultados obtenidos para la prueba de T  para cada variable (estadísitico y valor p asociado) se muestran en la siguiente tabla:

|Peso sin alimentar |Sangre ingerida |Huevos puestos |Índice de fecundidad |
|--------------- |------------- |------------- |------------------ |
|[0.191,0.853] |[-1.300, 0.234] |[1.681, 0.136] |[2.306, 0.054] |

> Como puede observarse, no hay diferencias significativas entre el tamaño de los individuos que forman parte de cada grupo, ni en la cantidad de sangre ingerida por los mismos. Tampoco se observan diferencias en la oviposición. Sin embargo, como se mencionó anteriormente, es importante tener en cuenta que se está trabajando con un número inferior al tamaño muestral requerido para esta comparación, por lo que el resultado podría cambiar con el aumento de individuos. 

> En cuanto al índice de fecundidad, se observa una diferencia significativa con un valor p =0.054. Sin embargo, para esta variable no se observó una distribución normal, lo cual limita la utilidad de la prueba de T aplicada. Si bien es probable que esto se deba a que se está trabajando con un bajo número de individuos, no puede tomarse este resultado como válido. Se realiza a continuación un análisis no paramétrico.


### Análisis no paramétrico

Se elige la prueba U de Mann-Whitney, dado que se trata de datos continuos pertenecientes a dos grupos de muestras independientes con varianzas homogéneas.

	H0: La probabilidad de que una observación al azar del grupo 1 exceda a una observación al azar del grupo 2 es igual a la probabilidad de que una observación al azar del grupo 2 exceda a una observación al azar del grupo 1.
	H1: La probabilidad de que una observación al azar del grupo 1 exceda a una observación al azar del grupo 2 es diferente a la probabilidad de que una observación al azar del grupo 2 exceda a una observación al azar del grupo 1.

> Los resultados obtenidos para este análisis indican que no se puede rechazar la hipótesis nula (p = 0.19, estadístico = 16). Por lo tanto, la distribución de los grupos analizados es la misma.

> Sería deseable aumentar el número de individuos analizados para evaluar si se alcanza la normalidad de los datos y con ellos repetir la prueba de T para tener un resultado confiable sobre la diferencia entre las medias de los grupos.


### Análisis de dependencia de variables categóricas

Con el fin de realizar un análisis de datos categóricos utilizando el mismo set de datos, se realiza una discretización de la variable Índice de Fecundidad. Para ello, se clasifican los índices en alto/bajo, tomando como bajo un Índice de Fecundidad menor a 2.51, y como alto un valor mayor a ese número. Como resultado, se obtiene la siguiente tabla de contingencia:

|------------------ |Grupo control	|Grupo interferido |Total |
|------------------ |------------------ |----------------------- |------- |
|IF bajo (<2.51) |1 |5 |6 |
|IF alto (>2.51) |3 |0 |3 |
|Total |4 |5 |9 |

Para llevar a cabo este análisis se decidió aplicar el test de Fisher debido a que la cantidad de individuos que componen cada grupo es pequeña. Se plantean las siguientes hipótesis:

	H0: El índice de fecundidad es independiente del tratamiento de interferencia.
	H1: El índice de fecundidad depende del tratamiento de interferencia recibido.

> El test de Fisher para la tabla de contingencia analizada arrojó un estadístico de 0 con un p-value de 0.047. Por lo tanto, según este test podemos rechazar la hipótesis nula: el índice de fecundidad depende del tratamiento recibido, con una probabilidad de encontrar este resultado al azar de 4,7%.

> Es importante tener en cuenta que este resultado se obtiene a partir de una clasificación (fecundidad alta/baja) establecida con un punto de corte arbitrario. Asimismo, el número de individuos es muy bajo. Sería deseable aumentar el número de individuos para evaluar la validez del punto de corte establecido.


### Análisis de correlación

Con el fin de evaluar la relación lineal entre el peso sin alimentar y los huevos puestos por cada individuo con respecto a la sangre ingerida, se plantea el cálculo del coeficiente de correlación de Pearson y su correspondiente valor p.

	H0: Las variables no están correlacionadas
	H1: Las variables están correlacionadas

> El resultado del cálculo arrojó un coeficiente de correlación de 0.266 (con un valor de p = 0.487) para las variables _peso sin alimentar_ y _sangre ingerida_, mientras que para _huevos puestos_ y _sangre ingerida_ el coeficiente es de -0.166 (p value = 0.66). A continuación, se muestran los gráficos resultantes, en donde puede visualizarse claramente la falta de correlación:

<img src=./peso_sing_vs_pesp_sin_alim_corr.png
     width="50%" 
     height=auto />

<img src=./huevosp_vs_peso_si_corr.png
     width="50%" 
     height=auto />

> Los resultados nos indican que en ninguno de los dos casos se rechaza la hipótesis nula, por lo que en el set de datos analizados la sangre ingerida no está correlacionada con el peso sin alimentar ni con el número de huevos puestos.

El análisis de correlación se repite utilizando también sólo el grupo control, para descartar que la falta de correlación observada se deba a la influencia del tratamiento que reciben los individuos del grupo tratado. Este análisis tampoco arrojó correlación en ningún caso (con un estadístico de 0.231 y un valor p de 0.768 para el caso de _peso sin alimentar_ y _sangre ingerida_ y un estadístico de  0.124 y un valor p de 0.875 para el caso de _huevos puestos_ y _sangre ingerida_). 

> El Índice de Fecundidad utilizado se compone de estas tres variables y es aceptado como un indicador válido de la fecundidad de estos insectos. Sin embargo, con los datos analizados no se halla correlación entre las variables. Considerando que se está trabajando con un número muy bajo de individuos, es probable que este hecho explique la falta de correlación observada.


## Conclusiones generales

Los datos analizados muestran una tendencia de los insectos interferidos a tener menor fecundidad que los insectos control, lo que indicaría un rol del gen ITG-like en alguno de los procesos relacionados a la fecundidad en la especie estudiada. Para una confirmación estadística válida, sería necesario aumentar el número de individuos incluídos en el experimento. Un número mayor de individuos sería útil también para analizar si para el caso de este diseño experimental es necesario plantear cambios en la forma de calcular el índice de fecundidad.

