#include <stdio.h>

int main() {
    int pas=25;
    int ans=0;

    while (pas != ans){
        scanf("%d", &ans);
        if (ans > pas){
            printf("Lower\n");
        }
        else if (ans < pas){
            printf("Higher\n");
        }
    }
    printf("Good");
    return 0;
}