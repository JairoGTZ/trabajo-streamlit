import streamlit as st

def suma_lista():
    st.title("Bienvenido a la función de suma de los valores de tu lista 😎")
    
    # Mensaje descriptivo sin barra de desplazamiento
    st.write("En este apartado encontrarás una función muy útil que te ayudará a sumar la cantidad de valores que tiene tu lista.")

    st.image("https://img.freepik.com/foto-gratis/robot-casco-sujetapapeles_1048-3602.jpg", 
              caption="Robot ayudando con la lista", use_column_width=True)

    # Cómo funciona
    st.subheader("¿Cómo funciona?")
    st.write("1. Ingresa los valores de tu lista, separados por espacios.")
    st.write("2. Haz clic en el botón 'Calcular'.")
    st.write("3. La aplicación mostrará la lista de valores y la suma total de esos valores.")

    valores_input = st.text_input("Ingresa los valores de la lista (separados por espacios):")

    if st.button("Calcular"):
        try:
            lista = [float(valor) for valor in valores_input.split()]
            lista_str = ', '.join(map(str, lista))
            st.markdown(f"<h4>Lista de valores: [ {lista_str} ]</h4>", unsafe_allow_html=True)

            suma_total = sum(lista)
            st.markdown(f"<h2 style='color: orange;'>La suma de los valores en la lista es: {suma_total}</h2>", unsafe_allow_html=True)
        except ValueError:
            st.error("Por favor, asegúrate de ingresar solo números separados por espacios.")

def main():
    suma_lista()

if __name__ == "__main__":
    main()

