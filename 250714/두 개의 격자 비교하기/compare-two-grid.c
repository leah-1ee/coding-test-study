#include <stdio.h>

int main() {
    int row, col;
    scanf("%d %d", &row, &col);

    int arr1[row][col];
    int arr2[row][col];
    int result[row][col];

    // 첫 번째 배열 입력
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%d", &arr1[i][j]);
        }
    }

    // 두 번째 배열 입력
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%d", &arr2[i][j]);
        }
    }

    // 비교하여 새로운 배열 생성
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (arr1[i][j] == arr2[i][j]) {
                result[i][j] = 0;
            } else {
                result[i][j] = 1;
            }
        }
    }

    // 결과 출력
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    return 0;
}
