#include <iostream>
#include <algorithm>

using namespace std;

int n, k;
int arr[502][502];
int prefix_sum[502][502] = {};

int main() {
    cin >> n >> k;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> arr[i][j];
        }
    }

    // Please write your code here.

    // 누적합 배열 만들기
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + arr[i][j];
        }
    }

    // k x k 탐색
    int maxSum = 0;

    for(int i=1; i<=n-k+1; i++){
        for(int j=1; j<=n-k+1; j++){
            int maxK = prefix_sum[i+k-1][j+k-1] - prefix_sum[i-1][j+k-1] - prefix_sum[i+k-1][j-1] + prefix_sum[i-1][j-1];
            maxSum = max(maxK, maxSum);
        }
    }

    cout<<maxSum;

    return 0;
}
