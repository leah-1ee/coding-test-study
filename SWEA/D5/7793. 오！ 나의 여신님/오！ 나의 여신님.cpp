#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

struct Node
{
	int r;
	int c;
	int time;
};

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int n, m;
		cin >> n >> m;

		vector<string> grid(n);
		for (int i = 0; i < n; i++) {
			cin >> grid[i];
		}

		int answer = -1;

		vector<vector<bool>> visited(n, vector<bool>(m, false));
		vector<vector<bool>> hand(n, vector<bool>(m, false));

		int startR, startC, endR, endC;

		int dr[4] = { -1,1,0,0 };
		int dc[4] = { 0,0,-1,1 };

		queue<Node> q;
		queue<Node> demon;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (grid[i][j] == 'S') {
					startR = i;
					startC = j;
				}
				if (grid[i][j] == 'D') {
					endR = i;
					endC = j;
				}
				if (grid[i][j] == '*') {
					demon.push({ i,j,0 });
					hand[i][j] = true;
				}
			}
		}

		q.push({ startR, startC, 0 });
		visited[startR][startC] = true;

		while (!q.empty()) {
			int r = q.front().r;
			int c = q.front().c;
			int time = q.front().time;
			q.pop();


			while (!demon.empty()) {
				int dmr = demon.front().r;
				int dmc = demon.front().c;
				int dmt = demon.front().time;

				if (dmt != time) break;

				demon.pop();

				for (int d = 0; d < 4; d++) {
					int ndmr = dmr + dr[d];
					int ndmc = dmc + dc[d];

					if (0 <= ndmr && ndmr < n && 0 <= ndmc && ndmc < m && !hand[ndmr][ndmc] && (grid[ndmr][ndmc] == '.' || grid[ndmr][ndmc] == 'S')) {
						demon.push({ ndmr, ndmc, dmt + 1 });
						hand[ndmr][ndmc] = true;
					}
				}
			}

			if (r == endR && c == endC) {
				answer = time;
				break;
			}

			for (int d = 0; d < 4; d++) {
				int nr = r + dr[d];
				int nc = c + dc[d];

				if (0 <= nr && nr < n && 0 <= nc && nc < m && !visited[nr][nc] && (grid[nr][nc] == '.' || grid[nr][nc] == 'D') && !hand[nr][nc]) {
					q.push({ nr, nc, time + 1 });
					visited[nr][nc] = true;
				}
			}
		}

		if (answer >= 0) cout << "#" << test_case << " " << answer <<"\n";
		else cout << "#" << test_case << " GAME OVER\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}