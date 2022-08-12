import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # regular expression search
    x = re.search(r"^([0-9]+):?([0-9]+)? (A?P?M) to ([0-9]+)?:?([0-9]+)? (A?P?M)$", s, re.IGNORECASE)
    try:
        # assigning variables
        hour_start = int(x.group(1))
        minute_start = x.group(2)
        meridiam_start = x.group(3)
        hour_end = int(x.group(4))
        minute_end = x.group(5)
        meridiam_end = x.group(6)

        # minutes may or may not be in user input
        if minute_start == None:
            minute_start = 0
        if minute_end == None:
            minute_end = 0
        minute_start = int(minute_start)
        minute_end = int(minute_end)

        # checking if user entered a valid time
        if (
            0 <= hour_start <= 12 and
            0 <= minute_start <= 59 and
            0 <= hour_end <= 12 and
            0 <= minute_end <= 59
        ) :
            if "PM" in meridiam_start and hour_start != 12:
                hour_start = int(x.group(1)) + 12
            if "PM" in meridiam_end and hour_start != 12:
                hour_end = hour_end + 12
            # convert 12 AM to 0:00
            if "AM" in meridiam_start and hour_start== 12:
                hour_start = 0
            if "AM" in meridiam_end and hour_end == 12:
                hour_end = 0

            return(f"{hour_start:02}:{minute_start:02} to {hour_end:02}:{minute_end:02}")
        # raise value error if bad input
        else:
            raise ValueError
    except AttributeError:
        raise ValueError


if __name__ == "__main__":
    main()