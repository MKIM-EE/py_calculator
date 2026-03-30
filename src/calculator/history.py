from calculator.operations import add, subtract, multiply, divide  # 패키지 내 참조

_history: list[str] = []

def calculate(a: float, op: str, b: float) -> float:
    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if op not in ops:
        raise ValueError(f"지원하지 않는 연산자: {op}")
    result = ops[op](a, b)
    _history.append(f"{a} {op} {b} = {result}")
    return result

def get_history() -> list[str]:
    return list(_history)

def clear_history() -> None:
    _history.clear()