# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
import numpy as np
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .mpsListener import mpsListener
else:
    from mpsListener import mpsListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\23\u00a1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\5\2\61\n\2\3\2\5\2\64\n\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write(u"\5\3<\n\3\3\3\5\3?\n\3\3\4\3\4\6\4C\n\4\r\4\16\4D\3\5")
        buf.write(u"\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t")
        buf.write(u"\3\n\3\n\3\n\3\n\3\13\3\13\6\13[\n\13\r\13\16\13\\\3")
        buf.write(u"\f\6\f`\n\f\r\f\16\fa\3\r\6\re\n\r\r\r\16\rf\3\16\6\16")
        buf.write(u"j\n\16\r\16\16\16k\3\17\3\17\3\17\3\17\3\17\5\17s\n\17")
        buf.write(u"\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20|\n\20\3\20\3")
        buf.write(u"\20\3\21\3\21\3\21\3\21\3\21\5\21\u0085\n\21\3\21\3\21")
        buf.write(u"\3\22\3\22\3\22\3\22\5\22\u008d\n\22\3\22\3\22\3\23\3")
        buf.write(u"\23\6\23\u0093\n\23\r\23\16\23\u0094\3\23\3\23\3\24\3")
        buf.write(u"\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\2\2\26\2\4\6\b")
        buf.write(u"\n\f\16\20\22\24\26\30\32\34\36 \"$&(\2\5\4\2\6\6\20")
        buf.write(u"\20\4\2\7\7\20\20\4\2\b\b\20\20\u009b\2*\3\2\2\2\49\3")
        buf.write(u"\2\2\2\6@\3\2\2\2\bF\3\2\2\2\nI\3\2\2\2\fL\3\2\2\2\16")
        buf.write(u"O\3\2\2\2\20R\3\2\2\2\22T\3\2\2\2\24Z\3\2\2\2\26_\3\2")
        buf.write(u"\2\2\30d\3\2\2\2\32i\3\2\2\2\34m\3\2\2\2\36v\3\2\2\2")
        buf.write(u" \177\3\2\2\2\"\u0088\3\2\2\2$\u0090\3\2\2\2&\u0098\3")
        buf.write(u"\2\2\2(\u009c\3\2\2\2*+\b\2\1\2+,\5\4\3\2,-\5\6\4\2-")
        buf.write(u".\5\b\5\2.\60\5\n\6\2/\61\5\f\7\2\60/\3\2\2\2\60\61\3")
        buf.write(u"\2\2\2\61\63\3\2\2\2\62\64\5\16\b\2\63\62\3\2\2\2\63")
        buf.write(u"\64\3\2\2\2\64\65\3\2\2\2\65\66\5\20\t\2\66\67\7\2\2")
        buf.write(u"\3\678\b\2\1\28\3\3\2\2\29;\7\3\2\2:<\7\20\2\2;:\3\2")
        buf.write(u"\2\2;<\3\2\2\2<>\3\2\2\2=?\7\r\2\2>=\3\2\2\2>?\3\2\2")
        buf.write(u"\2?\5\3\2\2\2@B\7\4\2\2AC\5\22\n\2BA\3\2\2\2CD\3\2\2")
        buf.write(u"\2DB\3\2\2\2DE\3\2\2\2E\7\3\2\2\2FG\7\5\2\2GH\5\24\13")
        buf.write(u"\2H\t\3\2\2\2IJ\7\6\2\2JK\5\26\f\2K\13\3\2\2\2LM\7\7")
        buf.write(u"\2\2MN\5\30\r\2N\r\3\2\2\2OP\7\b\2\2PQ\5\32\16\2Q\17")
        buf.write(u"\3\2\2\2RS\7\t\2\2S\21\3\2\2\2TU\7\17\2\2UV\7\20\2\2")
        buf.write(u"VW\b\n\1\2W\23\3\2\2\2X[\5\34\17\2Y[\5$\23\2ZX\3\2\2")
        buf.write(u"\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\25\3\2")
        buf.write(u"\2\2^`\5\36\20\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2")
        buf.write(u"\2\2b\27\3\2\2\2ce\5 \21\2dc\3\2\2\2ef\3\2\2\2fd\3\2")
        buf.write(u"\2\2fg\3\2\2\2g\31\3\2\2\2hj\5\"\22\2ih\3\2\2\2jk\3\2")
        buf.write(u"\2\2ki\3\2\2\2kl\3\2\2\2l\33\3\2\2\2mn\7\20\2\2no\7\20")
        buf.write(u"\2\2or\7\21\2\2pq\7\20\2\2qs\7\21\2\2rp\3\2\2\2rs\3\2")
        buf.write(u"\2\2st\3\2\2\2tu\b\17\1\2u\35\3\2\2\2vw\t\2\2\2wx\7\20")
        buf.write(u"\2\2x{\7\21\2\2yz\7\20\2\2z|\7\21\2\2{y\3\2\2\2{|\3\2")
        buf.write(u"\2\2|}\3\2\2\2}~\b\20\1\2~\37\3\2\2\2\177\u0080\t\3\2")
        buf.write(u"\2\u0080\u0081\7\20\2\2\u0081\u0084\7\21\2\2\u0082\u0083")
        buf.write(u"\7\20\2\2\u0083\u0085\7\21\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write(u"\u0085\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\b\21\1")
        buf.write(u"\2\u0087!\3\2\2\2\u0088\u0089\7\16\2\2\u0089\u008a\t")
        buf.write(u"\4\2\2\u008a\u008c\7\20\2\2\u008b\u008d\7\21\2\2\u008c")
        buf.write(u"\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2")
        buf.write(u"\2\u008e\u008f\b\22\1\2\u008f#\3\2\2\2\u0090\u0092\5")
        buf.write(u"&\24\2\u0091\u0093\5\34\17\2\u0092\u0091\3\2\2\2\u0093")
        buf.write(u"\u0094\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2")
        buf.write(u"\2\u0095\u0096\3\2\2\2\u0096\u0097\5(\25\2\u0097%\3\2")
        buf.write(u"\2\2\u0098\u0099\7\20\2\2\u0099\u009a\7\n\2\2\u009a\u009b")
        buf.write(u"\7\13\2\2\u009b\'\3\2\2\2\u009c\u009d\7\20\2\2\u009d")
        buf.write(u"\u009e\7\n\2\2\u009e\u009f\7\f\2\2\u009f)\3\2\2\2\21")
        buf.write(u"\60\63;>DZ\\afkr{\u0084\u008c\u0094")
        return buf.getvalue()


class mpsParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'NAME'", u"'ROWS'", u"'COLUMNS'", u"'RHS'", 
                     u"'RANGES'", u"'BOUNDS'", u"'ENDATA'", u"''MARKER''", 
                     u"''INTORG''", u"''INTEND''", u"'FREE'" ]

    symbolicNames = [ u"<INVALID>", u"NAMEINDICATORCARD", u"ROWINDICATORCARD", 
                      u"COLUMNINDICATORCARD", u"RHSINDICATORCARD", u"RANGESINDICATORCARD", 
                      u"BOUNDSINDICATORCARD", u"ENDATAINDICATORCARD", u"KEYWORDMARKER", 
                      u"STARTMARKER", u"ENDMARKER", u"KEYWORDFREE", u"BOUNDKEY", 
                      u"ROWTYPE", u"BEZEICHNER", u"NUMERICALVALUE", u"WS", 
                      u"LINE_COMMENT" ]

    RULE_modell = 0
    RULE_firstrow = 1
    RULE_rows = 2
    RULE_columns = 3
    RULE_rhs = 4
    RULE_ranges = 5
    RULE_bounds = 6
    RULE_endata = 7
    RULE_rowdatacard = 8
    RULE_columndatacards = 9
    RULE_rhsdatacards = 10
    RULE_rangesdatacards = 11
    RULE_boundsdatacards = 12
    RULE_columndatacard = 13
    RULE_rhsdatacard = 14
    RULE_rangesdatacard = 15
    RULE_boundsdatacard = 16
    RULE_intblock = 17
    RULE_startmarker = 18
    RULE_endmarker = 19

    ruleNames =  [ u"modell", u"firstrow", u"rows", u"columns", u"rhs", 
                   u"ranges", u"bounds", u"endata", u"rowdatacard", u"columndatacards", 
                   u"rhsdatacards", u"rangesdatacards", u"boundsdatacards", 
                   u"columndatacard", u"rhsdatacard", u"rangesdatacard", 
                   u"boundsdatacard", u"intblock", u"startmarker", u"endmarker" ]

    EOF = Token.EOF
    NAMEINDICATORCARD=1
    ROWINDICATORCARD=2
    COLUMNINDICATORCARD=3
    RHSINDICATORCARD=4
    RANGESINDICATORCARD=5
    BOUNDSINDICATORCARD=6
    ENDATAINDICATORCARD=7
    KEYWORDMARKER=8
    STARTMARKER=9
    ENDMARKER=10
    KEYWORDFREE=11
    BOUNDKEY=12
    ROWTYPE=13
    BEZEICHNER=14
    NUMERICALVALUE=15
    WS=16
    LINE_COMMENT=17

    def __init__(self, input):
        super(mpsParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ModellContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.ModellContext, self).__init__(parent, invokingState)
            self.parser = parser

        def firstrow(self):
            return self.getTypedRuleContext(mpsParser.FirstrowContext,0)


        def rows(self):
            return self.getTypedRuleContext(mpsParser.RowsContext,0)


        def columns(self):
            return self.getTypedRuleContext(mpsParser.ColumnsContext,0)


        def rhs(self):
            return self.getTypedRuleContext(mpsParser.RhsContext,0)


        def endata(self):
            return self.getTypedRuleContext(mpsParser.EndataContext,0)


        def EOF(self):
            return self.getToken(mpsParser.EOF, 0)

        def ranges(self):
            return self.getTypedRuleContext(mpsParser.RangesContext,0)


        def bounds(self):
            return self.getTypedRuleContext(mpsParser.BoundsContext,0)


        def getRuleIndex(self):
            return mpsParser.RULE_modell

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterModell(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitModell(self)




    def modell(self):

        localctx = mpsParser.ModellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_modell)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)

            global row_types
            row_types = {}

            global b_vector
            b_vector = {}

            global c_vector
            c_vector = {}

            global a_vector
            a_vector = {}

            global slack_variables 
            slack_variables = {}
            global slack_prefix_g
            slack_prefix_g = "slkg_"
            global slack_prefix_l
            slack_prefix_l = "slkl_"

            global counter 
            counter = 0
            global slack_counter
            slack_counter = 0

            global cost_identifier
            global cost_seen
            cost_seen = 0

            global bound_count
            bound_count = 0

            global bound_prefix
            bound_prefix = "bound_"

            from sets import Set 
            # dictionary of variables
            global variables
            variables = Set([])


            self.state = 41
            self.firstrow()
            self.state = 42
            self.rows()
            self.state = 43
            self.columns()
            self.state = 44
            self.rhs()
            self.state = 46
            _la = self._input.LA(1)
            if _la==mpsParser.RANGESINDICATORCARD:
                self.state = 45
                self.ranges()


            self.state = 49
            _la = self._input.LA(1)
            if _la==mpsParser.BOUNDSINDICATORCARD:
                self.state = 48
                self.bounds()


            self.state = 51
            self.endata()
            self.state = 52
            self.match(mpsParser.EOF)

            global b_vector
            global c_vector
            b = []
            slack_indices = []
            slack_constraint = []
            for key in a_vector:
                if key not in b_vector:
                        b_vector[key] = 0
                row_a = a_vector[key]
                for column_a in row_a:
                        if column_a not in c_vector:
                                c_vector[column_a] = 0
            for key in b_vector:
                b = b + [b_vector[key]]
            variable_names = []
            virtual_constraint = []
            c = []
            for key in c_vector:
                c = c + [c_vector[key]]
                variable_names = variable_names + [key]
            for i in range(len(slack_variables)):
                c = c + [0]
                variable_names = variable_names + ["s_"+str(i+1)]
            global slack_variables
            global variables
            list_variables = list(variables)
            # a = [[0 for x in range(len(list_variables) + len(slack_variables))] for x in range(len(b))]
            a = [[0 for x in range(len(list_variables) + 2*len(b) - len(slack_variables))]
             for x in range(2*len(b) - len(slack_variables))]
            length = len(b)
            k_index = 0
            for key in b_vector:
                i = b_vector.keys().index(key)
                current_row = a_vector[key]
                for key_row in current_row:
                        j = c_vector.keys().index(key_row)
                        a[i][j] = current_row[key_row]
                if key in slack_variables:
                        j = slack_variables.keys().index(key) + len(list_variables)
                        if (slack_variables[key][:4] == "slkl"):
                                a[i][j] = 1
                                slack_indices = slack_indices + [j + 1]
                                slack_constraint = slack_constraint + [i + 1]
                        if (slack_variables[key][:4] == "slkg"):
                                a[i][j] = -1
                                slack_indices = slack_indices + [j + 1]
                                slack_constraint = slack_constraint + [i + 1]
                                for k in range(len(list_variables) + len(slack_variables)):
                                        a[i][k] = a[i][k]*(-1)
                                        b[i] = b[i]*(-1)
                else:
                    a[i][k_index + len(list_variables) + len(slack_variables) ] = 1
                    slack_indices = slack_indices + [k_index + len(list_variables) + len(slack_variables) + 1]
                    slack_constraint = slack_constraint + [i + 1]
                    variable_names = variable_names + ["s_"+str(len(slack_variables)+1 + k_index)]
                    for t in range(len(a[i])):
                        a[k_index + length ][t] = -a[i][t]
                    a[k_index + length ][k_index + len(list_variables) + len(slack_variables) + 1] = 1
                    b = b + [-b[i]]

                    slack_indices = slack_indices + [k_index + len(list_variables) + len(slack_variables) + 1 + 1]
                    slack_constraint = slack_constraint + [k_index + length  + 1]
                    variable_names = variable_names + ["s_"+str(len(slack_variables)+2 + k_index)]
                    k_index +=2
            virtual_constraint = []
            for t in range(len(b)):
                if b[t] < 0:
                    virtual_constraint = virtual_constraint + [t+1]
            while len(c) < len(a[0]):
                c = c + [0.0]

            np.savetxt("output/a" , a)
            np.savetxt("output/b" , b)
            np.savetxt("output/c" , c)
            np.savetxt("output/virtual_constraint" , virtual_constraint)
            np.savetxt("output/slack_constraints" , slack_constraint, fmt='%s')
            np.savetxt("output/slack_indexes" , slack_indices, fmt='%s')
            np.savetxt("output/variable_names" , variable_names, fmt='%s')

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FirstrowContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.FirstrowContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAMEINDICATORCARD(self):
            return self.getToken(mpsParser.NAMEINDICATORCARD, 0)

        def BEZEICHNER(self):
            return self.getToken(mpsParser.BEZEICHNER, 0)

        def KEYWORDFREE(self):
            return self.getToken(mpsParser.KEYWORDFREE, 0)

        def getRuleIndex(self):
            return mpsParser.RULE_firstrow

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterFirstrow(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitFirstrow(self)




    def firstrow(self):

        localctx = mpsParser.FirstrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_firstrow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(mpsParser.NAMEINDICATORCARD)
            self.state = 57
            _la = self._input.LA(1)
            if _la==mpsParser.BEZEICHNER:
                self.state = 56
                self.match(mpsParser.BEZEICHNER)


            self.state = 60
            _la = self._input.LA(1)
            if _la==mpsParser.KEYWORDFREE:
                self.state = 59
                self.match(mpsParser.KEYWORDFREE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RowsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.RowsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ROWINDICATORCARD(self):
            return self.getToken(mpsParser.ROWINDICATORCARD, 0)

        def rowdatacard(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mpsParser.RowdatacardContext)
            else:
                return self.getTypedRuleContext(mpsParser.RowdatacardContext,i)


        def getRuleIndex(self):
            return mpsParser.RULE_rows

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterRows(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitRows(self)




    def rows(self):

        localctx = mpsParser.RowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rows)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(mpsParser.ROWINDICATORCARD)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.rowdatacard()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mpsParser.ROWTYPE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColumnsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.ColumnsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COLUMNINDICATORCARD(self):
            return self.getToken(mpsParser.COLUMNINDICATORCARD, 0)

        def columndatacards(self):
            return self.getTypedRuleContext(mpsParser.ColumndatacardsContext,0)


        def getRuleIndex(self):
            return mpsParser.RULE_columns

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterColumns(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitColumns(self)




    def columns(self):

        localctx = mpsParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_columns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(mpsParser.COLUMNINDICATORCARD)
            self.state = 69
            self.columndatacards()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RhsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.RhsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RHSINDICATORCARD(self):
            return self.getToken(mpsParser.RHSINDICATORCARD, 0)

        def rhsdatacards(self):
            return self.getTypedRuleContext(mpsParser.RhsdatacardsContext,0)


        def getRuleIndex(self):
            return mpsParser.RULE_rhs

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterRhs(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitRhs(self)




    def rhs(self):

        localctx = mpsParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(mpsParser.RHSINDICATORCARD)
            self.state = 72
            self.rhsdatacards()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.RangesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RANGESINDICATORCARD(self):
            return self.getToken(mpsParser.RANGESINDICATORCARD, 0)

        def rangesdatacards(self):
            return self.getTypedRuleContext(mpsParser.RangesdatacardsContext,0)


        def getRuleIndex(self):
            return mpsParser.RULE_ranges

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterRanges(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitRanges(self)




    def ranges(self):

        localctx = mpsParser.RangesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ranges)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(mpsParser.RANGESINDICATORCARD)
            self.state = 75
            self.rangesdatacards()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoundsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.BoundsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BOUNDSINDICATORCARD(self):
            return self.getToken(mpsParser.BOUNDSINDICATORCARD, 0)

        def boundsdatacards(self):
            return self.getTypedRuleContext(mpsParser.BoundsdatacardsContext,0)


        def getRuleIndex(self):
            return mpsParser.RULE_bounds

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterBounds(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitBounds(self)




    def bounds(self):

        localctx = mpsParser.BoundsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bounds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(mpsParser.BOUNDSINDICATORCARD)
            self.state = 78
            self.boundsdatacards()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EndataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.EndataContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ENDATAINDICATORCARD(self):
            return self.getToken(mpsParser.ENDATAINDICATORCARD, 0)

        def getRuleIndex(self):
            return mpsParser.RULE_endata

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterEndata(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitEndata(self)




    def endata(self):

        localctx = mpsParser.EndataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_endata)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(mpsParser.ENDATAINDICATORCARD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RowdatacardContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.RowdatacardContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._ROWTYPE = None # Token
            self._BEZEICHNER = None # Token

        def ROWTYPE(self):
            return self.getToken(mpsParser.ROWTYPE, 0)

        def BEZEICHNER(self):
            return self.getToken(mpsParser.BEZEICHNER, 0)

        def getRuleIndex(self):
            return mpsParser.RULE_rowdatacard

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterRowdatacard(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitRowdatacard(self)




    def rowdatacard(self):

        localctx = mpsParser.RowdatacardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rowdatacard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            localctx._ROWTYPE = self.match(mpsParser.ROWTYPE)
            self.state = 83
            localctx._BEZEICHNER = self.match(mpsParser.BEZEICHNER)

            global row_types
            row_types[(None if localctx._BEZEICHNER is None else localctx._BEZEICHNER.text)] = (None if localctx._ROWTYPE is None else localctx._ROWTYPE.text)
            global cost_seen
            if ((None if localctx._ROWTYPE is None else localctx._ROWTYPE.text) == 'N' and cost_seen==0):
                global cost_identifier
                cost_identifier = (None if localctx._BEZEICHNER is None else localctx._BEZEICHNER.text)
                cost_seen=1
                
            if ((None if localctx._ROWTYPE is None else localctx._ROWTYPE.text) == 'G'):
                global slack_counter
                slack_counter = slack_counter + 1
                slack_name = slack_prefix_g + str(slack_counter)
                slack_variables[(None if localctx._BEZEICHNER is None else localctx._BEZEICHNER.text)] = slack_name
            if ((None if localctx._ROWTYPE is None else localctx._ROWTYPE.text) == 'L'):
                global slack_counter
                slack_counter = slack_counter + 1
                slack_name = slack_prefix_l + str(slack_counter)
                slack_variables[(None if localctx._BEZEICHNER is None else localctx._BEZEICHNER.text)] = slack_name

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColumndatacardsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.ColumndatacardsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def columndatacard(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mpsParser.ColumndatacardContext)
            else:
                return self.getTypedRuleContext(mpsParser.ColumndatacardContext,i)


        def intblock(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mpsParser.IntblockContext)
            else:
                return self.getTypedRuleContext(mpsParser.IntblockContext,i)


        def getRuleIndex(self):
            return mpsParser.RULE_columndatacards

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterColumndatacards(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitColumndatacards(self)




    def columndatacards(self):

        localctx = mpsParser.ColumndatacardsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_columndatacards)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 86
                    self.columndatacard()
                    pass

                elif la_ == 2:
                    self.state = 87
                    self.intblock()
                    pass


                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mpsParser.BEZEICHNER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RhsdatacardsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.RhsdatacardsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def rhsdatacard(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mpsParser.RhsdatacardContext)
            else:
                return self.getTypedRuleContext(mpsParser.RhsdatacardContext,i)


        def getRuleIndex(self):
            return mpsParser.RULE_rhsdatacards

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterRhsdatacards(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitRhsdatacards(self)




    def rhsdatacards(self):

        localctx = mpsParser.RhsdatacardsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_rhsdatacards)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.rhsdatacard()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mpsParser.RHSINDICATORCARD or _la==mpsParser.BEZEICHNER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangesdatacardsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.RangesdatacardsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def rangesdatacard(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mpsParser.RangesdatacardContext)
            else:
                return self.getTypedRuleContext(mpsParser.RangesdatacardContext,i)


        def getRuleIndex(self):
            return mpsParser.RULE_rangesdatacards

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterRangesdatacards(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitRangesdatacards(self)




    def rangesdatacards(self):

        localctx = mpsParser.RangesdatacardsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_rangesdatacards)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self.rangesdatacard()
                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mpsParser.RANGESINDICATORCARD or _la==mpsParser.BEZEICHNER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoundsdatacardsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.BoundsdatacardsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def boundsdatacard(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mpsParser.BoundsdatacardContext)
            else:
                return self.getTypedRuleContext(mpsParser.BoundsdatacardContext,i)


        def getRuleIndex(self):
            return mpsParser.RULE_boundsdatacards

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterBoundsdatacards(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitBoundsdatacards(self)




    def boundsdatacards(self):

        localctx = mpsParser.BoundsdatacardsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_boundsdatacards)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.boundsdatacard()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mpsParser.BOUNDKEY):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColumndatacardContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.ColumndatacardContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.b1 = None # Token
            self.b2 = None # Token
            self.n1 = None # Token
            self.b3 = None # Token
            self.n2 = None # Token

        def BEZEICHNER(self, i=None):
            if i is None:
                return self.getTokens(mpsParser.BEZEICHNER)
            else:
                return self.getToken(mpsParser.BEZEICHNER, i)

        def NUMERICALVALUE(self, i=None):
            if i is None:
                return self.getTokens(mpsParser.NUMERICALVALUE)
            else:
                return self.getToken(mpsParser.NUMERICALVALUE, i)

        def getRuleIndex(self):
            return mpsParser.RULE_columndatacard

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterColumndatacard(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitColumndatacard(self)




    def columndatacard(self):

        localctx = mpsParser.ColumndatacardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_columndatacard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            localctx.b1 = self.match(mpsParser.BEZEICHNER)
            self.state = 108
            localctx.b2 = self.match(mpsParser.BEZEICHNER)
            self.state = 109
            localctx.n1 = self.match(mpsParser.NUMERICALVALUE)
            self.state = 112
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 110
                localctx.b3 = self.match(mpsParser.BEZEICHNER)
                self.state = 111
                localctx.n2 = self.match(mpsParser.NUMERICALVALUE)



            global c_vector
            if((None if localctx.b2 is None else localctx.b2.text) == cost_identifier):
                c_vector[(None if localctx.b1 is None else localctx.b1.text)] = float((None if localctx.n1 is None else localctx.n1.text))
            else:
                global a_vector
                a_vector_row = {}
                if (None if localctx.b2 is None else localctx.b2.text) in a_vector:
                    a_vector_row = a_vector[(None if localctx.b2 is None else localctx.b2.text)]            
                    del a_vector[(None if localctx.b2 is None else localctx.b2.text)]
                a_vector_row[(None if localctx.b1 is None else localctx.b1.text)] = float((None if localctx.n1 is None else localctx.n1.text))
                a_vector[(None if localctx.b2 is None else localctx.b2.text)] = a_vector_row
            global list_variables
            variables.add((None if localctx.b1 is None else localctx.b1.text))
            if (localctx.b3 and localctx.n2):
                if((None if localctx.b3 is None else localctx.b3.text) == cost_identifier):
                    c_vector[(None if localctx.b1 is None else localctx.b1.text)] = float((None if localctx.n1 is None else localctx.n1.text))
                else:
                    global a_vector
                    a_vector_row = {}
                    if (None if localctx.b3 is None else localctx.b3.text) in a_vector:
                        a_vector_row = a_vector[(None if localctx.b3 is None else localctx.b3.text)]            
                        del a_vector[(None if localctx.b3 is None else localctx.b3.text)]
                    a_vector_row[(None if localctx.b1 is None else localctx.b1.text)] = float((None if localctx.n2 is None else localctx.n2.text))
                    a_vector[(None if localctx.b3 is None else localctx.b3.text)] = a_vector_row

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RhsdatacardContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.RhsdatacardContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.b1 = None # Token
            self.n1 = None # Token
            self.b2 = None # Token
            self.n2 = None # Token

        def BEZEICHNER(self, i=None):
            if i is None:
                return self.getTokens(mpsParser.BEZEICHNER)
            else:
                return self.getToken(mpsParser.BEZEICHNER, i)

        def RHSINDICATORCARD(self):
            return self.getToken(mpsParser.RHSINDICATORCARD, 0)

        def NUMERICALVALUE(self, i=None):
            if i is None:
                return self.getTokens(mpsParser.NUMERICALVALUE)
            else:
                return self.getToken(mpsParser.NUMERICALVALUE, i)

        def getRuleIndex(self):
            return mpsParser.RULE_rhsdatacard

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterRhsdatacard(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitRhsdatacard(self)




    def rhsdatacard(self):

        localctx = mpsParser.RhsdatacardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_rhsdatacard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==mpsParser.RHSINDICATORCARD or _la==mpsParser.BEZEICHNER):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 117
            localctx.b1 = self.match(mpsParser.BEZEICHNER)
            self.state = 118
            localctx.n1 = self.match(mpsParser.NUMERICALVALUE)
            self.state = 121
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 119
                localctx.b2 = self.match(mpsParser.BEZEICHNER)
                self.state = 120
                localctx.n2 = self.match(mpsParser.NUMERICALVALUE)



            global b_vector
            b_vector[(None if localctx.b1 is None else localctx.b1.text)] = float((None if localctx.n1 is None else localctx.n1.text))
            if(localctx.b2 and localctx.n2):
                global b_vector
                b_vector[(None if localctx.b2 is None else localctx.b2.text)] = float((None if localctx.n2 is None else localctx.n2.text))


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangesdatacardContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.RangesdatacardContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.b1 = None # Token
            self.b2 = None # Token
            self.n1 = None # Token
            self.b3 = None # Token
            self.n2 = None # Token

        def BEZEICHNER(self, i=None):
            if i is None:
                return self.getTokens(mpsParser.BEZEICHNER)
            else:
                return self.getToken(mpsParser.BEZEICHNER, i)

        def NUMERICALVALUE(self, i=None):
            if i is None:
                return self.getTokens(mpsParser.NUMERICALVALUE)
            else:
                return self.getToken(mpsParser.NUMERICALVALUE, i)

        def RANGESINDICATORCARD(self):
            return self.getToken(mpsParser.RANGESINDICATORCARD, 0)

        def getRuleIndex(self):
            return mpsParser.RULE_rangesdatacard

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterRangesdatacard(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitRangesdatacard(self)




    def rangesdatacard(self):

        localctx = mpsParser.RangesdatacardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_rangesdatacard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            localctx.b1 = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==mpsParser.RANGESINDICATORCARD or _la==mpsParser.BEZEICHNER):
                localctx.b1 = self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 126
            localctx.b2 = self.match(mpsParser.BEZEICHNER)
            self.state = 127
            localctx.n1 = self.match(mpsParser.NUMERICALVALUE)
            self.state = 130
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 128
                localctx.b3 = self.match(mpsParser.BEZEICHNER)
                self.state = 129
                localctx.n2 = self.match(mpsParser.NUMERICALVALUE)



            global a_vector
            new_a_row = a_vector[(None if localctx.b2 is None else localctx.b2.text)]
            new_name = (None if localctx.b2 is None else localctx.b2.text) + "_1"
            a_vector[new_name] = new_a_row
            global row_types
            if( row_types[(None if localctx.b2 is None else localctx.b2.text)] == 'G'):
                global slack_counter
                slack_counter = slack_counter + 1
                slack_name = slack_prefix_l + str(slack_counter)
                slack_variables[new_name] = slack_name
                global b_vector
                b_vector[new_name] =  b_vector[(None if localctx.b2 is None else localctx.b2.text)] + abs(float((None if localctx.n1 is None else localctx.n1.text)))

            if (row_types[(None if localctx.b2 is None else localctx.b2.text)] == 'L'):
                global slack_counter
                slack_counter = slack_counter + 1
                slack_name = slack_prefix_g + str(slack_counter)
                slack_variables[new_name] = slack_name
                global b_vector
                b_vector[new_name] =  b_vector[(None if localctx.b2 is None else localctx.b2.text)] - abs(float((None if localctx.n1 is None else localctx.n1.text)))

            if (row_types[(None if localctx.b2 is None else localctx.b2.text)] == 'E' and float((None if localctx.n1 is None else localctx.n1.text))>0):
                global slack_counter
                slack_counter = slack_counter + 1
                slack_name = slack_prefix_l + str(slack_counter)
                slack_variables[new_name] = slack_name
                global b_vector
                b_vector[new_name] =  b_vector[(None if localctx.b2 is None else localctx.b2.text)] + abs(float((None if localctx.n1 is None else localctx.n1.text)))

            if (row_types[(None if localctx.b2 is None else localctx.b2.text)] == 'E' and float((None if localctx.n1 is None else localctx.n1.text))<0):
                global slack_counter
                slack_counter = slack_counter + 1
                slack_name = slack_prefix_g + str(slack_counter)
                slack_variables[new_name] = slack_name
                global b_vector
                b_vector[new_name] =  b_vector[(None if localctx.b2 is None else localctx.b2.text)] - abs(float((None if localctx.n1 is None else localctx.n1.text)))
            if(localctx.b3 and localctx.n2):
                global a_vector
                new_a_row = a_vector[(None if localctx.b3 is None else localctx.b3.text)]
                new_name = (None if localctx.b3 is None else localctx.b3.text) + "_1"
                a_vector[new_name] = new_a_row
                global row_types
                if( row_types[(None if localctx.b3 is None else localctx.b3.text)] == 'G'):
                    global slack_counter
                    slack_counter = slack_counter + 1
                    slack_name = slack_prefix_l + str(slack_counter)
                    slack_variables[new_name] = slack_name
                    global b_vector
                    b_vector[new_name] =  b_vector[(None if localctx.b3 is None else localctx.b3.text)] + abs(float((None if localctx.n2 is None else localctx.n2.text)))

                if (row_types[(None if localctx.b3 is None else localctx.b3.text)] == 'L'):
                    global slack_counter
                    slack_counter = slack_counter + 1
                    slack_name = slack_prefix_g + str(slack_counter)
                    slack_variables[new_name] = slack_name
                    global b_vector
                    b_vector[new_name] =  b_vector[(None if localctx.b3 is None else localctx.b3.text)] - abs(float((None if localctx.n2 is None else localctx.n2.text)))

                if (row_types[(None if localctx.b3 is None else localctx.b3.text)] == 'E' and float((None if localctx.n2 is None else localctx.n2.text))>0):
                    global slack_counter
                    slack_counter = slack_counter + 1
                    slack_name = slack_prefix_l + str(slack_counter)
                    slack_variables[new_name] = slack_name
                    global b_vector
                    b_vector[new_name] =  b_vector[(None if localctx.b3 is None else localctx.b3.text)] + abs(float((None if localctx.n2 is None else localctx.n2.text)))

                if (row_types[(None if localctx.b3 is None else localctx.b3.text)] == 'E' and float((None if localctx.n2 is None else localctx.n2.text))<0):
                    global slack_counter
                    slack_counter = slack_counter + 1
                    slack_name = slack_prefix_g + str(slack_counter)
                    slack_variables[new_name] = slack_name
                    global b_vector
                    b_vector[new_name] =  b_vector[(None if localctx.b3 is None else localctx.b3.text)] - abs(float((None if localctx.n2 is None else localctx.n2.text)))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoundsdatacardContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.BoundsdatacardContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.b1 = None # Token
            self.b2 = None # Token
            self._NUMERICALVALUE = None # Token

        def BOUNDKEY(self):
            return self.getToken(mpsParser.BOUNDKEY, 0)

        def BEZEICHNER(self, i=None):
            if i is None:
                return self.getTokens(mpsParser.BEZEICHNER)
            else:
                return self.getToken(mpsParser.BEZEICHNER, i)

        def BOUNDSINDICATORCARD(self):
            return self.getToken(mpsParser.BOUNDSINDICATORCARD, 0)

        def NUMERICALVALUE(self):
            return self.getToken(mpsParser.NUMERICALVALUE, 0)

        def getRuleIndex(self):
            return mpsParser.RULE_boundsdatacard

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterBoundsdatacard(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitBoundsdatacard(self)




    def boundsdatacard(self):

        localctx = mpsParser.BoundsdatacardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_boundsdatacard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            localctx.b1 = self.match(mpsParser.BOUNDKEY)
            self.state = 135
            _la = self._input.LA(1)
            if not(_la==mpsParser.BOUNDSINDICATORCARD or _la==mpsParser.BEZEICHNER):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 136
            localctx.b2 = self.match(mpsParser.BEZEICHNER)
            self.state = 138
            _la = self._input.LA(1)
            if _la==mpsParser.NUMERICALVALUE:
                self.state = 137
                localctx._NUMERICALVALUE = self.match(mpsParser.NUMERICALVALUE)



            if ( (None if localctx.b1 is None else localctx.b1.text) == "MI"  or (None if localctx.b1 is None else localctx.b1.text) == "PL"):
                global bound_count
                bound_count = bound_count + 1
                global a_vector
                a_vector_row = {}
                a_vector_row[(None if localctx.b2 is None else localctx.b2.text)] = 1
                bound_name = bound_prefix + str(bound_count)
                a_vector[bound_name] = a_vector_row
                    
                global b_vector
                
                if ( (None if localctx.b1 is None else localctx.b1.text) == "MI"):
                    b_vector[bound_name] = 0
                    global slack_counter
                    slack_counter = slack_counter + 1
                    slack_name = slack_prefix_l + str(slack_counter)
                    slack_variables[bound_name] = slack_name
                if ( (None if localctx.b1 is None else localctx.b1.text) == "PL"):
                    b_vector[bound_name] = 0
                    global slack_counter
                    slack_counter = slack_counter + 1
                    slack_name = slack_prefix_g + str(slack_counter)
                    slack_variables[bound_name] = slack_name
            else:
                global bound_count
                bound_count = bound_count + 1
                global a_vector
                a_vector_row = {}
                a_vector_row[(None if localctx.b2 is None else localctx.b2.text)] = 1
                bound_name = bound_prefix + str(bound_count)
                a_vector[bound_name] = a_vector_row
                
                global b_vector
                b_vector[bound_name] = float((None if localctx._NUMERICALVALUE is None else localctx._NUMERICALVALUE.text))

                if (None if localctx.b1 is None else localctx.b1.text) == "UP":
                    global slack_counter
                    slack_counter = slack_counter + 1
                    slack_name = slack_prefix_l + str(slack_counter)
                    slack_variables[bound_name] = slack_name
                    
                if (None if localctx.b1 is None else localctx.b1.text) == "LO":
                    global slack_counter
                    slack_counter = slack_counter + 1
                    slack_name = slack_prefix_g + str(slack_counter)
                    slack_variables[bound_name] = slack_name

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntblockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.IntblockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def startmarker(self):
            return self.getTypedRuleContext(mpsParser.StartmarkerContext,0)


        def endmarker(self):
            return self.getTypedRuleContext(mpsParser.EndmarkerContext,0)


        def columndatacard(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(mpsParser.ColumndatacardContext)
            else:
                return self.getTypedRuleContext(mpsParser.ColumndatacardContext,i)


        def getRuleIndex(self):
            return mpsParser.RULE_intblock

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterIntblock(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitIntblock(self)




    def intblock(self):

        localctx = mpsParser.IntblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_intblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.startmarker()
            self.state = 144 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 143
                    self.columndatacard()

                else:
                    raise NoViableAltException(self)
                self.state = 146 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 148
            self.endmarker()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StartmarkerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.StartmarkerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BEZEICHNER(self):
            return self.getToken(mpsParser.BEZEICHNER, 0)

        def KEYWORDMARKER(self):
            return self.getToken(mpsParser.KEYWORDMARKER, 0)

        def STARTMARKER(self):
            return self.getToken(mpsParser.STARTMARKER, 0)

        def getRuleIndex(self):
            return mpsParser.RULE_startmarker

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterStartmarker(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitStartmarker(self)




    def startmarker(self):

        localctx = mpsParser.StartmarkerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_startmarker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(mpsParser.BEZEICHNER)
            self.state = 151
            self.match(mpsParser.KEYWORDMARKER)
            self.state = 152
            self.match(mpsParser.STARTMARKER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EndmarkerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(mpsParser.EndmarkerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BEZEICHNER(self):
            return self.getToken(mpsParser.BEZEICHNER, 0)

        def KEYWORDMARKER(self):
            return self.getToken(mpsParser.KEYWORDMARKER, 0)

        def ENDMARKER(self):
            return self.getToken(mpsParser.ENDMARKER, 0)

        def getRuleIndex(self):
            return mpsParser.RULE_endmarker

        def enterRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.enterEndmarker(self)

        def exitRule(self, listener):
            if isinstance( listener, mpsListener ):
                listener.exitEndmarker(self)




    def endmarker(self):

        localctx = mpsParser.EndmarkerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_endmarker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(mpsParser.BEZEICHNER)
            self.state = 155
            self.match(mpsParser.KEYWORDMARKER)
            self.state = 156
            self.match(mpsParser.ENDMARKER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




