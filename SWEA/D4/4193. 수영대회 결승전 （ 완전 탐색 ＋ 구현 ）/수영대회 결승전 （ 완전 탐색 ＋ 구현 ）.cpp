#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node
{
	int r; int c; int t;
};

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		int answer = -1;

		int n;
		cin >> n;

		vector<vector<int>> grid(n, vector<int>(n));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> grid[i][j];
			}
		}

		int sr, sc, er, ec;
		cin >> sr >> sc >> er >> ec;

		queue<Node> q;
		q.push({ sr,sc,0 });

		vector<vector<bool>> visited(n, vector<bool>(n, false));

		visited[sr][sc] = true;

		while (!q.empty()) {
			Node cur = q.front();
			q.pop();

			if (cur.r == er && cur.c == ec) {
				answer = cur.t;
				break;
			}

			for (int d = 0; d < 4; d++) {
				int nr = cur.r + dr[d];
				int nc = cur.c + dc[d];

				bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < n);
				if (isRange && !visited[nr][nc] && grid[nr][nc] != 1) {
					if (grid[nr][nc] == 2 && cur.t % 3 != 2) {
						q.push({ cur.r, cur.c, cur.t + 1 });
						continue;
					}
						

					q.push({ nr, nc, cur.t + 1 });
					visited[nr][nc] = true;

				}

			}
		}

		cout << "#" << test_case << " " << answer << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}