#include <stdio.h>
#include <stdlib.h>


int main()
{
    double raio,volume;
    //printf("raio:\n");
    scanf("%lf", &raio);
    volume = 4/3.0*3.14159*raio*raio*raio;
    printf("VOLUME = %.3lf\n",volume);
    return 0;
}
