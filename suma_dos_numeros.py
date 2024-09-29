import streamlit as st

def suma_dos_numeros():
    """Función para sumar dos números y mostrar el resultado."""
    st.header("Calculadora de Suma \U0001F60E")  # Título de la sección con emoji

    # Mensaje explicativo sobre cómo utilizar la calculadora
    st.write("Esta aplicación te permite sumar dos números. Para usarla, ingresa los valores que deseas sumar en los campos proporcionados y presiona el botón 'Sumar' para ver el resultado.")

    # Agregar la imagen
    st.image("https://www.shutterstock.com/image-illustration/funny-white-robot-stay-calculator-260nw-47151223.jpg", 
              caption="¡Sumemos con ayuda de nuestro robot!", use_column_width=True)

    # Entradas de usuario
    a = st.number_input("Ingresa el primer valor a sumar:", 0)
    b = st.number_input("Ingresa el segundo valor a sumar:", 0)
    
    # Botón para calcular la suma
    if st.button("Sumar"):
        suma = a + b
        # Mostrar el resultado de forma vistosa
        st.markdown(f"<h3 style='color: blue;'>Resultado de la suma es : <strong>{suma}</strong></h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    suma_dos_numeros()
