#include <stdio.h>

int main() {
    int num[4][4];
    int hap;

    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            scanf("%d", &num[i][j]);
        }
    }

    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            hap += num[i][j];
        }
    printf("%d\n", hap);
    hap = 0;
    }

    return 0;
}