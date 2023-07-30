#include <bits/stdc++.h>

using namespace std;

int r, c;
string grid[1005];
string pass;

bool check(int i, int dec) {
    for (int idx = 0; idx < c; idx++) {
        if (pass[(idx+dec)%c] == '0' || ('0' == grid[i][idx]))
            continue;
        return false;
    }
    return true;
}

bool solve() {
    queue<pair<int,int>> q;

    vector<vector<bool>> vis(r, vector<bool>(c));
    for (int i = 0; i < c; i++) {
        if (check(0, i)) {
            q.push({0, i});
            vis[0][i] = true;
        }
    }

    while (q.size()) {
        auto [i, strides] = q.front(); q.pop();
        if (i == r - 1) 
            return true;
        // cout << i << " " << strides <<endl;
        if (i + 1 < r && !vis[i+1][strides] && check(i + 1, strides)) {
            vis[i+1][strides] = true;
            q.push({i+1, strides});
        }

        if (strides + 1 < c && !vis[i][strides + 1] && check(i, strides + 1)) {
            vis[i][strides+1] = true;
            q.push({i, strides + 1});
        }
        else if(strides + 1 >= c && !vis[i][0] && check(i, 0)) {
            vis[i][0] = true;
            q.push({i, 0});
        }

        if (strides > 0 && !vis[i][strides-1] && check(i, strides - 1)) {
            vis[i][strides-1] = true;
            q.push({i, strides - 1});
        }
        else if (strides <= 0 && !vis[i][c - 1] && check(i, c - 1)) {
            vis[i][c - 1] = true;
            q.push({i, c - 1});
        }
        if (i > 0 && !vis[i-1][strides] && check(i - 1, strides)) {
            vis[i-1][strides] = true;
            q.push({i - 1, strides});
        }
    }
    return false;
}

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> r >> c;
    cin >> pass;

    for (int i = 0; i < r; i++) {
        cin >> grid[i];
    }
    
    bool ans = solve();
    if (!ans) {
        reverse(pass.begin(), pass.end());
        ans = solve();
    }
    cout << (ans ? "Y" : "N") << endl;
}