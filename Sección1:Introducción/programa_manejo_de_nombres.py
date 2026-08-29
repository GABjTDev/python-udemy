name_1 = "Gabriel"
name_2 = "María"
name_3 = "Pedro"

def formatName(name, name2, name3):

    firstLetter1 = name[1].upper() + '.' + name[-2:]
    firstLetter2 = name2[1].upper() + '.' + name2[-2:]
    firstLetter3 = name3[1].upper() + '.' + name3[-2:]

    return firstLetter1 + '_' + firstLetter2 + '_' + firstLetter3


print(formatName(name_1, name_2, name_3))