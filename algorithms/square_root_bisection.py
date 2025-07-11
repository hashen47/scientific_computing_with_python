from typing import Optional

def get_square_root(square_target: int, tolerance: float = 1e-7, max_iterations: int=100) -> Optional[float]:
    if square_target < 0:
        raise ValueError("square root of negative numbers not with in real numbers")

    if square_target == 1 or square_target == 0:
        return square_target 

    low: float = 0
    high: float = max(1, square_target)

    for _ in range(max_iterations):
        mid: float = (high + low)/2
        square_mid: float = mid**2

        if abs(square_mid - square_target) < tolerance:
            return mid
        elif square_mid < square_target: 
            low = mid
        else:
            high = mid

    return None


for n in range(0, 26):
    print(f"n: {n}, square_root: {get_square_root(n)}")