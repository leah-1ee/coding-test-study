#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>

using namespace std;

int n;
int grid[500][500];
int dp[500][500];

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int main() {
    cin >> n;

    vector<tuple<int, int, int>> cells;

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            cin >> grid[r][c];
            cells.push_back({grid[r][c], r, c});
            dp[r][c] = 1;
        }
    }

    sort(cells.begin(), cells.end());

    int best = 1;

    for (auto [value, r, c] : cells) {
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= n || nc < 0 || nc >= n)
                continue;

            if (grid[r][c] < grid[nr][nc]) {
                dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1);
                best = max(best, dp[nr][nc]);
            }
        }
    }

    cout << best;
}