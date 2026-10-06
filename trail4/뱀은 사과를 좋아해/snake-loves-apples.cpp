#include <iostream>
#include <deque>

using namespace std;

int N, M, K;
int grid[101][101];
deque<pair<int, int>> snake;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int getDir(char d) {
    if (d == 'U') return 0;
    if (d == 'D') return 1;
    if (d == 'L') return 2;
    return 3;
}

bool moveSnake(int dir) {
    auto [r, c] = snake.front();

    int nr = r + dr[dir];
    int nc = c + dc[dir];

    if (nr < 0 || nr >= N || nc < 0 || nc >= N)
        return false;

    bool hasApple = (grid[nr][nc] == 2);

    if (!hasApple) {
        auto [tr, tc] = snake.back();
        grid[tr][tc] = 0;
        snake.pop_back();
    }

    if (grid[nr][nc] == 1)
        return false;

    snake.push_front({nr, nc});
    grid[nr][nc] = 1;

    return true;
}

int main() {
    cin >> N >> M >> K;

    for (int i = 0; i < M; i++) {
        int r, c;
        cin >> r >> c;
        grid[r - 1][c - 1] = 2;
    }

    snake.push_front({0, 0});
    grid[0][0] = 1;

    int time = 0;

    for (int i = 0; i < K; i++) {
        char d;
        int dist;
        cin >> d >> dist;

        int dir = getDir(d);

        while (dist--) {
            time++;

            if (!moveSnake(dir)) {
                cout << time;
                return 0;
            }
        }
    }

    cout << time;
    return 0;
}