def addDigits(str):
    sum = 0
    for digit in str:
        sum += int(digit)
    return sum

def luckCheck(str):
    if str == '' or not str.isdigit():
        return 'Please enter a valid ticket number!'
    else:
        two_remainder = len(str) % 2
        two_quotient = len(str) // 2
        if two_remainder == 0:
            first_part = str[:two_quotient]
            second_part = str[two_quotient:]
        elif two_remainder == 1:
            if len(str) == 1:
                return "You've entered a one-digit ticket number, which by definition cannot be lucky! Please try again!"
            else:
                first_part = str[:two_quotient]
                second_part = str[two_quotient+1:]
        first_sum = addDigits(first_part)
        second_sum = addDigits(second_part)
        return first_sum == second_sum

# test it out
print(luckCheck(''))
print('********************')
print(luckCheck('h345'))
print('********************')
print(luckCheck('luck'))
print('********************')
print(luckCheck('7'))
# lucky tickets
print('********************')
print(luckCheck('77'))
print('********************')
print(luckCheck('777'))
print('********************')
print(luckCheck('003111'))
print('********************')
print(luckCheck('813372'))
print('********************')
print(luckCheck('17935'))
# unlucky tickets
print('********************')
print(luckCheck('56'))
print('********************')
print(luckCheck('567'))
print('********************')
print(luckCheck('5346713'))
print('********************')
print(luckCheck('534704'))
