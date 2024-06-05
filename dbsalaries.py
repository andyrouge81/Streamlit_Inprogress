import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# configuracion


st.set_page_config(page_title= "Repositorio DataBAse Salarios" , page_icon=":bar_chart:", layout='centered')
st.title("++STREAMLIT CON UNA DATABASE++")
st.image('Leyenda_db.png', width= 800, caption='Leyenda de la base de Datos de los Salarios' )



# contenido prueba en cadena texto

#st.write("### Pincha en uno de los valores")
st.subheader("Pincha en uno de los valores", divider='green')
# contenido texto con markdown
#st.markdown('## GRAFICO A MOSTRAR')


# sidebar
st.sidebar.success('Menú Gráficas')


# vamos a colocar unas columnas en la sidebar

option = st.sidebar.radio("Selecciona una Columna:",
                            ["Año", 'Titulacion','Salario', 'Salario en EEUU-(inprogress)', 'Ver Dataset'])
# ejemplo de carga de un dframe
df = pd.read_csv('/Users/andresrojo/Desktop/Bootcamp/Temario/Modulo1/Graficos/ds_salaries.csv')
#st.dataframe(df)

# colocamos graficos

def ano_trabajado():
     #función para mostrar la distribución de salarios
    #¿Cómo ha cambiado el salario medio con el paso del tiempo (work_year)?

# Primero tenemos qu calcular el salario medio por año
    average_salary_per_year = df.groupby('work_year')['salary_in_usd'].mean().reset_index() # agrupamos por años porque son pocos,si agrupamos primero por salario salen muchas filas
    print(average_salary_per_year)
    fig = px.area(average_salary_per_year, x='work_year', y='salary_in_usd', 
              title='Evolución del salario medio con el paso del tiempo', template="plotly_dark", color_discrete_sequence=['yellow'])
    st.plotly_chart(fig, use_container_width=True)

def salario(): #función para mostrar la distribución de salarios
    st.header("Salario según nivel de experiencia")
    fig = px.box(df, x="work_year", y="salary_in_usd", template="plotly_dark")
    
    #fig = px.histogram(df, x='salary_in_usd', title="Distribución de Salarios en USD")
    st.plotly_chart(fig, use_container_width=True)

def mostrar_titulacion(): #función para mostrar la comparativa de salarios por país
   # Usando plotly
    fig = px.strip(df, x="experience_level", y="salary_in_usd", template="plotly_dark", color='job_title', title="Titulacióm", labels={'salary_in_usd':'Salario', 'experience_level':' Nivel_experiencia','job_title':'Especialidad'})
    fig.update_xaxes(tickangle=90)

    st.plotly_chart(fig, use_container_width=True)

def mostrar_dataset(): #función para mostrar el dataset
    st.header("Dataset Completo")
    st.dataframe(df)
#colocamos secciones con tabs ejemplo a borrar


opciones = { #diccionario con las opciones
    "Año": ano_trabajado,
    "Salario": salario,
    "Titulacion": mostrar_titulacion,
    
    "Ver Dataset": mostrar_dataset,
}
opciones[option]()