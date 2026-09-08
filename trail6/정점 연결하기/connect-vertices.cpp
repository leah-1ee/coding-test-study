#include <iostream>

using namespace std;

int n;
int from[100000], to[100000];

// 부모 노드 저장
int uf[100001];

int find(int x){
    if(uf[x] == x) return x;

    int root = find(uf[x]);
    uf[x] = root;
    return root;
}

void merge(int x, int y){
    int rootX = find(x);
    int rootY = find(y);

    uf[rootX] = rootY;
}

int main() {
    cin >> n;
    for (int i = 0; i < n - 2; i++) {
        cin >> from[i] >> to[i];
    }

    // Please write your code here.

    for(int i=0; i<=n; i++){
        uf[i] = i;
    }

    for(int i=0; i< n - 2; i++){
        merge(from[i], to[i]);
    }

    for(int i=1; i<n; i++){
        if(find(i)!=find(i+1)) {
            cout<<1<<" "<<i+1;
            break;
        } 
    }


    return 0;
}