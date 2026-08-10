#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std; 

int len;
int homeR, homeC;
 
void dfs(
	const vector<pair<int, int>>& costomers,
	vector<bool>& visited,
	int depth,
	int curLen,
	int preR,
	int preC
) {
	if (curLen > len) return;

	if (depth == costomers.size()) {
		curLen += (abs(homeR - preR) + abs(homeC - preC));
		len = min(len, curLen);
	}

	for (int i = 0; i < costomers.size(); i++) {
		if (visited[i] == true) continue;

		visited[i] = true;
		int r = costomers[i].first;
		int c = costomers[i].second;

		int temp = abs(r - preR) + abs(c - preC);

		dfs(costomers, visited, depth + 1, curLen + temp, r, c);

		visited[i] = false;
	}

}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		len = INT_MAX;

		int n;
		cin >> n;

		int workR, workC;
		cin >> workR >> workC >> homeR >> homeC;

		vector<pair<int, int>> costomers(n);
		for (int i = 0; i < n; i++) {
			cin >> costomers[i].first >> costomers[i].second;
		}

		vector<bool> visited(n, false);
		
		dfs(costomers, visited, 0, 0, workR, workC);

		cout << "#" << test_case << " " << len << "\n";
	}
	return 0;
}