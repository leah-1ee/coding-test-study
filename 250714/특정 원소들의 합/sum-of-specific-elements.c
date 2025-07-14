#include <stdio.h>

int main() {
    int mat[4][4];
    int cnt=0;

    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            scanf("%d", &mat[i][j]);
        }
    }

    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            if (i >= j){
                cnt += mat[i][j];
            }
        }
    }
    printf("%d", cnt);
    return 0;
}