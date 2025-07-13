#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);

    for (int i=1; i<=a; i++){
        for (int j=1; j<=a; j++){
            printf("%d * %d = %d", i, j, i*j);
            if (j%a != 0){
                printf(", ");
            }
        }
        printf("\n");
    }
    return 0;
}