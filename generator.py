import random
import re

date = input("Podaj datę urodzenia w formacie: dd.mm.rrrr: ")

gender_choice = input("Podaj płeć M/K: ")

pattern = r"^([0-2][\d]|[3][0-1])\.(1[0-2]|0[\d])\.([1-2][09][\d]{2})$"
match = re.match(pattern, date)

if match:
    pass
else:
    print("Błędna data")
    quit()


intmatch3 = int(match.group(3))


def year():
    if intmatch3 >= 1900 and intmatch3 <= 1999:
        return '%02d' % (intmatch3-1900)
    elif intmatch3 >= 2000 and intmatch3 <= 2009:
        return '%02d' % (intmatch3-2000)
    else:
        return '%02d' % (intmatch3 - 2000)


intmatch2 = int(match.group(2))


def month():
    if intmatch3 >= 1900 and intmatch3 <= 1999:
        return '%02d' % intmatch2
    else:
        return '%02d' % (intmatch2+20)


def day():
    return str(match.group(1))


def gender():
    if gender_choice.lower() == "m":
        return "%04d" % random.randrange(1, 10000, 2)
    elif gender_choice.lower() == "k":
        return "%04d" % random.randrange(2, 10000, 2)
    else:
        print("Błędna płeć")
        quit()


result = str(year()+month()+day()+gender())


def control_number():
    a = int(result[0])*1 % 10
    b = int(result[1])*3 % 10
    c = int(result[2])*7 % 10
    d = int(result[3])*9 % 10
    e = int(result[4])*1 % 10
    f = int(result[5])*3 % 10
    g = int(result[6])*7 % 10
    h = int(result[7])*9 % 10
    i = int(result[8])*1 % 10
    j = int(result[9])*3 % 10

    return (10-(a+b+c+d+e+f+g+h+i+j)) % 10


print(result+(str(control_number())))

input("\nAby zakończyć naciśnij klawisz Enter")