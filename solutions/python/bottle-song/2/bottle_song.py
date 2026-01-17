def recite(start, take = 1):
    def verse(n):
        nums = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        c, nxt = nums[n].capitalize(), nums[n-1]
        b1, b2 = ("bottle" if n == 1 else "bottles"), ("bottle" if n-1 == 1 else "bottles")
        return [
            f"{c} green {b1} hanging on the wall,",
            f"{c} green {b1} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {nxt} green {b2} hanging on the wall."
        ]

    verses = [verse(i) for i in range(start, start - take, -1)]
    return [line for i, v in enumerate(verses) for line in (v + ([""] if i < len(verses)-1 else []))]