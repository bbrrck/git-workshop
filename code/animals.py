import sys


def default():
    print("👋 Ahoj")


def dog():
    print("🐕 Hav")


def cat():
    print("🐱 Mňau")


def main():
    if sys.argv[1] == "pes":
        dog()
    elif sys.argv[1] == "macka":
        cat()
    else:
        default()


if __name__ == "__main__":
    main()
