import random

def get_number():
    """
    Take number from user
    :return: integer; user number
    """
    while True:
        try:
            result = int(input("Choose the number:"))
            break
        except ValueError:
            print("It's not a number")
    return result

def get_numbers():
    """
    Take 6 different numbers in range from 1 to 49
    :return: list; numbers from user
    """
    result = []
    while len(result) < 6:
        number = get_number()
        if number not in result and 0 < number <= 49:
            result.append(number)
    return result

def print_numbers(numbers):
    """
    Print given numbers in asceding order
    :param numbers: list of numbers
    """
    print(", ".join(str(number) for number in sorted(numbers)))

def drawing_numbers():
    """
    Choose 6 random numbers
    :return: list
    """
    numbers = list(range(1, 49))
    random.shuffle(numbers)
    return numbers[:6]

def lotto():
    """
    Main function of program
    """
    user_numbers = get_numbers()
    print("Your numbers are:")
    print_numbers(user_numbers)

    lotto_numbers = drawing_numbers()
    print("Lotto numbers are:")
    print_numbers(lotto_numbers)

    hits = 0
    for i in user_numbers:
        if i in lotto_numbers:
            hits += 1
    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")

if __name__ == '__main__':
    lotto()

