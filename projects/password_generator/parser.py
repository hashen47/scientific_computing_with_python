from argparse import ArgumentParser
from typing import Optional
from constraint_pair import ConstraintPair
from password_generator import generate_password

class Parser: 
    def __init__(self):
        self.constraintPair: ConstraintPair = ConstraintPair()
        self.error_msg: str = ""
        self.parser = ArgumentParser(prog="password generator", description="generate a random password with given parameters", add_help=True)
        self.add_arguments()

    def set_error_msg(self, msg: str):
        self.error_msg = msg

    def print_error_msg(self):
        print(f"\n{self.error_msg}")

    def add_arguments(self):
        self.parser.add_argument('--version', action='version', version='%(prog)s 1.0') 
        self.parser.add_argument("-l", help="password length", default=str(self.constraintPair.length))
        self.parser.add_argument("-d", help="minimum digit count", default=str(self.constraintPair.min_digit_count))
        self.parser.add_argument("-lc", help="minimum lowercase character count", default=str(self.constraintPair.min_lowercase_count))
        self.parser.add_argument("-uc", help="minimum uppercase character count", default=str(self.constraintPair.min_uppercase_count))
        self.parser.add_argument("-s", help="minimum symbol count", default=str(self.constraintPair.min_symbol_count))

    def generate_password(self) -> Optional[str]:
        try:
            return generate_password(self.constraintPair)
        except Exception as e:
            self.set_error_msg(str(e))
            return None

    def run(self):
        args = self.parser.parse_args()

        if not self.constraintPair.set_length(args.l):
            self.set_error_msg(self.constraintPair.get_error_msg())
            self.parser.print_help()
            self.print_error_msg()
            return

        if not self.constraintPair.set_digit_count(args.d):
            self.set_error_msg(self.constraintPair.get_error_msg())
            self.parser.print_help()
            self.print_error_msg()
            return

        if not self.constraintPair.set_lowercase_count(args.lc):
            self.set_error_msg(self.constraintPair.get_error_msg())
            self.parser.print_help()
            self.print_error_msg()
            return

        if not self.constraintPair.set_uppercase_count(args.uc):
            self.set_error_msg(self.constraintPair.get_error_msg())
            self.parser.print_help()
            self.print_error_msg()
            return

        if not self.constraintPair.set_symbol_count(args.s):
            self.set_error_msg(self.constraintPair.get_error_msg())
            self.parser.print_help()
            self.print_error_msg()
            return

        password: Optional[str] = self.generate_password()
        if password is None:
            self.parser.print_help()
            self.print_error_msg()
            return

        print(password)