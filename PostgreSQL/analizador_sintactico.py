# Importamos herramientas principales de ANTLR
from antlr4 import InputStream, CommonTokenStream

# Importamos ErrorListener para capturar errores sintacticos
from antlr4.error.ErrorListener import ErrorListener

# Importamos el lexer y el parser generados por ANTLR
from ExprLexer import ExprLexer
from ExprParser import ExprParser


# Clase para guardar errores sintacticos
class ErroresSintacticos(ErrorListener):

    # Constructor
    def __init__(self):
        # Lista donde guardaremos los errores
        self.lista = []

        #arbol sintactico
        self.arbol = None

    # Metodo que ANTLR ejecuta cuando encuentra error sintactico
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        # Guardamos el error en la lista
        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


# Clase para hacer el analisis sintactico
class AnalizadorSintactico:

    # Constructor
    def __init__(self):

        # Variable para guardar el lexer
        self.lexer = None

        # Variable para guardar el parser
        self.parser = None

        # Variable para guardar los tokens
        self.tokens = None

        # Objeto para guardar errores sintacticos
        self.errores = ErroresSintacticos()

    # Metodo para analizar codigo
    def analizar(self, codigo):

        # Convertimos el texto en entrada para ANTLR
        entrada = InputStream(codigo)

        # Creamos el lexer
        self.lexer = ExprLexer(entrada)

        # Creamos el flujo de tokens a partir del lexer
        self.tokens = CommonTokenStream(self.lexer)

        # Creamos el parser a partir del flujo de tokens
        self.parser = ExprParser(self.tokens)

        # Quitamos los errores normales de ANTLR
        self.parser.removeErrorListeners()

        # Agregamos nuestro capturador de errores
        self.parser.addErrorListener(self.errores)

        #metodo para obtener el arbol je
        def arbol_sintactico(self):
            if self.arbol is None:
                return ""
            return self.arbol.toStringTree(recog=self.parser)

    # Metodo para obtener errores sintacticos
    def obtener_errores(self):
        
        # Retornamos la lista de errores
        return self.errores.lista