import numpy as np
import math

class Market:
    def __init__(self , sellFactor, marketFunc ):
        self.sellFactor = sellFactor
        self.time = 0
        self.marketFunc = marketFunc
        self.players = []    
    
    def addPlayer(player):
        self.players.append(player)
    
        
    def nextStep(self, buy, sell):
        self.time +=1
        
        if(self.players[0].buyPrice >= self.players[1].sellPrice):
            self.players[0].buyOther(players[1] , (self.players[0].buyPrice + self.players[1].sellPrice)//2 )
           

        if(self.players[1].buyPrice >= self.players[0].sellPrice):
            self.players[1].buyOther(self.players[0] , (self.players[1].buyPrice + self.players[0].sellPrice)//2 )
           
        for player in self.players:
            if(player.buyPrice >= market.getBuyPrice()):
                player.buyStock()
               

            if(player.sellPrice <= market.getSellPrice()):
                player.sellStock()
        
        
        return self.time
    
    def getState(self):
        return [self.getBuyPrice() , self.getSellPrice() , self.players[0].money , self.players[0].stock ]
    
    def getReward(self):
        return player[0].value()
    
    def getBuyPrice(self):
        return self.marketFunc(self.time)
    
    def getSellPrice(self):
        return self.getBuyPrice() * self.sellFactor
    

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
            
    def buyStock(self ):
        stockPrice = self.market.getBuyPrice()
        if(self.money >= stockPrice):
            print(self.name , "bought stock from the market for $" , stockPrice)
            self.money -= stockPrice
            self.stock += 1
            return 1
        else:
            return 0
    
    def sellStock(self):
        stockPrice = self.market.getSellPrice()
        if(self.stock >= 1):
            print(self.name , "sold stock to the market for $" , stockPrice)
            self.money += stockPrice
            self.stock -=1
            return 1
        else:
            return 0
        
    def buyOther(self , other , price):
        if(self.money >= price and other.stock >= 1):
            print(self.name , "bought stock from " , other.name , " for $" , price)
            self.money -= price
            self.stock += 1
            
            other.money += price
            other.stock -=1          
            return 1
        else:
            return 0
        
    def value(self):
        stockPrice = self.market.getSellPrice()
        return stockPrice * self.stock + self.money
    
    def setBuySellPrice(self , inputDict):
        self.buyPrice , self.sellPrice = self.buySellPriceFunc(inputDict)
    
def sinFunc(t):
    return 10 * math.sin(t) + 20
    
    
