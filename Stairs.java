import java.math.*;


public class Stairs{
  public static void main(String args[]){
    BigInteger[] results = new BigInteger[22001];
    results[1].valueOf(1);
    System.out.print(results[1]);
  }
}
// int main(void){
//   // printf("start");  
//   long long results[22001];
//   results[1] = 1;
//   results[2] = 2;
//   for (int i = 3; i < 22001 ;i++){
//     results[i] = results[i-1] + results[i-2];
//   }

//   printf("%lld\n", results[10000]);
//   int t;
//   int steps;
//   scanf("%d", &t);
//   for(int i = 0; i < t; i++){
//     scanf("%d", &steps);
//     printf("%lld\n", results[steps]);
//   }
// }