import string
from typing import List, Tuple, Optional

class ConstraintPair:
    def __init__(self):
        self.error_msg: str = ""
        self.length: int = 16
        self.min_digit_count: int = 1 
        self.min_lowercase_count: int = 1 
        self.min_uppercase_count: int = 1 
        self.min_symbol_count: int = 1
        self.mult: int = 10

    def str_to_int(self, num_str: str) -> Optional[int]:
        try:
            if num_str.strip() == "":
                self.set_error_msg("number value cannot be empty")
                return None
            return int(float(num_str))
        except ValueError:
            self.set_error_msg(f"invalid integer value: {num_str}")
            return None

    def set_error_msg(self, msg: str):
        self.error_msg = f"ERROR: {msg}"
    
    def get_error_msg(self) -> str:
        return self.error_msg

    def get_constraints_length(self) -> int:
        return self.min_digit_count + self.min_lowercase_count + self.min_uppercase_count + self.min_symbol_count

    def set_length(self, val: str) -> bool:
        v: Optional[int] = self.str_to_int(val)
        if v is None:
            return False
        value: int = v 

        if value <= 0:
            self.set_error_msg(f"password length cannot be zero or negative: {value}")
            return False
        self.length = value
        return True

    def set_digit_count(self, val: str) -> bool:
        v: Optional[int] = self.str_to_int(val)
        if v is None:
            return False
        value: int = v

        if value < 0:
            self.set_error_msg(f"digit count cannot be negative: {value}")
            return False
        self.min_digit_count = value
        return True

    def set_lowercase_count(self, val: str) -> bool:
        v: Optional[int] = self.str_to_int(val)
        if v is None:
            return False
        value: int = v

        if value < 0:
            self.set_error_msg(f"lowercase character count cannot be negative: {value}")
            return False
        self.min_lowercase_count = value
        return True

    def set_uppercase_count(self, val: str) -> bool:
        v: Optional[int] = self.str_to_int(val)
        if v is None:
            return False
        value: int = v

        if value < 0:
            self.set_error_msg(f"uppercase character count cannot be negative: {value}")
            return False
        self.min_uppercase_count = value
        return True

    def set_symbol_count(self, val: str) -> bool:
        v: Optional[int] = self.str_to_int(val)
        if v is None:
            return False
        value: int = v

        if value < 0:
            self.set_error_msg(f"symbol character count cannot be negative: {value}")
            return False
        self.min_symbol_count = value
        return True

    def get_digit_constraint(self) -> str:
        word: str = string.digits
        while True:
            if len(word) >= self.min_digit_count * self.mult:
                break
            word += string.digits
        return word

    def get_lowercase_constraint(self) -> str:
        word: str = string.ascii_lowercase
        while True:
            if len(word) >= self.min_lowercase_count * self.mult:
                break
            word += string.ascii_lowercase
        return word

    def get_uppercase_constraint(self) -> str:
        word: str = string.ascii_uppercase
        while True:
            if len(word) >= self.min_uppercase_count * self.mult:
                break
            word += string.ascii_uppercase
        return word 

    def get_symbol_constraint(self) -> str:
        word: str = string.punctuation
        while True:
            if len(word) >= self.min_symbol_count * self.mult:
                break
            word += string.punctuation
        return word

    def get_all_chars(self) -> str:
        return self.get_digit_constraint() + self.get_lowercase_constraint() + self.get_uppercase_constraint() + self.get_symbol_constraint()

    def get_constraints_pairs(self) -> List[Tuple[str, int]]:
        return [
            (string.digits, self.min_digit_count),
            (string.ascii_lowercase, self.min_lowercase_count),
            (string.ascii_uppercase, self.min_uppercase_count),
            (string.punctuation, self.min_symbol_count),
        ]

    def validate_constraints_length_vs_length(self) -> bool:
        if self.get_constraints_length() > self.length:
            self.set_error_msg(f"constraint combine length cannot exceed password length, password length: {self.length}, constraints length: {self.get_constraints_length()}")
            return False
        return True