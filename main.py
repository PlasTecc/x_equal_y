from functions import generate_level, validate_input, save_changes, clear_terminal
from settings import DATA, ANSWER


def main():
    while True:
        clear_terminal()
        print(f"Q - QUIT\t|\tS - SKIP\t|\tSCORE: {DATA['score']}")
        numbers = generate_level() if DATA['numbers'] is None else DATA['numbers']
        print(f"{numbers} = {ANSWER}")
        try:
            while True:
                user_input = input("> ").lower()
                if user_input == "q":
                    raise KeyboardInterrupt

                if user_input == "s":
                    DATA['numbers'] = None
                    break

                if validate_input(user_input, numbers):
                    DATA['score'] += 1
                    DATA['numbers'] = None
                    break

        except KeyboardInterrupt:
            save_changes(numbers)
            exit(1)


if __name__ == '__main__':
    main()
