#include <stdio.h>

int main() {
    int cnt = 0;
    int mat[4][4];

    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            scanf("%d", &mat[i][j]);
        }
    }

    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            if (mat[i][j] % 5 == 0){
                cnt++;
            }
        }
    }

    printf("%d", cnt);
    return 0;
}