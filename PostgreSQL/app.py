import streamlit as st
from archivo import Archivo
from analizador_lexico import AnalizadorLexico
from validador_sql import ValidadorSQL


class App:

    def __init__(self):
        st.set_page_config(page_title="Analizador Lexico", layout="wide")
        self.analizador = AnalizadorLexico()
        self.validador = ValidadorSQL()

    def ejecutar(self):
        st.title("Analizador Lexico con ANTLR y Streamlit")
        st.write("Sube un archivo `.sql` para ver tokens y errores lexicos.")

        archivo_subido = st.file_uploader("Selecciona tu archivo", type=["sql"])

        if archivo_subido is None:
            st.info("Primero sube un archivo .sql")
            return

        archivo = Archivo(archivo_subido)

        if not archivo.es_txt():
            st.error("El archivo debe ser .sql")
            return

        codigo = archivo.leer()

        ##continuacion de la validacion de sql (archivo.py)
        if not self.validador.validar_sql(codigo):
            st.error("El contenido del archivo no parece ser SQL válido.")
            return

        info = archivo.obtener_info()

        st.subheader("Informacion del archivo")
        st.write("Nombre:", info["nombre"])
        st.write("Extension:", info["extension"])

        st.subheader("Codigo original")
        st.code(codigo, language="text")

        self.analizador.analizar(codigo)

        tokens = self.analizador.obtener_tokens()
        errores = self.analizador.obtener_errores()

        st.subheader("Tokens")

        if len(tokens) == 0:
            st.warning("No se encontraron tokens")
        else:
            st.dataframe(tokens, use_container_width=True)

        st.subheader("Errores lexicos")

        if len(errores) == 0:
            st.success("No hay errores lexicos")
        else:
            st.dataframe(errores, use_container_width=True)


if __name__ == "__main__":
    app = App()
    app.ejecutar()