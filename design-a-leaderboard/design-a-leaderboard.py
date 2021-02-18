class Leaderboard:

    def __init__(self):
        self.players = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.players.keys():
            self.players[playerId] += score
        else:
            self.players[playerId] = score
        self.players = dict(sorted(self.players.items(), key=operator.itemgetter(1),reverse=True))
        
    def top(self, K: int) -> int:
        sum = 0
        count = 0
        for key, val in self.players.items():
            if count < K:
                sum += val
            count += 1
        return sum
            

    def reset(self, playerId: int) -> None:
        del self.players[playerId]
        self.players = dict(sorted(self.players.items(), key=operator.itemgetter(1),reverse=True))


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)