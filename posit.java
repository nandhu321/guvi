import java.util.*; 

class main 
{ 
   static void min(int arr[],int n)
   {
       int count=2;
       
       for(int i=0;i<n;i++)
       {
      if(i%2==0&&arr[i]%2!=0)
      {
		System.out.print(arr[i]);
      }
		else if(i%2!=0&&arr[i]%2==0)
                {
		System.out.print(" "+arr[i]+" ");
                }
       }
       
   }
    
    public static void main (String[] args)  
    { 
        int n;
        int [] arr= new int[50];
        Scanner sc= new Scanner(System.in);
        n=sc.nextInt();
        for (int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
                
        }
        min(arr, n); 
    } 
}
    
