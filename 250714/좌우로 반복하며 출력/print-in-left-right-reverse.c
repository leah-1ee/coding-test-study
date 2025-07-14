#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    int mat[a][a];

    // 1. 배열 초기화
    for (int i=0; i<a; i++){
        for (int j=0; j<a; j++){
            mat[i][j] = j+1;
        }
    }

    // 2. 지그재그 출력
    for (int i=0; i<a; i++){
        if (i % 2 != 0){  
            for (int j=a-1; j>=0; j--){
                printf("%d", mat[i][j]);
            }
        }
        else {           
            for (int j=0; j<a; j++){
                printf("%d", mat[i][j]);
            }
        }
        printf("\n");
    }

    return 0;
}
