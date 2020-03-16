package polimorfism.zoo;

public abstract class Animal {
    private int nrIdentificare;
    private String nume;
    private int varsta;
    protected String tipHrana;
    protected String sunetSpecific;
s
    public Animal(String nume, int varsta){
        nrIndentificare = hashCode();
        this.nume = nume;
        this varsta = varsta;
    }

    public abstract void seHraneste();
    public abstract void scoateSunet();

    public void afiseazaDetalii(){
        System.out.println("Acesta este " + this.toString());
    }

    @Override
    public String toString(){
        return "Animal din categoria " +this.getClass().getSuperclass().getSimpleName() +
                ", din specia " +
    }
}
