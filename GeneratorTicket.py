from class_ticket import Ticket


def gameNumber(typegame):
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


def ticketsGeneration():       
    
    type_of_game = ('ambata', 'ambo', 'terno', 'quaterna', 'cinquina') 
    city = ('Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia', 'Tutte')  
    #list of tickets
    tickets = [] 
     
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
     money = 0
     input_game =""
     input_city = ""
     
     # select the type of game
     while True:
      print("seleziona un tipo di puntata fra quelli elencati")
      print(type_of_game)    
      input_game = input()
      if input_game in type_of_game:
         break
      else:
         print('valore non presente')
         input_game ==""
         
     # minumum range for the type of game
     minimum = gameNumber(input_game)
     
     #number selection
     while input_number < minimum or input_number > 10:    
      try:
       input_number = int(input('inserisci un numero fra %d e 10:' % minimum))
      except:
          print("devi inserire un numero")
       
     #money selection
     while money == 0:   
           try:
            money = int(input('inserisci la scommessa:'))
           except:
               print("devi inserire un numero")
      
     
     
     # city selection
     while True:
      print("seleziona una ruota fra quelle elencate")
      print(city)    
      input_city = input()
      if input_city in city:
          break
      else:
          print('valore non presente')
          input_city ==""
 
     # add the ticket at the list
     tickets.append(Ticket(input_number,money,input_game,input_city))
 
     
    return tickets