#include <iostream>

using namespace std;

int n, m;
char op;
int a, b;

int uf[100001] = {0};
int cnt[100001] = {1};

int find(int x){
    if(uf[x]==x) return x;
    int rootNode = find(uf[x]);
    uf[x] = rootNode;
    return rootNode;
}

void merge(int x, int y){
    int X = find(x);
    int Y = find(y);

    if(X==Y) return;

    uf[X] = Y;
    cnt[Y] += cnt[X];
}

int main() {
    cin >> n >> m;
    for(int i=1; i<=n; i++){
        uf[i] = i;
        cnt[i] = 1;
    }

    for (int i = 0; i < m; i++) {
        cin >> op;
        if (op == 'x') {
            cin >> a >> b;
            merge(a,b);
        } else {
            cin >> a;
            cout<<cnt[find(a)]<<"\n";
        }
    }

    // Please write your code here.
    

    return 0;
}