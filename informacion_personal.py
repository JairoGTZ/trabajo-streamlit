import streamlit as st

def informacion_personal(letras):
    st.markdown(f"<h2 style='color: blue;'>Información Proporcionada y organizada:</h2>", unsafe_allow_html=True)
    for clave, valor in letras.items():
        st.markdown(f"<p style='color: black; font-size: 20px;'>{clave}: {valor}</p>", unsafe_allow_html=True)

def main():
    st.title("Información Personal 🤖") 

    st.write("En esta sección organizaremos tu información personal y la guardaremos en nuestra base de datos, retornando la información de acuerdo a sus características.")

    st.image("https://img.freepik.com/fotos-premium/icon-3d-robot-ia-impulsado-datos-que-procesa-informacion_960080-18420.jpg", 
              caption="Procesando tu información")

    st.subheader("¿Cómo usar esta página?")
    st.write("1. Rellena los campos solicitados con tu información personal.")
    st.write("2. Asegúrate de completar todos los campos obligatorios.")
    st.write("3. Haz clic en el botón 'Enviar' para ver la información que proporcionaste.")

    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value=0)
    direccion = st.text_input("Dirección")
    ciudad = st.text_input("Ciudad")

    if st.button("Enviar"):
        if nombre and direccion and ciudad:
            informacion_personal({'Nombre': nombre, 'Edad': edad, 'Dirección': direccion, 'Ciudad': ciudad})
        else:
            st.warning("Por favor, completa todos los campos obligatorios.")

if __name__ == "__main__":
    main()
