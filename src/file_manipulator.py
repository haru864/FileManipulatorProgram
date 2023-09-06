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
    pass


def replaceString(inputpath: str, needle: str, newstring: str) -> None:
    pass


def _displayUsage() -> None:
    thisFileDir = os.path.dirname(os.path.abspath(__file__))
    manualFilePath = f"{thisFileDir}/file_manipulator_manual.txt"
    with open(manualFilePath, "r") as file:
        content = file.read()
        print(content)


def _isValidPath() -> bool:
    pass


if __name__ == "__main__":
    print(sys.argv)
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
            pass
        elif command == "replaceString":
            pass
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print("Invalid command was detected. Enter the correct command.\n")
        _displayUsage()
        exit()
