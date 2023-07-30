#include <bits/stdc++.h>

using namespace std;

signed main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        vector<int> a(n);
        int m = 1e9 + 1;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            m = min(m, a[i]);
        }

        set<tuple<int,int,int>> s;
        for (int i = 0; i < n; i++) {
            s.emplace(make_tuple(a[i]/k, a[i] % k, -i));
        }
        vector<int> solution;
        while (s.size()) {
            auto last = s.rbegin();
            auto [d, rem, idx] = *last;
            // cout << d << " " << rem << " " << idx << endl;
            s.erase(*last);
            if (d == 0 || (d == 1 and rem == 0)) {
                solution.push_back(idx);
            }
            else {
                s.emplace(make_tuple(d - 1, rem, idx));
            }
            
        }
        for (int i = 0; i <n; i++) {
            cout << -solution[i] + 1 << " ";
        }
        cout << endl;
    }
}