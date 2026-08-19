#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;

int n, k, answer;
int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

void dfs(vector<vector<int>>& grid, int r, int c, int len, bool flag, vector<vector<bool>>& visited) {

	answer = max(answer, len);
	
	for (int d = 0; d < 4; d++) {
		int nr = r + dr[d];
		int nc = c + dc[d];

		if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
		if (visited[nr][nc]) continue;
		if (grid[r][c] <= grid[nr][nc]) {
			if (flag) continue;
			if (grid[r][c] <= grid[nr][nc] - k) continue;

			visited[nr][nc] = true;
			flag = true;
			int temp = grid[nr][nc];
			grid[nr][nc] = grid[r][c] - 1;
			dfs(grid, nr, nc, len + 1, flag, visited);
			grid[nr][nc] = temp;
			flag = false;
			visited[nr][nc] = false;
		}
		else {
			visited[nr][nc] = true;
			dfs(grid, nr, nc, len + 1, flag, visited);
			visited[nr][nc] = false;
		}
	}
}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		answer = 0;
		cin >> n >> k;

		vector<vector<int>> grid(n, vector<int>(n));
		int highest = 0;
		for (auto& row : grid)
			for (auto& v : row) {
				cin >> v;
				highest = max(highest, v);
			}
				
		vector<int> maxR;
		vector<int> maxC;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (grid[i][j] == highest) {
					maxR.push_back(i);
					maxC.push_back(j);
				}
			}
		}

		vector<vector<bool>> visited(n, vector<bool>(n, false));

		for (int i = 0; i < maxR.size(); i++) {
			visited[maxR[i]][maxC[i]] = true;
			dfs(grid, maxR[i], maxC[i], 1, false, visited);
			visited[maxR[i]][maxC[i]] = false;
		}

		cout << "#" << test_case << " " << answer << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}