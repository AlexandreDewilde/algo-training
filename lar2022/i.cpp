#include <bits/stdc++.h>

#define int long long

using namespace std;

vector<vector<int>> grid;
int r, c;
pair<int,int> delta[4] = {make_pair(-1, 0), make_pair(1, 0), make_pair(0, -1), make_pair(0, 1)};

int solve(int i, int j) {
    queue<pair<int,int>> q;
    q.push({i,j});
    vector<vector<bool>> vis(r, vector<bool>(c));
    vis[i][j] = true;
    int eaten = 1;

    while (q.size()) {
        auto [i,j] = q.front();
        q.pop();
        for (auto [dx, dy] : delta) {
            if (0 > i + dx || i + dx >= r || 0 > j + dy || j + dy >= c || vis[i+dx][j+dy] || grid[i+dx][j+dy] < grid[i][j])
                continue;
            vis[i+dx][j+dy] = true;
            q.push(make_pair(i+dx, j + dy));
            eaten++;
        }
    }
    return eaten;
}

signed main() {
    cin >> r >> c;
    
    grid.assign(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++)
            cin >> grid[i][j];
    }
    int ans = 1;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++)
            ans = max(ans, solve(i, j));
    }
    cout << ans << endl;
    
}