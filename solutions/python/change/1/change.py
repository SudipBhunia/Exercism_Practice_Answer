def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    
    if target == 0:
        return []
    
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    parent = [-1] * (target + 1)
    
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                if dp[amount - coin] + 1 < dp[amount]:
                    dp[amount] = dp[amount - coin] + 1
                    parent[amount] = coin
    
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")
    
    result = []
    current = target
    while current > 0:
        result.append(parent[current])
        current -= parent[current]
    
    return sorted(result)