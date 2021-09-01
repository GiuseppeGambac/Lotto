from class_ticket import Ticket


class Generator():
    
 def __init__(self,gametypes : dict, cities : dict):
        
        self.gametypes = gametypes
        self.cities = cities
        
 def gameNumber(self,typegame):
    "Select the minimum value for let play the game"
    if typegame == "ambata":
        return 1
    elif typegame =="ambo":
        return 2
    elif typegame == "terno":
        return 3
    elif typegame == "quaterna":
        return 4
    elif typegame == "cinquina":
        return 5


 def ticketsGeneration(self):       
    #list of tickets
    self.tickets = [] 
     
    # tickets generation
    while True:
     try:
        ticketsnumber = int(input(("quanti biglietti vuoi generare? ")))
        if ticketsnumber > 0 and  ticketsnumber <= 5:
           
            break
     
        if ticketsnumber ==0:
            quit()
         
     except:
        print("inserisci un numero")
    
    # for every tickets generated    
    for i in range(ticketsnumber):
     input_number = 0
     input_game =""
     input_city = ""
     
     # select the type of game
     while True:
      print("seleziona un tipo di puntata fra quelli elencati")
      print(self.gametypes)    
      input_game = input()
      if input_game in self.gametypes:
         break
      else:
         print('valore non presente')
         input_game ==""
         
     # minumum range for the type of game
     minimum = self.gameNumber(input_game)
     
     #number selection
     while input_number < minimum or input_number > 10:    
      try:
       input_number = int(input('inserisci un numero fra %d e 10:' % minimum))
      except:
          print("devi inserire un numero")
      
     # cities selection
     while True:
      print("seleziona una ruota fra quelle elencate")
      print(self.cities)    
      input_city = input()
      if input_city in self.cities:
          break
      else:
          print('valore non presente')
          input_city ==""
 
     # add the ticket at the list
     self.tickets.append(Ticket(input_number,input_game,input_city))
 
     
    return self.tickets




 def printTicket(self):                                                                     # orrible...i know
      "print the list of tickets"
      
      # max length of the colonn plus two spaces, in case of different values
      maxlen_city =  max(len(x) for x in self.cities) +2
      maxlen_bet  =  max(len(x) for x in self.gametypes) +2
      
      # first line
      print('+----------+'+  "-"* (maxlen_city) +  '+'+"-"* (maxlen_bet)  +'+------------------------------+')
      
      city_spaces = int(((maxlen_city-4)/2))
      bet_spaces = int(((maxlen_bet-3)/2))
      
      
      print('|  Ticket  |'
            +" "*city_spaces+'city'+" "*city_spaces +"|"   
            +" "*bet_spaces+'Bet'+" "*(bet_spaces +1) 
            +'|            Numbers           |')
     
    # for evety ticket
      for i in range(len(self.tickets)):
        #same first line
        print('+----------+'+  "-"* (maxlen_city) +  '+'+"-"* (maxlen_bet)  +'+------------------------------+')
       
        #first spaces for the city
        ticketcityspaces = int((maxlen_city- len(self.tickets[i].city))/2)
        #second space for the city
        otherspacescity =  maxlen_city- len(self.tickets[i].city) - ticketcityspaces
        
        #first spaces for the bet
        ticketbetspaces =  int((maxlen_bet- len(self.tickets[i].gametype))/2)
        #second space for the bet
        otherspacesbet =  maxlen_bet- len(self.tickets[i].gametype) - ticketbetspaces
        
        #convert in string every int values
        stringlist = [str(x) for x in self.tickets[i].numberlist]
        #join every string in the list in a unique string
        string = "-".join(stringlist)
        #count the spaces missing for close the column
        spacesnumbers = (29  - len(string))
     
        print('| Ticket %d |' %(i+1)  
              +' '*(ticketcityspaces) + '%s' %(self.tickets[i].city)  + " "*otherspacescity +'|'
              +' '*(ticketbetspaces) +  '%s' %(self.tickets[i].gametype)  + " "*otherspacesbet  + '|' 
              +" " + '%s'  %(string) + ' ' * spacesnumbers  +'|')
        
      # last line
      print('+----------+'+  "-"* (maxlen_city) +  '+'+"-"* (maxlen_bet)  +'+------------------------------+')
         
         
