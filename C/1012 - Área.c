#include <stdio.h>
#include <stdlib.h>


int main()
{
    double A,B,C,triang,circ,trap,quadr,retan;
    scanf("%lf %lf %lf",&A,&B,&C);
    triang = A*C/2;
    circ = 3.14159*C*C;
    trap = C*(A+B)/2;
    quadr = B*B;
    retan = A*B;
    printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n",triang,circ,trap,quadr,retan);
}
