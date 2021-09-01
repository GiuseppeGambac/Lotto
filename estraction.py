import random


class Estractor():
    def __init__(self,wheel : list , tickets : list):
        self.wheel = wheel
        self.tickets = tickets
        
    
    def Random(self,citylist):
      "add a random number in a list if there is not that number "
      
      while True:
         
       number = random.randint(1,99)
         
       if number not in citylist:
         citylist.append(number)
         break 
      
    def checkWinner(self):
  # estraction for every wheel
         while True:
           victory = False
          
           for i in self.wheel:
             self.Random(self.wheel[i])
            
             # for every tickets
             for x in range(len(self.tickets)):                
               victory = False
              # for every winning number in the ticket
               for y in range(len(self.tickets[x].winningnumbers)):
                     #if the number is in the wheel of the tickets i go forward otherwise i go out the cycle
                  if self.tickets[x].winningnumbers[y] in  self.wheel[self.tickets[x].city]:
                     victory = True
                     
                  else:
                     victory = False
                     break
              
              #if at the end of the cycle i have this bit i stop the tickets checking
               if victory :
                    print("ha vinto il biglietto numero %d" % (x+1))
                    print("con i numeri  " + str(self.tickets[x].winningnumbers))
                    print("sulla ruota di  " + str(self.tickets[x].city))
                   
                    return self.tickets[x]
          
  


 
     
     
