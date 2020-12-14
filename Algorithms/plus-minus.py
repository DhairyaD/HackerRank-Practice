# Link: https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    pos, zero, neg = 0, 0, 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num == 0:
            zero += 1
        else:
            neg += 1

    print(format(pos/len(arr), '.6f'))
    print(format(neg/len(arr), '.6f'))
    print(format(zero/len(arr), '.6f'))


print(plusMinus([1, 1, 0, -1, -1]))
