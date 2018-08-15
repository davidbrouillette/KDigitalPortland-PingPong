import pygame

class Match:
    def __init__(self, player1, player2, firstServer, pointsInMatch, servesPerPlayer):
        self.pointsInMatch = pointsInMatch
        self.servesPerPlayer = servesPerPlayer
        self.player1 = player1
        self.player2 = player2
        self.score = {'player1':0, 'player2':0}
        self.numberOfServes = 0
        self.currentServer = firstServer
        self.winner = None

    def setServer(self, name):
        self.currentServer = name
        
    def isCurrentServer(self, name):
        return name == self.currentServer
    
    def getScore(self, name):
        score = 0
        playerName = name
        if playerName in self.score:
             score = self.score[playerName]
        return score
    
    def subtractPoint(self, id):
        name =""
        if id == self.player1.controllerId:
            name = self.player1.name
        elif id == self.player2.controllerId:
            name = self.player2.name
            
        if self.score[name] > 0:
            self.score[name] = self.score[name] - 1
        print("Subtract score: " + name + " ")
        print("Scores: ")
        print(self.score)
        print("")

    def scorePoint(self, playerId):
        self.score[playerId] = self.score[playerId] + 1
        self.numberOfServes = self.numberOfServes + 1
        self.checkScores(playerId)
        self.checkServes()
        print("after Scores: ")
        print(self.score)
        return self.score

    def checkScores(self, name):
        if self.score[name] == self.pointsInMatch:
            self.winScenerio(name)

    def winScenerio(self, name):
        print(name + " wins")
        print("\nFinal Scores ")
        print("Player1: " + str(self.score["player1"]))
        print("Player2: " + str(self.score["player2"]))
        print("\n")
        self.winner = name
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def checkServes(self):
        if self.numberOfServes > 0 and (self.numberOfServes % self.servesPerPlayer == 0):
            if self.currentServer == 'player1':
                self.currentServer = 'player2'
            else:
                self.currentServer = 'player1'
            
            print('CurrentServer: ' + self.currentServer + '\n')