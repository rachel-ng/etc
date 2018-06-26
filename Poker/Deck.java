import java.util.*;

public class Deck {

    private LinkedList<Card> deck;
    private int cardsLeft;
    
    public Deck () {
	
	deck = new LinkedList<Card>();
	
	for (int i = 2; i < 15; i++) {
	    deck.add(new Card(i, "diamonds"));
	    deck.add(new Card(i, "clubs"));
	    deck.add(new Card(i, "hearts"));
	    deck.add(new Card(i, "spades"));
	}

	cardsLeft = 52;
	
	shuffle();
    }

    public Card[] data () {
	Card[] c = deck.toArray(new Card[cardsLeft]);
	return c;
    }

    public LinkedList<Card> data (int i) {
	return deck;
    }
    
    public String toString () {
	Card[] c = data();
	String list = "{";
	
	for (int i = 0; i < cardsLeft; i++) {
	    list += c[i] + ", ";
	}

	return list + c[cardsLeft - 1] + "}";
    }

    public int size () {
	return cardsLeft;
    }
    
    public void shuffle () {
	Card[] shuffle = data(); // linkedlist to array of cards

	for (int i = 0; i < cardsLeft; i++) {
	    int rng = (int)(Math.random() * (cardsLeft - 1));
	    Card temp = shuffle[i];
	    shuffle[i] = shuffle[rng];
	    shuffle[rng] = temp;
	}

	LinkedList<Card> shuffled = new LinkedList<Card>(); // shuffled deck
	for (int i = 0; i < cardsLeft; i++) { // add cards in shuffled order to shuffled deck
	    shuffled.add(shuffle[i]);
	}

	deck = shuffled; // swap deck with shuffled deck
    }

    public Pocket deal (int game) { // deals one pocket
	
	if (game == 0) { // texas hold 'em
	    Card[] c = new Card[2];
	    for (int i = 0; i < 2; i++) {
		c[i] = deck.removeLast();
	    }

	    cardsLeft = cardsLeft - 2;
	    
	    Pocket pocket = new Pocket(c, game);
	    return pocket;
	}

	else {//  (game == 1) { // omaha
	    Card[] c = new Card[4];
	    for (int i = 0; i < 4; i++) {
		c[i] = deck.removeLast();
	    }

	    cardsLeft = cardsLeft - 4;
	    
	    Pocket pocket = new Pocket(c, game);
	    return pocket;
	}	
    }

    public void burn () { // burns (discards) one card 
	Card burnt = deck.removeLast();
	cardsLeft = cardsLeft - 1;
    }

    public Card drawF () {
	shuffle();
	cardsLeft = cardsLeft - 1;
	return deck.removeLast();
    }
    
    public Card draw () { // deals one card
	shuffle();
	burn();
	cardsLeft = cardsLeft - 1;
	return deck.removeLast();
    }
}
