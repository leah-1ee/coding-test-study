#include <iostream>
#include <algorithm>

using namespace std;

int n;
int sequence[1001];

int up[1001];
int down[1001];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> sequence[i];
    }

    // Please write your code here.

    for (int i=0; i<n; i++){
        up[i] = 1;

        for(int j=0; j<i; j++){
            if(sequence[j] >= sequence[i]) continue;
            up[i] = max(up[i], up[j]+1);
        }
    }

    for(int i=n-1; i>=0; i--){
        down[i] = 1;

        for(int j=i+1; j<n; j++){
            if(sequence[j] >= sequence[i]) continue;
            down[i] = max(down[i], down[j]+1);
        }
    }

    int ans = 0;
    for(int i=0; i<n; i++){
        ans = max(ans, up[i]+down[i]-1);
    }

    cout<<ans;


    return 0;
}
