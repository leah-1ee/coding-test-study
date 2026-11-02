#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int w[101], v[101];
int dp[10001];

int main() {
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        cin >> w[i] >> v[i];
    }

    // Please write your code here. 

    for (int j=0; j<N; j++){
        for(int i=M; i>=0; i--){
            if(i<w[j]) continue;
            dp[i] = max(dp[i], dp[i-w[j]]+v[j]);
        }

    }

    cout << dp[M];

    return 0;
}
