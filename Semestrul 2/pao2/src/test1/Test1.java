package test1;

public class Test1 {

    static char defaultChar;
    static double defaultDouble;

    public static void main(String[] args) {

        // char primitive

        System.out.println(Character.MIN_VALUE + 0); // '\u0000' in Unicode, not printable
        System.out.println(Character.MAX_VALUE + 0); // '\uffff' in Unicode
        System.out.println((int)defaultChar); // '\u0000' in Unicode

        // double primitive

        double d1 = 555; // int literal
        System.out.println(d1);

        double d2 = 123_456_789_000L; // long literal
        System.out.println(d2);

        double d3 = 123.4f; // float literal
        System.out.println(d3);

        double d4 = 12345.6d; // double literal, D or d is optional
        System.out.println(d4);

        double d5 = 1.23456e4D; // same value as d4, in scientific notation
        System.out.println(d5);

        System.out.println(defaultDouble);

        // long primitive

        long l1 = 1223343534;
        long l2 = 1223343534;  // if the literal ends with "L" or "l", it's a long, otherwise int
        System.out.println("l1 = " + l1);
        System.out.println("l2 = " + l2);
        long l3, l4;
        System.out.println(l3 = l4 = -0b1010101101010L);


    }
}
