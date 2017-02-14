#include<stdio.h>

int calc_first_arg(int number_1, int number_2){
    while (number_2 < 10){
        int multiple = number_1 * number_2;
        printf("%dx%d=%d\n", number_1, number_2, multiple);
        number_2 = number_2 + 1;
    }
}

int main(){

    int a = 1;
    int b = 1;

    while (a < 10){
        calc_first_arg(a, b);
        a = a + 1;
    }

    return 0;
}