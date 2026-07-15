# Generated from ./Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,155,11,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,1,0,1,0,1,5,
        0,1,0,0,0,10,0,5,1,0,0,0,2,4,9,0,0,0,3,2,1,0,0,0,4,7,1,0,0,0,5,6,
        1,0,0,0,5,3,1,0,0,0,6,8,1,0,0,0,7,5,1,0,0,0,8,9,5,0,0,1,9,1,1,0,
        0,0,1,5
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "<INVALID>", 
                     "'<'", "'>'", "'<='", "'>='", "':='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'^'", "'||'", "'|'", "'&'", "'#'", 
                     "'~'", "'@'", "'?'", "'.'", "','", "';'", "':'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "INSERT", 
                      "INTO", "VALUES", "UPDATE", "SET", "DELETE", "RETURNING", 
                      "CREATE", "TABLE", "DROP", "ALTER", "INDEX", "VIEW", 
                      "SCHEMA", "SEQUENCE", "CASCADE", "RESTRICT", "PRIMARY", 
                      "KEY", "FOREIGN", "REFERENCES", "UNIQUE", "CHECK", 
                      "CONSTRAINT", "NOT", "NULL_P", "DEFAULT", "AND", "OR", 
                      "IS", "IN", "LIKE", "ILIKE", "BETWEEN", "EXISTS", 
                      "CASE", "WHEN", "THEN", "ELSE", "END", "ORDER", "BY", 
                      "GROUP", "HAVING", "JOIN", "INNER", "LEFT", "RIGHT", 
                      "FULL", "OUTER", "ON", "AS", "DISTINCT", "LIMIT", 
                      "OFFSET", "WITH", "UNION", "ALL", "TRUE_P", "FALSE_P", 
                      "BEGIN_TX", "START", "TRANSACTION", "COMMIT", "ROLLBACK", 
                      "SAVEPOINT", "RELEASE", "WORK", "FUNCTION", "PROCEDURE", 
                      "RETURNS", "RETURN", "LANGUAGE", "DECLARE", "IF", 
                      "LOOP", "WHILE", "FOR", "EXECUTE", "CALL", "TRIGGER", 
                      "BEFORE", "AFTER", "INSTEAD", "OF", "EACH", "ROW", 
                      "STATEMENT", "NEW", "OLD", "PERFORM", "RAISE", "EXCEPTION", 
                      "SMALLINT_TYPE", "INT_TYPE", "BIGINT_TYPE", "SERIAL_TYPE", 
                      "BIGSERIAL_TYPE", "NUMERIC_TYPE", "REAL_TYPE", "DOUBLE_TYPE", 
                      "VARCHAR_TYPE", "CHAR_TYPE", "TEXT_TYPE", "BOOLEAN_TYPE", 
                      "DATE_TYPE", "TIME_TYPE", "TIMESTAMP_TYPE", "INTERVAL_TYPE", 
                      "JSON_TYPE", "BYTEA_TYPE", "ICONST", "FCONST", "SCONST", 
                      "ESCAPE_SCONST", "ID_COMILLAS", "DELIM_DOLAR", "DOLAR_PARAM", 
                      "ID", "IGUAL", "DISTINTO", "MENOR", "MAYOR", "MENOR_IGUAL", 
                      "MAYOR_IGUAL", "ASIGNA", "MAS", "MENOS", "POR", "DIV", 
                      "MODULO", "POTENCIA", "CONCAT", "PIPE", "AMPERSAND", 
                      "NUMERAL", "TILDE", "ARROBA", "INTERROGACION", "PUNTO", 
                      "COMA", "PUNTO_COMA", "DOS_PUNTOS", "PAR_IZQ", "PAR_DER", 
                      "COR_IZQ", "COR_DER", "LLAVE_IZQ", "LLAVE_DER", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE", "WS" ]

    RULE_root = 0

    ruleNames =  [ "root" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    WHERE=3
    INSERT=4
    INTO=5
    VALUES=6
    UPDATE=7
    SET=8
    DELETE=9
    RETURNING=10
    CREATE=11
    TABLE=12
    DROP=13
    ALTER=14
    INDEX=15
    VIEW=16
    SCHEMA=17
    SEQUENCE=18
    CASCADE=19
    RESTRICT=20
    PRIMARY=21
    KEY=22
    FOREIGN=23
    REFERENCES=24
    UNIQUE=25
    CHECK=26
    CONSTRAINT=27
    NOT=28
    NULL_P=29
    DEFAULT=30
    AND=31
    OR=32
    IS=33
    IN=34
    LIKE=35
    ILIKE=36
    BETWEEN=37
    EXISTS=38
    CASE=39
    WHEN=40
    THEN=41
    ELSE=42
    END=43
    ORDER=44
    BY=45
    GROUP=46
    HAVING=47
    JOIN=48
    INNER=49
    LEFT=50
    RIGHT=51
    FULL=52
    OUTER=53
    ON=54
    AS=55
    DISTINCT=56
    LIMIT=57
    OFFSET=58
    WITH=59
    UNION=60
    ALL=61
    TRUE_P=62
    FALSE_P=63
    BEGIN_TX=64
    START=65
    TRANSACTION=66
    COMMIT=67
    ROLLBACK=68
    SAVEPOINT=69
    RELEASE=70
    WORK=71
    FUNCTION=72
    PROCEDURE=73
    RETURNS=74
    RETURN=75
    LANGUAGE=76
    DECLARE=77
    IF=78
    LOOP=79
    WHILE=80
    FOR=81
    EXECUTE=82
    CALL=83
    TRIGGER=84
    BEFORE=85
    AFTER=86
    INSTEAD=87
    OF=88
    EACH=89
    ROW=90
    STATEMENT=91
    NEW=92
    OLD=93
    PERFORM=94
    RAISE=95
    EXCEPTION=96
    SMALLINT_TYPE=97
    INT_TYPE=98
    BIGINT_TYPE=99
    SERIAL_TYPE=100
    BIGSERIAL_TYPE=101
    NUMERIC_TYPE=102
    REAL_TYPE=103
    DOUBLE_TYPE=104
    VARCHAR_TYPE=105
    CHAR_TYPE=106
    TEXT_TYPE=107
    BOOLEAN_TYPE=108
    DATE_TYPE=109
    TIME_TYPE=110
    TIMESTAMP_TYPE=111
    INTERVAL_TYPE=112
    JSON_TYPE=113
    BYTEA_TYPE=114
    ICONST=115
    FCONST=116
    SCONST=117
    ESCAPE_SCONST=118
    ID_COMILLAS=119
    DELIM_DOLAR=120
    DOLAR_PARAM=121
    ID=122
    IGUAL=123
    DISTINTO=124
    MENOR=125
    MAYOR=126
    MENOR_IGUAL=127
    MAYOR_IGUAL=128
    ASIGNA=129
    MAS=130
    MENOS=131
    POR=132
    DIV=133
    MODULO=134
    POTENCIA=135
    CONCAT=136
    PIPE=137
    AMPERSAND=138
    NUMERAL=139
    TILDE=140
    ARROBA=141
    INTERROGACION=142
    PUNTO=143
    COMA=144
    PUNTO_COMA=145
    DOS_PUNTOS=146
    PAR_IZQ=147
    PAR_DER=148
    COR_IZQ=149
    COR_DER=150
    LLAVE_IZQ=151
    LLAVE_DER=152
    COMENTARIO_LINEA=153
    COMENTARIO_BLOQUE=154
    WS=155

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 2
                    self.matchWildcard() 
                self.state = 7
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 8
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





