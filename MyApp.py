import streamlit as st
st.title("My primer App")
click=st.button("dale click")
st.write("el valor de click es: ",click)

if click==True:
    st.image("perro.jpg")
#st.button("otro boton")
#st.text("Hola mundo")
#st.text("la siguiente es una integral")
#st.latex(" \int_1^6 sin(x)dx")
#st.markdown(" #titulo ")
#st.markdown(" **este es una vivnieta** ")
num1 = st.slider('Elige el numero 1', 0.0, 100.0, 25.0)
num2 = st.slider('Elige el numero 2', 0.0, 100.0, 25.0)
suma = num1+num2
st.write("la suma de",num1," y ",num2,"es :",suma)
