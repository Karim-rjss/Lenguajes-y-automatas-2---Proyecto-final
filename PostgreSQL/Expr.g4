grammar Expr;

root: .*? EOF ;

// Fragments para insensibilidad a mayúsculas/minúsculas
fragment A:[aA]; fragment B:[bB]; fragment C:[cC]; fragment D:[dD];
fragment E:[eE]; fragment F:[fF]; fragment G:[gG]; fragment H:[hH];
fragment I:[iI]; fragment J:[jJ]; fragment K:[kK]; fragment L:[lL];
fragment M:[mM]; fragment N:[nN]; fragment O:[oO]; fragment P:[pP];
fragment Q:[qQ]; fragment R:[rR]; fragment S:[sS]; fragment T:[tT];
fragment U:[uU]; fragment V:[vV]; fragment W:[wW]; fragment X:[xX];
fragment Y:[yY]; fragment Z:[zZ];

// Palabras reservadas
SELECT: S E L E C T ;
FROM: F R O M ;
WHERE: W H E R E ;
INSERT: I N S E R T ;
INTO: I N T O ;
VALUES: V A L U E S ;
UPDATE: U P D A T E ;
SET: S E T ;
DELETE: D E L E T E ;
CREATE: C R E A T E ;
TABLE: T A B L E ;
DROP: D R O P ;
ALTER: A L T E R ;
PRIMARY: P R I M A R Y ;
KEY: K E Y ;
FOREIGN: F O R E I G N ;
REFERENCES: R E F E R E N C E S ;
NOT: N O T ;
NULL_: N U L L ;
DEFAULT: D E F A U L T ;
AND: A N D ;
OR: O R ;
ORDER: O R D E R ;
BY: B Y ;
GROUP: G R O U P ;
HAVING: H A V I N G ;
JOIN: J O I N ;
INNER: I N N E R ;
LEFT: L E F T ;
RIGHT: R I G H T ;
ON: O N ;
AS: A S ;
DISTINCT: D I S T I N C T ;
LIMIT: L I M I T ;

// Tipos de datos
INT_TYPE: I N T (E G E R)? ;
VARCHAR_TYPE: V A R C H A R ;
TEXT_TYPE: T E X T ;
BOOLEAN_TYPE: B O O L E A N ;
DATE_TYPE: D A T E ;
NUMERIC_TYPE: N U M E R I C ;
SERIAL_TYPE: S E R I A L ;

// Literales
NUM: [0-9]+ ('.' [0-9]+)? ;
CADENA: '\'' (~['\r\n] | '\'\'')* '\'' ;

// Identificadores
ID: [a-zA-Z_][a-zA-Z0-9_]* ;
ID_COMILLAS: '"' (~["\r\n])* '"' ;

// Operadores
IGUAL: '=' ;
DISTINTO: '<>' | '!=' ;
MENOR: '<' ;
MAYOR: '>' ;
MENOR_IGUAL: '<=' ;
MAYOR_IGUAL: '>=' ;
MAS: '+' ;
MENOS: '-' ;
POR: '*' ;
DIV: '/' ;
CONCAT: '||' ;

// Signos de puntuación
PUNTO: '.' ;
COMA: ',' ;
PUNTO_COMA: ';' ;
PAR_IZQ: '(' ;
PAR_DER: ')' ;

// Comentarios
COMENTARIO_LINEA: '--' ~[\r\n]* -> skip ;
COMENTARIO_BLOQUE: '/*' .*? '*/' -> skip ;

WS: [ \t\r\n]+ -> skip ;
