# Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

# One-liner
def birthdayCakeCandles(candles):
    return candles.count(max(candles))


# without using count() or max() and finding them manually
def birthdayCakeCandles1(candles):
    max_candle = candles[0]
    count = 0

    for candle in candles:
        if candle > max_candle:
            max_candle = candle

    for candle in candles:
        if candle == max_candle:
            count += 1
    return count


print(birthdayCakeCandles([3, 2, 1, 3]))
print(birthdayCakeCandles([4, 4, 1, 3]))
print(birthdayCakeCandles([4, 4, 1, 3, 4, 6, 1, 6, 3, 6, 6, 1, 6]))

print('----------------------')

print(birthdayCakeCandles1([3, 2, 1, 3]))
print(birthdayCakeCandles1([4, 4, 1, 3]))
print(birthdayCakeCandles1([4, 4, 1, 3, 4, 6, 1, 6, 3, 6, 6, 1, 6]))
