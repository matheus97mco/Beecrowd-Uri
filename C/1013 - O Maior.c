#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A,B,C,maiorAB,maiorABC;
    //printf("numeros:\n");
    scanf("%d %d %d",&A,&B,&C);
    maiorAB = (A+B+abs(A-B))/2;
    maiorABC = (maiorAB+C+abs(maiorAB-C))/2;
    printf("%d eh o maior\n",maiorABC);
    return 0;
}
