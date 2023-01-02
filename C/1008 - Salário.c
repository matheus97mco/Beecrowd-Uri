#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num,hrsT;
    float vlr,salario;
    //print("Informe o numero, horas e valor");
    scanf("%d%d%f",&num,&hrsT,&vlr);
    printf("NUMBER = %d\n",num);
    printf("SALARY = U$ %.2f\n",hrsT*vlr);
    return 0;
}
