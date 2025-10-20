## DECISIONS.md

## Overview
  The refactored version of the program focuses on making the code cleaner, easier to read, and more efficient. In the original script, both functions used loops and manual string concatenation, which worked correctly but made the code longer and less direct. The updated version replaces those loops with list comprehensions and generator expressions. This approach keeps the same logic but allows Python to handle the iteration more efficiently with fewer lines of code.
  Function names were also improved to be more descriptive of their purpose. Instead of generic names like do_math_stuff and do_string_stuff, the functions are now called multiply_nums and capitalize_fruits. This makes the program easier to understand at a glance. Simple docstrings were added to explain what each function does, and only brief comments were included where they help clarify intent without cluttering the code.
