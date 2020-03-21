package imutabilitate;

import org.omg.PortableInterceptor.ServerRequestInfo;

public final class Persoana {

    private final  int id;
    private final String nume;

    public Persoana(int id, String nume) {
        this.id = id;
        this.nume = nume;
    }

    public int getId() {
        return id;
    }

    public String getNume() {
        return nume;
    }


}
