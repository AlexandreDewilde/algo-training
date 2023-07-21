#include <bits/stdc++.h>

#define int long long

using namespace std;

signed main() {
    int t; cin >> t;
    while (t--) {
        int m; cin >> m;
        vector<vector<int>> g(3000, vector<int>());
        unordered_map<string,int> mappings;

        while (m--) {
            string s1, s2; cin >> s1 >> s2;
            if (!mappings.count(s1)) {
                mappings[s1] = mappings.size();
            }
            if (!mappings.count(s2)) {
                mappings[s2] = mappings.size();
            }
            g[mappings[s1]].push_back(mappings[s2]);
            g[mappings[s2]].push_back(mappings[s1]);
        }
        int ans = 0;
        for (int i = 0; i < mappings.size(); i++) {
            queue<int> q; q.push(i);
            vector<int> dst(3001, 4000);
            dst[i] = 0;
            while (q.size()) {
                int x = q.front();
                q.pop();
                for (int adj: g[x]) {
                    if (dst[adj] == 4000) {
                        dst[adj] = dst[x] + 1;
                        q.push(adj);
                    }
                }
            }
            for (int j = 0; j < mappings.size(); j++) {
                if (dst[j] > 6) {
                    ans++;
                    break;
                }
            }
        }
        cout << (ans < 0.05 * mappings.size() ? "YES": "NO" ) << endl;
    }
}