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
