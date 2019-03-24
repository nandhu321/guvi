import java.util.*; 

class main 
{ 
    static void min(int arr[], int arr_size) 
    { 
       
      int l, r, min_sum, sum, min_l, min_r; 
       
      
      if(arr_size < 2) 
      { 
        System.out.println("Invalid Input"); 
        return; 
      } 
       

      min_l = 0; 
      min_r = 1; 
      min_sum = arr[0] + arr[1]; 
       
      for(l = 0; l < arr_size - 1; l++) 
      { 
        for(r = l+1; r < arr_size; r++) 
        { 
          sum = arr[l] + arr[r]; 
          if(Math.abs(min_sum) > Math.abs(sum)) 
          { 
            min_sum = sum; 
            min_l = l; 
            min_r = r; 
          } 
        } 
      } 
       
      System.out.println( arr[min_l]+" "+arr[min_r]); 
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
