#include <stdio.h>

int main() {
    int b=0;
    int sum=0;

    scanf("%d %d", &sum, &b);

    while (sum<=b){
        if (sum%2 != 0){
            printf("%d ", sum);
            sum *= 2;
            
        }
        else if (sum%2 == 0){
            printf("%d ", sum);
            sum += 3;
            
        }
    }
    return 0;
}
    