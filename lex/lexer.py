# from Simplex2 import Simplex
# from Simplex2 import simple_simplex
# import sys
import copy

# sys.path.insert(0, "../..")

# if sys.version_info[0] >= 3:
#     raw_input = input

tokens = (
    'NUMBER', 'LTE', 'GTE', 'LT', 'GT', 'PLUS',
    'MINUS', 'MULT', 'NAME', 'EQ', 'NL',
)

literals = ['=', ';', ',']


t_NAME = r'[a-zA-Z][a-zA-Z]*[_]*[0-9]*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_LTE = r'<='
t_GTE = r'>='
t_LT = r'<'
t_GT = r'>'
t_EQ = r'='
t_MULT = r'\*'
t_NL = r'\r\n'


def t_NUMBER(t):
    r'\d+'
    t.value = float(t.value)
    return t

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex
lex.lex()


# Parsing rules

precedence = (
    ('left', 'MULT'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'UMINUS'),
)

# dictionary of variables
variables = set([])
slack_variables = set([])
list_variables = []
list_slack_variables = []
x_matrix = []
c_matrix = []
b_matrix = []
a_matrix = [[]]
value_temp = float(0)

slack_prefix = "slk_"
counter = 0

variable_factors_matrix = []
variable_factors_row = list([])
goal_factors_row = []

goal = ''
start = 'statement'


def p_statement_assign(p):
    '''statement : NAME goal subjects ';' NL '''
    if p[1] == 'min':
        goal = 'min'
    elif p[1] == 'max':
        goal = 'max'
    global variables
    global slack_variables
    global list_variables
    global list_slack_variables
    global x_matrix
    global c_matrix
    global b_matrix
    global a_matrix
    list_variables = list(variables)
    list_slack_variables = list(slack_variables)
    a_matrix = [[0 for x in range(len(list_variables) + len(list_slack_variables))] for x in range(len(b_matrix))]
    for row_index, row in enumerate(variable_factors_matrix):
        for col_index, (value, key) in enumerate(row):
            index = -1
            try:
                index = list_variables.index(key)
            except ValueError:
                index = -1
            if index >= 0:
                a_matrix[row_index][index] = value
            index = -1
            try:
                index = list_slack_variables.index(key)
            except ValueError:
                index = -1
            if index >= 0:
                a_matrix[row_index][len(list_variables) + index] = value
    c_matrix = [0 for x in range(len(list_variables) + len(list_slack_variables))]
    for (value, key) in goal_factors_row:
        index = -1
        try:
            index = list_variables.index(key)
        except ValueError:
            index = -1
        if index >= 0:
            c_matrix[index] = -1 * value

    #for col , val in enumerate(list_stack_variables):
    #    c_matrix[col + len(list_variables)] = 0

    b_matrix.insert(0, 0)

    # print("variable + slacks ", list_variables, list_slack_variables)
    # print("c matrix", c_matrix)
    # print("b matrix", b_matrix)
    # print("a matrix", a_matrix)
    p[0] = [a_matrix, b_matrix, c_matrix]


def p_statement_goal(p):
    '''goal : expression ';' '''
    global variable_factors_row
    global goal_factors_row
    goal_factors_row = copy.deepcopy(variable_factors_row)
    variable_factors_row = []


def p_statement_goal_uminus(p):
    '''goal : MINUS expression ';' %prec UMINUS '''
    global variable_factors_row
    (key, value) = variable_factors_row[0]
    variable_factors_row.insert(0, (-key, value))
    goal_factors_row = copy.deepcopy(variable_factors_row)
    variable_factors_row = []


def p_subjects_subject(p):
    ''' subjects : subject ',' subjects
     | subject '''


def p_statement_subject(p):
    '''subject : expression EQ value
    | expression LT value
    | expression GT value
    | expression LTE value
    | expression GTE value '''

    global variable_factors_row
    global counter
    global b_matrix
    b_matrix.append(p[3])
    if p[2] == '<=' or p[2] == '<':
        slack_name = slack_prefix + str(counter)
        variable_factors_row.append((float(1) , slack_name) )
        slack_variables.add(slack_name)
        counter += 1
    elif p[2] == '>=' or p[2] == '>':
        slack_name = slack_prefix + str(counter)
        variable_factors_row.append((float(-1) , slack_name) )
        slack_variables.add(slack_name)
        counter += 1
    global variable_factors_matrix
    if variable_factors_row != []:
        variable_factors_matrix.append(variable_factors_row)
    variable_factors_row = []


def p_statement_subject_uminus(p):
    '''subject : MINUS expression EQ  value  %prec UMINUS
    | MINUS expression LT value  %prec UMINUS
    | MINUS expression GT value  %prec UMINUS
    | MINUS expression LTE value  %prec UMINUS
    | MINUS expression GTE value  %prec UMINUS '''

    global variable_factors_row
    global counter
    global b_matrix
    b_matrix.append(p[4])
    (key, value) = variable_factors_row[0]
    variable_factors_row.insert(0 , ( - key , value))
    if p[3] == '<=' or p[3] == '<':
        slack_name = slack_prefix + str(counter)
        variable_factors_row.append((float(1), slack_name))
        slack_variables.add(slack_name)
        counter += 1
    elif p[3] == '>=' or p[3] == '>':
        slack_name = slack_prefix + str(counter)
        variable_factors_row.append((float(-1), slack_name))
        slack_variables.add(slack_name)
        counter += 1

    global variable_factors_matrix
    if variable_factors_row:
        variable_factors_matrix.append(variable_factors_row)
    variable_factors_row = []


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression'''
    #print(p[1] , " --- " , p[2] , " --- " ,p[3])
    global variable_factors_row
    if p[2] == '-':
        (key, value) = p[3]
        variable_factors_row.append((-key, value))
    else:
        variable_factors_row.append(p[3])


def p_value_uminus(p):
    '''value : MINUS value %prec UMINUS'''
    p[0] = - p[2]


def p_value_number(p):
    '''value :  NUMBER '''
    p[0] = p[1]


def p_expression_name(p):
    '''expression : NUMBER MULT NAME
    | NAME '''

    if isinstance(p[1], float):
        variables.add(p[3])
        p[0] = (p[1], p[3])
    else:
        variables.add(p[1])
        p[0] = (float(1), p[1])
    global variable_factors_row
    if variable_factors_row == []:
        variable_factors_row.append(p[0])


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        print(p)
    else:
        print("Syntax error at EOF")


def parse_problem(s):
    import ply.yacc as yacc
    parser = yacc.yacc(debug=False, write_tables=False)
    return parser.parse(s)