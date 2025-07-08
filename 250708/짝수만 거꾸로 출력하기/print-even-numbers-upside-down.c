#include <stdio.h>

int main() {
    int a;
    int num[101];

    scanf("%d", &a);
    
    for (int i=0; i<a; i++){
        scanf("%d", &num[i]);
    }
    for (int i=a-1; i>=0; i--){
        if (num[i]%2==0){
            printf("%d ", num[i]);
        }
    }
    return 0;
    
}