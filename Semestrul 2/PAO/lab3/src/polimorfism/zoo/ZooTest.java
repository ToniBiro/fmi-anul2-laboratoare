package polimorfism.zoo;

import polimorfism.zoo.carnivor.Leu;
import polimorfism.zoo.carnivor.Pisica;
import polimorfism.zoo.ierbivor.Elefant;

import java.util.Scanner;

//java.lang - importat default

public class ZooTest {
    public static void main(String[] args) {
//        int nrAnimaleZoo = Integer.parseInt(args[0]);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Precizati numarul maxim de animale gazduite la zoo: ");
        int nrAnimaleZoo = scanner.nextInt();
        scanner.close();

        Zoo zooBucuresti = new Zoo(nrAnimaleZoo);
        adaugaAnimaleLaZoo();

        for (int i = 0; i < zooBucuresti.animaleZoo.length; i++){
            Animal animal = zooBucuresti.animaleZoo[i];
            animal.afiseazaDetalii();
            animal.seHraneste();
            animal.scoateSunet();
        }
    }

    public static void adaugaAnimaleLaZoo(Zoo zoo) {

        Leu leu = new Leu("Simba", 7);
        zoo.adaugaAnimal(leu);
        Elefant elefant = new Elefant("Eli", 10);
        zoo.adaugaAnimal(elefant);
        Urs urs = new Urs("Fram", 4);
        zoo.adaugaAnimal(urs);
        Pisica pisica = new Pisica("Tom", 2);
        zoo.adaugaAnimal(pisica);
        Caine caine = new Caine("Toto", 3);
        zoo.adaugaAnimal(caine);
        Cal cal = new Cal("Thunder", 3);
        zoo.adaugaAnimal(cal);

    }
}
