import java.util.*;

public class Player {

    private String name;
    private Pocket pocket;
    
    private int game;
    
    public Player (String n, Pocket p, int g) {
	name = n;
	pocket = p;
	game = g;
    }

    public String toString () {
	String str = "";
	str += name + "\t";
	if (game == 0) {
	    str += "{**,**}";
	}
	if (game == 1) {
	    str += "{**,**,**,**}";
	}
	return str;
    }

    public String end () {
	String str = "";
	str += name + "\t" + getPocket();
	return str;
    }

    public Pocket getPocket () {
	return pocket;
    }
    
    public String getP () {
	return pocket.toString();
    }

}
