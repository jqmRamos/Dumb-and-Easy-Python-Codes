import random

random.seed()


class Deck:
    def __init__(self):
        #self.number = 1 # 1 to 10 - Jack 8 Queen 9 King 10   
        self.name = input(f"Your name: ")
        self.change = random.randrange(1,11) 
        self.hand = [random.randrange(1,11) for i in range(3)] #Max 3
        self.suits = [random.randrange(1,5) for i in range(3)] # 1- Clubs 2- Spades 3- Diamonds 4- Hearts     
        self.points = 0
        self.rounds = 0
        self.suit_choose = 0
        print(self.hand)
        
    def match(self, other_deck):
        while(True):
            other_d_index = random.randrange(0,len(other_deck.hand))
            choose = int(input(f"Choose one of the cards in your hand\n{self.hand} :"))
            for i in range(len(self.hand)):
                if choose == self.hand[i]:
                    self.hand.pop(i)
                    self.suit_choose = self.suits.pop(i)
                    break
            other_d_choose = other_deck.hand.pop(other_d_index)
            other_deck.suit_choose = other_deck.suits.pop(other_d_index)
            win = self.wincondition(choose, other_d_choose)
            if win == 1:
                self.points +=1
            elif win == 0:
                other_deck.points += 1
            self.rounds +=1
            print(f"round: {self.rounds}\n{self.name} points: {self.points} \n{other_deck.name} points: {other_deck.points}")
            if self.rounds >= 3:
                return self.winner(self.points, other_deck.points)            

                
    def wincondition(self, choose, other_d_choose):
        if 0 < choose < 4:
            choose += 10
        if choose == self.change +1:
            choose = choose * 10 + self.suit_choose
        if 0 < other_d_choose < 4:
            other_d_choose += 10
        if choose == self.change +1:
            other_d_choose = choose * 10 + self.suit_choose

        if choose > other_d_choose:
            return 1 
        elif choose < other_d_choose:
            return 0
        return -1 
    
    def winner(self, points, other_points):
        if points > other_points:
            print("you win")
        elif points < other_points:
            print("You lose")
        else:
            print("Draw")
other = Deck()
me = Deck()
me.match(other)