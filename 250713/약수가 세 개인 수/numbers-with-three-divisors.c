#include <stdio.h>

int main() {
    int s, e;
    int hap=0;

    scanf("%d %d", &s, &e);

    for (int i=s; i<=e; i++){
        int sum=0;
        for(int j=1; j<=i; j++){
            if (i%j == 0){
                sum ++;
            }
        }

        if(sum==3){
            hap ++;
        }
    }
    printf("%d", hap);
    return 0;
}