#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>
#include <climits>
using namespace std;

const int MAXH = 15, MAXW = 12; // 문제 제약조건에 맞게 필요시 조정
typedef int Grid[MAXH][MAXW];

int N, W, H;
struct Block
{
	int r; int c; int num;
};
int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };
int bestRemain;

bool isZeroCol(int c, Grid& temp) {
	for (int r = 0; r < H; r++) {
		if (temp[r][c] != 0) return false;
	}
	return true;
}

void bfs(int col, Grid& temp) {
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

void gravity(Grid& temp) {
	for (int c = 0; c < W; c++) {
		int nonzero[MAXH];
		int cnt = 0;
		for (int r = 0; r < H; r++) {
			if (temp[r][c] != 0)
				nonzero[cnt++] = temp[r][c];
		}
		int start = H - cnt;
		for (int r = 0; r < H; r++) {
			temp[r][c] = (r < start) ? 0 : nonzero[r - start];
		}
	}

}

int countBlock(Grid& temp) {
	int cnt = 0;
	for (int r = 0; r < H; r++)
		for (int c = 0; c < W; c++)
			if (temp[r][c] != 0) cnt++;
	return cnt;
}

void dfs(int depth, Grid& v) {
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
		Grid temp;
		memcpy(temp, v, sizeof(Grid));
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
		Grid grid;
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