import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #expect an embedded youtube url: <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
    # parse to a shorter shareable url: https://youtu.be/xvFZjo5PgG0
    short = re.search(r'<iframe src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)"', s, re.IGNORECASE)
    if short:
        shareable = 'https://youtu.be/'+short.group(1)
        return shareable




if __name__ == "__main__":
    main()