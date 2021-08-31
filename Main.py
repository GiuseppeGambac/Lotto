from Lotto.GeneratorTicket import ticketsGeneration
import GeneratorTicket
import random



# a list for every city
wheel ={"Bari":[] , "Cagliari" : [] ,'Firenze': [], 'Genova' : [], 'Milano' : [], 'Napoli' : [], 'Palermo' : [], 'Roma' : [], 'Torino' : [], 'Venezia' : [], 'Tutte' : []}

def Random(citylist):
   
   while True:
        
    number = random.randint(1,99)
        
    if number not in citylist:
        citylist.append(number)
        break
        
        


if __name__ == '__main__':
    
 tickets = ticketsGeneration()
 
 while True:
  # estraction for every wheel
  victory = False
  for i in wheel:
     Random(wheel[i])
     
  # for every tickets
  for x in range(len(tickets)):                
      victory = False
      # for every winning number in the ticket
      for y in range(len(tickets[x].winningnumbers)):
          #if the number is in the wheel of the tickets i go forward otherwise i go out the cycle
       if tickets[x].winningnumbers[y] in  wheel[tickets[x].city]:
          victory = True
          
       else:
           victory = False
           break
      
      #if at the end of the cycle i have this bit i stop the tickets checking
      if victory :
           print("ha vinto il biglietto numero %d" % x)
           print("con i numeri  " + str(tickets[x].winningnumbers))
           print("sulla ruota di  " + str(tickets[x].city))
           break
       
  if victory:
        break
           