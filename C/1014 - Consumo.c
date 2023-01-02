#include <stdio.h>
#include <stdlib.h>

int main()
{
    int X; //dist percor
    float Y,media;//combust gasto = Y
    scanf("%d",&X);
    scanf("%f",&Y);
    media = X/Y;
    printf("%.3f km/l\n",media);
    return 0;
}
