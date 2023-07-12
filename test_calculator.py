from hypothesis import given, assume
import unittest
import hypothesis.strategies as st
from calculator import Calculator

strategies = [
    st.none(),
    st.booleans(),
    st.characters(),
    st.text(),
    st.lists(st.integers()),
    st.tuples(st.integers(), st.floats()),
    st.dictionaries(st.text(), st.integers()),
    st.sets(st.integers()),
]


class TestCalculator(unittest.TestCase):
    @given(
        x=st.floats(allow_nan=False, allow_infinity=False),
        y=st.floats(allow_nan=False, allow_infinity=False),
    )
    def test_add(self, x, y):
        calculator = Calculator(x)
        calculator.__add__(y)
        self.assertEqual(calculator.get_num(), x + y)

    @given(x=st.one_of(strategies))
    def test_inst_type(self, x):
        with self.assertRaises(TypeError):
            Calculator(x)

    @given(x=st.one_of(strategies))
    def test_add_type(self, x):
        calculator = Calculator()
        with self.assertRaises(TypeError):
            calculator + x

    @given(
        x=st.floats(allow_nan=False, allow_infinity=False),
        y=st.floats(allow_nan=False, allow_infinity=False),
    )
    def test_sub(self, x, y):
        calculator = Calculator(x)
        calculator.__sub__(y)
        self.assertEqual(calculator.get_num(), x - y)

    @given(
        x=st.floats(allow_nan=False, allow_infinity=False),
        y=st.floats(allow_nan=False, allow_infinity=False),
    )
    def test_mul(self, x, y):
        calculator = Calculator(x)
        calculator.__mul__(y)
        self.assertEqual(calculator.get_num(), x * y)

    @given(
        x=st.floats(allow_nan=False, allow_infinity=False),
        y=st.floats(allow_nan=False, allow_infinity=False),
    )
    def test_div(self, x, y):
        assume(x != 0)
        assume(y != 0)
        calculator = Calculator(x)
        calculator.__truediv__(y)
        self.assertEqual(calculator.get_num(), x / y)

    @given(x=st.floats(allow_nan=False, allow_infinity=False),
           y=st.integers(min_value = 1))
    def test_root(self, x, y):
        assume(x >= 0)
        calculator = Calculator(x)
        calculator.root(y)
        self.assertEqual(calculator.get_num(), x ** (1 / y))

    @given(x=st.floats(allow_nan=False, allow_infinity=False))
    def test_reset(self, x):
        calculator = Calculator(x)
        calculator.reset()
        self.assertEqual(calculator.memory, 0)


if __name__ == "__main__":
    unittest.main()
