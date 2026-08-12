#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int s1R, s1C, s1K, s2R, s2C, s2K;
vector<pair<int, int>> people;
int minTime;

// 계단까지의 거리
vector<int> group1, group2;

int calTime(int num) {
	int k;
	vector<int> grp;

	if (num == 1) { k = s1K; grp = group1; }
	else { k = s2K; grp = group2; }

	if (grp.empty()) return 0;

	sort(grp.begin(), grp.end());

	int slots[3] = { 0, 0, 0 };
	int finish = 0;

	for (int a : grp) {
		sort(slots, slots + 3);

		int start = max(a, slots[0]);
		int end = start + k;

		slots[0] = end;
		finish = max(finish, end);
	}
	return finish;
}

int distance(int d, int num) {
	if (num == 1) return abs(people[d].first - s1R) + abs(people[d].second - s1C) + 1;
	return abs(people[d].first - s2R) + abs(people[d].second - s2C) + 1;
}

void dfs(int depth) {

	if (depth == people.size()) {
		// 그룹 별 시간 계산, 큰 것을 취함 
		int t1 = calTime(1);
		int t2 = calTime(2);

		minTime = min(minTime, max(t1, t2));
		return;
	}

	int dist1 = distance(depth, 1);
	int dist2 = distance(depth, 2);

	// 계단 1 선택
	group1.push_back(dist1);
	dfs(depth + 1);
	group1.pop_back();

	// 계단 2 선택
	group2.push_back(dist2);
	dfs(depth + 1);
	group2.pop_back();

}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		people.clear();
		minTime = INT_MAX;

		// 입력받기
		int n;
		cin >> n;

		bool first = false;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int a;
				cin >> a;
				if (a == 1) people.push_back({ i, j });
				if (a > 1) {
					if (!first) {
						s1R = i;
						s1C = j;
						s1K = a;
						first = true;
					}
					else {
						s2R = i;
						s2C = j;
						s2K = a;
					}
				}
			}
		}

		// dfs 
		dfs(0);

		cout << "#" << test_case << " " << minTime << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}