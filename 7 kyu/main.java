// Beginner Series #3 Sum of Numbers
public class Sum
{
   public int GetSum(int a, int b)
     
   {
    
    if (a==b){
          return a;
      }
    if(a>b){
        int c = a;
        a = b;
        b = c;
          
      }
      int c=0;
      for (int i=a; i<=b;i++){
        c+=i;
      
      }
      return c;
   }
}

// Cats and shelves
public class Kata 
{
  public static int solution(int start, int finish)
  {
    int way = finish-start;
    int i=way/3;
    i+=way%3;
    return i;
  }
}

// 
// 
// 
// 
// 
// 
// 
// 
// 
