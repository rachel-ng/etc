import java.util.*;

public class CommunityCards {

    private Card[] cc;
    private Card flop1, flop2, flop3, turn, river;
    private int cardsIn;
    
    public CommunityCards () {
	cc = new Card[5];
	cardsIn = 0;
    }

    public String toString () {
	if (cardsIn == 0) {
	    return "";
	}

	String str = "{";
	
	for (int i = 0; i < cardsIn - 1; i++) {
	    str += cc[i] + ", ";
	}

	return str + cc[cardsIn - 1] + "}";
    }

    public int getCardsIn () {
	return cardsIn;
    }

    public Card getFlop1 () {
	return cc[0];
    }

    public Card getFlop2 () {
	return cc[1];
    }

    public Card getFlop3 () {
	return cc[2];
    }

    public Card getTurn () {
	return cc[3];
    }
    
    public Card getRiver () {
	return cc[4];
    }
    
    public void dealt (Card c) {
	cc[cardsIn] = c;
	cardsIn++;
    }

    public Card[] data () {
	return cc;
    }

}
