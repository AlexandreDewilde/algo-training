#include <bits/stdc++.h>

using namespace std;

int n;
vector<pair<int,int>> edges;
vector<vector<int>> g;
vector<bool> vis;

void dfs(int x, int y) {
    vis[x] = true;
    for (int adj : g[x]) {
        if (!vis[adj] && adj != y) dfs(adj, y);
    }
}

signed main() {
    cin >> n;
    g.resize(n);
    for (int i = 0; i < n; i++) {
        int x, y; cin >> x >> y;
        g[x - 1].push_back(i);
        g[y - 1].push_back(i);
        edges.push_back({x - 1, y - 1});
    }

    for (int i = 0; i < n; i++) {
        vector<int> reachable(n);
        int tovis[3] = {i, edges[i].first, edges[i].second};
        
        for (int x: tovis) {
            vis.assign(n, false);
            dfs(x, i);
            for (int j = 0; j < n; j++) if (vis[j]) reachable[j]++;
        }
        bool win = true;
        for (int j = 0; j < n; j++) {
            if (reachable[j] == 3) {
                win = false;
                break;
            }
        }
        cout << (win ? "N":"Y");
    }
    cout << endl;

    
}