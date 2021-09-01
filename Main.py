from TicketGenerator import Generator



                
        
        


if __name__ == '__main__':
 # a list for every city
 
 gametypes = ('ambata', 'ambo', 'terno', 'quaterna', 'cinquina') 
 cities = ('Bari', 'Cagliari', 'Firenze', 'Genova', 'Milano', 'Napoli', 'Palermo', 'Roma', 'Torino', 'Venezia', 'Tutte')  
 
    
    
generatore = Generator(gametypes,cities)
    
generatore.ticketsGeneration()
generatore.printTicket()
         
