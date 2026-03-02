from dataclasses import dataclass
from typing import Optional

from quick_calc.core import Calculator


@dataclass
class CalcState:
    display: str = "0"
    left: Optional[float] = None
    op: Optional[str] = None
    reset_next: bool = False


class QuickCalcApp:
    # class-level defaults (prevents "no attribute" even if something is weird)
    calc: Calculator = Calculator()
    state: CalcState = CalcState()

    def init(self) -> None:
        # instance state
        self.calc = Calculator()
        self.state = CalcState()

    def press(self, key: str) -> str:
        key = key.strip()

        if key == "C":
            self.state = CalcState()
            return self.state.display

        if key in "0123456789.":
            return self._digit(key)

        if key in {"+", "-", "*", "/"}:
            return self._operator(key)

        if key == "=":
            return self._equals()

        raise ValueError(f"Unsupported key: {key}")

    def _digit(self, ch: str) -> str:
        s = self.state

        if s.reset_next:
            s.display = "0"
            s.reset_next = False

        if ch == "." and "." in s.display:
            return s.display

        if s.display == "0" and ch != ".":
            s.display = ch
        else:
            s.display += ch

        return s.display

    def _operator(self, op: str) -> str:
        s = self.state
        s.left = float(s.display)
        s.op = op
        s.reset_next = True
        return s.display

    def _equals(self) -> str:
        s = self.state

        if s.left is None or s.op is None:
            return s.display

        right = float(s.display)

        try:
            if s.op == "+":
                result = self.calc.add(s.left, right)
            elif s.op == "-":
                result = self.calc.subtract(s.left, right)
            elif s.op == "*":
                result = self.calc.multiply(s.left, right)
            elif s.op == "/":
                result = self.calc.divide(s.left, right)
            else:
                raise ValueError("Invalid operator")
        except ZeroDivisionError:
            s.display = "Error"
            s.left = None
            s.op = None
            s.reset_next = True
            return s.display

        s.display = str(int(result)) if result == int(result) else str(result)
        s.left = None
        s.op = None
        s.reset_next = True
        return s.display