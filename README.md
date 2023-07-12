# Calculator package

  

## Summary

  

The package contains a calculator class which is a python representation of a calculator.
Calculator objects are used to perform following
operations:

Addition

 - Subtraction
   
 - Multiplication
   
 - Division
   
 - Taking n-th root of a positive number.
   
 - Reseting the memory

  

# Calculator package

  

## Summary

  

The package contains a calculator class which is a python representation of a calculator.
Calculator objects are used to perform following
operations:

- Addition

 - Subtraction
   
 - Multiplication
   
 - Division
   
 - Taking n-th root of a positive number.
   
 - Reseting the memory

  

## Installation

  

#### To install the package:

    pip install tc-ds-2023-calculator



## Using the package

#### To import the package:

    from calculator import Calculator
    
#### Instantiating an object:

    obj = Calculator(memory=0)

Memory stores the initial value which will later be manipulated. The variable is 0 by default but can be set to any other number of type int or float.

### Operator behaviour and instance methods
#### Operators:


The class uses operator overloading for addition, subtraction, multiplication and division operations.

 

|+|Addition|
|--|--|
|-|**Subtraction**|
|*| **Multiplication** |
|/|**Division**|



These operations are done in a following manner:

    object <operator> input

Example:

    >>> obj = Calculator(2)
    >>> obj
        Calculator(2)
    >>> obj + 2
    >>> obj
        Calculator(4)
    >>> obj/2
    >>> obj
        Calculator(2)
    >>> obj * 3
    >>> obj
        Calculator(6)
    >>> obj / 2
    >>> obj
        Calculator(3)
    
   #### Methods:
   Calculator class provides following methods:
   
|.root(n=2)| Takes the n-th root of a positive number stored in the calculator memory. The n value must be an integer number. Only works with positive memory numbers even when n is odd. Takes the square root by default|
|--|--|
|**.reset()**| **Sets the calculator memory to 0** |
|**.get_num()**|**Returns calculator memory** |


Example:

    >>> obj = Calculator(4)
    >>> obj.root()
    >>> obj
        Calculator(2)
    >>> obj.reset()
    >>> obj
        Calculator(0)
    >>> obj.get_num()
        0
        

## Testing
Install dependencies:

    pip install -r requirements.txt

Test:

    python3 -m unittest

   
   
   
   
 
