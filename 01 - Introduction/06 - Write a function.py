def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400 == 0:
        return not leap
    elif year%100==0:
        return leap
    elif year%4 == 0:
        return not leap
    else:
        return leap

year = int(input())
print(is_leap(year))
