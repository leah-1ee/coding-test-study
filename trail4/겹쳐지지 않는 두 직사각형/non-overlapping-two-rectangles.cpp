#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int grid[5][5];

struct Rect {
    int r1, c1, r2, c2;
    int sum;
};

Rect rects[300];
int cnt = 0;

// 모든 사각형 저장
void makeRects() {
    for(int r1=0; r1<n; r1++){
        for(int c1=0; c1<m; c1++){            
            for(int r2=r1; r2<n; r2++){
                for(int c2=c1; c2<m; c2++){

                    int sum = 0;
                    for(int r=r1; r<=r2; r++){
                        for(int c=c1; c<=c2; c++){
                            sum += grid[r][c];
                        }
                    }
                    rects[cnt] = {r1, c1, r2, c2, sum};
                    cnt++;


                }
            }
            
        }
    }
}

bool overlap(int a, int b) {
    if(rects[a].r1 > rects[b].r2) return false;
    if(rects[a].r2 < rects[b].r1) return false;
    if(rects[a].c1 > rects[b].c2) return false;
    if(rects[a].c2 < rects[b].c1) return false;

    return true;
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.
    makeRects();

    int maxSum = -1e9;

    // 두 개 뽑기
    for(int i=0; i<cnt; i++){
        for(int j=i+1; j<cnt; j++){
            // 겹치는지 확인
            if(overlap(i, j)) continue;

            maxSum = max(maxSum, rects[i].sum + rects[j].sum);
        }
    }

    cout<<maxSum;

    return 0;
}
