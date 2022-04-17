#author : mjwakex
#title: blackjack vs CPU - CLI edition in python 
#---------------------------------------------------------------------------------------------------------
#this module is imported for random selection of cards
import random 

#both decks have 4 of every card in the range of (1,13) in clusive - 1 represents Ace and 11,12,13 are Jack,Queen,King
player_deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
dealer_deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
#the empty arrays are where the hands are stores to
player_hand, dealer_hand = [], []
#flags to call a function based on a codition - check main()
player_stick, dealer_stick = 0, 0

#function that gets a random card pout of the player deck, removes the card from the deck and appends it to the player hand
def choose_player_card ():
    card = random.choice(player_deck)
    player_deck.remove(card)
    player_hand.append(card)
#on first round 2 cards are dealt, then each other round only one is
def deal(player_deals):
    if player_deals == 1:
        choose_player_card()
        choose_player_card()
    else:
        choose_player_card()
    print(player_hand)
    check(player_deals, 'hit')
#checks the players hand to see wether the player has gone bust or had blackjack or has more than 5 cards
def check(player_deals, ans):
    global player_stick
    if sum(player_hand) > 21:
        print(f"Bust! you where {sum(player_hand) - 21} over 21. You did this in {player_deals} goes. Dealer wins")
    elif sum(player_hand) == 21:
        print(f"BLACKJACK! You did this in {player_deals} goes. Player wins")
    elif player_deals > 5:
        print(f"Unlucky. You have got 5 cards and are still {21 - sum(player_hand)} away!. Dealer wins") 
    elif ans == 'stick':
        player_stick = 1
    else:
        hit_or_stick(player_deals)
#asks the user of they want another card or to keep their current ones
def hit_or_stick(player_deals):
    while True:
        try:
            ans = input("hit or stick: ").lower()
            if ans == 'stick':
                check(player_deals, ans)
                break
            elif ans == 'hit':
                if player_deals < 5:
                    deal(player_deals + 1 )
                    break
                elif player_deals == 5:
                    break
        except:
            pass
        print("Incorrect input, please try again.")
#same function as choose_player_cards just for dealer
def choose_dealers_card():
    card = random.choice(dealer_deck)
    dealer_deck.remove(card)
    dealer_hand.append(card)
#same function as deal just for dealer
def dealer_deal(dealer_deals):
    if dealer_deals == 1:
        choose_dealers_card()
        choose_dealers_card()
    else:
        choose_dealers_card()
    dealer_check(dealer_deals,'hit')
#checks the dealers cards
def dealer_check(dealer_deals, ans):
    global dealer_stick
    if ans.lower() == 'stick':
        dealer_stick = 1
    else:
        dealer_hit_or_stick(dealer_deals)
#the dealer will only hit if he has less than 5 cards in his hand and his total is less than 19
def dealer_hit_or_stick(dealer_deals):
    if (sum(dealer_hand) >= 21) or (sum(dealer_hand) >= 19 and sum(dealer_hand) < 21) or (dealer_deals == 4) :
        dealer_check(dealer_deals, 'stick')
    else:
        dealer_deal(dealer_deals+1)
#this compares the dealers cards to the players cards. as seen in the dealer_check funtion, even if the dealer is bust, it will only be known if the layer sticks
def dealer_vs_player():
    if sum(player_hand) > sum(dealer_hand):
        print(f"Player wins !\nPlayer had a total of {sum(player_hand)}\nThe dealer had a total of {sum(dealer_hand)}. Dealers hand: {dealer_hand}")
    elif (sum(dealer_hand) > sum(player_hand)) and (sum(dealer_hand) <= 21) :
        print(f"Dealer wins !\nPlayer had a total of {sum(player_hand)}\nThe dealer had a total of {sum(dealer_hand)}. Dealers hand: {dealer_hand}")
    else:
        print(f"Player wins. Dealer went bust ! dealers hand was {dealer_hand}")

#main fucntion calls everything
def main():
    player_deals , dealer_deals = 1, 1
    dealer_deal(dealer_deals)
    deal(player_deals)
    if dealer_stick == 1 and player_stick == 1:
        dealer_vs_player()
    

#calling main    
main()

