#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<pair<int, int>> normalize(vector<pair<int, int>> shape) {
    int minR = shape[0].first;
    int minC = shape[0].second;

    for (auto [r, c] : shape) {
        minR = min(minR, r);
        minC = min(minC, c);
    }

    for (auto& [r, c] : shape) {
        r -= minR;
        c -= minC;
    }

    sort(shape.begin(), shape.end());
    return shape;
}

// target=0: 빈칸, target=1: 퍼즐 조각
vector<vector<pair<int, int>>> findShapes(
    const vector<vector<int>>& board, int target
) {
    int n = board.size();

    vector<vector<bool>> visited(n, vector<bool>(n, false));
    vector<vector<pair<int, int>>> shapes;

    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            if (board[r][c] != target || visited[r][c])
                continue;

            queue<pair<int, int>> q;
            vector<pair<int, int>> shape;

            q.push({r, c});
            visited[r][c] = true;

            while (!q.empty()) {
                auto [cr, cc] = q.front();
                q.pop();

                shape.push_back({cr, cc});

                for (int d = 0; d < 4; d++) {
                    int nr = cr + dr[d];
                    int nc = cc + dc[d];

                    if (nr < 0 || nr >= n ||
                        nc < 0 || nc >= n)
                        continue;

                    if (visited[nr][nc]) continue;
                    if (board[nr][nc] != target) continue;

                    visited[nr][nc] = true;
                    q.push({nr, nc});
                }
            }

            shapes.push_back(normalize(shape));
        }
    }

    return shapes;
}

vector<pair<int, int>> rotate90(
    const vector<pair<int, int>>& piece
) {
    vector<pair<int, int>> rotated;

    for (auto [r, c] : piece) {
        rotated.push_back({c, -r});
    }

    return normalize(rotated);
}

int solution(
    vector<vector<int>> game_board,
    vector<vector<int>> table
) {
    int answer = 0;

    vector<vector<pair<int, int>>> blanks = findShapes(game_board, 0);
    vector<vector<pair<int, int>>> pieces = findShapes(table, 1);

    vector<bool> used(pieces.size(), false);

    for (auto blank : blanks) {
        for (int j = 0; j < pieces.size(); j++) {
            if (used[j]) continue;
            if (blank.size() != pieces[j].size()) continue;

            auto rotated = pieces[j];
            bool match = false;

            for (int k = 0; k < 4; k++) {
                if (rotated == blank) {
                    match = true;
                    break;
                }

                rotated = rotate90(rotated);
            }

            if (match) {
                used[j] = true;
                answer += blank.size();

                break;
            }
        }
    }

    return answer;
}
