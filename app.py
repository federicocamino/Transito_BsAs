import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df_homicidios=pd.read_csv('Datos_procesados/df_homicidios.csv')


# funcion que crea el grafico de barras y lo muestra
def bar_chart_by_year():
    fig, ax = plt.subplots()
    df_yearly_victims = df_homicidios.groupby('año')['N_VICTIMAS'].sum()
    df_yearly_victims.plot(kind='bar', ax=ax)
    plt.xlabel('Año')
    plt.ylabel('Número de Víctimas')
    st.pyplot(fig)

# funcion que crea el grafico de torta y lo muestra
def pie_chart(column):
    fig, ax = plt.subplots()
    df_column_count = df_homicidios[column].value_counts()
    df_column_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.xlabel(column)
    st.pyplot(fig)

# Botones para seleccionar la COMUNA
selected_comuna = st.sidebar.selectbox('Seleccionar COMUNA', df_homicidios['COMUNA'].unique())

# filtro lo que se seleccione en el boton
df_selected_comuna = df_homicidios[df_homicidios['COMUNA'] == selected_comuna]

# Mostrar gráficos
st.header('Suma de N_VICTIMAS por año')
bar_chart_by_year()

st.header('Distribución de TIPO_DE_CALLE')
pie_chart('TIPO_DE_CALLE')

st.header('Distribución de VICTIMA')
pie_chart('VICTIMA')

st.header('Distribución de ACUSADO')
pie_chart('ACUSADO')