#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

set<string> numbers;

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

void dfs(const vector<vector<char>>& grid, int r, int c, int level, string s) {
	if (level == 7) {
		numbers.insert(s);
		return;
	}

	for (int d = 0; d < 4; d++) {
		int nr = r + dr[d];
		int nc = c + dc[d];

		if (nr < 0 || nr >= 4 || nc < 0 || nc >= 4) continue;
		dfs(grid, nr, nc, level + 1, s + grid[nr][nc]);
	}

}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{

		vector<vector<char>> grid(4, vector<char>(4));

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> grid[i][j];
			}
		}

		numbers.clear();

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				string s(1, grid[i][j]);
				dfs(grid, i, j, 1, s);
			}
		}

		cout << "#" << test_case << " " << numbers.size() << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}