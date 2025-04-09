import random

random.seed()


class Deck:
    def __init__(self):
        #self.number = 1 # 1 to 10 - Jack 8 Queen 9 King 10 
        #self.suits = [1, 2, 3, 4]# 1- Clubs 2- Spades 3- Diamonds 4- Hearts       
        self.name = input(f"Your name: ")
        self.change = random.randrange(1,11) 
        self.hand = [random.randrange(1,11) for i in range(3)] #Max 3
        self.points = 0
        self.rounds = 0
        print(self.hand)
        
    def match(self, other_deck):
        while(True):
            try:
                choose = input(int(f"Choose one of the cards in your hand\n{self.hand}"))
                for i in range(self.hand):
                    if choose == self.hand[i]:
                        self.hand.pop(i)
                        break
                other_d_choose = other_deck.hand.pop(random.randrange(0,len(other_d_choose.hand)))
                win = self.wincondition(choose, other_d_choose)
                if win == 1:
                    self.points +=1
                elif win == 0:
                    other_deck.points += 1
                self.rounds +=1
                if self.rounds >= 3:
                    return self.winner(self.points, other_d_choose.points)            
            except: 
                print("You need to use a number")
                
    def wincondition(self, choose, other_d_choose):
        pass
    
    def winner(self, points, other_points):
        pass
Deck()