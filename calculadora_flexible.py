import streamlit as st

def calculadora_flexible():
    # Título de la aplicación
    st.title("Calculadora Flexible 🤖")
    
    # Mensaje de bienvenida
    st.write("¡Bienvenido a la Calculadora Flexible! Aquí puedes realizar diferentes operaciones matemáticas de manera sencilla.")

    # Imagen
    st.image("https://www.shutterstock.com/image-vector/futuristic-robot-interacting-digital-data-260nw-2500204599.jpg", 
              caption="Calculadora Flexible en Acción")

    # Características de la calculadora
    st.subheader("Características de la Calculadora:")
    st.write("- Permite realizar operaciones de suma, resta, multiplicación y división.")
    st.write("- Sencilla de usar.")
    st.write("- Resultados precisos y rápidos.")

    # Instrucciones de uso
    st.subheader("¿Cómo funciona?")
    st.write("1. Ingrese los dos números que desea calcular.")
    st.write("2. Seleccione la operación que desea realizar.")
    st.write("3. Haga clic en el botón 'Calcular' para ver el resultado.")

    # Entradas de usuario
    numero1 = st.number_input("Ingrese el primer número:",0)
    numero2 = st.number_input("Ingrese el segundo número:",0)
    operacion = st.selectbox("Seleccione la operación:", ["suma", "resta", "multiplicacion", "division"])

    # Lógica de cálculo dentro de la misma función
    if st.button("Calcular"):
        match operacion:
            case "suma":
                resultado = numero1 + numero2
            case "resta":
                resultado = numero1 - numero2
            case "multiplicacion":
                resultado = numero1 * numero2
            case "division":
                resultado = numero1 / numero2 if numero2 != 0 else "Error: División por cero"
            case _:
                resultado = "Operación no válida"

        # Mostrar el resultado
        st.markdown(f"<h2 style='color: green; font-size: 40px;'>El resultado de {operacion} entre los numeros {numero1} y {numero2} es: {resultado}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    calculadora_flexible()
