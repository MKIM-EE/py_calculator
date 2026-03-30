from calculator.history import calculate, get_history, clear_history

def main():
    print("=== CMD 계산기 ===")
    print("형식: 숫자 연산자 숫자  (예: 3 + 4)")
    print("명령어: history, clear, quit\n")

    while True:
        user_input = input("> ").strip()

        if user_input == "quit":
            break
        elif user_input == "history":
            history = get_history()
            if not history:
                print("  기록 없음")
            else:
                for line in history:
                    print(f"  {line}")
        elif user_input == "clear":
            clear_history()
            print("  기록 삭제됨")
        else:
            try:
                parts = user_input.split()
                a, op, b = float(parts[0]), parts[1], float(parts[2])
                result = calculate(a, op, b)
                print(f"  = {result}")
            except ValueError as e:
                print(f"  오류: {e}")
            except (IndexError, TypeError):
                print("  형식 오류. 예: 3 + 4")

if __name__ == "__main__":
    main()