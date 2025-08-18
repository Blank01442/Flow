# Flow Language Grammar

This document describes the formal grammar of the Flow programming language using a notation similar to Extended Backus-Naur Form (EBNF).

## Lexical Grammar

### Characters
```
newline        = "\n"
whitespace     = " " | "\t" | newline
letter         = "a".."z" | "A".."z"
digit          = "0".."9"
```

### Tokens
```
identifier     = letter { letter | digit | "_" }
integer        = digit { digit }
float          = digit { digit } "." digit { digit }
string         = "\"" { character } "\""
comment        = "#" { character } newline
```

### Literals
```
literal        = integer | float | string | "true" | "false" | "null"
```

### Operators
```
arithmetic_op  = "+" | "-" | "*" | "/" | "%" | "**"
comparison_op  = "==" | "!=" | "<" | "<=" | ">" | ">="
logical_op     = "and" | "or" | "not"
assignment_op  = "="
```

## Syntactic Grammar

### Program Structure
```
program        = { statement }
statement      = expression_statement
               | declaration_statement
               | control_statement
               | function_statement
```

### Expressions
```
expression     = logical_or
logical_or     = logical_and { "or" logical_and }
logical_and    = equality { "and" equality }
equality       = comparison { ( "==" | "!=" ) comparison }
comparison     = term { ( "<" | "<=" | ">" | ">=" ) term }
term           = factor { ( "+" | "-" ) factor }
factor         = unary { ( "*" | "/" | "%" ) unary }
unary          = [ "not" | "-" ] primary
primary        = literal
               | identifier
               | list
               | function_call
               | "(" expression ")"
               | "if" expression "then" expression "else" expression
```

### Declarations
```
declaration    = "let" identifier "=" expression
```

### Lists
```
list           = "[" [ expression { "," expression } ] "]"
```

### Function Calls
```
function_call  = identifier "(" [ arguments ] ")"
arguments      = expression { "," expression }
```

### Control Statements
```
control_statement = if_statement
                  | while_statement
                  | for_statement
                  | try_statement

if_statement   = "if" expression block
               { "else" "if" expression block }
               [ "else" block ]

while_statement = "while" expression block

for_statement  = "for" identifier "in" expression block

try_statement  = "try" block "catch" identifier block

block          = "{" { statement } "}"
```

### Function Statements
```
function_statement = "func" identifier "(" [ parameters ] ")" block

parameters     = identifier { "," identifier }
```

## Reserved Words

The following words are reserved and cannot be used as identifiers:

```
and, break, catch, continue, else, false, for, func, if, in, let, not, null, or, return, try, true, while
```

## Operators Precedence

From highest to lowest precedence:
1.  `()` (grouping), `[]` (list access), `function()` (call)
2.  `-` (unary), `not`
3.  `**` (power)
4.  `*`, `/`, `%`
5.  `+`, `-`
6.  `<`, `<=`, `>`, `>=`
7.  `==`, `!=`
8.  `and`
9.  `or`
10. `=` (assignment)

## Comments

Flow supports single-line comments that begin with `#` and continue to the end of the line:

```flow
# This is a comment
let x = 5  # This is also a comment
```

## Examples

### Valid Flow Programs

Simple assignment:
```flow
let x = 5
```

Function definition:
```flow
func add(a, b) {
    return a + b
}
```

Control flow:
```flow
if x > 0 {
    print "Positive"
} else {
    print "Non-positive"
}
```

Loop:
```flow
let i = 0
while i < 10 {
    print i
    i = i + 1
}
```

### Grammar Derivation Example

For the expression `let x = 5 + 3 * 2`:

1. `program` → `statement` → `declaration_statement`
2. `declaration` → `"let" identifier "=" expression`
3. `expression` → `logical_or` → `logical_and` → `equality` → `comparison` → `term`
4. `term` → `factor { ("+" | "-") factor }`
5. `factor` → `unary { ("*" | "/" | "%" ) unary }`
6. The parser correctly applies operator precedence to parse `5 + 3 * 2` as `5 + (3 * 2)`

## Language Evolution

This grammar specification describes the current version of Flow. As the language evolves, this document will be updated to reflect new syntax and features.

## Extensions

Flow may support additional syntax features in the future, such as:
- Import statements for modules
- More complex data structures (dictionaries, sets)
- Pattern matching
- More sophisticated type annotations

These extensions would be added to this grammar specification when implemented.

## Implementation Notes

The grammar described here is intended for reference and may not exactly match the implementation details of the parser. The actual parser may use different techniques or have additional restrictions for error handling and performance.