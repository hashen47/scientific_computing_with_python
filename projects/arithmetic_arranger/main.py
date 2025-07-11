from typing import List, Dict


def validate_number(string: str) -> int:
    error_msg: str = "" 
    n: int = 0
    try:
        n = int(string)
        if n > 9999:
            error_msg = "Error: Numbers cannot be more than four digits."
    except:
        error_msg = "Error: Numbers must only contain digits."

    if error_msg != "":
        raise ValueError(error_msg)

    return n


def calculate_answer(n1: int, n2: int, operator: str) -> int:
    if operator == "+":
        return n1 + n2
    if operator == "-":
        return n1 - n2
    raise ValueError("Error: Operator must be '+' or '-'.")


def arithmetic_arranger(problems: List[str], show_answers: bool=False) -> str:
    try:
        if len(problems) > 5:
            raise ValueError("Error: Too many problems.")

        solutions: List[Dict[str, str|int]] = []

        for problem in problems:
            parts: List[str] = problem.split(" ")
            calculate_answer(0, 0, parts[1])

            solution: Dict[str, str|int] = {}
            solution["opt"] = parts[1]
            solution["n1"] = validate_number(parts[0])
            solution["n2"] = validate_number(parts[2])
            solution["answer"] = calculate_answer(solution["n1"], solution["n2"], solution["opt"])
            solution["max_length"] = max(len(parts[0]), len(parts[2])) + 2    # +2 for operator and space between operator and longest number 

            solutions.append(solution)

        output: str = ""

        statements: List[str] = []
        for solution in solutions:
            max_length: int = int(solution["max_length"])
            n1_length: int = len(str(solution["n1"]))
            statements.append("".join([" " for _ in range(max_length - n1_length)]) + str(solution["n1"]))
        output += "    ".join(statements) + "\n"

        statements: List[str] = []
        for solution in solutions:
            max_length: int = int(solution["max_length"])
            n2_length: int = len(str(solution["n2"]))
            statements.append(str(solution["opt"]) + "".join([" " for _ in range(max_length - n2_length - 1)]) + str(solution["n2"]))
        output += "    ".join(statements) + "\n"

        statements: List[str] = []
        for solution in solutions:
            max_length: int = int(solution["max_length"])
            statements.append("".join(["-" for _ in range(max_length)]))
        output += "    ".join(statements)

        if show_answers:
            output += "\n"
            statements: List[str] = []
            for solution in solutions:
                max_length: int = int(solution["max_length"])
                answer_length: int = len(str(solution["answer"]))
                statements.append("".join([" " for _ in range(max_length - answer_length)]) + str(solution["answer"]))
            output += "    ".join(statements)

        return output

    except ValueError as e:
        return str(e)