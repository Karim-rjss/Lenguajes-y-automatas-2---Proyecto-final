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

        self.arbol = None #arbol

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

        self.arbol = self.parser.root()

    # Metodo para obtener errores sintacticos
    def obtener_errores(self):

        # Retornamos la lista de errores
        return self.errores.lista

    #metodo del arbol
    def arbol_sintactico(self):
        if self.arbol is None:
            return ""
        return self.arbol.toStringTree(recog=self.parser)
    
    def arbol_identado(self):
        if self.arbol is None:
            return ""
        resultado = []

        def recorrido_nodos(nodo, nivel):
            from antlr4.tree.Tree import TerminalNode
            if isinstance(nodo, TerminalNode):
                texto = nodo.getText()
                resultado.append("  " * nivel + texto)
            else:
                nom_regla = self.parser.ruleNames[nodo.getRuleIndex()]
                resultado.append("  " * nivel + nom_regla)
                for i in range(nodo.getChildCount()):
                    recorrido_nodos(nodo.getChild(i), nivel + 1)

        recorrido_nodos(self.arbol, 0)
        return "\n".join(resultado)