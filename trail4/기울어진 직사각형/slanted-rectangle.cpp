#include <iostream>
#include <algorithm>

using namespace std;

int n;
int grid[20][20];

// 우상 좌상 좌하 우하
int dr[4] = {-1,-1,1,1};
int dc[4] = {1,-1,-1,1};

int canDrawRect(int r, int c, int a, int b){
    int step[4] = {a,b,a,b};
    int sum = 0;

    for(int d=0; d<4; d++){
        for(int i=0; i<step[d]; i++){
            r+=dr[d];
            c+=dc[d];
            if(r<0||r>=n||c<0||c>=n) return -1;
            sum+=grid[r][c];
        }
    }
    return sum;
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.
    int maxSum = 0;

    for(int r=0; r<n; r++){
        for(int c=0; c<n; c++){
            for(int a=1; a<n; a++){
                for(int b=1; b<n; b++){
                    int sum = canDrawRect(r,c,a,b);
                    if(sum != -1) maxSum = max(maxSum, sum);
                }
            }
        }
    }

    cout<<maxSum;

    return 0;
}
