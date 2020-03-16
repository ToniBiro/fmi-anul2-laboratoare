package polimorfism.zoo.carnivor;

public class Leu extends Carnivor{

    public Leu(){
        super();
    }

    sunetSpecific = "urla";

    @Override
    public void seHraneste(){
        System.out.println(this + " se hraneste cu " + this.tipHrana);
    }

    @Override
    public void scoateSunet() {
        System.out.println("Leul " + this.sunetSpecific);
    }
}