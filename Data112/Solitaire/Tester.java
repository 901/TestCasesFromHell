
public class Tester{

    private int [] state;
    public static int indexOf(int [] l, int k){
	for(int i = 0; i < l.length; i++){
	    if(l[i] == k) return i;
	}
	return -1;
    }
    
    public Tester(Solitaire victim){
	this.state = new int[28];

	int i = 0;
	for(CardNode t = victim.deckRear.next; t != victim.cardRear; t = t.next, i++){
	    this.state[i] = t.cardValue;
	}
	this.state[28] = victim.deckRear.cardValue;

	int ja = indexOf(this.state, 27);
	int t = this.state[(ja + 1) % 28];
	this.state[(ja + 1) % 28] = 27;
	this.state[ja] = t;
	ja = (ja + 1) % 28;

	int jb = indexOf(this.state, 28);
	int t = this.state[(jb + 2) % 28];
	this.state[(jb + 2) % 28] = 28;
	this.state[jb] = this.state[(jb + 1) % 28];
	this.state[(jb + 1) % 28] = t;
	jb = (jb + 2) % 28;

	int [] tSt = new int[28];
	int fj = Math.max(ja, jb);
	int lj = Math.min(ja, jb);
	
    }
}
