from datetime import date, timedelta
import sys
import inflect


p = inflect.engine()

def main():
    print(convert(input('Date you were born (YYYY-MM-DD): ')))

def convert(s):
    try:
        x = date.fromisoformat(s)
        y = date.today()
        z = y - x # now we're in total days between birthday and today

        #convert days to minutes
        minutes = z.days*60*24
        #convert digit to words
        minutes = p.number_to_words(minutes, andword="").capitalize()
        return (minutes + ' minutes')
    except:
        sys.exit(1)
if __name__ == "__main__":
    main()