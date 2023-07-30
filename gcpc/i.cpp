#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define int long long
    
    
signed main() {
    int n; cin >> n;
    vector<int> x(n);
    set<int> s;
    gp_hash_table<int,int> pos;
    for (int i = 0; i < n; i++) {
        cin >> x[i];
        s.emplace(x[i] + 1);
        pos[x[i]] = 1;
    }
    
    for (int i = 0; i < n; i++) {
        if (s.count(x[i]))
            s.erase(x[i]);
    }
    
    int q; cin >> q;
    for (int ii = 0; ii < q; ii++) {
        int i; cin >> i; i--;
        int current = x[i];
        auto new_pos = s.upper_bound(current);
        // if (new_pos == s.end())
        //     continue;
    
        s.erase(new_pos);
        pos[x[i]] = 0;
        pos[*new_pos] = 1;
    
        x[i] = *new_pos;
        cout << x[i] << endl;
    
    
        if (pos[(current - 1)])
            s.emplace(current);
        if (!pos[(x[i] + 1)]) {
            s.emplace(x[i] + 1);
        }
    }
}