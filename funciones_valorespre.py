import streamlit as st

def producto(nombre, cantidad=1, precio=10):
    total = cantidad * precio
    return f"<h2 style='color: #FF5733; font-weight: bold;'>El total a pagar por {cantidad} unidad(es) de '{nombre}' es: ${total:.2f} pesos</h2>"

def main():
    st.title("Calculadora de Precio de Productos 🛒💰")

    st.image("https://static.vecteezy.com/system/resources/previews/040/825/876/non_2x/ai-generated-robot-assistant-in-a-grocery-store-photo.jpg", 
              caption="Asistente robot en la tienda", use_column_width=True)

    st.markdown(
        """
        Esta calculadora te ayudará a calcular el total a pagar por los productos que deseas comprar. 
        Simplemente ingresa el nombre del producto, la cantidad que deseas y el precio por unidad.
        """, 
        unsafe_allow_html=True
    )

    # Entradas del usuario
    nombre = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", min_value=1, value=1)
    precio = st.number_input("Precio por unidad", min_value=0.0, value=10.0, format="%.2f")

    # Botón para calcular el total
    if st.button("Calcular"):
        if nombre:  # Verifica que se haya ingresado un nombre
            resultado = producto(nombre, cantidad, precio)  # Llama a la función para calcular
            st.markdown(resultado, unsafe_allow_html=True)  # Muestra el resultado con formato HTML
        else:
            st.warning("Por favor, ingresa el nombre del producto.")  # Mensaje de advertencia si no hay nombre

if __name__ == "__main__":
    main()

