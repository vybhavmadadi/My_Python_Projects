# Different types of variables
# LEGB
# Local, Enclosing, Global, Built-in
# Local - Defined within a function
# Enclosing - Variable defined within the local scope but enclosing functions
# Global - Variables defined at the top level of a module that are implicitly delcared using 'global' keyword
# Built-in - Names that are pre-assigned in pyton

import builtins  # Import for all built in variables

# Examples:
x = "global x"  # This is a global variable as this is defined at the top level of the module


def test():
    y = "local y"
    print(y)


test()

# Built ins
print(dir(builtins))
