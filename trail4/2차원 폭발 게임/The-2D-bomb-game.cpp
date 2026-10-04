#include <iostream>
#include <vector>

using namespace std;

int N, M, K;
int grid[100][100];

bool findAndErase() {
    bool erased = false;
    for(int c=0; c<N; c++){
        int start = 0;
        while(start < N){
            if(grid[start][c]==0){
                start++;
                continue;
            }
            int end = start+1;
            while(end<N && grid[end][c]== grid[start][c]){
                end++;
            }
            int len = end-start;

            if(len>=M){
                for(int i=start; i<end; i++){
                    grid[i][c] = 0;
                }               
                erased = true;
            }
            start = end;

        }
    }
    return erased;
}

void gravity() {
    for(int c=0; c<N; c++){
        int temp[100] = {0};
        int pt = 0;
        for(int r=N-1; r>=0; r--){
            if(grid[r][c] > 0) {
                temp[pt++] = grid[r][c];
            }
        }
        pt = 0;
        for(int r=N-1; r>=0; r--){
            grid[r][c] = temp[pt++];
        }
    }
}

void explodeAll() {
    while(findAndErase()) gravity();
}

void rotate() {
    int newGrid[100][100];
    for(int r=0; r<N; r++){
        for(int c=0; c<N; c++){
            newGrid[c][N-1-r] = grid[r][c];
        }
    }
    for(int r=0; r<N; r++){
        for(int c=0; c<N; c++){
            grid[r][c] = newGrid[r][c];
        }
    }
}

void countBombs() {
    int cnt = 0;
    for(int r=0; r<N; r++){
        for(int c=0; c<N; c++){
            if(grid[r][c] > 0) cnt++;
        }
    }
    cout << cnt;
}

int main() {
    cin >> N >> M >> K;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.
    for(int i=0; i<K; i++){
        explodeAll();
        rotate();
        gravity();
    }
    explodeAll();

    countBombs();

    return 0;
}
