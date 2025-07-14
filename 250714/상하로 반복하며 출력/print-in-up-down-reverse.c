#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int mat[n][n];

    // 배열 채우기
    for (int col = 0; col < n; col++) {
        if (col % 2 == 0) { // 짝수 열: 위 → 아래
            for (int row = 0; row < n; row++) {
                mat[row][col] = (row % n) + 1;
            }
        } else { // 홀수 열: 아래 → 위
            for (int row = n - 1; row >= 0; row--) {
                mat[n - 1 - row][col] = (row % n) + 1;
            }
        }
    }

    // 배열 출력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d", mat[i][j]);
        }
        printf("\n");
    }

    return 0;
}
