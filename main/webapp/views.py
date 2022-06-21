from django.shortcuts import render
import random


def guess_numbers(secret, actual):
    print(secret, actual)
    if len(actual) != 4:
        return "Incorrect number of elements, you should enter 4 elements."
    for a in actual:
        if a < 1 or a > 9:
            return "The numbers should be in a range between 1 and 9."
        if type(a) != int:
            return "You can only input integers."
        if actual.count(a) > 1:
            return "The elements cannot not be repetitive."

    bulls = 0
    cows = 0
    for i in range(4):
        if secret[i] == actual[i]:
            bulls += 1
    for i in range(4):
        for j in range(4):
            if i != j and secret[i] == actual[j]:
                cows += 1
                break

    if bulls == 4:
        return "You got it right!"

    return "You got " + str(bulls) + " bulls, " + str(cows) + " cows.";


def generate_numbers(n):
    arr = []
    i = 0
    while i < n:
        new_rand = random.randint(1, 9)
        same = False
        for j in range(i):
            if new_rand == arr[j]:
                same = True
                break
        if same == True:
            continue

        arr.append(new_rand)
        i += 1
    return arr


def guess(request):
    if request.method == "GET":
        return render(request, "guess_numbers.html")
    else:
        user = {
            "name": "Test",
            "age": 25,
            "email": "test@mail.ru"
        }
        secret = generate_numbers(4)
        if request.POST.get("numbers"):
            numbers_str = (request.POST.get("numbers")).split()
            actual = list(map(int, numbers_str))
            response = guess_numbers(secret, actual)
        else:
            print("Error")

        context = {
            "guess_numbers": request.POST.get("numbers"),
            "actual": actual,
            "response": response
        }

        return render(request, "guess_numbers.html", context)


def view_history(request):
    if request.method == "GET":
        return render(request, "history.html")
    else:
        user = {
            "name": "Test",
            "age": 25,
            "email": "test@mail.ru"
        }
        response = guess.response
        list_of_attempts = []
        if response:
            list_of_attempts.append()
    context = {
        "list_of_attempts": list_of_attempts
    }

    return render(request, "history.html", context)