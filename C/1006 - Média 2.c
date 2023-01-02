#include <stdio.h>
#include <stdlib.h>

int main()
{
    double MEDIA,A,B,C; //notas
    //printf("informe as notas:\n")

    if(A=0||A<10.0)
    {
        scanf("%lf",&A);
    }

    if(B=0||B<10.0)
    {
        scanf("%lf",&B);
    }
    if(C=0||C<10.0){
        scanf("%lf",&C);
    }

    MEDIA = (A*2+B*3+C*5)/(2+3+5) ; //3+2+5 peso A B C = 10
    printf("MEDIA = %.1lf\n",MEDIA);

    return 0;
}
