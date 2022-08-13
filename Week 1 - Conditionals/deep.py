phrase = input('what is the answer to the great question of life? ')
phrase = phrase.lower().strip()



match phrase:
    case "42":
        print('yes')
    case "forty two":
        print('yes')
    case "forty-two":
        print('yes')
    case _:
        print('no')