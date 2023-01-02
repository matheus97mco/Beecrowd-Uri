#include <stdio.h>
#include <stdlib.h>

int main()
{
    double MEDIA,A,B; //notas
    //printf("informe as notas:\n")

    if(A=0||A<10.0)
    {
        scanf("%lf",&A);

        if(B=0||B<10.0)

            scanf("%lf",&B);


        MEDIA = (A*3.5+B*7.5)/(3.5+7.5) ; //3.5 peso A  7.5 peso B = 11
        printf("MEDIA = %.5lf\n",MEDIA);


    }


    return 0;
}
