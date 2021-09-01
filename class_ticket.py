import random


class Ticket():
    
    def __init__(self,numberquanity,money,gametype : str, city):
        self.numberquantity = numberquanity
        self.money = money
        self.gametype = gametype
        self.city = city
        
        
        # there is a limit in the program but i prefer have another limit here inside the object
        if self.numberquantity > 10:
            self.numberquantity = 10
            print("limiteraggiunto")
        #Here the numbers are generated in a list using random.sample    
        self.numberlist =  self.numberlist = random.sample(range(1,91), self.numberquantity)
        
        #a selection of numbers based on the type of game
        self.winningnumbers = self.numberSelection()
     
        
    def numberSelection(self):
        if self.gametype == "ambata":
            winningnumbers = random.sample(self.numberlist,1)
            return winningnumbers
        elif self.gametype =="ambo":
            winningnumbers = random.sample(self.numberlist,2)
            return winningnumbers
        elif self.gametype == "terno":
            winningnumbers = random.sample(self.numberlist,3)
            return winningnumbers
        elif self.gametype == "quaterna":
            winningnumbers = random.sample(self.numberlist,4)
            return winningnumbers
        elif self.gametype == "cinquina":
            winningnumbers = random.sample(self.numberlist,5)
            return winningnumbers
        
        
    def WinningMoney(self):
        moneyambata   = 0.0
        moneyambo     = 0.0
        moneyterno    = 0.0
        moneyquaterna  =  0.0
        moneycinquina =  0.0
        
        
        if self.numberquantity ==1:
           moneyambata = 11,23
        elif self.numberquantity==2:
            moneyambata =5.61
            moneyambo = 250
        elif self.numberquantity ==3:
          moneyambata   = 3.74	
          moneyambo     = 83.33
          moneyterno    = 4500
        elif self.numberquantity ==4:
          moneyambata   = 2.80	
          moneyambo     = 41.66	
          moneyterno    = 1125
          moneyquaterna  =  12000	  
        elif self.numberquantity ==5:
          moneyambata   = 2.24
          moneyambo     = 25	
          moneyterno    = 450
          moneyquaterna  =  24000	
          moneycinquina =  6000000
        elif self.numberquantity ==6:
          moneyambata   = 1.87	
          moneyambo     = 16.66
          moneyterno    = 225
          moneyquaterna  =  8000	
          moneycinquina =  1000000
        elif self.numberquantity ==7:
          moneyambata   = 1.60	
          moneyambo     = 11.90	
          moneyterno    = 128.57	
          moneyquaterna  =  2428.57	
          moneycinquina =  285714.28
        elif self.numberquantity ==8:
          moneyambata   = 1.40	
          moneyambo     = 8.92	
          moneyterno    = 80.35
          moneyquaterna  =  1714.28
          moneycinquina =  107142.85 
        elif self.numberquantity ==9:
          moneyambata   = 1.24	
          moneyambo     = 6.94	
          moneyterno    = 53.57
          moneyquaterna  =  952.38	
          moneycinquina =  47619.04
        elif self.numberquantity ==10:
          moneyambata   = 1.12	
          moneyambo     = 5.55	
          moneyterno    = 37.50	
          moneyquaterna  =  571,42	
          moneycinquina =  23809.52
        
        
        if self.gametype == "ambata":
          total= self.money * moneyambata
        elif self.gametype == "ambo":
           total=  self.money * moneyambo
        elif self.gametype == "terno":
          total = self.money * moneyterno
        elif self.gametype == "quaterna":
          total = self.money * moneyquaterna
        elif self.gametype == "cinquina":
          total= self.money * moneycinquina
        if total > 500:
            withtax = total *0.92
            return total,withtax
        else:   
       
         return total
        
        
    

    
 
         
