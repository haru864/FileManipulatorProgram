import random


def isValidInteger(num: str) -> bool:
    try:
        int(num)
    except Exception as e:
        return False
    return True


def acceptIntegerFromInput(msg: str) -> int:
    while True:
        inputNumber: str = input(msg)
        if isValidInteger(inputNumber):
            return int(inputNumber)
        else:
            print("Please enter an integer")


def main() -> None:
    print("Randomly generates numbers in the specified minimum to maximum range.")
    print(
        "Specify the maximum and minimum values to predict the random number to be generated."
    )
    numOfChallenges: int = acceptIntegerFromInput("How many times do you challenge? > ")
    while True:
        minNumber: int = acceptIntegerFromInput("min number > ")
        maxNumber: int = acceptIntegerFromInput("minmax number > ")
        if minNumber > maxNumber:
            print("min number must be smaller than or equal to max number")
        else:
            break
    randomInteger = random.randint(minNumber, maxNumber)
    while numOfChallenges > 0:
        guess = acceptIntegerFromInput("What is your prediction? > ")
        if int(guess) == randomInteger:
            print("Congraturations!!")
            break
        else:
            numOfChallenges -= 1
            if numOfChallenges == 0:
                print(f"Miss. Try again later.")
                break
            print(f"Miss. Try again. (Remaining times: {numOfChallenges})")
    return None


if __name__ == "__main__":
    main()
    exit()
