// Generated from c:/LAII/Lenguajes-y-automatas-2---Proyecto-final/PostgreSQL/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SELECT=1, FROM=2, WHERE=3, INSERT=4, INTO=5, VALUES=6, UPDATE=7, SET=8, 
		DELETE=9, CREATE=10, TABLE=11, DROP=12, ALTER=13, PRIMARY=14, KEY=15, 
		FOREIGN=16, REFERENCES=17, NOT=18, NULL_=19, DEFAULT=20, AND=21, OR=22, 
		ORDER=23, BY=24, GROUP=25, HAVING=26, JOIN=27, INNER=28, LEFT=29, RIGHT=30, 
		ON=31, AS=32, DISTINCT=33, LIMIT=34, INT_TYPE=35, VARCHAR_TYPE=36, TEXT_TYPE=37, 
		BOOLEAN_TYPE=38, DATE_TYPE=39, NUMERIC_TYPE=40, SERIAL_TYPE=41, NUM=42, 
		CADENA=43, ID=44, ID_COMILLAS=45, IGUAL=46, DISTINTO=47, MENOR=48, MAYOR=49, 
		MENOR_IGUAL=50, MAYOR_IGUAL=51, MAS=52, MENOS=53, POR=54, DIV=55, CONCAT=56, 
		PUNTO=57, COMA=58, PUNTO_COMA=59, PAR_IZQ=60, PAR_DER=61, COMENTARIO_LINEA=62, 
		COMENTARIO_BLOQUE=63, WS=64;
	public static final int
		RULE_root = 0;
	private static String[] makeRuleNames() {
		return new String[] {
			"root"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, "'='", null, 
			"'<'", "'>'", "'<='", "'>='", "'+'", "'-'", "'*'", "'/'", "'||'", "'.'", 
			"','", "';'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SELECT", "FROM", "WHERE", "INSERT", "INTO", "VALUES", "UPDATE", 
			"SET", "DELETE", "CREATE", "TABLE", "DROP", "ALTER", "PRIMARY", "KEY", 
			"FOREIGN", "REFERENCES", "NOT", "NULL_", "DEFAULT", "AND", "OR", "ORDER", 
			"BY", "GROUP", "HAVING", "JOIN", "INNER", "LEFT", "RIGHT", "ON", "AS", 
			"DISTINCT", "LIMIT", "INT_TYPE", "VARCHAR_TYPE", "TEXT_TYPE", "BOOLEAN_TYPE", 
			"DATE_TYPE", "NUMERIC_TYPE", "SERIAL_TYPE", "NUM", "CADENA", "ID", "ID_COMILLAS", 
			"IGUAL", "DISTINTO", "MENOR", "MAYOR", "MENOR_IGUAL", "MAYOR_IGUAL", 
			"MAS", "MENOS", "POR", "DIV", "CONCAT", "PUNTO", "COMA", "PUNTO_COMA", 
			"PAR_IZQ", "PAR_DER", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(5);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(2);
					matchWildcard();
					}
					} 
				}
				setState(7);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(8);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001@\u000b\u0002\u0000\u0007\u0000\u0001\u0000\u0005\u0000\u0004"+
		"\b\u0000\n\u0000\f\u0000\u0007\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0005\u0000\u0001\u0000\u0000\u0000\n\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0002\u0004\t\u0000\u0000\u0000\u0003\u0002\u0001\u0000\u0000\u0000"+
		"\u0004\u0007\u0001\u0000\u0000\u0000\u0005\u0006\u0001\u0000\u0000\u0000"+
		"\u0005\u0003\u0001\u0000\u0000\u0000\u0006\b\u0001\u0000\u0000\u0000\u0007"+
		"\u0005\u0001\u0000\u0000\u0000\b\t\u0005\u0000\u0000\u0001\t\u0001\u0001"+
		"\u0000\u0000\u0000\u0001\u0005";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}