grammar Expr;

//Reglas sintacticas
root: stmt+ EOF;
stmt : select_stmt PUNTO_COMA
        | insert_stmt PUNTO_COMA
        | update_stmt PUNTO_COMA
        | delete_stmt PUNTO_COMA 
        | begin_stmt PUNTO_COMA
        | commit_stmt PUNTO_COMA
        | rollback_stmt PUNTO_COMA
        | create_table_stmt PUNTO_COMA
        | create_index_stmt PUNTO_COMA
        | create_view_stmt PUNTO_COMA 
        | create_function_stmt PUNTO_COMA
        | create_procedure_stmt PUNTO_COMA
        | create_trigger_stmt PUNTO_COMA
        | alter_table_stmt PUNTO_COMA
        | drop_stmt PUNTO_COMA
        ;

identificador : ID | ID_COMILLAS ; //identificador global, puede ser un ID normal o un ID entre comillas

//SELECT ----------------------------------------------------------------------------
select_stmt : SELECT lista_columnas FROM tabla_ref (join_clausula)* (WHERE condicion)? (GROUP BY lista_ids)? (HAVING condicion_having)? (ORDER BY (identificador PUNTO)? identificador)? ;
tabla_ref : identificador (AS? identificador)? ;
join_clausula : joins tabla_ref ON condicion_join ;
joins : JOIN | INNER JOIN | LEFT JOIN | RIGHT JOIN | FULL JOIN | OUTER JOIN ;
condicion : (identificador PUNTO)? identificador operador_comp valor ;
condicion_join : identificador PUNTO identificador operador_comp identificador PUNTO identificador ;
condicion_having : func_agregadas_select operador_comp valor ;
operador_comp : IGUAL | DISTINTO | MENOR | MAYOR | MENOR_IGUAL | MAYOR_IGUAL ;
valor : ICONST | FCONST | SCONST | identificador | valor_boolean ;
as_clausula : AS identificador ;
columna_select : (identificador PUNTO)? identificador (as_clausula)? ;
elemento_select : columna_select | func_agregadas_select ;
lista_columnas : POR | elemento_select (COMA elemento_select)* ;
func_agregadas : COUNT | SUM | AVG | MIN | MAX ;
func_agregadas_select : func_agregadas PAR_IZQ (POR | (identificador PUNTO)? identificador) PAR_DER (as_clausula)? ;
lista_ids : identificador (COMA identificador)* ;
valor_boolean : TRUE_P | FALSE_P ;

//INSERT ----------------------------------------------------------------------------
insert_stmt : INSERT INTO identificador PAR_IZQ lista_ids PAR_DER VALUES PAR_IZQ lista_valores_insert PAR_DER ;
lista_valores_insert : valor (COMA valor)* ;

//UPDATE ----------------------------------------------------------------------------
asignacion : identificador IGUAL valor ;
lista_asignaciones : asignacion (COMA asignacion)* ;
update_stmt : UPDATE identificador SET lista_asignaciones (WHERE condicion)? ;

//DELETE ----------------------------------------------------------------------------
delete_stmt : DELETE FROM identificador (WHERE condicion)? ;

//Transacciones ---------------------------------------------------------------------
begin_stmt : BEGIN_TX ;
commit_stmt : COMMIT ;
rollback_stmt : ROLLBACK ;

//Tablas
//CREATE TABLE -----------------------------------------------------------------------
tipo_dato : SMALLINT_TYPE | INT_TYPE | BIGINT_TYPE | SERIAL_TYPE | BIGSERIAL_TYPE | NUMERIC_TYPE | REAL_TYPE | 
DOUBLE_TYPE | VARCHAR_TYPE | CHAR_TYPE | TEXT_TYPE | BOOLEAN_TYPE | DATE_TYPE | TIME_TYPE | TIMESTAMP_TYPE | INTERVAL_TYPE 
| JSON_TYPE | BYTEA_TYPE ;
columna_create : identificador tipo_dato (restricciones)? ;
restricciones : PRIMARY KEY | NOT NULL_P | UNIQUE | DEFAULT valor | REFERENCES identificador PAR_IZQ identificador PAR_DER ;
fk_tabla : FOREIGN KEY PAR_IZQ identificador PAR_DER REFERENCES identificador PAR_IZQ identificador PAR_DER ;
pk_tabla : PRIMARY KEY PAR_IZQ lista_ids PAR_DER ; 
elemento_create : columna_create | fk_tabla | pk_tabla ;
lista_columnas_create : elemento_create (COMA elemento_create)* ;
create_table_stmt : CREATE TABLE identificador PAR_IZQ lista_columnas_create PAR_DER ;

//Indices
//CREATE INDEX -----------------------------------------------------------------------
create_index_stmt : CREATE (UNIQUE)? INDEX identificador ON identificador PAR_IZQ lista_ids PAR_DER ;

//Vistas
//CREATE VIEW ------------------------------------------------------------------------
create_view_stmt : CREATE VIEW identificador AS select_stmt ;

//Funciones
//CREATE FUNCTION --------------------------------------------------------------------
create_function_stmt : CREATE FUNCTION identificador PAR_IZQ lista_parametros PAR_DER RETURNS tipo_dato LANGUAGE ID AS DELIM_DOLAR ;
lista_parametros : (parametro (COMA parametro)*)? ;
parametro : identificador tipo_dato ;

//CREATE PROCEDURE --------------------------------------------------------------------
create_procedure_stmt : CREATE PROCEDURE identificador PAR_IZQ lista_parametros PAR_DER LANGUAGE ID AS DELIM_DOLAR ;

//TRIGGERS
//CREATE TRIGGER ---------------------------------------------------------------------
create_trigger_stmt : CREATE TRIGGER identificador when_trigger evento_trigger ON identificador FOR EACH row_stmt EXECUTE FUNCTION identificador PAR_IZQ PAR_DER ;
when_trigger : BEFORE | AFTER | INSTEAD OF ;
evento_trigger : evento (OR evento)* ;
evento : INSERT | UPDATE | DELETE ;
row_stmt : ROW | STATEMENT ;

//ALTER TABLE ----------------------------------------------------------------------
alter_table_stmt : ALTER TABLE identificador alter_sentences ;
alter_sentences : ADD COLUMN columna_create | DROP COLUMN identificador | ADD CONSTRAINT identificador PRIMARY KEY PAR_IZQ lista_ids PAR_DER | 
ADD CONSTRAINT identificador FOREIGN KEY PAR_IZQ lista_ids PAR_DER REFERENCES identificador PAR_IZQ lista_ids PAR_DER ;

//algunos drops vaya
drop_opciones: DROP TABLE | DROP INDEX | DROP VIEW | DROP FUNCTION | DROP PROCEDURE | DROP TRIGGER ;
drop_stmt : DROP (TABLE | INDEX | VIEW | FUNCTION | PROCEDURE) identificador (CASCADE | RESTRICT)? 
| DROP TRIGGER identificador ON identificador (CASCADE | RESTRICT)?;


//Lexico
// Fragments para insensibilidad a mayúsculas/minúsculas
fragment A:[aA]; fragment B:[bB]; fragment C:[cC]; fragment D:[dD];
fragment E:[eE]; fragment F:[fF]; fragment G:[gG]; fragment H:[hH];
fragment I:[iI]; fragment J:[jJ]; fragment K:[kK]; fragment L:[lL];
fragment M:[mM]; fragment N:[nN]; fragment O:[oO]; fragment P:[pP];
fragment Q:[qQ]; fragment R:[rR]; fragment S:[sS]; fragment T:[tT];
fragment U:[uU]; fragment V:[vV]; fragment W:[wW]; fragment X:[xX];
fragment Y:[yY]; fragment Z:[zZ];

// Palabras reservadas: DML básico
SELECT: S E L E C T ;
FROM: F R O M ;
WHERE: W H E R E ;
INSERT: I N S E R T ;
INTO: I N T O ;
VALUES: V A L U E S ;
UPDATE: U P D A T E ;
SET: S E T ;
DELETE: D E L E T E ;
RETURNING: R E T U R N I N G ;

// DDL
CREATE: C R E A T E ;
TABLE: T A B L E ;
DROP: D R O P ;
ALTER: A L T E R ;
INDEX: I N D E X ;
VIEW: V I E W ;
SCHEMA: S C H E M A ;
SEQUENCE: S E Q U E N C E ;
CASCADE: C A S C A D E ;
RESTRICT: R E S T R I C T ;
COLUMN: C O L U M N ;
ADD: A D D ; 

// Restricciones
PRIMARY: P R I M A R Y ;
KEY: K E Y ;
FOREIGN: F O R E I G N ;
REFERENCES: R E F E R E N C E S ;
UNIQUE: U N I Q U E ;
CHECK: C H E C K ;
CONSTRAINT: C O N S T R A I N T ;
NOT: N O T ;
NULL_P: N U L L ;
DEFAULT: D E F A U L T ;

// Lógicos / condicionales de consulta
AND: A N D ;
OR: O R ;
IS: I S ;
IN: I N ;
LIKE: L I K E ;
ILIKE: I L I K E ;
BETWEEN: B E T W E E N ;
EXISTS: E X I S T S ;
CASE: C A S E ;
WHEN: W H E N ;
THEN: T H E N ;
ELSE: E L S E ;
END: E N D ;
ORDER: O R D E R ;
BY: B Y ;
GROUP: G R O U P ;
HAVING: H A V I N G ;
JOIN: J O I N ;
INNER: I N N E R ;
LEFT: L E F T ;
RIGHT: R I G H T ;
FULL: F U L L ;
OUTER: O U T E R ;
ON: O N ;
AS: A S ;
DISTINCT: D I S T I N C T ;
LIMIT: L I M I T ;
OFFSET: O F F S E T ;
WITH: W I T H ;
UNION: U N I O N ;
ALL: A L L ;

// Booleanos y NULL
TRUE_P: T R U E ;
FALSE_P: F A L S E ;

// Transacciones
BEGIN_TX: B E G I N ;
START: S T A R T ;
TRANSACTION: T R A N S A C T I O N ;
COMMIT: C O M M I T ;
ROLLBACK: R O L L B A C K ;
SAVEPOINT: S A V E P O I N T ;
RELEASE: R E L E A S E ;
WORK: W O R K ;

// Funciones y triggers
FUNCTION: F U N C T I O N ;
PROCEDURE: P R O C E D U R E ;
RETURNS: R E T U R N S ;
RETURN: R E T U R N ;
LANGUAGE: L A N G U A G E ;
DECLARE: D E C L A R E ;
IF: I F ;
LOOP: L O O P ;
WHILE: W H I L E ;
FOR: F O R ;
EXECUTE: E X E C U T E ;
CALL: C A L L ;
TRIGGER: T R I G G E R ;
BEFORE: B E F O R E ;
AFTER: A F T E R ;
INSTEAD: I N S T E A D ;
OF: O F ;
EACH: E A C H ;
ROW: R O W ;
STATEMENT: S T A T E M E N T ;
NEW: N E W ;
OLD: O L D ;
PERFORM: P E R F O R M ;
RAISE: R A I S E ;
EXCEPTION: E X C E P T I O N ;

// Tipos de datos
SMALLINT_TYPE: S M A L L I N T ;
INT_TYPE: I N T (E G E R)? ;
BIGINT_TYPE: B I G I N T ;
SERIAL_TYPE: S E R I A L ;
BIGSERIAL_TYPE: B I G S E R I A L ;
NUMERIC_TYPE: N U M E R I C ;
REAL_TYPE: R E A L ;
DOUBLE_TYPE: D O U B L E ' ' P R E C I S I O N ;
VARCHAR_TYPE: V A R C H A R ;
CHAR_TYPE: C H A R ;
TEXT_TYPE: T E X T ;
BOOLEAN_TYPE: B O O L E A N ;
DATE_TYPE: D A T E ;
TIME_TYPE: T I M E ;
TIMESTAMP_TYPE: T I M E S T A M P ;
INTERVAL_TYPE: I N T E R V A L ;
JSON_TYPE: J S O N ;
BYTEA_TYPE: B Y T E A ;

// Funciones agregadas
COUNT: C O U N T ;
SUM: S U M ;
AVG: A V G ;
MIN: M I N ;
MAX: M A X ;

// Enteros
ICONST: [0-9]+ ;

// Decimales / punto flotante (incluye notación exponencial)
FCONST: [0-9]+ '.' [0-9]* | '.' [0-9]+ | ([0-9]+ ('.' [0-9]*)?) [eE] [+-]? [0-9]+ | [0-9]+ [eE] [+-]? [0-9]+ ;

// Cadenas de texto estándar
SCONST: '\'' ( ~['] | '\'\'' )* '\'' ;

// Cadenas con escape estilo C
ESCAPE_SCONST: ('E'|'e') '\'' ( ~['\\] | '\\' . | '\'\'' )* '\'' ;

// Identificador delimitado
ID_COMILLAS: '"' (~["\r\n])* '"' ;

// Cadena delimitada por dólar
DELIM_DOLAR: '$' [a-zA-Z_]* '$' .*? '$' [a-zA-Z_]* '$' ;

// Parámetro posicional
DOLAR_PARAM: '$' [0-9]+ ;

// Identificadores
ID: [a-zA-Z_][a-zA-Z0-9_$]* ;

// Operadores
IGUAL: '=' ;
DISTINTO: '<>' | '!=' ;
MENOR: '<' ;
MAYOR: '>' ;
MENOR_IGUAL: '<=' ;
MAYOR_IGUAL: '>=' ;
ASIGNA: ':=' ;
MAS: '+' ;
MENOS: '-' ;
POR: '*' ;
DIV: '/' ;
MODULO: '%' ;
POTENCIA: '^' ;
CONCAT: '||' ;
PIPE: '|' ;
AMPERSAND: '&' ;
NUMERAL: '#' ;
TILDE: '~' ;
ARROBA: '@' ;
INTERROGACION: '?' ;

// Delimitadores
PUNTO: '.' ;
COMA: ',' ;
PUNTO_COMA: ';' ;
DOS_PUNTOS: ':' ;
PAR_IZQ: '(' ;
PAR_DER: ')' ;
COR_IZQ: '[' ;
COR_DER: ']' ;
LLAVE_IZQ: '{' ;
LLAVE_DER: '}' ;

// Comentarios y espacios en blanco
COMENTARIO_LINEA: '--' ~[\r\n]* -> skip ;
COMENTARIO_BLOQUE: '/*' .*? '*/' -> skip ;

WS: [ \t\r\n]+ -> skip ;