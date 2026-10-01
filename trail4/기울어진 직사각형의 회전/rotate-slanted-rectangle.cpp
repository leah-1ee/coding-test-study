#include <iostream>
#include <vector>

using namespace std;

int n;
int grid[100][100];
int r, c, m1, m2, m3, m4, dir;

vector<pair<int, int>> pos;
vector<int> vals;

// 반시계: 우상 좌상 좌하 우하 
int dr[4] = {-1, -1, 1, 1};
int dc[4] = {1, -1, -1, 1};

// 좌표 모으기
void collectPos() {
    int length[4] = {m1, m2, m3, m4};

    for(int l=0; l<4; l++){
        for(int i=0; i<length[l]; i++){
            pos.push_back({r, c});
            r += dr[l];
            c += dc[l];
        }
    }
}

// 값 모으기
void collectVals() {
    for(int i=0; i<pos.size(); i++){
        int a = pos[i].first;
        int b = pos[i].second;
        vals.push_back(grid[a][b]);
    }
}


// 값 이동
void moveVals() {
    if(dir==0){
        int last = vals.back();
        for(int i=vals.size()-1; i>=1; i--){
            vals[i] = vals[i-1];
        }
        vals[0] = last;
    }

    if(dir==1){
        int start = vals[0];
        for(int i=0; i<vals.size()-1; i++){
            vals[i] = vals[i+1];
        }
        vals.back() = start;
    }
}


// grid 반영
void setGrid() {
    for(int i=0; i<pos.size(); i++){
        int a = pos[i].first;
        int b = pos[i].second;

        grid[a][b] = vals[i];
    }
}

// 출력
void printGrid() {
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout<<grid[i][j]<<" ";
        }
        cout<<"\n";
    }
}



int main() {
    cin >> n;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> grid[i][j];

    cin >> r >> c >> m1 >> m2 >> m3 >> m4 >> dir;
    r--; c--;

    // Please write your code here.
    collectPos();
    collectVals();
    moveVals();
    setGrid();
    printGrid();

    return 0;
}
