import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df_homicidios=pd.read_csv('Datos_procesados/df_homicidios.csv')


#barra lateral para seleccionar la comuna
comuna_seleccionada = st.sidebar.selectbox('Seleccionar Comuna', df_homicidios['COMUNA'].unique())

# filtro de datos
df_comuna = df_homicidios[df_homicidios['COMUNA'] == comuna_seleccionada]

# grafico de barras
fig1, ax1 = plt.subplots()
df_comuna.groupby('año')['N_VICTIMAS'].sum().plot(kind='bar', ax=ax1)
ax1.set_xlabel('Año')
ax1.set_ylabel('Número de Víctimas')
st.pyplot(fig1)

# Graficos de torta
fig2, ax2 = plt.subplots(1, 3, figsize=(15, 5))
df_comuna['TIPO_DE_CALLE'].value_counts().plot(kind='pie', ax=ax2[0], autopct='%1.1f%%')
ax2[0].set_title('Tipo de Calle')
df_comuna['VICTIMA'].value_counts().plot(kind='pie', ax=ax2[1], autopct='%1.1f%%')
ax2[1].set_title('Víctima')
df_comuna['ACUSADO'].value_counts().plot(kind='pie', ax=ax2[2], autopct='%1.1f%%')
ax2[2].set_title('Acusado')
st.pyplot(fig2)