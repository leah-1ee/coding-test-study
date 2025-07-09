#include <stdio.h>

int main() {
    int sum=0;
    int n;
    scanf("%d", &n);

    for (int i=1; i<=100; i++){
        sum+=i;
        if (sum>=n){
            printf("%d", i);
            break;
        }
    }
    return 0;
}