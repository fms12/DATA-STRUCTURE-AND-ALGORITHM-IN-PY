def birthdayCakeCandles(candles):
    x = max(candles)  # here you store the max vlue between the candles list
    return candles.count(x)  # count he value which come more than times


candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
result = birthdayCakeCandles(candles)
