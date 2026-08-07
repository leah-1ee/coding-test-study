#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {

	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; ++test_case) {

		int dayCost, monthCost, threeCost, yearCost;
		cin >> dayCost >> monthCost >> threeCost >> yearCost;

		vector<int> plan(13);

		for (int i = 1; i < 13; i++) {
			cin >> plan[i];
		}

		vector<int> dp(13, 0);

		for (int i = 1; i < 13; i++) {
			int useDay = dp[i - 1] + plan[i] * dayCost;
			int useMonth = dp[i - 1] + monthCost;

			dp[i] = min(useDay, useMonth);

			if (i >= 3) {
				dp[i] = min(dp[i], dp[i - 3] + threeCost);
			}
		}

		int answer = min(dp[12], yearCost);

		cout << "#" << test_case << " " << answer << "\n";

	}

	return 0;
}