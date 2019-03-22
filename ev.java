
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
if(la>0)
{
 
 if(la%2==0)
{
System.out.println("Even");
}
else 
{
System.out.println("Odd");
}
}
else
{
   System.out.println("Invalid"); 
}


}
catch (NumberFormatException e)
{
    System.out.println("Invalid");
    
}

}
}
