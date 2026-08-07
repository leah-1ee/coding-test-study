#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int day, oneMonth, threeMonth, year;
int minPrice;

void dfs(const vector<int>& swim, int curMonth, int price) {
	if (curMonth >= 12) {
		minPrice = min(minPrice, price);
		return;
	}

	if (swim[curMonth] == 0) dfs(swim, curMonth + 1, price);

	dfs(swim, curMonth + 1, price + (swim[curMonth] * day));
	dfs(swim, curMonth + 1, price + oneMonth);
	dfs(swim, curMonth + 3, price + threeMonth);

}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{

		
		cin >> day >> oneMonth >> threeMonth >> year;
		minPrice = INT32_MAX;

		vector<int> swim(12);
		for (int i = 0; i < 12; i++) {
			cin >> swim[i];
		}

		dfs(swim, 0, 0);
		
		minPrice = min(minPrice, year);


		cout << "#" << test_case << " " << minPrice << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}