---
aliases: [""]
tags: []
---

## Header file

In programming, particularly in languages like C and C++, header files are files with a .h (or sometimes .hpp) extension that contain declarations for functions, classes, variables, constants, and other resources that will be used in multiple source (.cpp or .c) files.

Key Points About Header Files:
- Declarations Only: Header files typically only declare what functions, classes, or variables exist and don’t include the actual implementation. For instance, they specify the function's name, return type, and parameters but not the code that defines what the function does.
- Code Organization: They help organize code by separating interface (declarations) from implementation (definitions in .cpp files). This makes it easier to manage large codebases by keeping definitions separate and allowing source files to include only the necessary headers.
- Avoids Redundancy: By including a header file in multiple source files, you can use the same functions or classes across these files without rewriting code. If you want to change a function, you only need to update it once in the header file, and it applies everywhere it’s used.
- Promotes Code Reusability: Header files make it possible to create libraries or modules that other programs can easily incorporate by including the header file(s) and linking to the compiled library.

For example, a header file named math_utils.h might declare functions like add() and subtract(), which can then be used in various parts of a program by including math_utils.h. The actual implementations of add() and subtract() would be in a corresponding math_utils.cpp file.
