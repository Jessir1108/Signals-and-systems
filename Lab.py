import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import streamlit as st
import sk_dsp_comm.sigsys as ss

#TITULOS
st.sidebar.title('Laboratorio 1 - Señales y sistemas')
st.sidebar.subheader("Jessir Daniel Florez Hamburger - Mateo Jose Muñoz - Dylan Abuchaibe")
st.sidebar.subheader('Etapa 1 - Generación de señales')

#SELECCIONADOR DE SEÑALES
opcion = st.sidebar.selectbox(
     'Escoja la señal que desea generar a continuación:',
     ('Seno','Pulso','Cuadratica',"Exponencial","Lineal","Triangular","Cuadrada","Secuencia de impulsos"))

st.sidebar.write('Has seleccionado la función tipo :', opcion)

#FUNCION SENO
if opcion == "Seno":

    st.title("Función Seno")

    frecuencia = st.number_input("Por favor ingrese el valor de la frecuencia f: ",step=0.1,min_value=0.1)
    amplitude = st.number_input("Por favor ingrese el valor de la amplitud A: ")
    
    paso=(1/(300*frecuencia))
    x=np.arange(0,2/frecuencia,paso)
    y=np.sin(2*np.pi*frecuencia*x)
    y=y*amplitude

    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función Seno")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)

#FUNCION PULSO
if opcion == "Pulso":

    st.title("Función Pulso")

    amplitud = st.number_input("Por favor ingrese el valor de la amplitud del pulso: ")
    anchura = st.number_input("Por favor ingrese el valor de la anchura del pulso: ")
    
    visualize=anchura/2
    percentage=visualize*0.5
    x = np.arange((-visualize)-percentage,(visualize)+percentage,.02)
    x_rect = ss.rect(x,anchura)
    y=x_rect*amplitud

    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función pulso")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)

#FUNCION CUADRATICA
if opcion == "Cuadratica":

    st.title("Función Cuadrática")
    st.subheader("y(t)= At^2 + bt + c.")

    A=st.number_input("Ingrese el valor de la constante A: ")
    B=st.number_input("Ingrese el valor de la constante B: ")
    C=st.number_input("Ingrese el valor de la cosntante C: ")

    x = np.arange(-10,10,.01)
    y = A*x**2+B*x+C
        
    
    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función cuadratica")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)

#FUNCION EXPONENCIAL
if opcion == "Exponencial":
    
    st.title("Funcion Exponencial")

    A=st.number_input("Ingrese el valor de la constante A: ")
    b=st.number_input("Ingrese el valor de la constante b: ")
    x= np.arange(0,2*np.pi,0.01)
    
    y = A*np.exp(-b*x)

    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función exponencial")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)
    
#FUNCION LINEAL
if opcion=="Lineal":

    st.title("Función Lineal")
    st.subheader("y=mx+b")

    m=st.number_input("Ingrese el valor de la constante m: ")
    b=st.number_input("Ingrese el valor de la cosntante b: ")

    x = np.arange(0, 10, 0.01)
    y = (m*x)+b

    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función lineal")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)

#FUNCION TRIANGULAR
if opcion == "Triangular":
   
    st.title('Funcion Triangular')

    a = st.number_input('Ingrese a continuacion el valor de la amplitud:')
    f = st.number_input('Ingrese a continuación el valor de la frecuencia:',step=0.1,min_value=0.1)

    paso=(1/(300*f))
    x = np.arange(0,2/f,paso)
    y = a*signal.sawtooth(2 *np.pi*f*x)
    
    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función triangular")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)

#FUNCION CUADRADA
if opcion == "Cuadrada":
   
    st.title('Funcion Cuadrada')

    a = st.number_input('Ingrese a continuacion el valor de la amplitud:')
    f = st.number_input('Ingrese a continuación el valor de la frecuencia:',step=0.1,min_value=0.1)

    paso=(1/(300*f))
    x = np.arange(0,2/f,paso)
    y = a*signal.square(2*np.pi*f*x)
    
    fig,ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title("Función cuadrada")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)
    
#SECUENCIA DE IMPULSOS
if opcion == "Secuencia de impulsos":
   
    st.title('Secuencia de impulsos')

    x = st.text_input("Ingrese el valor de los vectores de x: ",args=None)
    y = st.text_input("Ingrese el valor de los vectores de y: ",args=None)

    
    
    if len(x) != len(y):
        st.write("Ingrese vectores equivalentes")

    else:
        fig,ax=plt.subplots()
        ax.set_xlim(-1,11)
        ax.set_ylim(0,10)
        ax.stem(x,y)
        ax.set_title("Función secuencia de impulsos")
        ax.set_xlabel("Eje x")
        ax.set_ylabel("Eje y")
        ax.grid(True)
        st.pyplot(fig)


st.sidebar.subheader('Etapa 2 - Transformación de señales')

transformaciones = st.sidebar.multiselect(
     'Escoja las transformaciones que desea realizar a continuación: ',
     ['Desplazamiento', 'Escalamiento en tiempo', 'Escalamiento en amplitud'])

frames=5
if "Desplazamiento" in transformaciones:
    st.sidebar.subheader('Escoja a continuación cuantas unidades desea desplazar: ')
    val = st.sidebar.number_input("",step=1,min_value=-5,max_value=5)
    
    traslado=(x+val)
    fig,ax=plt.subplots()
    for i in range(frames+1):   
        ax.plot(x,y)
        ax.plot(x+i*(val)/frames,y,linestyle="dashed")
        ax.legend(['Original', 'Desplazada'])
        ax.set_title("Función Seno")
        ax.set_xlabel("Eje x")
        ax.set_ylabel("Eje y")
        ax.grid(True)
        st.pyplot(fig)