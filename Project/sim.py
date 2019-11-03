import numpy as np
import math

class Market:
    def __init__(self , sellFactor, marketFunc ):
        self.sellFactor = sellFactor
        self.time = 0
        self.marketFunc = marketFunc
        self.players = []
        self.marketPrices = []  
        self.actions = np.arange(0, 110, 10)
    
    def addPlayer(self, player):
        self.players.append(player)
    
    
    # Should take in an action    
    def nextStep(self):
        self.time +=1
        
        if(self.players[0].buyPrice >= self.players[1].sellPrice and self.getBuyPrice(self.time) >= self.players[1].sellPrice):
            self.players[0].buyOther(self.players[1] , (self.players[0].buyPrice + self.players[1].sellPrice) // 2)
           

        if(self.players[1].buyPrice >= self.players[0].sellPrice and self.getBuyPrice(self.time) >= self.players[0].sellPrice):
            self.players[1].buyOther(self.players[0] , (self.players[1].buyPrice + self.players[0].sellPrice) // 2)
           
        for player in self.players:
            if(player.buyPrice >= self.getBuyPrice(self.time)):
                player.buyStock()
               

            if(player.sellPrice <= self.getSellPrice(self.time)):
                player.sellStock()
        
        
        # should return a next state and reward
        return self.time
    
    def getState(self):
        ret = []
        for i in range(10):
            ret.append(self.getBuyPrice(self.time - i))
        return ret
    
    def getReward(self):
        return self.players[0].value()
    
    def getBuyPrice(self, time):
        return self.marketFunc(time)
    
    def getSellPrice(self, time):
        return self.getBuyPrice(time) * self.sellFactor
    

class Player:
    def __init__(self, market , startMoney , buySellPriceFunc=0, name="Bot" , startStock = 0):
        self.money = startMoney
        self.stock = startStock
        self.market = market
        self.market.addPlayer(self)
        self.buySellPriceFunc = buySellPriceFunc
        self.buyPrice = 0
        self.sellPrice = 0 
        self.name = name
            
    def buyStock(self):
        stockPrice = self.market.getBuyPrice(self.market.time)
        if(self.money >= stockPrice):
            # print(self.name , "bought stock from the market for $" , stockPrice)
            self.money -= stockPrice
            self.stock += 1
            return 1
        else:
            return 0
    
    def sellStock(self):
        stockPrice = self.market.getSellPrice(self.market.time)
        if(self.stock >= 1):
            # print(self.name , "sold stock to the market for $" , stockPrice)
            self.money += stockPrice
            self.stock -=1
            return 1
        else:
            return 0
        
    def buyOther(self , other , price):
        if(self.money >= price and other.stock >= 1):
            # print(self.name , "bought stock from " , other.name , " for $" , price)
            self.money -= price
            self.stock += 1
            
            other.money += price
            other.stock -=1          
            return 1
        else:
            return 0
        
    def value(self):
        stockPrice = self.market.getSellPrice(self.market.time)
        return stockPrice * self.stock + self.money
    
    def setBuySellPrice(self , inputDict):
        self.buyPrice , self.sellPrice = self.buySellPriceFunc(inputDict)
    
def sinFunc(t, period=3):
    return 10 * math.sin(t/period) + 20

def sinFunc9(t, period=9):
    return 10 * math.sin(t/period) + 20

def sinFunc1(t, period=9):
    return 10 * math.sin(t) + 20

def increasing(t):
    return t / 2

def decreasing(t):
    return (100 - t) / 2
def constant(t):
    return 25
    
    
