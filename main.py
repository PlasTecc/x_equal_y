from functions import *


def main():
    while True:
        print(f"Q - QUIT\t|\tSCORE: {DATA['score']}")
        numbers = "".join(map(str, generate_numbers())) if DATA['numbers'] is None else DATA['numbers']
        print(" ".join(numbers))
        try:
            while True:
                user_input = input("> ").lower()
                if user_input == "q":
                    raise KeyboardInterrupt

                if validate_input(user_input, numbers):
                    DATA['score'] += 1
                    DATA['numbers'] = None
                    break

        except KeyboardInterrupt:
            save_changes(numbers)
            exit(1)


if __name__ == '__main__':
    main()
