#include <stdio.h>

int main() {
    int row, col;
    int mat[3][3];

    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            scanf("%d", &mat[i][j]);
        }
    }

    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            mat[i][j] = mat[i][j] * 3;
        }
    }

    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            printf("%d ", mat[i][j]);
        }
    printf("\n");
    }

    return 0;
}