import java.util.*;

public class Driver {

    public static void main(String[]args) {

	System.out.println("\n\n\n\n\nSTART OF CURRENT TEST");
	
	System.out.println("\n\ntest cards"); // testing cards' constructor
	
	for (int i = 1; i < 15; i++) {
	    Card a = new Card (i, "spades");
	    System.out.println(a.toString() + "\t (" + a.getValue() + " of " + a.getSuit() + ")");
	}


	System.out.println("\n\ntest equals"); // testing equals
	
	Card a = new Card (2, "hearts");
	Card b = new Card (2, "hearts");
	Card c = new Card (2, "clubs");
	Card d = new Card (2, "spades");
	Card e = new Card (14, "spades");
	
	System.out.println(a.toString() + " equals " + b.toString() + "? " + a.equals(b));
	System.out.println(a.toString() + " equals " + c.toString() + "? " + a.equals(c));
	System.out.println(b.toString() + " equals " + c.toString() + "? " + b.equals(c));


	System.out.println("\n\ntest compareTo"); // testing compareto
		
	System.out.println(a.toString() + " compareTo " + b.toString() + "? " + a.compareTo(b) + "\t 0");
	System.out.println(a.toString() + " compareTo " + c.toString() + "? " + a.compareTo(c) + "\t 1");
	System.out.println(b.toString() + " compareTo " + c.toString() + "? " + b.compareTo(c) + "\t 1");
	System.out.println(a.toString() + " compareTo " + d.toString() + "? " + a.compareTo(d) + "\t -1");
	System.out.println(b.toString() + " compareTo " + d.toString() + "? " + b.compareTo(d) + "\t -1");
	System.out.println(a.toString() + " compareTo " + e.toString() + "? " + a.compareTo(e) + "\t -1");
	System.out.println(b.toString() + " compareTo " + e.toString() + "? " + b.compareTo(e) + "\t -1");



	
	System.out.println("\n\n\n\ntest pocket"); // testing pocket
	
	Card[] cards = {a, b, c, d, e};
	Pocket h = new Pocket(cards, 1);

	String list = "{"; // expected tostring of pocket
	for (int i = 0; i < 4; i++) {
	    list += cards[i] + ", ";
	}
	System.out.println(list + cards[4] + "}");
	
	System.out.println(h.toString());


	System.out.println("\n\ntest pocketpair"); // testing pocketpair

	Card[] h1c = {a, b};
	Pocket h1 = new Pocket(h1c, 0);
	
	Card[] h2c = {a, e};
	Pocket h2 = new Pocket(h2c, 0);

	System.out.println(h.toString() + "\n" + h.pocketPair());
	System.out.println(h1.toString() + "\n" + h1.pocketPair());
	System.out.println(h2.toString() + "\n" + h2.pocketPair());



	
	System.out.println("\n\n\n\ntest deck + community cards"); // testing deck + community cards
	Deck f = new Deck();

	System.out.println(f.toString());
	System.out.println(f.size());

	
	System.out.println("\n\ntest shuffle"); // testing shuffle

	Card[] shuffledDeck = f.data();
	Card[] ordered = new Card[52];

	String[] suits = {"diamonds", "clubs", "hearts", "spades"};
	int ind = 0;
	
       	for (int i = 2; i < 15; i++) {
	    for (String s : suits) {
		ordered[ind] = new Card(i, s);
		ind++;
	    }
	}

	/* not the right one, but might be useful at some point
	   ordered[i - 2] = new Card(i, "diamonds");
	   ordered[(i - 2) + 13] = new Card(i, "clubs");
	   ordered[(i - 2) + 26] = new Card(i, "hearts");
	   ordered[(i - 2) + 39] = new Card(i, "spades");
	*/
	
	String order = "{"; // expected tostring of pocket
	for (int i = 0; i < 51; i++) {
	    order += ordered[i] + ", ";
	}
	System.out.println(order + ordered[51] + "}");
	System.out.println("\n");
	System.out.println(f.toString());
	
	int same = 0;
	for (int i = 0; i < 52; i++) {
	    if (shuffledDeck[i].equals(ordered[i])) {
		same++;
	    }
	}
	boolean pass = same / 52 < 1;
	
	System.out.println("\nsimilarities: " + same + " (" + pass + ")");


	System.out.println("\n\ntest deal community cards"); // testing dealing of community cards
	CommunityCards cc = new CommunityCards();

	f.burn();
	cc.dealt(f.drawF());
	cc.dealt(f.drawF());
	cc.dealt(f.drawF());

	System.out.println(cc.toString());
	System.out.println(cc.getCardsIn());
	

	System.out.println("\n\ntest deal (pockets)"); // testing dealing of pockets
	
	Pocket texas = f.deal(0);
	Pocket omaha = f.deal(1);

	System.out.println(texas);
	System.out.println(omaha);

	
	System.out.println("\n\ntest post-deal"); // after dealing pockets
	
	System.out.println(f.toString());
	System.out.println(f.size());

	
	System.out.println("\n\ntest draw card (+ burn)"); // testing drawing of cards after burning one
	
	Card d1 = f.draw();
	cc.dealt(d1);
	System.out.println(d1.toString());

	
	System.out.println("\n\ntest post-draw"); // after drawing cards
	
	LinkedList<Card> currentDeck = f.data(0);

	System.out.println("remove " + d1.toString() + " (" + !currentDeck.remove(d1) + ")"); 
	System.out.println(f.toString());
	System.out.println(f.size());
	System.out.println("\n");
	System.out.println(cc.toString());
	System.out.println(cc.getCardsIn());
	System.out.println("\n");
	cc.dealt(f.draw());
	System.out.println(cc.toString());
	System.out.println(cc.getCardsIn());

	
	System.out.println("\n\ntest getting community cards"); // testing getting of community cards
	System.out.println(cc.getFlop1());
	System.out.println(cc.getFlop2());
	System.out.println(cc.getFlop3());
    	System.out.println(cc.getTurn());
    	System.out.println(cc.getRiver());




	System.out.println("\n\n\n\ntest pot"); // testing pot
	Pot p = new Pot(4);

	System.out.println("pot: "+ p.getPot());
	System.out.println("sidepot: "+ p.getSidePot());

	p.addBet(0,10);
	p.addSidePot(0,10);

	System.out.println("added 10 to pot: " + p.getPot());
	System.out.println("added 10 to sidepot: " + p.getSidePot());

	p.addBet(3,40);
	p.addSidePot(3,40);

	System.out.println("added 40 to pot: " + p.getPot());
	System.out.println("added 40 to sidepot: " + p.getSidePot());

	System.out.println("player 0 in side pot? " + p.inSP(0));
	System.out.println("player 3 in side pot? " + p.inSP(3));


	

	System.out.println("\n\n\n\ntest combos"); // testing pot
	CommunityCards cc1 = new CommunityCards();
	Deck f1 = new Deck();
	
	System.out.println("h2: " + h2.toString() + "\n" + h2.pocketPair());
	System.out.println("h: " + h.toString() + "\n" + h.pocketPair());

	f1.burn();
	cc1.dealt(f1.drawF());
	cc1.dealt(f1.drawF());
	cc1.dealt(f1.drawF());
	System.out.println(cc1.toString() + "\t" + cc1.getCardsIn() + "\n");
	
	h2.combos(cc1);
	System.out.println("h2: " + h2.toString());
	System.out.println(h2.possibleHands());
	System.out.println("\n\n");
	
	h.combos(cc1);
	System.out.println("h: " + h.toString());
	System.out.println(h.possibleHands());
	System.out.println("\n\n");

	cc1.dealt(f1.draw());
	System.out.println(cc1.toString() + "\t" + cc1.getCardsIn() + "\n");

	h2.combos(cc1);
	System.out.println("h2: " + h2.toString());
	System.out.println(h2.possibleHands());
	System.out.println("\n\n");

	h.combos(cc1);
	System.out.println("h: " + h.toString());
	System.out.println(h.possibleHands());
	System.out.println("\n\n");
	
	cc1.dealt(f1.draw());
	System.out.println(cc1.toString() + "\t" + cc1.getCardsIn() + "\n");

	h2.combos(cc1);
	System.out.println("h2: " + h2.toString());
	System.out.println(h2.possibleHands());
	System.out.println("\n\n");

	h.combos(cc1);
	System.out.println("h: " + h.toString());
	System.out.println(h.possibleHands());
	System.out.println("\n\n");
    }

    
}
