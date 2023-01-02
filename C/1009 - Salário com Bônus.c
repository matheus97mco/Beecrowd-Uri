#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char nome[50];
    double salarioFixo, montanteTotal,total;
    //printf("Nome\n");
    //printf("Salario\n");
    //printf("Vendas\n");
    gets(nome);
    scanf("%lf",&salarioFixo);
    scanf("%lf",&montanteTotal);

    total = salarioFixo + (montanteTotal*0.15);

    printf("TOTAL = R$ %.2lf\n",total);
    return 0;
}