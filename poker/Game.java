import java.util.*;

public class Game {

    private Deck deck;
    private CommunityCards cc;
    private int game;

    private Player[] players; 
    private int play;

    private int dealer, smallBlind, bigBlind;

    public Game (int type, int p) {
	deck = new Deck();
	cc = new CommunityCards();
	game = type;

	play = p;
	players = new Player[p];

	dealer = 0;
	bigBlind = 1;
	smallBlind = 2;
    }

    public String toString () {
	String str = "";
	return str;
    }

    public String players() {
	String str = "";
	for (int i = 0; i < play; i++) {
	    str += players[i] + "\n";
	}
	return str;
    }

    public String revealAll() {
	String str = "";
	for (int i = 0; i < play; i++) {
	    str += players[i].end() + "\n";
	}
	return str;
    }
    
    public void dealAll () {
	for (int i = 0; i < play; i++) {
	    players[i] = new Player ("" + i, deck.deal(game), game);
	}
    }

    public static void main(String[]args) {

	/*
	Scanner scan = new Scanner(System.in);

	
	System.out.println("SIMULATION (S) OR CALCULATIONS (C)");

	String simorcalc = scan.nextLine();
	System.out.println(simorcalc);

	int players = scan.nextInt();
	Game g = new Game(players);
	*/

	Game g = new Game(1, 4);

	System.out.println("THE GAME WILL NOW BEGIN");

	g.dealAll();
	System.out.println("ALL PLAYERS HAVE BEEN DEALT CARDS, BETTING WILL NOW BEGIN");

	System.out.println(g.players());
	
	System.out.println(g.players[0].getP());
	
	g.cc.dealt(g.deck.drawF());
	g.cc.dealt(g.deck.drawF());
	g.cc.dealt(g.deck.drawF());
	
	System.out.println(g.cc.toString() + "\n");
	
	System.out.println(g.players[0].getP());
	//g.players[0].getPocket().combos(g.cc);
	//System.out.println(g.players[0].getPocket().possibleHands() + "\n");
	
	g.cc.dealt(g.deck.draw());
	System.out.println(g.cc.toString() + "\n");
	
	//System.out.println(g.players[0].getH());
	//g.players[0].getPocket().combos(g.cc);
	//System.out.println(g.players[0].getPocket().possibleHands() + "\n");
	
	g.cc.dealt(g.deck.draw());
	System.out.println(g.cc.toString() + "\n");
	
	//System.out.println(g.players[0].getH());
	//g.players[0].getPocket().combos(g.cc);
	//System.out.println(g.players[0].getPocket().possibleHands() + "\n");

	System.out.println(g.cc.toString() + "\n");
	System.out.println(g.revealAll());
    }

}
