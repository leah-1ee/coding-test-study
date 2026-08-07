#include <iostream>
#include <vector>

using namespace std;

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

int dfs(const vector<vector<int>>& room, int r, int c, int n) {
	int cnt = 1;

	for (int d = 0; d < 4; d++) {
		int nr = r + dr[d];
		int nc = c + dc[d];

		if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
		if (room[nr][nc] != room[r][c] + 1) continue;
		cnt += dfs(room, nr, nc, n);
	}

	return cnt;
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

		vector<vector<int>> room(n, vector<int>(n));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> room[i][j];
			}
		}

		int startRoom = 0;
		int maxRoom = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {

				int temp = dfs(room, i, j, n);
				if (temp > maxRoom ||
					(temp == maxRoom && startRoom>room[i][j])
					) {
					startRoom = room[i][j];
					maxRoom = temp;
				}
			}
		}

		cout << "#" << test_case << " " << startRoom << " " << maxRoom << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}