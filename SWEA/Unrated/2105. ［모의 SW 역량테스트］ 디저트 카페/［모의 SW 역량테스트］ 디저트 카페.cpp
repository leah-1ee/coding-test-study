#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 우하 좌하 좌상 우상
int dr[4] = { 1,1,-1,-1 };
int dc[4] = { 1,-1,-1,1 };

int startR, startC;
int answer;

void dfs(const vector<vector<int>>& grid, int dir, int r, int c, int n, int cnt, vector<bool>& dessert) {
	

	// 방향: 현재 방향 or 다음 방향
	for (int d = dir; d <= dir + 1 && d < 4; d++) {
		int nr = r + dr[d];
		int nc = c + dc[d];

		if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;

		if (nr == startR && nc == startC) {
			if (d == 3) answer = max(answer, cnt);
			continue;
		}

		if (dessert[grid[nr][nc]]) continue;
		dessert[grid[nr][nc]] = true;
		dfs(grid, d, nr, nc, n, cnt + 1, dessert);
		dessert[grid[nr][nc]] = false;
	}

}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{

		int n;
		cin >> n;

		vector<vector<int>> grid(n, vector<int>(n));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> grid[i][j];
			}
		}

		answer = -1;

		for (int i = 0; i < n - 2; i++) {
			for (int j = 1; j < n - 1; j++) {
				startR = i;
				startC = j;

				vector<bool> dessert(101, false);

				dessert[grid[i][j]] = true;

				dfs(grid, 0, i, j, n, 1, dessert);
			}
		}

		cout << "#" << test_case << " " << answer << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}