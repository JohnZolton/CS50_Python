def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # all valid plates must start with two letters
    if not s[0:1].isalpha():
        return False
    # must have 2 to 6 characters
    if not 2 <= len(s) <= 6:
        return False
    #first number can't be 0
    first_num = True
    for i in s:
        if i == '0' and first_num == True:
            return False
        if i.isdigit():
            first_num = False
        #can't have letters after numbers
        if i.isalpha() and first_num ==  False:
            return False
        # no special characters allowed
        if not i.isalpha() and not i.isdigit():
            return False
    return True

if __name__=="__main__":
    main()