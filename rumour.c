#include <stdio.h>



int main(void){
  int t;
  int a, b;
  int count;
  scanf("%d", &t);
  for(int i = 0; i < t; i++){
    count = 0;
    scanf("%d %d", &a, &b);
    while(a != b){
      if(a > b){
        a = a>>1;
        count = count + 1;
      }
      if(a < b){
        b = b>>1;
        count = count + 1;
      }
    }
    printf("%d\n", count);
  }
}