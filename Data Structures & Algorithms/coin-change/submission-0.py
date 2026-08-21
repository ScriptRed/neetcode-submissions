class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP map: amount → minimum coins to reach that amount
        coinMap = {0: 0}

        if amount == 0:
            return 0
        # BFS/DP expansion
        queue = [0]

        while queue:
            curr = queue.pop(0)

            for coin in coins:
                new_amount = curr + coin
                if new_amount > amount:
                    continue

                # If we found a better way to reach new_amount
                if new_amount not in coinMap or coinMap[new_amount] > coinMap[curr] + 1:
                    coinMap[new_amount] = coinMap[curr] + 1
                    queue.append(new_amount)

                # If we reached the target, return immediately
                if new_amount == amount:
                    return coinMap[new_amount]

        return -1
