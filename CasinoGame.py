# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 04:17:13 2021

@author: ASUS
"""

#blackjack game


#random to shuffle cards later in shuffle function
import random


#global variables to create the deck etc
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
          'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#creating the class
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


#creating a deck    
class Deck:
    
    def __init__(self):
        
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                
                self.all_cards.append(Card(suit,rank))


#shuffle the deck
    def shuffle(self):
    
        random.shuffle(self.all_cards)


#to deal cards
    def deal_one(self):
        return self.all_cards.pop()
        
    
#to hit
    def hit(self):
        return self.all_cards.pop()
    
class Hand:
   
    

    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
    

    
    def add_cards(self,new_cards):
            self.all_cards.append(new_cards)
            
    def show_all_cards(self):
        print(" Hand is ", *self.all_cards, sep = " , ")
      
        
    def show_some(self):
        print(f"The dealer has a {self.all_cards[0]} and a hidden card. ")
        
    def show_latest(self):
        print(f"New card is {self.all_cards[-1]} ")
        
        
    

    

    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
class bank:
    
    #instantiate the attributes
    def __init__(self,round_winnings=0,balance=0,bet_amount=0,coins=0,total_winnings=0,dealer_winnings=0,total_losses=0):
        self.round_winnings= round_winnings
        self.balance=balance
        self.bet_amount = bet_amount
        self.coins = coins
        self.total_winnings = total_winnings
        self.dealer_winnings = dealer_winnings
        self.total_losses = total_losses
        
        
    #buy in amount and coins for the player    
    def Buy_in(self):
        self.coins = int(input("how many coins do you wanna buy : "))
        print(f'{self.coins} coins purchased ')
        self.balance = self.balance + self.coins
        print('Your balance is : ' , self.balance)
              
        
    #player bet
    def bet(self):
        betisless = True
        while betisless:
            self.bet_amount = int(input("Enter the amount of coins you wanna bet in this round : "))
            while self.bet_amount<= self.balance:
                print(f'Player has bet {self.bet_amount} coins. ')
                self.balance = self.balance - self.bet_amount
                print(f'current balance is {self.balance} coins.')
                betisless = False
                break  #doubt
            else:
                buy_more = input("Do you want to buy more coins: Yes or No")
                if buy_more == 'Yes':
                    self.Buy_in()
                    break
                else:
                    print('Betting amount should not exceed balance ')
                
        
    
    #player win    
    def win(self):
        
        self.round_winnings =  (self.bet_amount*2)
        print(f'You won {self.round_winnings} coins this round. ' )
        self.balance = self.balance + (self.bet_amount*2)
        print(f'Your new balance is {self.balance} coins. ' )
        
        
        self.total_winnings =  self.total_winnings + self.round_winnings
        self.total_losses = self.total_losses + self.total_losses
        
    #player loses
    def loss(self):
        print (f' You lost {self.bet_amount} coins in that round. ')
        self.total_losses = self.total_losses + self.bet_amount
    
    def draw(self):
        print("You will get your coins back, coins refunded :" , self.bet_amount)
        self.balance = self.balance + self.bet_amount
    
    
    
    #total winnings of the player from all the rounds    
    def final_winnings(self):
        print(f'Your total winnings are {self.total_winnings-self.total_losses} coins. ')
        
    
        
def sum_of_cards(list1):
    Sumofallcards = 0 
    for k in range(len(list1)):
        value_of_card = list1[k].value
        Sumofallcards += value_of_card
    return Sumofallcards




def play():
    global continue_playing
    choice = input("do you want to continue playing the game : Yes or No ")
    if choice == 'Yes':
        print('Its time for the next round')
        
    elif choice== 'No':
        print("Thanks for playing blackjack")
        print("See you soon")
        continue_playing = False
        
         
    
    
    
    
    
    
    
    

#main setup-beginning
print("Welcome to Blackjack")
player_chips = bank()
player_chips.Buy_in()
    
    
#gamesetup

continue_playing = True
while continue_playing:
    new_deck = Deck()
    new_deck.shuffle()
    
    player = Hand("Player")
    dealer = Hand("Dealer")
    
    
    for x in range(2):
        player.add_cards(new_deck.deal_one())
        dealer.add_cards(new_deck.deal_one())
    
    
    
    #list of hand
    P = []
    P.extend(player.all_cards)
    D = []
    D.extend(dealer.all_cards)
    
    
    
    
 
    
    
    
    
    #tobet
    player_chips.bet()
    
    #show the hands

    player.show_all_cards()
    dealer.show_some() #shows one hand
    
    
    #for player
     
    
    player_total = sum_of_cards(P)
    print("The value of your hand is:" ,player_total)
    
    #for dealer
    
    
    dealer_total = sum_of_cards(D)
    
    game_on = True
    players_turn = True
    while game_on:
        
        
        if players_turn:
            #players turn
            while player_total <=21 :
                hit_or_stay = input("do you want to hit or stay : ")
                if hit_or_stay == 'hit':
                    player.add_cards(new_deck.hit())
                    player.show_latest()
                    P.append(player.all_cards[-1])
                    print("Card total:" , sum_of_cards(P) )
                    player_total = sum_of_cards(P)
                
                elif hit_or_stay == 'stay':
                    print (f'Your total is  {sum_of_cards(P)} , its time for the dealers turn')
                    players_turn = False
                    break
                
            else:
                print('you have gone bust, dealer wins')
                play()
                game_on = False
                
            
        
        
        else:
            #dealers turn
            print("Dealers turn:")
            print("current dealer total:" , dealer_total )
            print("dealers current cards" , *D , sep= " ")
            
            while dealer_total <= player_total :
                dealer.add_cards(new_deck.hit())
                dealer.show_latest()
                D.append(dealer.all_cards[-1])
                print("new total is" , sum_of_cards(D) )
                dealer_total = sum_of_cards(D)
                
            else:    
                #iterating only once
                
                
                
                
                if  dealer_total > 21:
                    print('The dealer has gone bust')
                    player_chips.win()
                    play()
                    game_on = False
                    break
                
                elif dealer_total > player_total and dealer_total <=21:
                    print('dealer wins this round')
                    player_chips.loss()
                    play()
                    game_on = False
                    break
            
                    
                elif player_total > dealer_total:
                    print("Player wins")
                    player_chips.win()
                    play()
                    game_on = False
                    break
                
                elif player_total == dealer_total:
                    print("its a draw")
                    player_chips.draw()
                    play()
                    game_on = False
                    break
        

                    '''  else:  #if u wanna use less than 17 rule
                 if dealer_total > 21:
                    print('The dealer has gone bust')
                    player_chips.win()
                    play()
                    game_on = False
                    break
                
                 elif dealer_total > player_total and dealer_total <=21:
                    print('Dealer wins this round')
                    player_chips.loss()
                    play()
                    game_on = False
                    break
                    
                 elif player_total > dealer_total:
                    print("Player wins")
                    player_chips.win()
                    play()
                    game_on = False
                    break '''

                
                
           
                
        











