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
        
    
    def printTicket(self):
        #dovrei sistemare la tabella
        print('+--------+---------+------------------------+----------------+')
        print('|%s|   |%s|'  %(self.city,self.gametype))
        for i in range(len(self.numberlist)):
         print('|%d|' %self.numberlist[i])
        
    
            
prova = Ticket(15,"ciao","culo")        
    
type_of_game = ('ambata', 'ambo', 'terno', 'quaterna', 'cinquina') 
city = ('Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia', 'Tutte')  
#list of tickets
tickets = [] 


   
while True:
    try:
        ticketsnumber = int(input(("quanti biglietti vuoi generare? ")))
        break
    except:
        print("inserisci un numero")
    
for i in range(ticketsnumber):
 input_number = 0
 input_game =""
 input_city = ""
 #number selection
 while input_number <= 0 or input_number > 10:   
  try:
   input_number = int(input('inserisci un numero fra 1 e 10:'))
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
 tickets[i].printTicket()

