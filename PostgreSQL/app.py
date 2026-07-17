import streamlit as st
from archivo import Archivo
from analizador_lexico import AnalizadorLexico
from analizador_sintactico import AnalizadorSintactico
from validador_sql import ValidadorSQL


class App:

    def __init__(self):
        st.set_page_config(page_title="Analizador Lexico y Sintactico", layout="wide")
        self.analizador_lexico = AnalizadorLexico()
        self.analizador_sintactico = AnalizadorSintactico()
        self.validador = ValidadorSQL()

    def ejecutar(self):
        st.title("Analizador Lexico y Sintactico con ANTLR y Streamlit")
        st.write("Sube un archivo `.sql` para ver tokens y errores.")

        archivo_subido = st.file_uploader("Selecciona tu archivo", type=["sql"])

        if archivo_subido is None:
            st.info("Primero sube un archivo .sql")
            return

        archivo = Archivo(archivo_subido)

        if not archivo.es_txt():
            st.error("El archivo debe ser .sql")
            return

        codigo = archivo.leer()

        # --- Validacion previa de que el contenido sea SQL ---
        if not self.validador.validar_sql(codigo):
            st.error("El contenido del archivo no parece ser SQL válido.")
            return

        info = archivo.obtener_info()

        st.subheader("Informacion del archivo")
        st.write("Nombre:", info["nombre"])
        st.write("Extension:", info["extension"])

        st.subheader("Codigo original")
        st.code(codigo, language="text")

        # --- Analisis lexico ---
        self.analizador_lexico.analizar(codigo)

        tokens = self.analizador_lexico.obtener_tokens()
        errores_lexicos = self.analizador_lexico.obtener_errores()

        st.subheader("Tokens")

        if len(tokens) == 0:
            st.warning("No se encontraron tokens")
        else:
            st.dataframe(tokens, use_container_width=True)

        st.subheader("Errores lexicos")

        if len(errores_lexicos) == 0:
            st.success("No hay errores lexicos")
        else:
            st.dataframe(errores_lexicos, use_container_width=True)

        # --- Analisis sintactico ---
        self.analizador_sintactico.analizar(codigo)

        errores_sintacticos = self.analizador_sintactico.obtener_errores()

        st.subheader("Errores sintacticos")

        if len(errores_sintacticos) == 0:
            st.success("No hay errores sintacticos")
        else:
            st.dataframe(errores_sintacticos, use_container_width=True)

        #arbol sintactico
        st.subheader("Arbol sintactico")

        if len(errores_sintacticos) == 0:
            arbol = self.analizador_sintactico.arbol_sintactico()
            st.code(arbol, language="text")
        else:
            st.warning("No se puede mostrar el arbol sintactico debido a errores sintacticos.")


if __name__ == "__main__":
    app = App()
    app.ejecutar()
    