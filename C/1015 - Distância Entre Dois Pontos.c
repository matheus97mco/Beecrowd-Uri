#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    float X1,Y1,X2,Y2,distancia;
    scanf("%f %f\n %f %f",&X1,&Y1,&X2,&Y2);
    distancia = sqrt((X2-X1)*(X2-X1)+(Y2-Y1)*(Y2-Y1));
    printf("%.4f\n",distancia);
    return 0;
}
