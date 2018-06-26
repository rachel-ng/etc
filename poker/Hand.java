import java.util.*;

public class Hand {

    private Card[] hand = new Card[5];
    private String type;
    
    public Hand(Card[] c, String t) {
	hand = c;
	type = t;
    }

    public String toString () {
	String str = "{";
	for (int i = 0; i < 4; i++) {
	    str += hand[i].toString() + ", ";
	}
	return str + hand[4].toString() + "}";
    }
    
}
