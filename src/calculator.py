from math import isnan, isinf
from typing import Union


class Calculator:
    """

    A class intended to represent a calculator which performs
    basic arithmetic operations: addition, subtraction, multiplication,
    division and taking the nth root of a positive number.

    """
    @staticmethod
    def __validate_type(variable):
        if isnan(variable) or isinf(variable):
            raise TypeError(
                f"Expected type int or float, \
got {variable} instead."
            )
        if not isinstance(variable, (int, float)) or isinstance(variable, bool):
            raise TypeError(
                f"Expected type int or float, \
got {variable.__class__.__name__} instead."
            )

    def __init__(self, memory:Union[int,float]=0):
        
        """

        Constructor for the Calculator class.

        Parameters
        ----------

            memory: Union[int,float]
                Sets the initial starting number for the calculator.
                The default value is set to 0.


        To instantiate an object:
    >>> from calculator import Calculator
    >>> obj = Calculator()
    >>> obj
        Calculator(0)


"""
        self.__validate_type(memory)
        self.memory = memory

    def __add__(self, other:Union[int,float])->None:
        
        """

        Adds a number to the memory
        
        Parameters
        ----------

            other: Union[int,float]


        Example:
    
    >>> obj = Calculator(0)
    >>> obj + 3
    >>> obj
        Calculator(3)
        
        """
        self.__validate_type(other)
        self.memory += other

    def __sub__(self, other:Union[int,float])->None:
        
        """

        Subtracts a number from the memory
        
        Parameters
        ----------

            other: Union[int,float]
    
        Example:
    
    >>> obj = Calculator(0)
    >>> obj - 3
    >>> obj
        Calculator(-3)
        
        """
        
        self.__validate_type(other)
        self.memory -= other

    def __mul__(self, other:Union[int,float])->None:
        """

        Multiplies memory by the specified number.
        
        Parameters
        ----------

            other: Union[int,float]

    
        Example:
    
    >>> obj = Calculator(2)
    >>> obj * 3
    >>> obj
        Calculator(6)
        
        """
        
        self.__validate_type(other)
        self.memory *= other

    def __truediv__(self, other:Union[int,float])->None:
        """

        Divides memory by the specified number.
        
        Parameters
        ----------

            other: Union[int,float]

    
        Example:
    
    >>> obj = Calculator(6)
    >>> obj / 3
    >>> obj
        Calculator(2)
        
        """
        
        self.__validate_type(other)
        if other == 0:
            raise ZeroDivisionError("Division by zero is not supported")
        self.memory /= other

    def root(self, n:int=2)->None:
        """
        Takes the n-th root of a number

        Example:
        
    >>> obj = Calculator(16)
    >>> obj.root()
    >>> obj
        4
        
        """
        if not float(n).is_integer():
            raise ValueError("n must be an integer number")
        if n <= 0:
            raise ValueError("n must be positive")
        if self.memory < 0:
            raise ValueError("Roots of negative numbers are not supported")
        self.__validate_type(n)
        self.memory = self.memory ** (1 / n)

    def __str__(self):
        return f"The current value is {self.memory}"

    def __repr__(self):
        return f"Calculator({self.memory})"

    def reset(self)->None:
        """
        Sets the memory to 0
        
        """
        self.memory = 0

    def get_num(self)->Union[int,float]:
        """
        Returns the memory value.
        
        """
        return self.memory


