from Lotto.GeneratorTicket import ticketsGeneration
import GeneratorTicket

if __name__ == '__main__':   
 tickets = ticketsGeneration()
 
 for i in tickets:
     i.printTicket()

   
