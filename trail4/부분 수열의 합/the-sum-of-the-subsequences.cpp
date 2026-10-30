#include <iostream>

using namespace std;

int n, m;
int A[100];
bool dp[10001];

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // Please write your code here.
    dp[0] = true;

    for(int j=0; j<n; j++){
        for(int i=m; i>0; i--){

            if(i<A[j]) continue;

            if(dp[i-A[j]] == true) dp[i] = true;
        }
    }


    if(dp[m]) cout<< "Yes"; else cout<<"No";

    return 0;
}
