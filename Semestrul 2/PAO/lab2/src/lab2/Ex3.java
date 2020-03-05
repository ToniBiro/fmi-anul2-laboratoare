package lab2;


import java.util.Arrays;

public class Ex3 {
    public static void main(String[] args){
        int[] ints = new int[]{23, 55, 66, 4};

        System.out.println(ints);
        System.out.println(Arrays.toString(ints));
    }

    int[] ints1 = {2, 3, 4, 5};
    int[] intsCopy = ints1.clone();

    int[] anotherCopy = new int[5];
//    System.arraycopy(intsCopy, 0, anotherCopy, 0, 4);
}
