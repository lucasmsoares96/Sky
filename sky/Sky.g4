grammar Sky;

prog
    : (decl | expr | call)+ EOF              # Program
    ;

decl
    : ID ':' INT_TYPE '=' NUM                # Declaration 
    ;

expr
    : expr '*' expr                          # Multiplication
    | expr '+' expr                          # Addition
    | ID                                     # Variable
    | NUM                                    # Number
    ;
    
call
    : ID '(' ID ')'                          # Function
    ;

ID: [a-z][a-zA-Z0-9_]*;
NUM: '0' | '-'? [1-9][0-9]*;
INT_TYPE: 'INT';
COMMENT: '--' ~[\r\n]* -> skip;
WP: [ \t\n\r]+ -> skip;