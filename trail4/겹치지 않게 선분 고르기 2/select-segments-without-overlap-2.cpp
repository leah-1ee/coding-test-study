#include <iostream>
#include <algorithm>

using namespace std;

int n;
pair<int, int> lines[1001];
int dp[1001];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> lines[i].first >> lines[i].second;
    }

    // Please write your code here.
    int ans = 0;

    sort(lines, lines+n);

    for(int i=0; i<n; i++){
        dp[i] = 1;

        for(int j=0; j<i; j++){
            if(lines[j].second >= lines[i].first) continue;

            dp[i] = max(dp[i], dp[j] + 1);
        }

        ans = max(ans, dp[i]);
    }

    cout << ans;

    return 0;
}
