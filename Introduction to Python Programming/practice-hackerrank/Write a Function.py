def is_leap(year):
    leap = False

    # Write your logic here
    if not year % 4:
        if not year % 100:
            if not year % 400:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap


year = int(input())
