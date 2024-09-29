import streamlit as st

def pagina_principal():

    st.title("BIENVENIDO :smiley:")
    st.write("¡Bienvenido a nuestra página web! Estamos encantados de tenerte aquí.")
    st.write("En esta página web encontrarás cosas útiles y esperamos que sea fácil de usar y muy provechosa.")
    st.write("### Cómo usar esta página :question:")
    st.write("- Navega por las diferentes secciones utilizando el menú de opciones ubicado en el apartado izquierdo.")
    st.write("- Explora las funcionalidades que ofrecemos.")
    st.write("- Si tienes alguna duda, no dudes en contactarnos.")

    # Agregar la imagen del robot
    st.image("https://st5.depositphotos.com/48172140/66256/i/950/depositphotos_662560680-stock-photo-artificial-intelligence-robot-greeting-concept.jpg", 
              caption="¡Saludos de nuestro robot!", use_column_width=True)

    # Apartado de Dudas y Sugerencias
    st.write("### Dudas y Sugerencias :sunglasses:")
    st.write("Si tienes alguna duda o sugerencia, por favor compártela con nosotros:")
    
    nombre = st.text_input("Tu nombre:")
    email = st.text_input("Tu email:")
    mensaje = st.text_area("Tu mensaje:")
    
    if st.button("Enviar"):
        if nombre and email and mensaje:
            st.success("¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.")
        else:
            st.error("Por favor, completa todos los campos.")

if __name__ == "__main__":
    pagina_principal()
