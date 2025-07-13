import secrets
from constraint_pair import ConstraintPair

def generate_password(constraintPair: ConstraintPair) -> str:
    if not constraintPair.validate_constraints_length_vs_length():
        raise ValueError(constraintPair.get_error_msg())

    all_chars: str = constraintPair.get_all_chars() 
    password: str = ""
    while True:
        is_password_strong: bool = True
        password = ""
        for _ in range(constraintPair.length):
            password += secrets.choice(all_chars)

        for constraint, min_count in constraintPair.get_constraints_pairs():
            count: int = 0
            for ch in constraint: 
                for password_ch in password:
                    if ch == password_ch:
                        count += 1
            if count < min_count:
                is_password_strong = False

        if is_password_strong:
            break

    return password
