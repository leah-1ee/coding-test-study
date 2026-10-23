#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[1001];
int dp[1001];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    int ans = 0;

    dp[0] = 0;
    
    for(int i=1; i<n; i++){
        dp[i] = -1;

        for(int j=0; j<i; j++){
            if(dp[j] == -1) continue;
            if(arr[j] < i-j) continue;

            dp[i] = max(dp[i], dp[j]+1);
        }
        
        ans = max(ans, dp[i]);
    }

    cout << ans;

    return 0;
}
