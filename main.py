
import streamlit as st
import saludosimple as ss
import pagina_principal as pp
import area_triangulo as at
import calcu_desc as cd
import sum_lista as sl
import funciones_valorespre as fv
import par_impar as pi
import multiplicar_todos as mt
import informacion_personal as ip
import calculadora_flexible as cf
import suma_dos_numeros as sdn

def mostrar_pagina_principal():
    st.sidebar.title("Menú de opciones")
    pagina = st.sidebar.selectbox("Selecciona la opción que desees", (
        "Página principal",        
        "Saludo",
        "Suma de dos números",
        "Área de un triángulo",
        "Calculadora de descuento",
        "Suma de una lista de números",
        "Funciones con valores predeterminados",
        "Números pares e impares",
        "Multiplicación con *args",
        "Información de una persona con **kwargs",
        "Calculadora flexible"
    ))

    if pagina == "Página principal":
        pp.pagina_principal()
    elif pagina == "Saludo":
        ss.mostrar_saludo_app()
    elif pagina == "Suma de dos números":
        sdn.suma_dos_numeros()
    elif pagina == "Área de un triángulo":
        at.area_triangulo()
    elif pagina == "Calculadora de descuento":
        cd.calc_desc()
    elif pagina == "Suma de una lista de números":
        sl.suma_lista()
    elif pagina == "Funciones con valores predeterminados":
        fv.main()
    elif pagina == "Números pares e impares":
        pi.numeros_pares_e_impares()
    elif pagina == "Multiplicación con *args":
        mt.main()
    elif pagina == "Información de una persona con **kwargs":
        ip.main()
    elif pagina == "Calculadora flexible":
        cf.calculadora_flexible()

if __name__ == "__main__":
    mostrar_pagina_principal()
