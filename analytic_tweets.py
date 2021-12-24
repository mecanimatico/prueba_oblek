# 1. Se importan librerías necesarias al proyecto
import json
import pandas as pd

# Se carga el archivo
with open('tweets_test.json') as file:
    tweets_file = json.load(file)

# Se crea un dataframe con la información del archivo
df = pd.DataFrame(tweets_file)

# Se transponen los datos y se sobreescribe el df, para mejor visualización
df = pd.DataFrame.transpose(df)

print('--'*20)
# Se contabilizan los tweets
print('Solución punto 1')
conteo_tweets = len(df.index)
print(f'La cantidad de tweets son: {conteo_tweets}')
print('--'*20)

# Se listan los usuarios
lista_usuarios = list(dato['screen_name'] for dato in df['user'])
print(f'Solución punto 2: \n {lista_usuarios}')
print('--'*20)

# Se extrae la cantidad de seguidores por usuario y se totaliza
lista_seguidores = list(seguidor['followers_count'] for seguidor in df['user'])
print(f'Solución punto 3: \n {lista_seguidores}')

total_seguidores = sum(lista_seguidores)
print(f'El total de seguidores en el dataframe son: {total_seguidores} personas')

print('--'*20)
# Solución punto 4
usuarios_mencionados = []
for usuario in lista_usuarios:
    if df['text'].str.contains(usuario).any():
        usuarios_mencionados.append(usuario)
print(f'Solución punto 4: \nLos usuarios mencionados en los tweets son: {usuarios_mencionados}')

print('--'*20)
print('Solución punto 5')
for valor in range(3):
    # Se aplica el filtro al dataframe y se almacena en tendencia
    tendencia = df[df.tendencia == str(valor)]
    conteo_tendencia = len(tendencia.index)
    print(f'La cantidad de tweets con tendencia {valor} son: {conteo_tendencia}')