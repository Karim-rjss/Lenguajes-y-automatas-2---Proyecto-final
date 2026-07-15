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
        4,1,64,11,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,1,0,1,0,1,5,
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
                     "<INVALID>", "<INVALID>", "'='", "<INVALID>", "'<'", 
                     "'>'", "'<='", "'>='", "'+'", "'-'", "'*'", "'/'", 
                     "'||'", "'.'", "','", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "INSERT", 
                      "INTO", "VALUES", "UPDATE", "SET", "DELETE", "CREATE", 
                      "TABLE", "DROP", "ALTER", "PRIMARY", "KEY", "FOREIGN", 
                      "REFERENCES", "NOT", "NULL_", "DEFAULT", "AND", "OR", 
                      "ORDER", "BY", "GROUP", "HAVING", "JOIN", "INNER", 
                      "LEFT", "RIGHT", "ON", "AS", "DISTINCT", "LIMIT", 
                      "INT_TYPE", "VARCHAR_TYPE", "TEXT_TYPE", "BOOLEAN_TYPE", 
                      "DATE_TYPE", "NUMERIC_TYPE", "SERIAL_TYPE", "NUM", 
                      "CADENA", "ID", "ID_COMILLAS", "IGUAL", "DISTINTO", 
                      "MENOR", "MAYOR", "MENOR_IGUAL", "MAYOR_IGUAL", "MAS", 
                      "MENOS", "POR", "DIV", "CONCAT", "PUNTO", "COMA", 
                      "PUNTO_COMA", "PAR_IZQ", "PAR_DER", "COMENTARIO_LINEA", 
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
    CREATE=10
    TABLE=11
    DROP=12
    ALTER=13
    PRIMARY=14
    KEY=15
    FOREIGN=16
    REFERENCES=17
    NOT=18
    NULL_=19
    DEFAULT=20
    AND=21
    OR=22
    ORDER=23
    BY=24
    GROUP=25
    HAVING=26
    JOIN=27
    INNER=28
    LEFT=29
    RIGHT=30
    ON=31
    AS=32
    DISTINCT=33
    LIMIT=34
    INT_TYPE=35
    VARCHAR_TYPE=36
    TEXT_TYPE=37
    BOOLEAN_TYPE=38
    DATE_TYPE=39
    NUMERIC_TYPE=40
    SERIAL_TYPE=41
    NUM=42
    CADENA=43
    ID=44
    ID_COMILLAS=45
    IGUAL=46
    DISTINTO=47
    MENOR=48
    MAYOR=49
    MENOR_IGUAL=50
    MAYOR_IGUAL=51
    MAS=52
    MENOS=53
    POR=54
    DIV=55
    CONCAT=56
    PUNTO=57
    COMA=58
    PUNTO_COMA=59
    PAR_IZQ=60
    PAR_DER=61
    COMENTARIO_LINEA=62
    COMENTARIO_BLOQUE=63
    WS=64

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





