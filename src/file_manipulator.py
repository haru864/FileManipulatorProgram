import os
import sys


def reverse(inputpath: str, outputpath: str) -> None:
    with open(inputpath, "r") as readFile:
        contents = readFile.read()
    reversedContents = "".join(list(reversed(contents)))
    with open(outputpath, "w") as writeFile:
        writeFile.write(reversedContents)


def copy(inputpath: str, outputpath: str) -> None:
    with open(inputpath, "r") as readFile:
        contents = readFile.read()
    with open(outputpath, "w") as writeFile:
        writeFile.write(contents)


def duplicateContents(inputpath: str, count: int) -> None:
    with open(inputpath, "r") as readFile:
        contents = readFile.read()
    with open(inputpath, "a") as appendFile:
        while count > 0:
            appendFile.write("\n" + contents)
            count -= 1


def replaceString(inputpath: str, needle: str, newstring: str) -> None:
    with open(inputpath, "r") as readFile:
        contents = readFile.read()
    replacedContents = contents.replace(needle, newstring)
    with open(inputpath, "w") as writeFile:
        writeFile.write(replacedContents)


def _displayUsage() -> None:
    thisFileDir = os.path.dirname(os.path.abspath(__file__))
    manualFilePath = f"{thisFileDir}/file_manipulator_manual.txt"
    with open(manualFilePath, "r") as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    try:
        command: str = sys.argv[1]
        if command == "reverse":
            inputpath = sys.argv[2]
            outputpath = sys.argv[3]
            if os.path.exists(inputpath) == False:
                raise Exception("Inputpath does not exist.")
            if os.path.exists(outputpath) == False:
                raise Exception("Outputpath does not exist.")
            reverse(inputpath=inputpath, outputpath=outputpath)
        elif command == "copy":
            inputpath = sys.argv[2]
            outputpath = sys.argv[3]
            if os.path.exists(inputpath) == False:
                raise Exception("Inputpath does not exist.")
            if os.path.exists(outputpath) == False:
                raise Exception("Outputpath does not exist.")
            copy(inputpath=inputpath, outputpath=outputpath)
        elif command == "duplicateContents":
            inputpath = sys.argv[2]
            count = int(sys.argv[3])
            if os.path.exists(inputpath) == False:
                raise Exception("Inputpath does not exist.")
            if count < 0:
                raise Exception("Argument 'n' must be positive integer.")
            duplicateContents(inputpath=inputpath, count=count)
        elif command == "replaceString":
            inputpath = sys.argv[2]
            needle = sys.argv[3]
            newstring = sys.argv[4]
            if os.path.exists(inputpath) == False:
                raise Exception("Inputpath does not exist.")
            replaceString(inputpath=inputpath, needle=needle, newstring=newstring)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print("Invalid command was detected. Enter the correct command.")
        _displayUsage()
        exit()
