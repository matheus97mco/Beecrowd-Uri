#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num1, num2,cod1,cod2;
    float valor1,valor2,valorfinal;
    //printf("Informe o codigo, quantidade e valor\n");
    scanf("%d %d %f %d %d %f",&cod1,&num1,&valor1,&cod2,&num2,&valor2);

    valorfinal = (num1*valor1)+(num2*valor2);
    printf("VALOR A PAGAR: R$ %.2f\n",valorfinal);
    return 0;
}
