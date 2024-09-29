import streamlit as st

def calc_desc():
    """Calcula el precio con descuento y el IVA."""
    st.title("Calculadora de Descuento \U0001F4B0\U0001F4B5") 

    st.write("### ¿Qué es el descuento?")
    st.write("El descuento es una reducción en el precio original de un producto. Es importante conocerlo porque te permite ahorrar dinero y mejorar tu presupuesto.")
    st.write("___")

    st.write("### ¿Qué es el IVA?")
    st.write("El IVA (Impuesto sobre el Valor Añadido) es un impuesto que se aplica a la venta de bienes y servicios. Conocer el IVA es crucial para entender el costo final que pagarás por un producto.")
    st.write("___")
    
    st.image("https://img.freepik.com/foto-gratis/robot-entrega-3d-funcionamiento_23-2151150087.jpg?size=626&ext=jpg&ga=GA1.1.2008272138.1726876800&semt=ais_hybrid", 
              caption="Calculadora de Descuento", use_column_width=True)

    st.write("### ¿Cómo usar esta calculadora \U00002753")  
    st.write("1. Ingresa el precio original de tu producto.")
    st.write("2. Especifica el porcentaje de descuento que deseas aplicar.")
    st.write("3. Indica el porcentaje del IVA que corresponde.")
    st.write("4. Presiona el botón 'Calcular' para obtener el precio con descuento y el total con IVA.")
    st.write("___")
    
    precio_original = st.number_input("Ingresa el precio de tu producto:", min_value=0.0, format="%.2f")
    descuento = st.number_input("Ingresa el descuento que le aplicarás a tu producto (%):", min_value=0.0, max_value=100.0, value=10.0, format="%.2f")
    iva = st.number_input("Ingresa el IVA de tu producto (%):", min_value=0.0, max_value=100.0, value=16.0, format="%.2f")

    if st.button("Calcular"):
        if precio_original > 0:  # Asegurarse de que el precio original es válido
            precio_condescuento = precio_original * (descuento / 100)
            precio_con_descuento = precio_original - precio_condescuento
            precio_con_iva = precio_con_descuento * (1 + iva / 100)
            
            # Mostrar resultados en color azul con diferentes tonos y agregar "pesos"
            st.markdown(f"<h3 style='color: blue;'>Precio original: <strong>${precio_original:.2f} pesos</strong></h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: darkblue;'>Descuento aplicado: <strong>${precio_condescuento:.2f} pesos</strong></h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: blue;'>Precio después del descuento: <strong>${precio_con_descuento:.2f} pesos</strong></h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: darkblue;'>IVA aplicado: <strong>${precio_con_iva - precio_con_descuento:.2f} pesos</strong></h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: blue;'>Precio total con IVA: <strong>${precio_con_iva:.2f} pesos</strong></h3>", unsafe_allow_html=True)
        else:
            st.warning("Por favor, ingresa un precio original válido.")

if __name__ == "__main__":
    calc_desc()



