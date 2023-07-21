#include <bits/stdc++.h>
using namespace std;
#define int long long
vector<vector<char>> grid;
pair<int,int> delta[4] = {make_pair(-1, 0), make_pair(0, 1), make_pair(1, 0), make_pair(0, -1)};
pair<int,int> godzilla;
vector<pair<int,int>> mechs;
vector<vector<bool>> vis;
vector<vector<bool>> gvis;
int l, w;
int previous = 0;
int ans = 0;

bool move_g() {
    auto [x,y] = godzilla;
    for (auto [dx, dy] : delta) {
        if (0 > x + dx || x + dx >= w || y + dy < 0 || y + dy >= l || grid[x + dx][y + dy] != 'R') {
            continue;
        }
        godzilla.first = x + dx;
        godzilla.second = y + dy;
        grid[x+dx][y+dy] = '.';
        ans++;
        gvis[x + dx][y + dy] = true;
        return true;
    }
    for (auto [dx, dy] : delta) {
        if (0 > x + dx || x + dx >= w || y + dy < 0 || y + dy >= l || gvis[x + dx][y + dy] || grid[x + dx][y + dy] != '.') {
            continue;
        }
        godzilla.first = x + dx;
        godzilla.second = y + dy;
        gvis[x + dx][y + dy] = true;
        return true;
    }
    return false;
}

void move_mechs() {
    int lim =  mechs.size();
    for (int i = previous; i < lim; i++) {
        auto [x, y] = mechs[i];
        for (auto [dx, dy] : delta) {
            if (0 > x + dx || x + dx >= w || y + dy < 0 || y + dy >= l || vis[x + dx][y + dy] || grid[x + dx][y + dy] != '.') {
                continue;
            }
            grid[x + dx][y + dy] = 'M';
            vis[x + dx][y + dy] = true;
            mechs.push_back(make_pair(x + dx, y + dy));
        }
    }
    previous = lim;
}

bool check() {
    auto [x, y] = godzilla;
    int i = 0;
    while (x + i >= 0 && grid[x+i][y] == '.') {
        i--;
    }
    if (x + i >= 0 && grid[x+i][y] == 'M') {
        return true;
    }
    i = 0;
    while (x + i < w && grid[x+i][y] == '.') {
        i++;
    }
    if (x + i < w && grid[x+i][y] == 'M') {
        return true;
    }
    i = 0;
    while (y + i >= 0 && grid[x][y+i] == '.') {
        i--;
    }
    if (y + i >= 0 && grid[x][y+i] == 'M') {
        return true;
    }

    i = 0;
    while (y + i < l && grid[x][y+i] == '.') {
        i++;
    }
    if (y + i < l && grid[x][y+i] == 'M') {
        return true;
    }
    return false;
}

signed main() {
    int t; cin >> t;
    while (t--) {
        mechs.clear();
        cin >> l >> w;
        ans = 0;
        previous = 0;
        
        grid.assign(w, vector<char>(l));
        vis.assign(w, vector<bool>(l, false));
        gvis.assign(w, vector<bool>(l, false));
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < l; j++) {
                cin >> grid[i][j];
                if (grid[i][j] == 'G') {
                    godzilla = make_pair(i,j);
                    grid[i][j] = '.';
                }
                if (grid[i][j] == 'M')
                    mechs.push_back(make_pair(i,j));
            }
        }
        gvis[godzilla.first][godzilla.second] = true;
        do {
            bool res =move_g();
            // cout << godzilla.first << " " << godzilla.second << endl;
            if (!res) break;
            move_mechs();
        }
        while (!check());
        
        cout << ans << endl;
        
    }
}