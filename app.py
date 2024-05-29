import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df_homicidios=pd.read_csv('Datos_procesados/df_homicidios.csv')

#barra lateral
comuna_seleccionada = st.sidebar.selectbox('Seleccionar Comuna', df_homicidios['COMUNA'].unique())

#filtro con los datos de la barra
df_comuna = df_homicidios[df_homicidios['COMUNA'] == comuna_seleccionada]

# grafico de barras
fig1, ax1 = plt.subplots()
df_comuna.groupby('año')['N_VICTIMAS'].sum().plot(kind='bar', ax=ax1)
ax1.set_title('Suma de N_VICTIMAS por Año')
ax1.set_xlabel('Año')
ax1.set_ylabel('Número de Víctimas')
st.pyplot(fig1)

# graficos de torta
fig2, ax2 = plt.subplots(1, 3, figsize=(18, 6))

# TIPO_DE_CALLE
df_tipo_calle = df_comuna.groupby('TIPO_DE_CALLE')['N_VICTIMAS'].sum()
ax2[0].pie(df_tipo_calle, labels=df_tipo_calle.index, autopct='%1.1f%%', startangle=90)
ax2[0].set_title('Tipo de Calle')

# VICTIMA
df_victima = df_comuna.groupby('VICTIMA')['N_VICTIMAS'].sum()
ax2[1].pie(df_victima, labels=df_victima.index, autopct='%1.1f%%', startangle=90)
ax2[1].set_title('Vehículo de la víctima')

# ACUSADO
df_acusado = df_comuna.groupby('ACUSADO')['N_VICTIMAS'].sum()
ax2[2].pie(df_acusado, labels=df_acusado.index, autopct='%1.1f%%', startangle=90)
ax2[2].set_title('Vehículo victimario')

st.pyplot(fig2)
