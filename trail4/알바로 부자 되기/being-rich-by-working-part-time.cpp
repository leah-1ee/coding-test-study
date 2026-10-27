#include <iostream>
#include <algorithm>

using namespace std;

int N;
int s[1001], e[1001], p[1001];
int dp[1001];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> s[i] >> e[i] >> p[i];
    }

    // Please write your code here.
    int ans = 0;

    for (int i=0; i<N; i++){
        dp[i] = p[i];

        for (int j=0; j<i; j++){
            if(e[j] >= s[i]) continue;
            dp[i] = max(dp[i], dp[j] + p[i]);
        }

        ans = max(ans, dp[i]);
    }

    cout << ans;

    return 0;
}
