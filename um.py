import re

def main():
    print(count(input("Text: ")))


def count(s):
    phrase = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(phrase)


if __name__ == "__main__":
    main()