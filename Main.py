from TicketGenerator import Generator
from estraction import Estractor


                
        
        


if __name__ == '__main__':
 # a list for every city
 
 gametypes = ('ambata', 'ambo', 'terno', 'quaterna', 'cinquina') 
 cities = ('Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia', 'Tutte')  
 
 # a list for every city
 wheel ={"Bari":[] , "Cagliari" : [] ,'Firenze': [], 'Genova' : [], 'Milano' : [], 'Napoli' : [], 'Palermo' : [], 'Roma' : [], 'Torino' : [], 'Venezia' : [], 'Tutte' : []}
    
    
 Gen = Generator(gametypes,cities)

 Gen.ticketsGeneration()
 Gen.printTicket()

 Sort = Estractor(wheel,Gen.tickets)
   
 Sort.checkWinner()
         
