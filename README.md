# Blackjack-card-game
This Blackjack card game is a simple, text-based game made for terminal/console playing. 

## Rules
Two players (comuter and human) are given two cards each, numbers from 1 to 11. 
Human player can see his "hand", while only one of computer's cards is visible to player. Based on given cards, player shoud decide if he wants to open his cards or take another card from the deck.
After player makes the call, computer "decides" if it wants to take another card or open the cards. At the opening of the cards, sum is calculated to determine the winner.
Winner is the one that has greater sum of cards that is not greater then 21. If the sum is greater then 21, player that has sum of cards below 21 is winner.

## Functions
Functions defined in this script are:
- player(x1, x2, comp=False)
- game(player1, player2)
```python
player(x1, x2, comp=False)
```
This function takes two int type arguments and one boolean. x1 and x2 parameters are compared with sum, so they can take a value of 1 if there are two 11 cards.
comp=False parameter signals if the player is computer, so its cards are shown properly.

```python
game(player1, player2)
```
This function is gameplay function. It takes two int type arguments returned from player() function, and compares it. Input is required from human player to decide if cards shoud be shown or another card drawn from the deck (list of cards).
If human player has greater sum of cards, using random.choice() computer takes boolean value from boo_choice list to decide if it draws another card.
The function return boolean value. True if human player wins or False if computer wins.

## Game engine
Game engine of this game is simple while loop. At each looping, 4 random cards from cards_list are picked and assigned to variables passed to player() functions. 
First player function is human player, and has default comp=False, while comuter's player function has comp=True.  Game and player functions are inside winning variable, which ultimatly holds boolean value.
According to this value, statments are printed to signal winning or loosing. 
At the end of a loop, user input is required in the form of "y"(yes) or "n"(no) string. If user types "y", running condition is still met, so another game loop will be started. Else, running will be False, and the game will stop.

## Modules
Only module used in development of this game is standard random Python module, and its choice() function.

## Running the game
This game is intended to be run by Python IDE or other Python interpeter. 
To install Python 3 see [Tutorials Point page](https://www.tutorialspoint.com/how-to-install-python-in-windows).
