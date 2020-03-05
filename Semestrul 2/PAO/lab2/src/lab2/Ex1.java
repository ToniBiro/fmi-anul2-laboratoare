package lab2;

public class Ex1 {
    public static void main(String[] args){
        byte[] bytes;
        bytes = new byte[5];
        bytes[0] = -128;
        bytes[4] = 127;

        for (byte i = 0; i < bytes.length; i++){
            System.out.println(bytes[i]);
        }

        short[] shortArray;
        boolean[] booleanArray = new boolean[4];

        int[] ints = new int[]{23, 35, 11, 22};

        int[] anotherintArray = new int[]{23, 55, 66, 4};

//        System.out.println(Ex1.toString(anotherintArray));
//        System.out.println(Ex1(anotherintArray));

        char[] chars = {'j', 'a', 'v', 'a'};

        for (char c : chars){
            System.out.println(c);
        }
        System.out.println(chars);

        int[][] intMatrix = new int[3][3];
        intMatrix[0][0] = 22;
        intMatrix[2][2] = 11;

        for (int i[] : intMatrix){
            for (int j : i){
                System.out.print(j + " ");
            }
            System.out.println();
        }


        int[][] multidim = new int[3][];
        multidim[0] = new int[2];
        multidim[0][0] = 1;
        multidim[0][1] = 2;

        multidim[1] = new int[]{1, 5, 3};
        multidim[2] = new int[]{1, 5, 3};

        displayArrayValues(multidim);
    }

    private static void displayArrayValues(int[][] input){
        for(int[] i : input){
            for (int j : i){
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}
