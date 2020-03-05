package lab2;

import java.util.Arrays;

public class Ex6 {
    public static void main(String[] args){
        int[] ints = {2, 3, 4, 5, 66, 23, 1, -22};
        Arrays.sort(ints);
        System.out.println(Arrays.toString(ints));
        System.out.println(Arrays.binarySearch(ints, 66));
    }
}
