def min_coins_to_win(n, coins):
    coins.sort(reverse = True)
    total = sum(coins)
    my_sum = 0
    for i in range(n):
        my_sum += coins[i]
        if my_sum > total - my_sum:
            return i + 1

n = int(input())
coins = list(map(int, input().split()))
print(min_coins_to_win(n, coins))

