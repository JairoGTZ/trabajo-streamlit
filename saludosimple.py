import streamlit as st

def mostrar_saludo_app():
    st.title("Bienvenido a la página de generar un saludo simple 😊")

    st.header("¡Saludos desde nuestra aplicación!")
    st.write("Estamos aquí para ofrecerte un saludo personalizado.")

    # Agregar la imagen del robot
    st.image("https://thumbs.dreamstime.com/z/concepto-humano-y-robot-droid-caracter-sujet%C3%A1ndose-mutuamente-expresi%C3%B3n-de-amor-ternura-met%C3%A1fora-colaboraci%C3%B3n-con-inteligencia-261476079.jpg", 
              caption="¡Un saludo amistoso!", use_column_width=True)

    # Lista de por qué es importante saludar
    st.write("### ¿Por qué es importante saludar?")
    st.write("""
    - **Fomenta la conexión social:** Saludar ayuda a establecer vínculos con otras personas.
    - **Genera un ambiente positivo:** Un saludo amable puede alegrar el día de alguien.
    - **Mejora la comunicación:** Iniciar una conversación con un saludo abre las puertas a una mejor comunicación.
    - **Refuerza la cortesía:** Saludar es una muestra de respeto y amabilidad hacia los demás.
    - **Aumenta la confianza:** Un saludo cálido puede hacer que las personas se sientan más cómodas y seguras.
    """)

    nombre_usuario = st.text_input("Ingresa tu nombre:")
    
    def saludo_simple():
        if nombre_usuario:
            st.markdown(f"<h3 style='color: purple;'>¡Hola {nombre_usuario}! Mucho gusto, es un placer saludarte.</h3>", unsafe_allow_html=True)
        else:
            st.warning("Por favor, ingresa tu nombre para generar un saludo.")

    if st.button("Generar saludo"):
        saludo_simple()

if __name__ == "__main__":
    mostrar_saludo_app()



