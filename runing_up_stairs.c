#include <stdio.h>



int main(void){
  // printf("start");  
  long long results[22000];
  results[1] = 1;
  results[2] = 2;
  for (int i = 3; i < 22001 ;i++){
    results[i] = results[i-1] + results[i-2];
    if(results[i] < 0){
      printf("current i: %d\n", i);
      break;
    }
  }

  printf("%lld\n", results[10000]);
  int t;
  int steps;
  scanf("%d", &t);
  for(int i = 0; i < t; i++){
    scanf("%d", &steps);
    printf("%lld\n", results[steps]);
  }
}