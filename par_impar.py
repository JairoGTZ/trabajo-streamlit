import streamlit as st

def numeros_pares_e_impares():
    st.title("Bienvenido a la función de Números Pares e Impares")

    st.image("https://previews.123rf.com/images/cycloneproject/cycloneproject1602/cycloneproject160200058/54536250-robot-tiene-un-saludo-mientras-se-toma-una-taza-de-caf%C3%A9-en-una-mano-imagen-generada-por-ordenador.jpg", 
              caption="Asistente robot")

    st.subheader("¿Qué son los números pares? &#x2753;")
    st.write("Los números **pares** son aquellos que son divisibles entre 2 sin dejar residuo (ejemplo: 0, 2, 4).")
    st.subheader("¿Qué son los números impares? &#x2753;")
    st.write("Los números **impares** son aquellos que no son divisibles entre 2 (ejemplo: 1, 3, 5).")
    
    st.subheader("¿Cómo usar esta aplicación? &#x2753;")
    st.write("1. Introduce una serie de números separados por comas (,) o espacios en el campo de texto.")
    st.write("2. Haz clic en el botón 'Calcular Pares e Impares' para ver la clasificación.")
    st.write("3. Los números pares e impares se mostrarán a continuación.")

    numeros_input = st.text_input("Introduce los números separados por comas o espacios:")

    lista_pares = []
    lista_impares = []

    if st.button("Calcular Pares e Impares"):
        lista_pares.clear()
        lista_impares.clear()

        try:
            numeros = [int(num) for num in numeros_input.replace(',', ' ').split()]
            
            for numero in numeros:
                if numero % 2 == 0:
                    lista_pares.append(numero)
                else:
                    lista_impares.append(numero)

            # Mostrar resultados en color rojo
            st.markdown("<h3 style='color: black;'>Números Pares: </h3>", unsafe_allow_html=True)
            st.write('<h2 style="color: black;">' + ', '.join(map(str, lista_pares)) + '</span>', unsafe_allow_html=True)
            st.markdown("<h3 style='color: red;'>Números Impares: </h3>", unsafe_allow_html=True)
            st.write('<h2 style="color: red;">' + ', '.join(map(str, lista_impares)) + '</span>', unsafe_allow_html=True)

        except ValueError:
            st.error("Por favor, introduce solo números válidos separados por comas o espacios.")

if __name__ == "__main__":
    numeros_pares_e_impares()
