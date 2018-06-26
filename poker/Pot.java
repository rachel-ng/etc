import java.util.*;

public class Pot {

    private int pot;
    private int round;

    private int sidePot;
    private boolean[] sPlayer; 

    private int players;
    private int[] bets;

    private int pBet;
    
    public Pot (int p) {
	players = p;
	
	bets = new int[players];
	for (int i = 0; i < players; i++) {
	    bets[i] = 0;
	}

	pot = 0;
	round = 1;

	pBet = 0;
	
	sidePot = 0;
	sPlayer = new boolean[players];
	for (int i = 0; i < players; i++) {
	    sPlayer[i] = false;
	}
    }

    public void call (int p, int amount) { // add bet
	bets[p] += amount;
	pot += amount;
    }

    public int getPot() {
	return pot;
    }

    public void addSidePot (int p, int amount) {
	sPlayer(p);
	sidePot += amount;
    }

    public int getSidePot() {
	return sidePot;
    }
    
    public void sPlayer (int p) { // player in sidepot
	sPlayer[p] = true;
    }

    public boolean inSP (int p) {
	return sPlayer[p];
    }

    public void raise () {

	
    }
}
