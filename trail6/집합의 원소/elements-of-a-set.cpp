#include <iostream>

using namespace std;

int n, m;
int query[100000][3];

// 인덱스 x: 현재 노드 번호
// 값 uf[x]: 부모 노드 번호 
int uf[100000] = {0};

// 루트 찾기
int find(int x){
    // 내가 루트면 리턴
    if(uf[x] == x) return x;

    // 내가 루트가 아니면 루트 찾기
    int root_node = find(uf[x]);
    // 내 값을 루트로 업데이트 
    uf[x] = root_node;
    // 루트 리턴 
    return root_node;
}

// 병합
void merge(int x, int y){
    // x, y 루트 찾기
    int X = find(x);
    int Y = find(y);

    // Y가 X의 부모가 됨
    uf[X] = Y;
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> query[i][0] >> query[i][1] >> query[i][2];
    }

    // Please write your code here.
    for(int i=1; i<=n; i++){
        uf[i] = i;
    }

    // 0: merge, 1: find
    for(int i=0; i<m; i++){
        int order = query[i][0];
        int x = query[i][1];
        int y = query[i][2];

        if(order==0) merge(x,y);
        else {
            if(find(x)==find(y)) cout<<"1\n";
            else cout<<"0\n";
        }        
    }

    return 0;
}