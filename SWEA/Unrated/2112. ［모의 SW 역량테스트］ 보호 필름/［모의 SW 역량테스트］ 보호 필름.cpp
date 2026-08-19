#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int d, w, k;
vector<vector<int>> grid;
vector<vector<int>> temp;
int bestInput;

bool test() {
	for (int i = 0; i < w; i++) {
		int streak = 1;
		for (int j = 1; j < d; j++) {
			if (streak >= k) break;
			if (temp[j][i] == temp[j - 1][i]) streak++;
			else streak = 1;
		}
		if (streak >= k) continue;
		return false;
	}
	return true;
}

void dfs(int input, int depth) {
	if (input >= bestInput) return;

	if (test()) {
		bestInput = min(bestInput, input);
		return;
	}

	if (depth == d)
		return;

	for (int i = 0; i < w; i++) {
		temp[depth][i] = 0;
	}
	dfs(input + 1, depth + 1);
	for (int i = 0; i < w; i++) {
		temp[depth][i] = grid[depth][i];
	}
		

	for (int i = 0; i < w; i++) {
		temp[depth][i] = 1;
	}
	dfs(input + 1, depth + 1);
	for (int i = 0; i < w; i++) {
		temp[depth][i] = grid[depth][i];
	}
	

	dfs(input, depth + 1);
}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> d >> w >> k;
		grid.assign(d, vector<int>(w));
		for (auto& row : grid) {
			for (auto& v : row) {
				cin >> v;
			}
		}

		temp = grid;

		bestInput = INT_MAX;
		dfs(0, 0);

		cout << "#" << test_case << " " << bestInput << "\n";
	}
	return 0;
}