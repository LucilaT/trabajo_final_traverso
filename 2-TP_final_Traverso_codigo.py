import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
from statsmodels.stats.power import TTestIndPower
import numpy as np
import seaborn as sns

#carga de la tabla de datos

path = "./tabla_final.tsv"
tabla = pd.read_csv(path, sep="\t")

#nueva tabla para cada grupo, solo con variable "peso sin alimentar"

psa_control = tabla[["insecto","peso_sin_alimentar"]].iloc[0:4]
psa_int = tabla[["insecto","peso_sin_alimentar"]].iloc[4:9]

#nueva tabla para cada grupo, solo con variable "peso de la sangre ingerida"

psi_control = tabla[["insecto","peso_sangre_ingerida"]].iloc[0:4]
psi_int = tabla[["insecto","peso_sangre_ingerida"]].iloc[4:9]

#nueva tabla para cada grupo, solo con variable "número de huevos puestos"

hp_control = tabla[["insecto","huevos_puestos"]].iloc[0:4]
hp_int = tabla[["insecto","huevos_puestos"]].iloc[4:9]

#nueva tabla para cada grupo, solo con variable "índice de fecundidad"

if_control = tabla[["insecto","indice_de_fecundidad"]].iloc[0:4]
if_int = tabla[["insecto","indice_de_fecundidad"]].iloc[4:9]

#CREACIÓN DE HISTOGRAMAS

plt.hist([psa_control["peso_sin_alimentar"], psa_int["peso_sin_alimentar"]], bins=8, label = ["control", "interferidos"])
plt.title('Peso de los insectos sin alimentar - Histograma')
plt.legend()
plt.show()

plt.hist([psi_control["peso_sangre_ingerida"], psi_int["peso_sangre_ingerida"]], bins=8, label = ["control", "interferidos"])
plt.title('Peso de la sangre ingerida - Histograma')
plt.legend()
plt.show()

plt.hist([hp_control["huevos_puestos"], hp_int["huevos_puestos"]], bins=8, label = ["control", "interferidos"])
plt.title('Huevos puestos - Histograma')
plt.legend()
plt.show()

plt.hist([if_control["indice_de_fecundidad"], if_int["indice_de_fecundidad"]], bins=8, label = ["control", "interferidos"])
plt.title('Índice de fecundidad - Histograma')
plt.legend()
plt.show()

#MEDIDAS CARACTERÍSTICAS
#1. MEDIDAS DE CENTRALIZACIÓN

#MEDIA, MEDIANA Y MODA

#peso sin alimentar

media_psa_total = tabla["peso_sin_alimentar"].mean()
media_psa_control = psa_control["peso_sin_alimentar"].mean()
media_psa_int = psa_int["peso_sin_alimentar"].mean()

mediana_psa_total = tabla["peso_sin_alimentar"].median()
mediana_psa_control = psa_control["peso_sin_alimentar"].median()
mediana_psa_int = psa_int["peso_sin_alimentar"].median()

#se redondea a 2 decimales para ser más precisos en el cálculo de la moda

moda_psa_total = tabla["peso_sin_alimentar"].round(decimals=2).mode()
moda_psa_control = psa_control["peso_sin_alimentar"].round(decimals=2).mode()
moda_psa_int = psa_int["peso_sin_alimentar"].round(decimals=2).mode()

caracteristicas_psa_dict = {'Característica': ["Media","Mediana","Moda"], 'Ambos grupos': [media_psa_total,mediana_psa_total, (moda_psa_total.to_string(index=False)).replace("\n",";")], 'Grupo control':[media_psa_control,mediana_psa_control, (moda_psa_control.to_string(index=False)).replace("\n",";")], 'Grupo interferido' : [media_psa_int,mediana_psa_int,(moda_psa_int.to_string(index=False)).replace("\n",";")]}
print("En la siguiente tabla se muestran las características calculadas para Peso sin alimentar en cada grupo. En el caso de que no haya una única moda, se muestran todos los valores separados por ;")
caracteristicas_psa = pd.DataFrame(data=caracteristicas_psa_dict)
caracteristicas_psa_mostrar = caracteristicas_psa.to_string(index=False)
print(caracteristicas_psa_mostrar)

#sangre ingerida

media_psi_total = tabla["peso_sangre_ingerida"].mean()
media_psi_control = psi_control["peso_sangre_ingerida"].mean()
media_psi_int = psi_int["peso_sangre_ingerida"].mean()

mediana_psi_total = tabla["peso_sangre_ingerida"].median()
mediana_psi_control = psi_control["peso_sangre_ingerida"].median()
mediana_psi_int = psi_int["peso_sangre_ingerida"].median()

#se redondea a 2 decimales para hacer más preciso el cálculo de la moda

moda_psi_total = tabla["peso_sangre_ingerida"].round(decimals=2).mode()
moda_psi_control = psi_control["peso_sangre_ingerida"].round(decimals=2).mode()
moda_psi_int = psi_int["peso_sangre_ingerida"].round(decimals=2).mode()

caracteristicas_psi_dict = {'Característica': ["Media","Mediana","Moda"], 'Ambos grupos': [media_psi_total, mediana_psi_total,(moda_psi_total.to_string(index=False)).replace("\n",";")], 'Grupo control':[media_psi_control, mediana_psi_control,(moda_psi_control.to_string(index=False)).replace("\n",";")], 'Grupo interferido' : [media_psi_int, mediana_psi_int,(moda_psi_int.to_string(index=False)).replace("\n",";")]}
print("En la siguiente tabla se muestran las características calculadas para Sangre ingerida en cada grupo. En el caso de que no haya una única moda, se muestran todos los valores separados por ;")
caracteristicas_psi = pd.DataFrame(data=caracteristicas_psi_dict)
caracteristicas_psi_mostrar = caracteristicas_psi.to_string(index=False)
print(caracteristicas_psi_mostrar)

#huevos puestos

media_hp_total = tabla["huevos_puestos"].mean()
media_hp_control = hp_control["huevos_puestos"].mean()
media_hp_int = hp_int["huevos_puestos"].mean()

mediana_hp_total = tabla["huevos_puestos"].median()
mediana_hp_control = hp_control["huevos_puestos"].median()
mediana_hp_int = hp_int["huevos_puestos"].median()

moda_hp_total = tabla["huevos_puestos"].astype(int).mode()
moda_hp_control = hp_control["huevos_puestos"].astype(int).mode()
moda_hp_int = hp_int["huevos_puestos"].astype(int).mode()

#en caso de que no haya una moda, se muestran todos los valores separados por ";"

caracteristicas_hp_dict = {'Característica': ["Media","Mediana","Moda"], 'Ambos grupos': [media_hp_total,mediana_hp_total,(moda_hp_total.to_string(index=False)).replace("\n",";")], 'Grupo control':[media_hp_control,mediana_hp_control,(moda_hp_control.to_string(index=False)).replace("\n",";")], 'Grupo interferido': [media_hp_int,mediana_hp_int,(moda_hp_int.to_string(index=False)).replace("\n",";")]}
print("En la siguiente tabla se muestran las características calculadas para Cantidad de huevos puestos por cada grupo. En el caso de que no haya una única moda, se muestran todos los valores separados por ;")
caracteristicas_hp = pd.DataFrame(data=caracteristicas_hp_dict)
caracteristicas_hp_mostrar = caracteristicas_hp.to_string(index=False)
print(caracteristicas_hp_mostrar)

#indice de fecundidad

media_if_total = tabla["indice_de_fecundidad"].mean()
media_if_control = if_control["indice_de_fecundidad"].mean()
media_if_int = if_int["indice_de_fecundidad"].mean()

mediana_if_total = tabla["indice_de_fecundidad"].median()
mediana_if_control = if_control["indice_de_fecundidad"].median()
mediana_if_int = if_int["indice_de_fecundidad"].median()

#como no hay dos valores iguales por tratarse de enteros con decimales, se eliminan decimales para tener
#una moda aproximada

moda_if_total = tabla["indice_de_fecundidad"].astype(int).mode()
moda_if_control = if_control["indice_de_fecundidad"].astype(int).mode()
moda_if_int = if_int["indice_de_fecundidad"].astype(int).mode()

caracteristicas_if_dict = {'Característica': ["Media","Mediana","Moda"], 'Ambos grupos': [media_if_total,mediana_if_total,(moda_if_total.to_string(index=False)).replace("\n",";")], 'Grupo control':[media_if_control,mediana_if_control,(moda_if_control.to_string(index=False)).replace("\n",";")], 'Grupo interferido': [media_if_int,mediana_if_int,(moda_if_int.to_string(index=False)).replace("\n",";")]}
caracteristicas_if = pd.DataFrame(data=caracteristicas_if_dict)
print("En la siguiente tabla se muestran las características calculadas para Índice de fecundidad en cada grupo. En el caso de que no haya una única moda, se muestran todos los valores separados por ;")
caracteristicas_if_mostrar = caracteristicas_if.to_string(index=False)
print(caracteristicas_if_mostrar)

#2. MEDIDAS DE DISPERSIÓN

#RECORRIDOS, VARIANZA Y DESVIACIÓN TÍPICA

#peso sin alimentar

rango_psa_total = tabla["peso_sin_alimentar"].max() - tabla["peso_sin_alimentar"].min()
rango_psa_control = psa_control["peso_sin_alimentar"].max() - psa_control["peso_sin_alimentar"].min()
rango_psa_int = psa_int["peso_sin_alimentar"].max() - psa_int["peso_sin_alimentar"].min()

ri_psa_total = tabla["peso_sin_alimentar"].quantile(0.75) - tabla["peso_sin_alimentar"].quantile(0.25)
ri_psa_control = psa_control["peso_sin_alimentar"].quantile(0.75) - psa_control["peso_sin_alimentar"].quantile(0.25)
ri_psa_int = psa_int["peso_sin_alimentar"].quantile(0.75) - psa_int["peso_sin_alimentar"].quantile(0.25)

sd_psa_total = tabla["peso_sin_alimentar"].std(axis=None)
sd_psa_control = psa_control["peso_sin_alimentar"].std(axis=None)
sd_psa_int = psa_int["peso_sin_alimentar"].std(axis=None)

var_psa_total = tabla["peso_sin_alimentar"].var(axis=None)
var_psa_control = psa_control["peso_sin_alimentar"].var(axis=None)
var_psa_int = psa_int["peso_sin_alimentar"].var(axis=None)

caracteristicas_disp_psa_dict = {'Característica': ["Rango","RI","SD","Varianza"], 'Ambos grupos': [rango_psa_total.round(decimals=2),ri_psa_total.round(decimals=2),sd_psa_total.round(decimals=4),var_psa_total.round(decimals=4)], 'Grupo control':[rango_psa_control.round(decimals=2),ri_psa_control.round(decimals=2),sd_psa_control.round(decimals=4),var_psa_control.round(decimals=4)], 'Grupo interferido': [rango_psa_int.round(decimals=2),ri_psa_int.round(decimals=2),sd_psa_int.round(decimals=4),var_psa_int.round(decimals=4)]}
caracteristicas_disp_psa = pd.DataFrame(data=caracteristicas_disp_psa_dict)
print("En la siguiente tabla se muestran las medidas de dispersión para Peso sin alimentar en cada grupo:")
caracteristicas_disp_psa_mostrar = caracteristicas_disp_psa.to_string(index=False)
print(caracteristicas_disp_psa_mostrar)

#sangre ingerida

rango_psi_total = tabla["peso_sangre_ingerida"].max() - tabla["peso_sangre_ingerida"].min()
rango_psi_control = psi_control["peso_sangre_ingerida"].max() - psi_control["peso_sangre_ingerida"].min()
rango_psi_int = psi_int["peso_sangre_ingerida"].max() - psi_int["peso_sangre_ingerida"].min()

ri_psi_total = tabla["peso_sangre_ingerida"].quantile(0.75) - tabla["peso_sangre_ingerida"].quantile(0.25)
ri_psi_control = psi_control["peso_sangre_ingerida"].quantile(0.75) - psi_control["peso_sangre_ingerida"].quantile(0.25)
ri_psi_int = psi_int["peso_sangre_ingerida"].quantile(0.75) - psi_int["peso_sangre_ingerida"].quantile(0.25)

sd_psi_total = tabla["peso_sangre_ingerida"].std(axis=None)
sd_psi_control = psi_control["peso_sangre_ingerida"].std(axis=None)
sd_psi_int = psi_int["peso_sangre_ingerida"].std(axis=None)

var_psi_total = tabla["peso_sangre_ingerida"].var(axis=None)
var_psi_control = psi_control["peso_sangre_ingerida"].var(axis=None)
var_psi_int = psi_int["peso_sangre_ingerida"].var(axis=None)

caracteristicas_disp_psi_dict = {'Característica': ["Rango","RI","SD","Varianza"], 'Ambos grupos': [rango_psi_total.round(decimals=2),ri_psi_total.round(decimals=2),sd_psi_total.round(decimals=4),var_psi_total.round(decimals=4)], 'Grupo control':[rango_psi_control.round(decimals=2),ri_psi_control.round(decimals=2),sd_psi_control.round(decimals=4),var_psi_control.round(decimals=4)], 'Grupo interferido': [rango_psi_int.round(decimals=2),ri_psi_int.round(decimals=2),sd_psi_int.round(decimals=4),var_psi_int.round(decimals=4)]}
caracteristicas_disp_psi = pd.DataFrame(data=caracteristicas_disp_psi_dict)
print("En la siguiente tabla se muestran las medidas de dispersión para Sangre ingerida en cada grupo:")
caracteristicas_disp_psi_mostrar = caracteristicas_disp_psi.to_string(index=False)
print(caracteristicas_disp_psi_mostrar)

#huevos puestos

rango_hp_total = tabla["huevos_puestos"].max() - tabla["huevos_puestos"].min()
rango_hp_control = hp_control["huevos_puestos"].max() - hp_control["huevos_puestos"].min()
rango_hp_int = hp_int["huevos_puestos"].max() - hp_control["huevos_puestos"].min()

ri_hp_total = tabla["huevos_puestos"].quantile(0.75) - tabla["huevos_puestos"].quantile(0.25)
ri_hp_control = hp_control["huevos_puestos"].quantile(0.75) - hp_control["huevos_puestos"].quantile(0.25)
ri_hp_int = hp_int["huevos_puestos"].quantile(0.75) - hp_int["huevos_puestos"].quantile(0.25)

sd_hp_total = tabla["huevos_puestos"].std(axis=None)
sd_hp_control = hp_control["huevos_puestos"].std(axis=None)
sd_hp_int = hp_int["huevos_puestos"].std(axis=None)

var_hp_total = tabla["huevos_puestos"].var(axis=None)
var_hp_control = hp_control["huevos_puestos"].var(axis=None)
var_hp_int = hp_int["huevos_puestos"].var(axis=None)

caracteristicas_disp_hp_dict = {'Característica': ["Rango","RI","SD","Varianza"], 'Ambos grupos': [rango_hp_total.round(decimals=2),ri_hp_total.round(decimals=2),sd_hp_total.round(decimals=4),var_hp_total.round(decimals=4)], 'Grupo control':[rango_hp_control.round(decimals=2),ri_hp_control.round(decimals=2),sd_hp_control.round(decimals=4),var_hp_control.round(decimals=4)], 'Grupo interferido': [rango_hp_int.round(decimals=2),ri_hp_int.round(decimals=2),sd_hp_int.round(decimals=4),var_hp_int.round(decimals=4)]}
caracteristicas_disp_hp = pd.DataFrame(data=caracteristicas_disp_hp_dict)
print("En la siguiente tabla se muestran las medidas de dispersión para Huevos puestos en cada grupo:")
caracteristicas_disp_hp_mostrar = caracteristicas_disp_hp.to_string(index=False)
print(caracteristicas_disp_hp_mostrar)

#Índice de fecundidad

rango_if_total = tabla["indice_de_fecundidad"].max() - tabla["indice_de_fecundidad"].min()
rango_if_control = if_control["indice_de_fecundidad"].max() - if_control["indice_de_fecundidad"].min()
rango_if_int = if_int["indice_de_fecundidad"].max() - if_int["indice_de_fecundidad"].min()

ri_if_total = tabla["indice_de_fecundidad"].quantile(0.75) - tabla["indice_de_fecundidad"].quantile(0.25)
ri_if_control = if_control["indice_de_fecundidad"].quantile(0.75) - if_control["indice_de_fecundidad"].quantile(0.25)
ri_if_int = if_int["indice_de_fecundidad"].quantile(0.75) - if_int["indice_de_fecundidad"].quantile(0.25)

sd_if_total = tabla["indice_de_fecundidad"].std(axis=None)
sd_if_control = if_control["indice_de_fecundidad"].std(axis=None)
sd_if_int = if_int["indice_de_fecundidad"].std(axis=None)

var_if_total = tabla["indice_de_fecundidad"].var(axis=None)
var_if_control = if_control["indice_de_fecundidad"].var(axis=None)
var_if_int = if_int["indice_de_fecundidad"].var(axis=None)

caracteristicas_disp_if_dict = {'Característica': ["Rango","RI","SD","Varianza"], 'Ambos grupos': [rango_if_total.round(decimals=2),ri_if_total.round(decimals=2),sd_if_total.round(decimals=4),var_if_total.round(decimals=4)], 'Grupo control':[rango_if_control.round(decimals=2),ri_if_control.round(decimals=2),sd_if_control.round(decimals=4),var_if_control.round(decimals=4)], 'Grupo interferido': [rango_if_int.round(decimals=2),ri_if_int.round(decimals=2),sd_if_int.round(decimals=4),var_if_int.round(decimals=4)]}
caracteristicas_disp_if = pd.DataFrame(data=caracteristicas_disp_if_dict)
print("En la siguiente tabla se muestran las medidas de dispersión para Indice de fecundidad en cada grupo:")
caracteristicas_disp_if_mostrar = caracteristicas_disp_if.to_string(index=False)
print(caracteristicas_disp_if_mostrar)

#coeficiente de variación de Pearson

CV_psa_total = sd_psa_total/ media_psa_total
CV_psa_control = sd_psa_control / media_psa_control
CV_psa_int = sd_psa_int / media_psa_int

CV_psi_total = sd_psi_total / media_psi_total
CV_psi_control = sd_psi_control/ media_psi_control
CV_psi_int = sd_psi_int / media_psi_int

CV_hp_total = sd_hp_total / media_hp_total
CV_hp_control = sd_hp_control/ media_hp_control
CV_hp_int = sd_hp_int / media_hp_int

CV_if_total = sd_if_total / media_if_total
CV_if_control = sd_if_control/ media_if_control
CV_if_int = sd_if_int / media_if_int

cv_todas_dict = {'Característica': ["Peso sin alimentar","Sangre ingerida","Huevos puestos","Índice de fecundidad"], 'Ambos grupos': [CV_psa_total.round(decimals=4),CV_psi_total.round(decimals=4),CV_hp_total.round(decimals=4),CV_if_total.round(decimals=4)], 'Grupo control':[CV_psa_control.round(decimals=4),CV_psi_control.round(decimals=4),CV_hp_control.round(decimals=4),CV_if_control.round(decimals=4)], 'Grupo interferido': [CV_psa_int.round(decimals=4),CV_psi_int.round(decimals=4),CV_hp_int.round(decimals=4),CV_if_int.round(decimals=4)]}
cv_todas = pd.DataFrame(data=cv_todas_dict)
print("En la siguiente tabla se muestran los Coeficientes de variacón de cada grupo y variable:")
cv_todas_mostrar = cv_todas.to_string(index=False)
print(cv_todas_mostrar)

#asimetría

sk_psa_total = tabla["peso_sin_alimentar"].skew()
sk_psa_control = psa_control["peso_sin_alimentar"].skew()
sk_psa_int = psa_int["peso_sin_alimentar"].skew()

sk_psi_total = tabla["peso_sangre_ingerida"].skew()
sk_psi_control = psi_control["peso_sangre_ingerida"].skew()
sk_psi_int = psi_int["peso_sangre_ingerida"].skew()

sk_hp_total = tabla["huevos_puestos"].skew()
sk_hp_control = hp_control["huevos_puestos"].skew()
sk_hp_int = hp_int["huevos_puestos"].skew()

sk_if_total = tabla["indice_de_fecundidad"].skew()
sk_if_control = if_control["indice_de_fecundidad"].skew()
sk_if_int = if_int["indice_de_fecundidad"].skew()

sk_todas_dict = {'Característica': ["Peso sin alimentar","Sangre ingerida","Huevos puestos","Índice de fecundidad"], 'Ambos grupos': [sk_psa_total.round(decimals=4),sk_psi_total.round(decimals=4),sk_hp_total.round(decimals=4),sk_if_total.round(decimals=4)], 'Grupo control':[sk_psa_control.round(decimals=4),sk_psi_control.round(decimals=4),sk_hp_control.round(decimals=4),sk_if_control.round(decimals=4)], 'Grupo interferido': [sk_psa_int.round(decimals=4),sk_psi_int.round(decimals=4),sk_hp_int.round(decimals=4),sk_if_int.round(decimals=4)]}
sk_todas = pd.DataFrame(data=sk_todas_dict)
print("En la siguiente tabla se muestran los Coeficientes de asimetría de cada grupo y variable:")
sk_todas_mostrar = sk_todas.to_string(index=False)
print(sk_todas_mostrar)

#curtosis

kurt_psa_total = tabla["peso_sin_alimentar"].kurt()
kurt_psa_control = psa_control["peso_sin_alimentar"].kurt()
kurt_psa_int = psa_int["peso_sin_alimentar"].kurt()

kurt_psi_total = tabla["peso_sangre_ingerida"].kurt()
kurt_psi_control = psi_control["peso_sangre_ingerida"].kurt()
kurt_psi_int = psi_int["peso_sangre_ingerida"].kurt()

kurt_hp_total = tabla["huevos_puestos"].kurt()
kurt_hp_control = hp_control["huevos_puestos"].kurt()
kurt_hp_int = hp_int["huevos_puestos"].kurt()

kurt_if_total = tabla["indice_de_fecundidad"].kurt()
kurt_if_control = if_control["indice_de_fecundidad"].kurt()
kurt_if_int = if_int["indice_de_fecundidad"].kurt()

kurt_todas_dict = {'Característica': ["Peso sin alimentar","Sangre ingerida","Huevos puestos","Índice de fecundidad"], 'Ambos grupos': [kurt_psa_total.round(decimals=4),kurt_psi_total.round(decimals=4),kurt_hp_total.round(decimals=4),kurt_if_total.round(decimals=4)], 'Grupo control':[kurt_psa_control.round(decimals=4),kurt_psi_control.round(decimals=4),kurt_hp_control.round(decimals=4),kurt_if_control.round(decimals=4)], 'Grupo interferido': [kurt_psa_int.round(decimals=4),kurt_psi_int.round(decimals=4),kurt_hp_int.round(decimals=4),kurt_if_int.round(decimals=4)]}
kurt_todas = pd.DataFrame(data=kurt_todas_dict)
print("En la siguiente tabla se muestran los Coeficientes de curtosis de cada grupo y variable:")
kurt_todas_mostrar = kurt_todas.to_string(index=False)
print(kurt_todas_mostrar)

#3. ESTIMACIÓN DE INTERVALOS DE CONFIANZA

ic_95_psa_total = st.t.interval(confidence = 0.95, df = len(tabla["peso_sin_alimentar"].index)-1, loc = media_psa_total, scale = st.sem(tabla["peso_sin_alimentar"]))
ic_95_psa_control = st.t.interval(confidence = 0.95, df = len(psa_control["peso_sin_alimentar"].index)-1, loc = media_psa_control, scale = st.sem(psa_control["peso_sin_alimentar"]))
ic_95_psa_int = st.t.interval(confidence = 0.95, df = len(psa_int["peso_sin_alimentar"].index)-1, loc = media_psa_int, scale = st.sem(psa_int["peso_sin_alimentar"]))

ic_95_psi_total = st.t.interval(confidence = 0.95, df = len(tabla["peso_sangre_ingerida"].index)-1, loc = media_psi_total, scale = st.sem(tabla["peso_sangre_ingerida"]))
ic_95_psi_control = st.t.interval(confidence = 0.95, df = len(psi_control["peso_sangre_ingerida"].index)-1, loc = media_psi_control, scale = st.sem(psi_control["peso_sangre_ingerida"]))
ic_95_psi_int = st.t.interval(confidence = 0.95, df = len(psi_int["peso_sangre_ingerida"].index)-1, loc = media_psi_int, scale = st.sem(psi_int["peso_sangre_ingerida"]))

ic_95_hp_total = st.t.interval(confidence = 0.95, df = len(tabla["huevos_puestos"].index)-1, loc = media_hp_total, scale = st.sem(tabla["huevos_puestos"]))
ic_95_hp_control = st.t.interval(confidence = 0.95, df = len(hp_control["huevos_puestos"].index)-1, loc = media_hp_control, scale = st.sem(hp_control["huevos_puestos"]))
ic_95_hp_int = st.t.interval(confidence = 0.95, df = len(hp_int["huevos_puestos"].index)-1, loc = media_hp_int, scale = st.sem(hp_int["huevos_puestos"]))

ic_95_if_total = st.t.interval(confidence = 0.95, df = len(tabla["indice_de_fecundidad"].index)-1, loc = media_if_total, scale = st.sem(tabla["indice_de_fecundidad"]))
ic_95_if_control = st.t.interval(confidence = 0.95, df = len(if_control["indice_de_fecundidad"].index)-1, loc = media_if_control, scale = st.sem(if_control["indice_de_fecundidad"]))
ic_95_if_int = st.t.interval(confidence = 0.95, df = len(if_int["indice_de_fecundidad"].index)-1, loc = media_if_int, scale = st.sem(if_int["indice_de_fecundidad"]))

#conversion de los resultados a listas para redondear y presentar

ic_95_psa_total_lista = list(ic_95_psa_total)
ic_95_psa_total_listar = [ round(elem, 2) for elem in ic_95_psa_total_lista ]

ic_95_psa_control_lista = list(ic_95_psa_control)
ic_95_psa_control_listar = [ round(elem, 2) for elem in ic_95_psa_control_lista ]

ic_95_psa_int_lista = list(ic_95_psa_int)
ic_95_psa_int_listar = [ round(elem, 2) for elem in ic_95_psa_int_lista ]


ic_95_psi_total_lista = list(ic_95_psi_total)
ic_95_psi_total_listar = [ round(elem, 2) for elem in ic_95_psi_total_lista ]

ic_95_psi_control_lista = list(ic_95_psi_control)
ic_95_psi_control_listar = [ round(elem, 2) for elem in ic_95_psi_control_lista ]

ic_95_psi_int_lista = list(ic_95_psi_int)
ic_95_psi_int_listar = [ round(elem, 2) for elem in ic_95_psi_int_lista ]


ic_95_hp_total_lista = list(ic_95_hp_total)
ic_95_hp_total_listar = [ round(elem, 2) for elem in ic_95_hp_total_lista ]

ic_95_hp_control_lista = list(ic_95_hp_control)
ic_95_hp_control_listar = [ round(elem, 2) for elem in ic_95_hp_control_lista ]

ic_95_hp_int_lista = list(ic_95_hp_int)
ic_95_hp_int_listar = [ round(elem, 2) for elem in ic_95_hp_int_lista ]


ic_95_if_total_lista = list(ic_95_if_total)
ic_95_if_total_listar = [ round(elem, 2) for elem in ic_95_if_total_lista ]

ic_95_if_control_lista = list(ic_95_if_control)
ic_95_if_control_listar = [ round(elem, 2) for elem in ic_95_if_control_lista ]

ic_95_if_int_lista = list(ic_95_if_int)
ic_95_if_int_listar = [ round(elem, 2) for elem in ic_95_if_int_lista ]

ic95_todas_dict = {'Característica': ["Peso sin alimentar","Sangre ingerida","Huevos puestos","Índice de fecundidad"], 'Ambos grupos': [ic_95_psa_total_listar,ic_95_psi_total_listar,ic_95_hp_total_listar,ic_95_if_total_listar], 'Grupo control':[ic_95_psa_control_listar,ic_95_psi_control_listar,ic_95_hp_control_listar,ic_95_if_control_listar], 'Grupo interferido': [ic_95_psa_int_listar,ic_95_psi_int_listar,ic_95_hp_int_listar,ic_95_if_int_listar]}
ic95_todas = pd.DataFrame(data=ic95_todas_dict)
print("En la siguiente tabla se muestran los Intervalos de Confianza (95%) estimados en base a cada grupo y variable:")
ic95_todas_mostrar = ic95_todas.to_string(index=False)
print(ic95_todas_mostrar)

#3. ESTIMACIÓN DE TAMAÑO MUESTRAL

# Utilizo la media y la desviación estándar calculada previamente
# Defino los parámetros de la prueba
effect_size_psa = abs(media_psa_control - media_psa_int) / sd_psa_total
effect_size_psi = abs(media_psi_control - media_psi_int) / sd_psi_total
effect_size_hp = abs(media_hp_control - media_hp_int) / sd_hp_total
effect_size_if = abs(media_if_control - media_if_int) / sd_if_total
alpha = 0.05
power = 0.8

# Crear una instancia de la clase TTestIndPower
ttp = TTestIndPower()

# Calcular el tamaño muestral necesario
n_psa = ttp.solve_power(effect_size=effect_size_psa, alpha=alpha, power=power, ratio=1.25, alternative='two-sided')
n_psi = ttp.solve_power(effect_size=effect_size_psi, alpha=alpha, power=power, ratio=1.25, alternative='two-sided')
n_hp = ttp.solve_power(effect_size=effect_size_hp, alpha=alpha, power=power, ratio=1.25, alternative='two-sided')
n_if = ttp.solve_power(effect_size=effect_size_if, alpha=alpha, power=power, ratio=1.25, alternative='two-sided')

# Imprimir el resultado
print("El tamaño muestral necesario para Peso sin alimentar es:", round(n_psa))
print("El tamaño muestral necesario para Peso sangre ingerida es:", round(n_psi))
print("El tamaño muestral necesario para Huevos puestos es:", round(n_hp))
print("El tamaño muestral necesario para Índice de fecundidad es:", round(n_psa))

#4 PRUEBAS DE HIPÓTESIS

#Chequeo de normalidad de los datos

norm_psa_total = st.shapiro(tabla["peso_sin_alimentar"])
norm_psa_control = st.shapiro(psa_control["peso_sin_alimentar"])
norm_psa_int = st.shapiro(psa_int["peso_sin_alimentar"])
print("El resultado de la prueba de Shapiro-Wilk para Peso sin alimentar en ambos grupos es", norm_psa_total)
print("El resultado de la prueba de Shapiro-Wilk para Peso sin alimentar en el grupo control es", norm_psa_control)
print("El resultado de la prueba de Shapiro-Wilk para Peso sin alimentar en el grupo interferido es", norm_psa_int)

norm_psi_total = st.shapiro(tabla["peso_sangre_ingerida"])
norm_psi_control = st.shapiro(psi_control["peso_sangre_ingerida"])
norm_psi_int = st.shapiro(psi_int["peso_sangre_ingerida"])
print("El resultado de la prueba de Shapiro-Wilk para Sangre ingerida en ambos grupos es", norm_psi_total)
print("El resultado de la prueba de Shapiro-Wilk para Sangre ingerida en el grupo control es", norm_psi_control)
print("El resultado de la prueba de Shapiro-Wilk para Sangre ingerida en el grupo interferido es", norm_psi_int)

norm_hp_total = st.shapiro(tabla["huevos_puestos"])
norm_hp_control = st.shapiro(hp_control["huevos_puestos"])
norm_hp_int = st.shapiro(hp_int["huevos_puestos"])
print("El resultado de la prueba de Shapiro-Wilk para Huevos puestos en ambos grupos es", norm_hp_total)
print("El resultado de la prueba de Shapiro-Wilk para Huevos puestos en el grupo control es", norm_hp_control)
print("El resultado de la prueba de Shapiro-Wilk para Huevos puestos en el grupo interferido es", norm_hp_int)

norm_if_total = st.shapiro(tabla["indice_de_fecundidad"])
norm_if_control = st.shapiro(if_control["indice_de_fecundidad"])
norm_if_int = st.shapiro(if_int["indice_de_fecundidad"])
print("El resultado de la prueba de Shapiro-Wilk para Índice de fecundidad en ambos grupos es", norm_if_total)
print("El resultado de la prueba de Shapiro-Wilk para Índice de fecundidad en el grupo control es", norm_if_control)
print("El resultado de la prueba de Shapiro-Wilk para Índice de fecundidad en el grupo interferido es", norm_if_int)

#Chequeo de homocedasticidad

hc_psa = st.levene(psa_control["peso_sin_alimentar"],psa_int["peso_sin_alimentar"], center='median', proportiontocut=0.05)

hc_psi = st.levene(psi_control["peso_sangre_ingerida"],psi_int["peso_sangre_ingerida"], center='median', proportiontocut=0.05)

hc_hp = st.levene(hp_control["huevos_puestos"],hp_int["huevos_puestos"], center='median', proportiontocut=0.05)

hc_if = st.levene(if_control["indice_de_fecundidad"],if_int["indice_de_fecundidad"], center='median', proportiontocut=0.05)

print("El resultado del test de Levene para Peso sin alimentar", hc_psa)
print("El resultado del test de Levene para Sangre ingerida", hc_psi)
print("El resultado del test de Levene para Huevos puestos", hc_hp)
print("El resultado del test de Levene para Índice de fecundidad", hc_if)

#COMPARACIÓN DE MEDIAS

#aplicar t-test

#PSA

resultado_ttest_psa = st.ttest_ind(psa_control["peso_sin_alimentar"], psa_int["peso_sin_alimentar"], alternative='two-sided')
print("El valor p resultante para la prueba de T para Peso sin alimentar es: ", resultado_ttest_psa.pvalue)
print("El estadístico resultante para la prueba de T para Peso sin alimentar es: ", resultado_ttest_psa.statistic)

#PSI

resultado_ttest_psi = st.ttest_ind(psi_control["peso_sangre_ingerida"], psi_int["peso_sangre_ingerida"], alternative='two-sided')
print("El valor p resultante para la prueba de T para Peso de la sangre ingerida es: ", resultado_ttest_psi.pvalue)
print("El estadístico resultante para la prueba de T para Peso de la sangre ingerida es: ", resultado_ttest_psi.statistic)

#HP

resultado_ttest_hp = st.ttest_ind(hp_control["huevos_puestos"], hp_int["huevos_puestos"], alternative='two-sided')
print("El valor p resultante para la prueba de T para Huevos puestos es: ", resultado_ttest_hp.pvalue)
print("El estadístico resultante para la prueba de T para Huevos puestos es: ", resultado_ttest_hp.statistic)

#IF

resultado_ttest_if = st.ttest_ind(if_control["indice_de_fecundidad"], if_int["indice_de_fecundidad"], alternative='two-sided')
print("El valor p resultante para la prueba de T para IF es: ", resultado_ttest_if.pvalue)
print("El estadístico resultante para la prueba de T para IF es: ", resultado_ttest_if.statistic)

#análisis no paramétrico IF

resultado_mw_if = st.mannwhitneyu(if_control["indice_de_fecundidad"], if_int["indice_de_fecundidad"], use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
print("El valor p resultante para la prueba no paramétrica U de Umann-Whitney para IF es: ",resultado_mw_if.pvalue)
print("El estadístico resultante para la prueba no paramétrica U de Umann-Whitney para IF es: ",resultado_mw_if.statistic)

#Análisis de IF en base a la variable categórica "bajo" y alto" (tomando como punto de corte > o < a 2.51)
#Se crea la siguiente tabla de contingencia:
#	            Grupo control	Grupo interferido	Total
#IF bajo (<2.51)	            1	                5   	6
#IF alto (>2.51)	            3	                0	    3
#Total	                       4	                5	    9
#utilizando el siguiente código:

tabla_contingencia_if = pd.crosstab(tabla.insecto, (tabla.indice_de_fecundidad > 2.51))

resultado_contingencia_if = (st.fisher_exact(tabla_contingencia_if, alternative='two-sided'))

print("El p-value resultante de la prueba de Fisher para IF es", resultado_contingencia_if.pvalue, "y el estadístico asociado es", resultado_contingencia_if.statistic)

#CORRELACIÓN

#entre peso sin alimentar y sangre ingerida
#se crea el dataframe y se reemplaza el índice por "insecto"

df_psa_psi = tabla.filter(items=["insecto","peso_sin_alimentar", "peso_sangre_ingerida"])

df_psa_psi_final = df_psa_psi.set_index(list(df_psa_psi)[0])

#graficar
sns.lmplot(x="peso_sin_alimentar", y="peso_sangre_ingerida", data=df_psa_psi_final)
plt.show()

#cálculo del coeficiente de correlación
psa_psi_coef_corr_todos = st.pearsonr(tabla["peso_sin_alimentar"], tabla["peso_sangre_ingerida"])
print("El coeficiente de correlación entre Peso sin alimentar y Sangre ingerida es", psa_psi_coef_corr_todos.statistic, "y el valor p asociado es de",psa_psi_coef_corr_todos.pvalue)

psa_psi_coef_corr_control = st.pearsonr(psa_control["peso_sin_alimentar"], psi_control["peso_sangre_ingerida"])
print("El coeficiente de correlación entre Peso sin alimentar y Sangre ingerida en el grupo control es", psa_psi_coef_corr_control.statistic, "y el valor p asociado es de",psa_psi_coef_corr_control.pvalue)

#entre sangre ingerida y huevos puestos
#se crea el dataframe y se reemplaza el índice por "insecto"

df_psi_hp = tabla.filter(items=["insecto", "peso_sangre_ingerida", "huevos_puestos"])

df_psi_hp_final = df_psi_hp.set_index(list(df_psi_hp)[0])

#graficar
sns.lmplot(x="peso_sangre_ingerida", y="huevos_puestos", data=df_psi_hp_final)
plt.show()

#cálculo del coeficiente de correlación
psi_hp_coef_corr_todos = st.pearsonr(tabla["peso_sangre_ingerida"], tabla["huevos_puestos"])
print("El coeficiente de correlación entre Sangre ingerida y huevos puestos es", psi_hp_coef_corr_todos.statistic, "y el valor p asociado es de",psi_hp_coef_corr_todos.pvalue)

psi_hp_coef_corr_control = st.pearsonr(psi_control["peso_sangre_ingerida"], hp_control["huevos_puestos"])
print("El coeficiente de correlación entre Sangre ingerida y huevos puestos en el grupo control es", psi_hp_coef_corr_control.statistic, "y el valor p asociado es de",psi_hp_coef_corr_control.pvalue)
