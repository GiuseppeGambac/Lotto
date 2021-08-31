import random


class Ticket():
    
    def __init__(self,numberquanity,gametype : str, city):
        self.numberquantity = numberquanity
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
        "Selection of winning number from all the numbers"
        
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
        
        
    
        """
        +----------+----------+-----------------------------+--------+
    | TICKET N |    BET   |            NUMBERS          |  CITY  |
    +----------+----------+-----------------------------+--------+
    | TICKET 1 | QUATERNA |       12 20 39 56 55 3      | TORINO |
    +----------+----------+-----------------------------+--------+
    | TICKET 2 |   AMBO   | 12 20 39 56 55 31 67 90 2 9 | TUTTE  |
    +----------+----------+-----------------------------+--------+
    """
    
    def printTicket(self):           # da migliorare
        "print the ticket"
        #dovrei sistemare la tabella
        print('+--------+---------+------------------------+----------------+')
        print('|%s|   |%s|'  %(self.city,self.gametype))
        for i in range(len(self.numberlist)):
         print('|%d|' %self.numberlist[i])
         
