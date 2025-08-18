# Language Grammar

```
program        := statement*
statement      := print_statement 
                 | variable_declaration
                 | assignment
                 | if_statement
                 | while_statement
                 | function_declaration
                 | expression_statement
print_statement := "print" expression ("," expression)*
variable_declaration := "let" IDENTIFIER "=" expression
assignment     := IDENTIFIER "=" expression
if_statement   := "if" expression block ("else" "if" expression block)* ("else" block)?
while_statement := "while" expression block
function_declaration := "func" IDENTIFIER "(" parameters? ")" block
block          := "{" statement* "}"
expression     := term (("+" | "-" | "<") term)*
term           := factor (("*" | "/") factor)*
factor         := NUMBER | STRING | IDENTIFIER | "(" expression ")" | list_literal
list_literal   := "[" (expression ("," expression)*)? "]"
parameters     := IDENTIFIER ("," IDENTIFIER)*
```