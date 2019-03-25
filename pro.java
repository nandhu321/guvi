import java.util.*;
public class Main
{
	public static void main(String[] args) {
   int n1,n2;
   Scanner sc =new Scanner(System.in);
   n1=sc.nextInt();
   n2=sc.nextInt();
   int i,j, num,p, count = 0;
   for(i=n1;i<=n2;i++)
   {
       p=0;
       for(j=1; j<=i; j++)
       {
           if(i%j==0)
           {
               p++;
           }
        }
        if(p==2)
        {
           System.out.print(" "+i);
        }
   }
}
}
