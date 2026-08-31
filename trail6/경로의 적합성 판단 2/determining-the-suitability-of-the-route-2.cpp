#include <iostream>

using namespace std;

// 정점 간선 순서길이
int n, m, k;
int from[100000], to[100000];
int path[100000];

int uf[100000] = {0};

int find(int x){
    if(uf[x]==x) return x;
    int rootNode = find(uf[x]);
    uf[x] = rootNode;
    return rootNode;
}

void merge(int x, int y){
    int X = find(x);
    int Y = find(y);

    uf[X] = Y;
}

int main() {
    cin >> n >> m >> k;

    for (int i = 0; i < m; i++) {
        cin >> from[i] >> to[i];
    }

    for (int i = 0; i < k; i++) {
        cin >> path[i];
    }

    // Please write your code here.
    for(int i=1; i<=n; i++){
        uf[i] = i;
    }

    for(int i=0; i<m; i++){
        merge(from[i], to[i]);
    }

    for(int i=1; i<k; i++){
        if(find(path[i-1]) != find(path[i])) {
            cout<<0;
            return 0;
        }
    }

    cout<<1;

    return 0;
}