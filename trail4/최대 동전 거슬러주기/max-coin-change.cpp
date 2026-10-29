#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int coin[101];
int dp[10001];

int main() {
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        cin >> coin[i];
    }

    // Please write your code here.
    dp[0] = 0;

    for(int i=1; i<=M; i++){
        dp[i] = -1;
        for(int j=0; j<N; j++){
            if (i<coin[j]) continue;
            if (dp[i-coin[j]] == -1) continue;

            dp[i] = max(dp[i], dp[i-coin[j]] + 1);
        }
    }

    cout << dp[M];

    return 0;
}
