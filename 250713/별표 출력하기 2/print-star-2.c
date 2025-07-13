#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);

    for (int i=a; i>0; i--){
        for (int k=0; k<i; k++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}