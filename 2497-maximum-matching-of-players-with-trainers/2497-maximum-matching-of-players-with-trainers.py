class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # 1) Sort both lists
        players.sort()
        trainers.sort()
        
        i = j = 0
        matches = 0
        
        # 2) Two-pointer greedy
        while i < len(players) and j < len(trainers):
            if trainers[j] >= players[i]:
                # We can match player i with trainer j
                matches += 1
                i += 1
                j += 1
            else:
                # Trainer j too weak: try the next trainer
                j += 1
        
        return matches
        