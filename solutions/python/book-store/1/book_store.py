from functools import lru_cache
from itertools import combinations

BOOK_PRICE = 800  # cents

GROUP_PRICE = {
    1: 800,
    2: 1520,
    3: 2160,
    4: 2560,
    5: 3000,
}


def total(basket):
    counts = [0] * 5
    for book in basket:
        counts[book - 1] += 1

    counts = tuple(counts)

    @lru_cache(None)
    def dp(state):
        if sum(state) == 0:
            return 0

        min_cost = float("inf")

        available = [i for i in range(5) if state[i] > 0]

        for size in range(1, len(available) + 1):
            for combo in combinations(available, size):
                new_state = list(state)
                for idx in combo:
                    new_state[idx] -= 1

                cost = GROUP_PRICE[size] + dp(tuple(new_state))
                min_cost = min(min_cost, cost)

        return min_cost

    return dp(counts)