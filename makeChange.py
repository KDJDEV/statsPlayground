# define the number of cents in a dollar
total = 100

# coins we have available
coins = [1, 5, 10, 25, 50]

# initialize ways of making change
# there is only 1 way to make 0 cents: use no coins
num_ways = [1]+[0]*total
print(num_ways)

for coin in coins:
    for i in range(coin, total+1):
        num_ways[i] += num_ways[i-coin]
print(num_ways)
print(num_ways[total])