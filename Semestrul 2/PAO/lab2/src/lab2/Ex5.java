package lab2;

import java.util.Arrays;

public class Ex5 {
    public static void main(String[] args){
        int[][] ints = new int[2][];
        ints[0] = new int[]{3, 4, 5};
        ints[1] = new int[]{1, 2, 3, 4, 5};

        System.out.println(Arrays.toString(ints));
        System.out.println(Arrays.deepToString(ints));
        System.out.println(Arrays.deepHashCode(ints));
        System.out.println(Arrays.hashCode(ints));
    }
}
