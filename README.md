# poker

a terrible poker simulator  
(wip)

<!--
```
poker/Calculations.java
      Card.java
      CommunityCards.java
      Deck.java
      Driver.java
      Game.java
      Hand.java
      Player.java
      Pocket.java
      Pot.java
``` -->

```
poker/Calculations.java
```
not yet finished, barely even started. 

```
poker/Card.java
```
the card! 

has a value and a suit, is comparable.

```
poker/CommunityCards.java
```
the community cards!

the `flop`, the `turn`, and the `river`

```
poker/Deck.java
```
a `linked list` of cards, has an `int` for the number for cards left

the constructor makes a deck of 52 cards with all values and suits and shuffles the deck. 

there are functions to `shuffle` the deck, `deal` a pocket, `burn` cards, draw the `flop`, and the `turn` and `river`

```
poker/Driver.java
```
kind of obvious, was originally used to test the objects/functions, doesn't work anymore because i changed how i was doing some of the things, `poker/Game.java` is better for checking it out 

```
poker/Game.java
```
the game. 

```
poker/Hand.java
```
for checking "combos" i guess you could say 

```
poker/Player.java
```
creates a player with a name and pocket cards. 

```
poker/Pocket.java
```
the player's "hand", i suppose you could say. 

the constructor takes your cards and the game type (texas or omaha), and sorts your cards for you with . 

- [ ] implement comparable 
- [ ] work on hands / possible hands / everything christ what was i trying to do 

```
poker/Pot.java
```
for betting! a wip
