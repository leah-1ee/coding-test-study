#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;

struct Marble {
    int r, c;
    int weight, dir;
    bool alive;
};

Marble marbles[101];

// U D L R
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int curTime;
int crashed;

int getDir(char d) {
    if (d == 'U') return 0;
    if (d == 'D') return 1;
    if (d == 'L') return 2;
    return 3;
}

void init() {
    cin >> N;

    curTime = 1;
    crashed = -1;

    for (int i = 1; i <= N; i++) {
        int x, y, w;
        char d;

        cin >> x >> y >> w >> d;

        x *= 2;
        y *= 2;

        int dir = getDir(d);

        // 기존 코드의 {-y, x} 좌표계 유지
        marbles[i] = {-y, x, w, dir, true};
    }
}

void moveMarbles() {
    for (int i = 1; i <= N; i++) {
        if (!marbles[i].alive) continue;

        marbles[i].r += dr[marbles[i].dir];
        marbles[i].c += dc[marbles[i].dir];
    }
}

bool higherPriority(int a, int b) {
    if (marbles[a].weight != marbles[b].weight)
        return marbles[a].weight > marbles[b].weight;

    return a > b;
}

void removeMarbles() {
    vector<int> alive;

    for (int i = 1; i <= N; i++) {
        if (marbles[i].alive)
            alive.push_back(i);
    }

    sort(alive.begin(), alive.end(), [](int a, int b) {
        if (marbles[a].r != marbles[b].r)
            return marbles[a].r < marbles[b].r;

        return marbles[a].c < marbles[b].c;
    });

    bool removed = false;

    int start = 0;

    while (start < alive.size()) {
        int end = start + 1;

        while (
            end < alive.size() &&
            marbles[alive[start]].r == marbles[alive[end]].r &&
            marbles[alive[start]].c == marbles[alive[end]].c
        ) {
            end++;
        }

        // [start, end)가 같은 위치의 구슬들
        if (end - start >= 2) {
            removed = true;

            int best = alive[start];

            for (int i = start + 1; i < end; i++) {
                int cur = alive[i];

                if (higherPriority(cur, best))
                    best = cur;
            }

            for (int i = start; i < end; i++) {
                int cur = alive[i];

                if (cur != best)
                    marbles[cur].alive = false;
            }
        }

        start = end;
    }

    if (removed)
        crashed = curTime;
}

int main() {
    cin >> T;

    for (int tc = 0; tc < T; tc++) {
        init();

        for (int t = 0; t < 4000; t++) {
            moveMarbles();
            removeMarbles();
            curTime++;
        }

        cout << crashed << '\n';
    }

    return 0;
}