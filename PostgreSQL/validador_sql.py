class ValidadorSQL:

    ##lista de palabras clave
    pal_clave = ["SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "TABLE",
                      "INDEX", "VIEW", "TRIGGER", "FUNCTION", "PROCEDURE", "BEGIN", "COMMIT", "ROLLBACK"]

    ##se agrega un metodo para validar si el contenido del archivo es SQL, si esta vacio o no contiene palabras sql
    def validar_sql(self, contenido):
        mayusculas = contenido.upper()
        for palabra in self.pal_clave:
            if palabra in mayusculas:
                return True
        return False