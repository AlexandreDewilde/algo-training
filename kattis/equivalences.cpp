#include <bits/stdc++.h>

using namespace std;

vector<vector<size_t>> g;
vector<vector<size_t>> g_inv;
vector<bool> vis;
vector<size_t> mappings;

void dfs(size_t x, vector<size_t> &order) {
    vis[x] = true;
    for (size_t adj : g[x]) {
        if (!vis[adj])
            dfs(adj, order);
    }
    order.push_back(x);
}

void dfs2(size_t x, size_t id) {
    if (vis[x])
        return;
    vis[x] = true;
    mappings[x] = id;
    for (size_t adj : g_inv[x])
        dfs2(adj, id);
}

signed main() {
    size_t t; cin >> t;
    while (t--) {
        size_t n, m; cin >> n >> m;
        
        g.assign(n, vector<size_t>());
        g_inv.assign(n, vector<size_t>());
        for (size_t i = 0; i < m; i++) {
            size_t s1, s2; cin >> s1 >> s2;
            s1--; s2--;
            g[s1].push_back(s2);   
            g_inv[s2].push_back(s1);
        }

        vis.assign(n, false);
        vector<size_t> order;
        for (size_t i = 0; i < n; i++) {
            if (!vis[i]) {
                dfs(i, order);
            }
        }

        size_t current = 0;
        mappings.assign(n, 0);
        vis.assign(n, false);
        while (order.size()) {
            size_t x = order[order.size() - 1];
            order.pop_back();
            if (!vis[x]) {
                dfs2(x, current++);
            }
        }
        if (current == 1) {
            cout << 0 << endl;
            continue;
        }

        vector<size_t> in(current, 0);
        vector<size_t> out(current, 0);

        for (size_t i = 0; i < n; i++) {
            for (size_t j : g[i]) {

                if (mappings[i] != mappings[j]) {
                    in[mappings[j]]++;
                    out[mappings[i]]++;
                }
            }
        }

        size_t maxIn = 0;
        size_t maxOut = 0;

        for (size_t i = 0; i < current; i++) {
            if (in[i] == 0) maxIn++;
            if (out[i] == 0) maxOut++;
        }
        cout << max(maxIn, maxOut) << endl;
    }

}