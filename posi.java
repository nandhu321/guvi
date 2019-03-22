
import java.util.*;
import java.io.*;
class Main
{
public static void main(String args[])
{
 String l;
 int la;
 Scanner sc=new Scanner(System.in);
 l=sc.next();
 
 try 
 {
la=Integer.parseInt(l);
 if(la<0)
{
System.out.println("Negative");
}
else if(la>0)
{
System.out.println("Positive");
}
else 
{
System.out.println("Zero");
}
}
catch (NumberFormatException e)
{
    System.out.println("Invalid Input");
    
}

}
}
