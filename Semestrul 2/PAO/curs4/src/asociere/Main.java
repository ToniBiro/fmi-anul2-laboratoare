package asociere;

public class Main {
    public static void main(String[] args) {
        Profesor profesorPrincipalMate = new Profesor(1, "Popescu");
        Profesor profesorSecundarMate = new Profesor(2, "Ionescu");
        Profesor profesorInfo = new Profesor(3, "Anghel");
        Profesor profesorMateSiInfo = new Profesor(4, "Petrescu");
        Profesor profesorInfoSiMate = new Profesor(5, "Andrei");

        Departament departamentInfo = new Departament("info");
        departamentInfo .setProfesori(new Profesor[]{profesorInfo, profesorInfoSiMate, profesorMateSiInfo});
        Departament departamentMate = new Departament("mate");
        departamentMate.setProfesori(new Profesor[]{profesorPrincipalMate, profesorSecundarMate,profesorInfoSiMate, profesorMateSiInfo});

        Universitate unibuc = new Universitate("UNIBUC", new Departament[]{departamentInfo, departamentMate});

        departamentInfo = null;
        System.out.println(unibuc);

        System.out.println(departamentMate);
        profesorSecundarMate = null;

        departamentMate.getProfesori()[1] = null;
        System.out.println(departamentMate);
        System.out.println(profesorSecundarMate);
    }
}
