#include <iostream>

using namespace std;

const int MAX_N = 1001;

int N;
int arr[MAX_N];
int dp[MAX_N];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    int ans = 0;

    for(int i=0; i<N; i++){
        dp[i] = 1;

        for(int j=0; j<i; j++){
            if(arr[i] >= arr[j]) continue;

            dp[i] = max(dp[j]+1, dp[i]);
        }

        ans = max(ans, dp[i]);
    }

    cout << ans;

    return 0;
}
