# Poker

An unfinished poker simulator - mostly just a card simulator at the moment. 

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
Not yet finished, for calculating probability, etc. 

```
poker/Card.java
```

Has a value and a suit, is comparable.

```
poker/CommunityCards.java
```
The community cards!

The `flop`, the `turn`, and the `river`

```
poker/Deck.java
```
A `linked list` of cards, has an `int` for the number for cards left

The constructor makes a deck of 52 cards with all values and suits and shuffles the deck. 

There are functions to `shuffle` the deck, `deal` a pocket, `burn` cards, draw the `flop`, and the `turn` and `river`

```
poker/Driver.java
```
Was originally used to test the objects/functions, doesn't work anymore because i changed how i was doing some of the things, `poker/Game.java` is better for checking it out! 

```
poker/Game.java
```
The game

```
poker/Hand.java
```
For checking "combos" i guess you could say 

```
poker/Player.java
```
Creates a player with a name and pocket cards. 

```
poker/Pocket.java
```
The player's `hand`

The constructor takes your cards and the game type (texas or omaha), and sorts your cards for you with 

- [ ] implement comparable 
- [ ] work on hands / possible hands / everything christ what was i trying to do 

## In Progress

```
poker/Pot.java
```
For betting! A wip
