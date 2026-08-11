#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int d, w, k;
vector<vector<int>> grid;
vector<vector<int>> temp;
int bestInput;

bool test() {
	for (int i = 0; i < w; i++) {
		int film = 1;
		bool ok = false;

		for (int j = 1; j < d; j++) {
			if (temp[j][i] == temp[j - 1][i]) film++;
			else film = 1;
			if (film >= k) {
				ok = true;
				break;
			}
		}
		if (!ok) return false;
		
	}
	return true;
}

void dfs(int curInput, int start) {	

	if (curInput > bestInput) return;

	if (test()) {
		bestInput = min(bestInput, curInput);
		return;
	}

	for (int i = start; i < d; i++) {
		// A
		for (int j = 0; j < w; j++)
			temp[i][j] = 0;

		dfs(curInput + 1, i+1);

		for (int j = 0; j < w; j++)
			temp[i][j] = grid[i][j];

		// B
		for (int j = 0; j < w; j++)
			temp[i][j] = 1;

		dfs(curInput + 1, i+1);

		for (int j = 0; j < w; j++)
			temp[i][j] = grid[i][j];

		
	}
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


		// 0 = A, 1 = B
		for (int i = 0; i < d; i++) {
			for (int j = 0; j < w; j++) {
				cin >> grid[i][j];
			}
		}

		temp = grid;

		bestInput = k;


		dfs(0, 0);

		cout << "#" << test_case << " " << bestInput << "\n";

	}
	return 0;
}