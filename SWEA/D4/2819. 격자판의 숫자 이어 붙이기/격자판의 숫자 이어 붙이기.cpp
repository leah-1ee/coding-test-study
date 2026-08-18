#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;
set<string> numbers;

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

void dfs(const vector<vector<char>>& grid, int depth, string result, int r, int c) {
	if (depth == 7) {
		numbers.insert(result);
		return;
	}

	for (int d = 0; d < 4; d++) {
		int nr = r + dr[d];
		int nc = c + dc[d];

		if (nr < 0 || nr >= 4 || nc < 0 || nc >= 4) continue;
		dfs(grid, depth + 1, result + grid[nr][nc], nr, nc);
	}

}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	

	for (test_case = 1; test_case <= T; ++test_case)
	{
		numbers.clear();

		vector<vector<char>> grid(4, vector<char>(4));
		for (auto &row : grid)
			for (auto &v : row)
				cin >> v;


		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				dfs(grid, 1, string(1, grid[i][j]), i, j);
			}
		}

		cout << "#" << test_case << " " << numbers.size() << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}