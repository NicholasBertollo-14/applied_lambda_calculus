def PBOOL(x):
    print(x(True)(False))

# Identity function
IDENTITY = lambda f: lambda x: f(x)

# Definitions of TRUE and FALSE
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

PBOOL(TRUE)
PBOOL(FALSE)

# Universal - All logic stems from here
NAND = lambda x: lambda y: x(y)(x)(FALSE)(TRUE)
NOR = lambda x: lambda y: x(x)(y)(FALSE)(TRUE)

# Derived
OR = lambda x: lambda y: NOR(NOR(x)(y))(NOR(x)(y))
AND = lambda x: lambda y: NAND(NAND(x)(y))(NAND(x)(y))
NOT = lambda x: NAND(x)(TRUE)

# Further Derived
XOR = lambda x: lambda y: AND(NAND(x)(y))(OR(x)(y))
XNOR = lambda x: lambda y: NOT(XOR(x)(y))

# Ternary IF
IF = lambda a: lambda b: lambda c: a(b)(c)

IF(FALSE)(lambda x: print("Hello"))(lambda y: print("Bye!"))(None)

# Defining the next number
SUCCESSOR = lambda NUM: lambda f: lambda x: f(NUM(f)(x))
PRESUCCESSOR = lambda NUM: lambda f: lambda x: NUM(lambda g: lambda h: h(g(f)))(lambda w: x)(lambda x: x)

# Cast from lambda calculus int to python int
INT = lambda NUM: NUM(lambda x: 1 + x)(0)

# Defining ZERO as FALSE
ZERO = FALSE

# Defining ONE as IDENTITY
ONE = IDENTITY

# Defining Arithmetic
ADD = lambda a: lambda b: a(SUCCESSOR)(b) # Literally perform SUCCESSOR on b a times
MULT = lambda a: lambda b: lambda c: a(b(c)) # Performing b on c a times
POW = lambda a: lambda b: b(a) # Performing a b times 

SUB = lambda a: lambda b: b(PRESUCCESSOR)(a)
DIFF = lambda a: lambda b: ADD(SUB(a)(b))(SUB(b)(a))

# I think this is cool but I need recursion to do multiple digits
ONE_D_CONCAT = lambda a: lambda b: ADD(MULT(a)(MULT(TWO)(FIVE)))(b)

# Quality of life
PINT = lambda a: print(INT(a))

PINT(ZERO)
PINT(ONE)
PINT(TWO := lambda f: lambda x: f(f(x)))
PINT(THREE := lambda f: lambda x: f(f(f(x))))
PINT(FOUR := lambda f: lambda x: f(f(f(f(x)))))
PINT(FIVE := SUCCESSOR(FOUR))
PINT(SIX := MULT(THREE)(TWO))
PINT(SEVEN := ADD(ONE)(MULT(THREE)(TWO)))
PINT(EIGHT := MULT(FOUR)(TWO))
PINT(NINE := POW(THREE)(TWO))