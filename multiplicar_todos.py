import streamlit as st

def multiplicar_todos(numeros):
    if not numeros:  
        return 1
    resultado = 1
    for valor in numeros:
        resultado *= valor
    return resultado

def main():
    st.title("Bienvenido al Multiplicador de Números 😎")

    # Imagen
    st.image("https://thumbs.dreamstime.com/b/ret%C3%A9n-blanco-de-la-robusteza-con-la-calculadora-19893085.jpg", 
              caption="Calculadora de Multiplicación")

    # Explicación
    st.subheader("¿Qué es la multiplicación?")
    st.write("La multiplicación es una operación matemática que consiste en sumar un número a sí mismo varias veces. Por ejemplo, \(3 veces 4\) es lo mismo que \(3 + 3 + 3 + 3 = 12\).")
    
    st.subheader("¿Cómo usar esta aplicación?")
    st.write("1. Introduce una serie de números separados por comas (,) en el campo de texto.")
    st.write("2. Haz clic en el botón 'Calcular' para ver el resultado de la multiplicación.")
    st.write("3. El resultado se mostrará a continuación en color azul.")

    numeros = st.text_input("Introduce los números separados por comas:")
    
    if st.button("Calcular"):
        if numeros:
            lista_numeros = [float(num.strip()) for num in numeros.split(",")]
            resultado = multiplicar_todos(lista_numeros)
            st.markdown(f"<h2 style='color: blue;'>El resultado de la multiplicación es: {resultado}</h2>", unsafe_allow_html=True)
        else:
            st.write("Por favor, introduce al menos un número.")

if __name__ == "__main__":
    main()
