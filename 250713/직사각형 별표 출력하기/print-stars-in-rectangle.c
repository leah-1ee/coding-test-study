#include <stdio.h>

int main() {
    
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i=0; i<n; i++){
        for (int k=0; k<m; k++){
            printf("* ");
        }
        printf("\n");
    }


    return 0;
}