#! pyhon3
# blackjack card game
import sys,random

HEARTS = chr(9829)   # Character 9829 is '♥'.
DIAMONDS = chr(9830)   # Character 9830 is '♦'.
SPADES = chr(9824)   # Character 9824 is '♠'.
CLUBS = chr(9827)   # Character 9827 is '♣'.
BACKSIDE = 'backside'

def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com
 
    Rules:
     Try to get as close to 21 without going over.
     Kings, Queens, and Jacks are worth 10 points.
     Aces are worth 1 or 11 points.
     Cards 2 through 10 are worth their face value.
     (H)it to take another card.
     (S)tand to stop taking cards.
     On your first play, you can (D)ouble down to increase your bet
     but must hit exactly one more time before standing.
     In case of a tie, the bet is returned to the player.
     The dealer stops hitting at 17.''')
    money = 5000
    while True:
        if money <=0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

            print('Money:', money)
            bet=getBet(money)

            #give cards
            deck=getDeck()
            dealerHand = [deck.pop(),deck.pop()]
            playerHand = [deck.pop(),deck.pop()]

            #handle actions
            print('Bet:',bet)
            while True:
                displayHands(playerHand,dealerHand,False)
                print()

                #check if the player has bust
                if getHandValue(playerHand) > 21:
                    break
                move = getMove(playerHand,money-bet)

                if move == 'D':
                    #player can increase bet
                    additionalBet = getBet(min(bet,(money-bet)))
                    bet += additionalBet
                    print('Be increased to {}.'.format(bet))
                    print('Bet:',bet)

                if move in ('H','D'):
                    #Hit/Double down takes anothe card.
                    newCard = deck.pop()
                    rank,suit = newCard
                    print('you drew a {} of {}.'.format(rank,suit))
                    playerHand.append(newCard)

                    if getHandValue(playerHand) > 21:
                        # the player has busted:
                        continue
                if move in ('S','D'):
                    #stand/doubling down
                    break

            #Handle dealer actions
            if getHandValue(playerHand) <= 21:
                while getHandValue(dealerHand) < 17:
                    #The dealer Hits:
                    print('Dealer hits....')
                    dealerHand.append(deck.pop())
                    displayHands(playerHand,dealerHand,False)

                    if getHandValue(dealerHand) > 21:
                        break
                    input('press Enter tocontinue....')
                    print('\n\n')

            displayHands(playerHand,dealerHand,True)

            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)

            # Handle whether the player won,lost or tied:
            if dealerValue > 21:
                print('Dealer Busts! you win ${}!'.format(bet))
            elif (playerValue > 21) or (playerValue < dealerValue):
                print('you lost')
                money -= bet
            elif playerValue > dealerValue:
                print('you won ${}!'.format(bet))
                money += bet
            elif playerValue == dealerValue:
                print('Its a tie , the bet is retured')

            input('press enter to continue')
            print('\n\n')

def getBet(maxBet):
    #"""Ask the player how much they want to bet for this round."""
    while True:  # Keep asking until they enter a valid amount.
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('>').upper().strip()
        if bet == 'QUIT':
            print('thank you for playing')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1<= bet <= maxBet:
            return bet

def getDeck():
    #"""Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS,DIAMONDS,SPADES,CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit)) #add number cards
        for rank in ('J','Q','K','A'):
            deck.append((rank,suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand , dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('DEALER:',getHandValue(dealerHand))
        displayCards(dealerHAnd)
    else:
        print('DEALER:???')
        displayCards([BACKSIDE] + dealerHand[1:])

    #show player cards
    print('PLAYER:', getHandValue(playerHand))
          displayCards(playerHand)

def getHandValue(cards):
   # """Returns the value of the cards. Face cards are worth 10, aces are
   # 171. worth 11 or 1 (this function picks the most suitable ace value)."""
   value = 0
   numberOfAces = 0

   #add the value for the non ace cards
   for card in cards:
       rank = card[0] #card is atuple like(rank,suit)
       if rank == 'A':
           numberOfAces +=1
       elif rank in ('K','Q','J'):
           value +=10
       else:
           value += int(rank)  #numbered cards worth their number

    #add value of aces
   for i in range(numberOfAces):
       if value+10<21
           value += 10
    return value

