import java.util.*;

public class Card implements Comparable<Card>{

    private int value;
    private String suit;

    public Card (int v, String st) {
	value = v;
	
	if (v == 1) {
	    value = 14;
	}

	suit = st;
    }
    
    public Card (String v, String st) {
	for (int i = 2; i < 11; i++) {
	    if (v.equals("" + i)) {
		value = Integer.parseInt(v);
	    }
	}
	if (v.equals("J")) {
	    value = 11;
	}
	else if (v.equals("Q")) {
	    value = 12;
	}
	else if (v.equals("K")) {
	    value = 13;
	}
	else if (v.equals("A")) {
	    value = 14;
	}

	suit = st;
    }

    public String toString () {
	return valueAlt() + suitAlt();
    }
    
    public int getValue () {
	return value;
    }

    public String valueAlt () {
	if (value == 11) {
	    return "J";
	}
	else if (value == 12) {
	    return "Q";
	}
	else if (value == 13) {
	    return "K";
	}
	else if (value == 14) {
	    return "A";
	}

	return "" + value;
    }

    public String getSuit () {
	return suit;
    }

    public String suitAlt () {
	if (suit == "clubs") {
	    return "♧"; // Character.toString((char)2663);
	}
	else if (suit == "hearts") {
	    return "♡"; // Character.toString((char)2661);
	}
	else if (suit == "spades") {
	    return "♤"; // Character.toString((char)2660);
	}

	return "♢"; // Character.toString((char)2662); // suit == "diamonds"
    }

    public boolean equals (Card other) {
       	return this.getValue() == other.getValue() && this.getSuit() == other.getSuit(); 
    }

    public int suitStrength () {
	if (suit.equals("clubs")) {
	    return 1;
	}
	else if (suit.equals("hearts")) {
	    return 2;
	}
	else if (suit.equals("spades")) {
	    return 3;
	}
	return 0; // value == "diamonds"
    }

    public int compareTo (Card other) {
	if (this.getValue() > other.getValue()) {
	    return 1;
	}
	else if (this.getValue() < other.getValue()) {
	    return -1;
	}
	else if (this.equals(other)) {
	    return 0;
	}
	else if (this.suitStrength() > other.suitStrength()) {
	    return 1;
	}

	return -1;
    }

}
