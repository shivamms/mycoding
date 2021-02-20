class Leaderboard:

    def __init__(self):
        self.players = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.players.keys():
            self.players[playerId] += score
        else:
            self.players[playerId] = score
        
        
    def top(self, K: int) -> int:
        self.players = dict(sorted(self.players.items(), key=operator.itemgetter(1),reverse=True))
        sum = 0
        count = 0
        for key, val in self.players.items():
            if count < K:
                sum += val
            count += 1
        return sum
            

    def reset(self, playerId: int) -> None:
        del self.players[playerId]



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

# lb = Leaderboard()
# print(lb.addScore(1,13))
# print(lb.addScore(2,93))
# print(lb.addScore(3,84))
# print(lb.addScore(4,6))
# print(lb.addScore(5,89))
# print(lb.addScore(6,31))
# print(lb.addScore(7,7))
# print(lb.addScore(8,1))
# print(lb.addScore(9,98))
# print(lb.addScore(10,42))
# print(lb.top(5))
# print(lb.reset(1))
# print(lb.reset(2))
# print(lb.addScore(3,76))
# print(lb.addScore(4,68))
# print(lb.top(1))
# print(lb.reset(3))
# print(lb.reset(4))
# print(lb.addScore(2,70))
# print(lb.reset(2))