import java.util.*;

public class Pocket {// implements Comparable<Pocket> {

    private Card[] pocket;
    private int size;
    private int[] values;
    private String[] suits;

    private CommunityCards cc;
    private LinkedList<Hand> combos;
    
    private int game;
    
    public Pocket (Card[] cards, int type) {
	pocket = cards;
	size = pocket.length;
	values = values();
	suits = suits();

	combos = new LinkedList<Hand>();

	game = type;
	// 0 = texas hold 'em
	// 1 = omaha

	msort();

    }

    private int[] values () {
	int[] v = new int[size];

	for (int i = 0; i < size; i++) {
	    v[i] = pocket[i].getValue();
	}

	return v;
    }

    private String[] suits () {
	String[] s = new String[size];

	for (int i = 0; i < size; i++) {
	    s[i] = pocket[i].getSuit();
	}

	return s;
    }

    public String toString (int[] data) {
	String str = "{";
	for (int i = 0; i < size - 1; i++) {
	    str += data[i] + ", ";
	}
	return str + data[size - 1] + "}";
    }
    
    public String toString (String[] data) {
	String str = "{";
	for (int i = 0; i < size - 1; i++) {
	    str += data[i] + ", ";
	}
	return str + data[size - 1] + "}";
    }

    public String toString () {
	String str = "{";
	for (int i = 0; i < size - 1; i++) {
	    str += pocket[i].toString() + ", ";
	}
	return str + pocket[size - 1].toString() + "}";
    }

    public void msort () { // m for manual merge sort because it's literally just 4 cards for christ's sake
	if (game == 0) {
	    sorts(0,1);
	}
	else if (game == 1) {
	    sorts(0,1); // sorts first half
	    sorts(2,3); // sorts second half
	    sorts(0,2); // swaps if l1 > l2
	    sorts(1,2); // swaps if h1 > l1 
	    sorts(2,3); // sorts second half
	}
    }

    public void sorts (int l, int h) { 
	if (pocket[l].compareTo(pocket[h]) == 1) {
	    swap(l,h);
	}
    }
    
    public void swap (int c1, int c2){
	Card temp = pocket[c1];
	pocket[c1] = pocket[c2];
	pocket[c2] = temp;
    }
    
    public void combos (CommunityCards cc) {
	if (game == 0) {
	    for (int a = 0; a < cc.getCardsIn(); a++) {
		for (int b = a + 1; b < cc.getCardsIn(); b++) {
		    for (int c = b + 1; c < cc.getCardsIn(); c++) {
			Card[] ca = {pocket[0], pocket[1], cc.data()[a], cc.data()[b], cc.data()[c]};
			combos.add(new Hand(ca,""));
		    }
		}
	    }
	}
	if (game == 1) {
	    for (int i = 0; i < 4; i++) {
		for (int j = i + 1; j < 4; j++) {
		    for (int a = 0; a < cc.getCardsIn(); a++) {
			for (int b = a + 1; b < cc.getCardsIn(); b++) {
			    for (int c = b + 1; c < cc.getCardsIn(); c++) {
				Card[] ca = {pocket[i], pocket[j], cc.data()[a], cc.data()[b], cc.data()[c]};
				combos.add(new Hand(ca,""));
			    }
			}
		    }
		}
	    }
	}
    }

    public Hand[] possibilities () {
	Hand[] h = combos.toArray(new Hand[combos.size()]);
	return h;
    }

    public String possibleHands () {
	Hand[] c = possibilities();
	combos.clear();
	String list = "{";
	
	for (int i = 0; i < c.length - 1; i++) {
	    list += c[i] + ", \n";
	}

	return list + c[c.length - 1] + "}";
    }

    public boolean pocketPair () { // e.g. "pocket aces" 
	if (game == 0){
	    return pocket[0].getValue() == pocket[1].getValue();
	}
	else if (game == 1) {
	    for (int i = 0; i < 3; i++) {
		for (int j = i++; j < 4; j++) {
		    if (pocket[i].getValue() == pocket[j].getValue()) {
			return true;
		    }
		}
	    }
	}
	return false; 
    }

    public int distance () {
	if (game == 0) {
	    return Math.abs(values[0] - values[1]);
	}
	else {
	    return 0;
	}
    }

    public int[] distance (int g) {
	int[] d = new int[24];
	if (game == 1) {
	    int index = 0;
	    
	    for (int i = 0; i < 3; i++) {
		for (int j = i++; j < 4; j++) {
		    d[index] = Math.abs(values[i] - values[j]);
		}
	    }
	    return d;
	}
	else {
	    return d;
	}
    }
	

}
