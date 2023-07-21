#include <bits/stdc++.h>

#define int long long

using namespace std;

int r[101];
int m[101];

signed main() {
    int t; cin >> t;
    while (t--) {
        int f, e; cin >> f >> e;

        vector<pair<int,int>> edges;
        edges.push_back(make_pair(0, e));
        for (int i = 0; i < e; i++) {
            cin >> r[i] >> m[i];
            for (int j = r[i]; j < f; j += m[i])
                edges.push_back(make_pair(j, i));
        }
        edges.push_back(make_pair(f - 1, e + 1));
        sort(edges.begin(), edges.end());

        vector<vector<pair<int,int>>> g(e + 2, vector<pair<int,int>>());
        
        for (int i = 0; i < edges.size() - 1; i++) {
            auto [s1, idx1] = edges[i];
            auto [s2, idx2] = edges[i + 1];
            g[idx1].push_back(make_pair(idx2, s2 - s1));
            g[idx2].push_back(make_pair(idx1, s2 - s1));
        }

        priority_queue<pair<int,int>> pq;
        pq.push(make_pair(0, e));
        vector<int> dst(e + 2, 1e9);
        dst[e] = 0;
        while (pq.size()) {
            auto [d, x] = pq.top();
            pq.pop();
            if (d > dst[x]) continue;
            for (auto [adj, w] : g[x]) {
                if (dst[adj] > dst[x] + w) {
                    dst[adj] = dst[x] + w;
                    pq.push(make_pair(dst[adj], adj));
                }
            }
        }

        int ans = -1;
        int best = -1;
        for (int i = 0; i < edges.size() - 1; i++) {
            auto [e1, idx1] = edges[i];
            auto [e2, idx2] = edges[i + 1];
            int mid = (e1 + e2 + dst[idx2] - dst[idx1]) / 2;
            if (dst[idx1] + mid - e1 > best) {

                best = dst[idx1] + mid - e1;
                ans = mid;
            }
        }

        cout << best << " " << ans << endl;

    }
}