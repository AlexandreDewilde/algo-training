#include <bits/stdc++.h>

#define int long long
using namespace std;

signed main() {
    int t; cin >> t;
    while (t--) {
        int m, s; cin >> m >> s;
        vector<pair<int,int>> coins(m, pair<int,int>());
        for (int i = 0; i < m; i++) {
            cin >> coins[i].first >> coins[i].second;
        }

        vector<vector<int>> dp(301, vector<int>(301, 1e9));
        dp[0][0] = 0;
        for (auto [x, y] : coins) {
            for (int i = x; i < dp.size(); i++) {
                for (int j = y; j < dp.size(); j++) {
                    dp[i][j] = min(dp[i][j], dp[i-x][j-y] + 1);
                }
            }
        }
        int ans = 1e9;
        for (int i = 0; i <= s; i++) {
            int target = s * s - i * i;
            int sq = sqrt(target) + 1e-9;
            if (sq * sq != target) continue;
            // cout << sq << endl;
            ans = min(ans, dp[i][sq]);
            ans = min(ans, dp[sq][i]);
        }

        if (ans == 1e9)
            cout << "not possible" << endl;
        else
            cout << ans << endl;

    }
}