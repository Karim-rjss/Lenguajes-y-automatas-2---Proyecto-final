# Proyecto final - Analizador léxico y sintáctico de PostgreSQL

---
## Descripción

Este es un proyecto hecho en ANTLR usando Python, G4 y Streamlit, donde se muestra un analizador léxico y sintáctico hecho para el lenguaje de PostgreSQL.

El propósito y la función de este programa, es poder tokenizar el lenguaje mediante el uso de reglas léxicas que se definieron en el archivo `Expr.g4`, de igual manera, agregar todas las reglas sintácticas dentro del mismo archivo para tomar en cuenta todas las validaciones que se tienen dentro del código a la hora de subir un código del tipo `.sql`.  

Se despliega una aplicación web basada en Streamlit para el uso del *analizador.*

<img width="1914" height="1126" alt="{2BA6C4A3-A17D-4B73-A0FD-788D907286F6}" src="https://github.com/user-attachments/assets/4ffcac55-f844-48b4-b819-021a2ee4c491" />

---
## Características
- Es una aplicación web que se despliega en un servidor local
- Solamente admite archivos `.sql`
- Muestra un árbol sintáctico en dos formatos:
	- Plano
	- Indentación por niveles
- En caso de errores, muestra los caracteres que no identifica el sistema
	- Esto aplica tanto para el **léxico** como el **sintáctico**
---
## Requisitos previos
>[!IMPORTANT]
>Tomar en cuenta que debemos de tener instalado tanto Java y el archivo `.jar` apuntando hacia la variable de entorno del sistema. Para descargar el `.jar` del ANTLR, lo obtenemos de la siguiente página: [https://www.antlr.org/download.html](https://www.antlr.org/download.html)
>De igual manera, es necesario tener la última versión de Python, se puede obtener de la siguiente liga: https://www.python.org/downloads/

---
## Instalación

### 1. Clonar el repositorio
Clonamos el repositorio dentro de nuestra máquina, el cual se usa el siguiente comando:

```powershell
git clone https://github.com/Karim-rjss/Lenguajes-y-automatas-2---Proyecto-final.git
```

### 2. Instalar dependencias de Python
Instalamos las dependencias de Python necesarias para el proyecto:

**Streamlit:**
```powershell
pip install streamlit
```

**ANTLR4:**
```powershell
pip install antlr4-python3-runtime
```

*Verificar que se han instalado:*
```powershell
pip show streamlit
```
```powershell
pip show antlr4-python3-runtime
```
### 3. Instalar Java y ANTLR
Es necesario tener instalado Java y ANTLR.

Se pueden encontrar en las siguientes ligas:

- ANTLR: https://www.antlr.org/download.html
	- Una vez descargado el archivo, lo guardamos dentro de una carpeta que no vamos a usar dentro de nuestras máquinas.
- Java JDK: https://jdk.java.net/ 
### 4. Compilar la gramática
Utilizando tu terminal (dependiendo de tu SO), debemos de ubicarnos dentro de la carpeta:
```powershell
cd "C:\TU_RUTA\Proyecto final\PostgreSQL"
```

Compilamos ANTLR:
```powershell
java -jar "C:\RUTA_ARCHIVO_JAR_ANTLR\antlr-4.13.2-complete.jar" -Dlanguage=Python3 -no-listener Expr.g4
```

Esto nos va a garantizar que el lenguaje esté listo para usarse.

>[!NOTE]
>*Si modificas `Expr.g4`, recuerda volver a ejecutar el comando de compilación antes de correr la app, o los cambios no se reflejarán.*

---
## Uso
Para poder usar la aplicación, simplemente debemos de ubicarnos con la terminal dentro de la ruta donde clonamos el repositorio:
```powershell
cd "C:\TU_RUTA\Proyecto final\PostgreSQL"
```

Una vez hecho esto, simplemente vamos a ejecutar Streamlit utilizando el siguiente comando:
```powershell
streamlit run app.py
```
Nos va a redirigir a la aplicación web del analizador de manera automática.

---
## Estructura del proyecto

```powershell
C:.
│   README.md
│   
└───PostgreSQL
    │   analizador_lexico.py
    │   analizador_sintactico.py
    │   app.py
    │   archivo.py
    │   Expr.g4
    │   Expr.interp
    │   Expr.tokens
    │   ExprLexer.interp
    │   ExprLexer.py
    │   ExprLexer.tokens
    │   ExprParser.py
    │   validador_sql.py
    │   
    ├───.antlr
    │       Expr.interp
    │       Expr.tokens
    │       ExprLexer.interp
    │       ExprLexer.java
    │       ExprLexer.tokens
    │       ExprParser.java
    │       
    ├───.streamlit
    │       config.toml
    │       
    └───__pycache__
            analizador_lexico.cpython-313.pyc
            analizador_sintactico.cpython-313.pyc
            archivo.cpython-313.pyc
            ExprLexer.cpython-313.pyc
            ExprParser.cpython-313.pyc
            validador_sql.cpython-313.pyc
```
---
## Autores
- Martín Arce Rodríguez 22030946  - (*MartinAR0703*)
- Adrián Esteban Velázquez Terán 22030482 - (*Tea-Run*)
- Gadiel Karim Ríos Rojas 22030161 -  (*Karim-rjss*)
