year = 2024

def isLeapYear(year):
    """
    Check if year is a leap year
    @param (int) year : year
    return (bool): year is a leap year
    """
    if year%4 == 0 and year%100!=0:
        return True
    elif year%100==0:
        return True
    return False

print(isLeapYear(year))