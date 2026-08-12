#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>

using namespace std;

int N, W, H;


struct Block
{
	int r; int c; int num;
};

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

int bestRemain;

bool isZeroCol(int c, const vector<vector<int>>& temp) {
	for (int r = 0; r < H; r++) {
		if (temp[r][c] != 0) return false;
	}
	return true;
}

void bfs(int col, vector<vector<int>>& temp) {
	queue<Block> q;

	for (int r = 0; r < H; r++) {
		if (temp[r][col] != 0) {
			q.push({ r, col, temp[r][col] });

			break;
		}
	}

	while (!q.empty()) {
		Block cur = q.front();
		int r = cur.r;
		int c = cur.c;
		q.pop();

		temp[r][c] = 0;

		for (int d = 0; d < 4; d++) {
			for (int p = 1; p < cur.num; p++) {
				int nr = r + dr[d] * p;
				int nc = c + dc[d] * p;

				if (nr < 0 || H <= nr || nc < 0 || W <= nc) break;

				if (temp[nr][nc] != 0) {
					q.push({ nr, nc, temp[nr][nc] });
					temp[nr][nc] = 0;
				}
				
			}
			
		}
	}

}

void gravity(vector<vector<int>>& temp) {
	for (int c = 0; c < W; c++) {
		vector<int> nonzero;
		for (int r = 0; r < H; r++) {
			if (temp[r][c] != 0) 
				nonzero.push_back(temp[r][c]);
		}
		int start = H - nonzero.size();

		for (int r = 0; r < H; r++) {
			temp[r][c] = (r < start) ? 0 : nonzero[r - start];
		}
	}
	
}

int countBlock(const vector<vector<int>>& temp) {
	int cnt = 0;
	for (auto row : temp) {
		for (int k : row) {
			if (k != 0) cnt++;
		}
	}

	return cnt;
}

void dfs(int depth, vector<vector<int>> v) {

	// 종료 조건
	if (depth == N) {
		int curRemain = countBlock(v);
		bestRemain = min(bestRemain, curRemain);

		return;
	}

	if (countBlock(v) == 0) {
		bestRemain = 0;
		return;
	}

	// 선택
	for (int c = 0; c < W; c++) {
		vector<vector<int>> temp = v;

		if (!isZeroCol(c, temp)) {
			// 제거 BFS 
			bfs(c, temp);

			// 중력
			gravity(temp);
		}

		// 재귀 
		dfs(depth + 1, temp);

	}

}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		bestRemain = INT_MAX;

		cin >> N >> W >> H;

		vector<vector<int>> grid(H, vector<int>(W, 0));


		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				cin >> grid[i][j];
			}
		}

		dfs(0, grid);

		cout << "#" << test_case << " " << bestRemain << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}