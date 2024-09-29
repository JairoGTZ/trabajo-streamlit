import streamlit as st

def area_triangulo():
    st.title("Bienvenido! 😊")
    st.markdown("En este apartado encontrarás una calculadora que te ayuda a sacar el área de un triángulo.")

    # Información sobre los triángulos
    st.write("### ¿Qué es un triángulo?")
    st.write("Un triángulo es una figura geométrica de tres lados y tres ángulos. Los triángulos se clasifican en diferentes tipos según la longitud de sus lados y la medida de sus ángulos:")

    # Tipos de triángulos y sus definiciones
    st.write("#### Tipos de triángulos:")
    st.write("""
    - **Triángulo equilátero:** Tiene los tres lados de la misma longitud y sus ángulos son todos iguales, midiendo 60 grados cada uno.
    ___
    - **Triángulo isósceles:** Tiene dos lados de la misma longitud y los ángulos opuestos a esos lados son iguales.
    ___
    - **Triángulo escaleno:** Tiene los tres lados de diferentes longitudes y, por lo tanto, todos sus ángulos son diferentes.
    ___
    - **Triángulo rectángulo:** Tiene un ángulo recto (90 grados).
    """)

    # Usar el enlace directo a la imagen del robot
    st.image("https://thumbs.dreamstime.com/z/profesor-del-robot-70280855.jpg", 
              caption="Profesor Robot explicando geometría.", use_column_width=True)

    base = st.number_input("Ingresa la base de tu triángulo (cm)", min_value=0)
    altura = st.number_input("Ingresa la altura de tu triángulo (cm)", min_value=0)
    
    if st.button("Calcular área"):
        if base > 0 and altura > 0:
            area = (base * altura) / 2
            # Mostrar el resultado en color verde con unidades
            st.markdown(f"<h3 style='color: green;'>El área del triángulo es: <strong>{area} cm²</strong></h3>", unsafe_allow_html=True)
        else:
            st.write("Por favor, ingresa valores válidos para la base y la altura.")

if __name__ == "__main__":
    area_triangulo()



