#include <stdio.h>
#include <stdlib.h>

int main()
{
    double tempo,velocMED;//hrs e km/h
    double litros;
    scanf("%lf\n %lf",&tempo,&velocMED);
    litros = (velocMED*tempo/12);
    //scanf("%.3f",&litros);
    printf("%.3lf\n",litros);
    return 0;
}
