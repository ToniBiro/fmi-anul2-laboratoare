package polimorfism.zoo.carnivor;

public class Pisica extends Carnivor{

    @Override
    public void seHraneste(){
        System.out.println(this + " se hraneste cu " + this.tipHrana);
    }
}
