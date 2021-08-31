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
        if self.gametype == "ambata":
            winningnumbers = random.sample(self.numberlist,1)
            return winningnumbers
        elif self.gametype =="ambo":
            winningnumbers = random.sample(self.numberlist,2)
            return winningnumbers
        elif self.gametype == "terna":
            winningnumbers = random.sample(self.numberlist,3)
            return winningnumbers
        elif self.gametype == "quaterna":
            winningnumbers = random.sample(self.numberlist,4)
            return winningnumbers
        elif self.gametype == "cinquina":
            winningnumbers = random.sample(self.numberlist,5)
            return winningnumbers
    
    
    def printTicket(self):
        #dovrei sistemare la tabella
        print('+--------+---------+------------------------+----------------+')
        print('|%s|   |%s|'  %(self.city,self.gametype))
        for i in range(len(self.numberlist)):
         print('|%d|' %self.numberlist[i])
         
def ticketsGeneration():       
    type_of_game = ('ambata', 'ambo', 'terno', 'quaterna', 'cinquina') 
    city = ('Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia', 'Tutte')  
    #list of tickets
    tickets = [] 
     
    while True:
     try:
        ticketsnumber = int(input(("quanti biglietti vuoi generare? ")))
        if ticketsnumber > 0 and  ticketsnumber <= 5:
           
            break
     
        if ticketsnumber ==0:
            quit() 
         
     except:
        print("inserisci un numero")
        
    for i in range(ticketsnumber):
     input_number = 0
     input_game =""
     input_city = ""
     #number selection
     while input_number <= 4 or input_number > 10:   
      try:
       input_number = int(input('inserisci un numero fra 5 e 10:'))
      except:
          print("devi inserire un numero")
          
    
     while True:
          print("seleziona un tipo di puntata fra quelli elencati")
          print(type_of_game)    
          input_game = input()
          if input_game in type_of_game:
              break
          else:
              print('valore non presente')
              input_game ==""
              
     while True:
      print("seleziona una ruota fra quelle elencate")
      print(city)    
      input_city = input()
      if input_city in city:
          break
      else:
          print('valore non presente')
          input_city ==""
 
 
     tickets.append(Ticket(input_number,input_game,input_city))
 
     
    return tickets
            
    
    
if __name__ == '__main__':   
 tickets = ticketsGeneration()
 
 for i in tickets:
     i.printTicket()


   

 
