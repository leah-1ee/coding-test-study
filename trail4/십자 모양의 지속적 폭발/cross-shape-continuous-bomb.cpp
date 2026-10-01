#include <iostream>
#include <vector>

using namespace std;

int n, m;
int grid[200][200];
int bomb_cols[15];

int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};

int findBomb(int c) {
    for(int r=0; r<n; r++){
        if(grid[r][c] > 0){
            return r;
        }
    }
    return -1;
}

void eraseBomb(int r, int c) {
    int k = grid[r][c];
    grid[r][c] = 0;

    for(int d=0; d<4; d++){
        for(int i=1; i<k; i++){
            int nr = r+dr[d]*i;
            int nc = c+dc[d]*i;

            if(nr<0 || nr>=n || nc<0 || nc>=n) continue;
            grid[nr][nc] = 0;
        }
    }
}

void gravity() {
    for (int c = 0; c < n; c++) {
        int col[200] = {0};
        int idx = 0;

        for (int r = n - 1; r >= 0; r--) {
            if (grid[r][c] == 0) continue;
            col[idx++] = grid[r][c];
        }

        idx = 0;

        for (int r = n - 1; r >= 0; r--) {
            grid[r][c] = col[idx++];
        }
    }
}

void printGrid() {
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout<<grid[i][j]<<" ";
        }
        cout<<"\n";
    }
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    for (int i = 0; i < m; i++) {
        cin >> bomb_cols[i];
        bomb_cols[i]--;
    }

    // Please write your code here.

    // 열을 순회하며
    // 가장 위 폭탄 찾기, 값 저장 (k)
    // 4방향 k-1칸 제거
    // 각 열에 중력 적용

    for(int i=0; i<m; i++){
        int col = bomb_cols[i];

        int r = findBomb(col);

        // 폭탄 못 찾음
        if(r==-1) continue;

        eraseBomb(r, col);

        gravity();

    }

    printGrid();

    return 0;
}