#include <bits/stdc++.h>

using namespace std;

#define int long long

signed main() {
    int h, c; cin >> h >> c;

    vector<int> d(c);
    set<pair<int,int>> s;
    for (int i = 0; i < c; i++) {
        int a;
        cin >> a >> d[i];
        s.emplace(make_pair(a + d[i], i));
    }

    for (int i = 0; i < h; i++) {
        pair<int,int> p = *s.begin();
        s.erase(s.begin());
        s.emplace(make_pair(p.first + d[p.second], p.second));
    }
    int ans = 0;
    for (auto current = s.begin(); current != s.end(); current++) {
        pair<int,int> p = *current;
        ans = max(ans, p.first - d[p.second]);
    }
    cout << ans << endl;
}