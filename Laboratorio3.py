import pandas as pd
import streamlit as st

df_car = pd.read_csv("Electric_Vehicle_Population.csv")
df_gym = pd.read_csv("GymExerciseTracking.csv")
df_steam = pd.read_csv("steam_store_data_2024.csv")
df_netflix = pd.read_csv("netflix_titles.csv")

df_steam["price"] = df_steam["price"].str.replace("$", "", regex = False).astype(float)
df_steam["salePercentage"] = df_steam["salePercentage"].str.replace("%", "", regex = False).str.replace("-", "", regex = False).astype(float)
df_netflix["duration"] = pd.to_numeric(df_netflix["duration"].str.replace(" min", "", regex = False), errors = "coerce")
df_netflix_peliculas = df_netflix.dropna(subset = ["duration"])

nombrar = ["carros", "personas de gym", "juegos", "catálogo de netflix"]
nombrar_df = [df_car, df_gym, df_steam, df_netflix]

st.title("BIENVENIDO A DATAINSIGHT ANALYTICS")
st.header("DATOS GENERALES")
for mostrar in range(len(nombrar)):
    st.write("Número de filas y columnas de", nombrar[mostrar])
    st.write(nombrar_df[mostrar].shape)

for mostrar in range(len(nombrar)):
    st.write("Columnas de", nombrar[mostrar])
    st.write(list(nombrar_df[mostrar].columns))

for mostrar in range(len(nombrar)):
    st.write("Primeras 6 filas de ", nombrar[mostrar])
    st.dataframe(nombrar_df[mostrar].head(6))

for mostrar in range(len(nombrar)):
    st.write("Datos generales de", nombrar[mostrar])
    st.dataframe(nombrar_df[mostrar].describe())


st.title("NUEVA FILA PARA DATOS EN STEAM")
new_title = st.text_input("Ingrese el título del nuevo juego: ")
new_description = st.text_input("Ingrese su descripción: ")
new_price = st.number_input("Ingrese el nuevo precio: ", min_value=0.0)
new_sale = st.number_input("Ingrese el porcentaje de descuento: ", min_value=0, max_value=100)
new_recent = st.text_input("Ingrese sus reviews recientes: ")
new_reviews = st.text_input("Ingrese sus reviews totales: ")

new_fila = {"title": new_title, "description": new_description, "price": new_price, "salePercentage": new_sale, "allReviews": new_reviews}
df_steam = pd.concat([df_steam, pd.DataFrame([new_fila])], ignore_index = True)

st.title("NUEVA FILA PARA DATOS EN GIMNASIO")
new_age = st.number_input("Ingrese la edad: ", min_value=0)
new_gender = st.text_input("Ingrese su género: ")
new_weight = st.number_input("Ingrese su peso en Kg: ", min_value=0.0)
new_height = st.number_input("Ingrese su altura en metros: ", min_value=0.0)
new_maxBPM = st.number_input("Ingrese su máximos latidos por minuto: ", min_value=0)
new_avgBPM = st.number_input("Ingrese sus latidos por minuto promedios: ", min_value=0)
new_restBPM = st.number_input("Ingrese sus latidos por minuto al estar en reposo: ", min_value=0)
new_session = st.number_input("Ingrese cuánto dura sus sesión en horas: ", min_value=0.0)
new_calories = st.number_input("Ingrese sus calorías quemadas: ", min_value=0.0)
new_workout = st.text_input("Ingrese el tipo de entrenamiento que hace: ")
new_fat = st.number_input("Ingrese su porcentaje de grasa: ", min_value=0.0, max_value=100.0)
new_water = st.number_input("Ingrese cuánta agua toma en litros: ", min_value=0.0)
new_frequency = st.number_input("Ingrese cuántos días a la semana hace ejercicio: ", min_value=1, max_value=7)
new_experience = st.number_input("Ingrese su nivel de experiencia (1-5): ", min_value=1, max_value=5)
new_BMI = st.number_input("Ingrese su BMI: ", min_value=0.0)

new_gym_fila = {"Age": new_age, "Gender": new_gender, "Weight (kg)": new_weight, "Max_BPM": new_maxBPM, "Avg_BPM": new_avgBPM, "Resting_BPM": new_restBPM, "Session_Duration (hours)": new_session, "Calories_Burned": new_calories, "Workout_Type": new_workout, "Fat_Percentage": new_fat, "Water_Intake (liters)": new_water, "Workout_Frequency (days/week)": new_frequency, "Experience_Level": new_experience, "BMI": new_BMI}
df_gym = pd.concat([df_gym, pd.DataFrame([new_gym_fila])], ignore_index = True)




st.title("FILTRADO DE DATOS PARA CARROS")
año_menor = []

año_max = st.number_input("Ingrese el año en donde quiere ver carros de años más viejos: ", min_value=2000, max_value=2025)

for indice, fila in df_car.iterrows():
    if fila ["Model Year"] < año_max:
        año_menor.append(fila)

st.dataframe(pd.DataFrame(año_menor))


base_menor = []

base_max = st.number_input("Ingrese el precio máximo de carros que quiere ver: ", min_value=0, max_value=845000)

for indice, fila in df_car.iterrows():
    if fila ["Base_MSRP"] < base_max:
        base_menor.append(fila)

st.dataframe(pd.DataFrame(base_menor))


st.title("FILTRADO DE DATOS PARA GIMNASIO")
calories_mayor = []

calories_max = st.number_input("Ingrese el número mínimo de calorías que quiere ver: ", min_value=0)

for indice, fila in df_gym.iterrows():
    if fila ["Calories_Burned"] >= calories_max:
        calories_mayor.append(fila)

st.dataframe(pd.DataFrame(calories_mayor))


fat_menor = []

fat_max = st.number_input("Ingrese el maximo de porcentaje de calorías quiere ver: ", min_value=0, max_value=100)

for indice, fila in df_gym.iterrows():
    if fila ["Fat_Percentage"] <= fat_max:
        fat_menor.append(fila)

st.dataframe(pd.DataFrame(fat_menor))


st.title("FILTRADO DE DATOS PARA STEAM")
precio_mayor = []

precio_max = st.number_input("Ingrese el precio de videojuegos menor que quiere ver: ", min_value=0)

for indice, fila in df_steam.iterrows():
    if fila ["price"] > precio_max:
        precio_mayor.append(fila)

st.dataframe(pd.DataFrame(precio_mayor))


descuento_menor = []

descuento_max = st.number_input("Ingrese el mayor porcentaje de descuento de videojuegos que quiere ver: ", min_value=0, max_value=100)

for indice, fila in df_steam.iterrows():
    if fila ["salePercentage"] < descuento_max:
        descuento_menor.append(fila)

st.dataframe(pd.DataFrame(descuento_menor))


st.title("FILTRADO DE DATOS PARA NETFLIX")
minutos_menor = []

minutos_max = st.number_input("Ingrese la menor duración en minutos de lo que quiere ver: ", min_value=0)

for indice, fila in df_netflix_peliculas.iterrows():
    if fila ["duration"] < minutos_max:
        minutos_menor.append(fila)

st.dataframe(pd.DataFrame(minutos_menor))


salida_menor = []

salida_max = st.number_input("Ingrese el año en el que quisiera ver algo más antiguo: ", min_value=1900, max_value=2025)

for indice, fila in df_netflix.iterrows():
    if fila ["release_year"] < salida_max:
        salida_menor.append(fila)

st.dataframe(pd.DataFrame(salida_menor))




st.title("FILTRADO DE CARROS POR RANGO ELÉCTRICO")
df_car["RangoCategoria"] = None
rango_bajo = []
rango_medio = []
rango_alto = []

for indice, fila in df_car.iterrows():
    if fila["Electric_Range"] <= 100:
        df_car.at[indice, "RangoCategoria"] = "Bajo"
        rango_bajo.append(fila)
    elif fila["Electric_Range"] <= 250:
        df_car.at[indice, "RangoCategoria"] = "Medio"
        rango_medio.append(fila)
    else:
        df_car.at[indice, "RangoCategoria"] = "Alto"
        rango_alto.append(fila)

datos_rango = df_car["RangoCategoria"].value_counts()
st.write("Rango eléctrico de carros:")
st.write(datos_rango)
st.bar_chart(datos_rango)
st.write("Datos de carros con rango eléctrico bajo")
st.dataframe(pd.DataFrame(rango_bajo))
st.write("Datos de carros con rango eléctrico medio")
st.dataframe(pd.DataFrame(rango_medio))
st.write("Datos de carros con rango eléctrico alto")
st.dataframe(pd.DataFrame(rango_alto))


st.title("FILTRADO DE USUARIOS DEL GIMNASIO POR NIVEL DE FRECUENCIA DE EJERCICIO")
df_gym["NivelFrecuencia"] = None
frecuencia_baja = []
frecuencia_moderada = []
frecuencia_alta = []

for indice, fila in df_gym.iterrows():
    if fila["Workout_Frequency (days/week)"] < 3:
        df_gym.at[indice, "NivelFrecuencia"] = "Baja"
        frecuencia_baja.append(fila)
    elif fila["Workout_Frequency (days/week)"] <= 5:
        df_gym.at[indice, "NivelFrecuencia"] = "Moderada"
        frecuencia_moderada.append(fila)
    else:
        df_gym.at[indice, "NivelFrecuencia"] = "Alta"
        frecuencia_alta.append(fila)

datos_frecuencia = df_gym["NivelFrecuencia"].value_counts()
st.write("Frecuencia de ejercicio:")
st.write(datos_frecuencia)
st.bar_chart(datos_frecuencia)
st.write("Datos de frecuencia de ejercicio bajo")
st.dataframe(pd.DataFrame(frecuencia_baja))
st.write("Datos de frecuencia de ejercicio moderada")
st.dataframe(pd.DataFrame(frecuencia_moderada))
st.write("Datos de frecuencia de ejercicio alta")
st.dataframe(pd.DataFrame(frecuencia_alta))


st.title("FILTRADO DE VIDEOJUEGOS DE STEAM POR TIPO DE GAMA")
df_steam["GamaJuego"] = None
gama_baja = []
gama_media = []
gama_alta = []

for indice, fila in df_steam.iterrows():
    if fila["price"] < 10:
        df_steam.at[indice, "GamaJuego"] = "Baja"
        gama_baja.append(fila)
    elif fila["price"] <= 24:
        df_steam.at[indice, "GamaJuego"] = "Media"
        gama_media.append(fila)
    else:
        df_steam.at[indice, "GamaJuego"] = "Alta"
        gama_alta.append(fila)

datos_gama = df_steam["GamaJuego"].value_counts()
st.write("Gamas de los juegos:")
st.write(datos_gama)
st.bar_chart(datos_gama)
st.write("Datos de juegos de gama baja")
st.dataframe(pd.DataFrame(gama_baja))
st.write("Datos de juegos de gama media")
st.dataframe(pd.DataFrame(gama_media))
st.write("Datos de juegos de gama alta")
st.dataframe(pd.DataFrame(gama_alta))


st.title("FILTRADO DE CONTENIDO DE NETFLX POR CLASIFICACIÓN DE EDAD")
df_netflix["TipoAudiencia"] = None
audiencia_niños = []
audiencia_adolescentes = []
audiencia_jovenes = []
audiencia_adultos = []

for indice, fila in df_netflix.iterrows():
    if fila["rating"] == "G" or fila["rating"] == "TV-Y" or fila["rating"] == "TV-G" or fila["rating"] == "TV-Y7" or fila["rating"] == "TV-Y7-FV":
        df_netflix.at[indice, "TipoAudiencia"] = "Niños"
        audiencia_niños.append(fila)
    elif fila["rating"] == "PG" or fila["rating"] == "TV-PG":
        df_netflix.at[indice, "TipoAudiencia"] = "Adolescentes"
        audiencia_adolescentes.append(fila)
    elif fila["rating"] == "PG-13" or fila["rating"] == "TV-14":
        df_netflix.at[indice, "TipoAudiencia"] = "Adultos Jóvenes"
        audiencia_jovenes.append(fila)
    else:
        df_netflix.at[indice, "TipoAudiencia"] = "Adultos"
        audiencia_adultos.append(fila)

datos_audiencia = df_netflix["TipoAudiencia"].value_counts()
st.write("Clasificación por audiencia:")
st.write(datos_audiencia)
st.bar_chart(datos_audiencia)
st.write("Datos de contenido para niños")
st.dataframe(pd.DataFrame(audiencia_niños))
st.write("Datos de contenido para adolescentes")
st.dataframe(pd.DataFrame(audiencia_adolescentes))
st.write("Datos de contenido para jóvenes adultos")
st.dataframe(pd.DataFrame(audiencia_jovenes))
st.write("Datos de contenido para adultos")
st.dataframe(pd.DataFrame(audiencia_adultos))