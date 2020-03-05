package lab2;

public class Arrays {
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
        
    }
}
