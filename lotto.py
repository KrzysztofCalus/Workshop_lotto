import random

user_numbers = []
pc_numbers = list(range(1, 7))
random.shuffle(pc_numbers)
pc_numbers = pc_numbers[:6]
correct_number = []

for i in range(6):
    user_number = input("Choose the number: ")
    try:
        user_number = int(user_number)
        if user_number not in range(1, 50):
            print("Number outside range 1-49. Try one more time")
            break
        if user_number in user_numbers:
            print("Number already added. Try one more time")
            break
        else:
            user_numbers.append(user_number)
    except ValueError:
        print("It's not a number. Try one more time")
        break
for i in user_numbers:
    if i in pc_numbers:
        correct_number.append(i)

user_numbers.sort()
print(f"Yor numbers: \n{user_numbers}")
print(f"Lotto numbers: \n{pc_numbers}")
print(f"You hit {len(correct_number)} number/s")