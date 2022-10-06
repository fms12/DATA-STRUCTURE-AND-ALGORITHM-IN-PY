package com.company;

public class Pattern9 {

    public static void main(String[] args) {
    /*  * * * * *
        * * * *
        * * *
        * *
        *
     */
    int row = 3;
    int column = 3;

    for (int i = 0 ; i <=row ; i++)
    {
        for (int j=0 ; j<=(column-i); j++ )
        {
            System.out.print("* ");
        }
       System.out.println("");
    }



    }
}
