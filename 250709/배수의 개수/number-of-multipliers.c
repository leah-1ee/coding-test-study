#include <stdio.h>

int main() {
    int a[10];
    int sum3=0;
    int sum5=0;

    for (int i=0; i<10; i++){
        scanf("%d", &a[i]);
    }

    for(int i=0; i<10; i++){
        if (a[i]%3==0){
            sum3++;
        }
        if (a[i]%5==0){
            sum5++;
        }
    }
    printf("%d %d", sum3, sum5);
    return 0;
}