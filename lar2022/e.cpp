#include <bits/stdc++.h>

using namespace std;

bool dp[1001][1001];

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n, k, e; cin >> n >> k >> e;
    int l = e;
    int r = n - k - e;
    dp[0][0] = 1;

    for (int el = 1; el <= n; el++) {
        if (el == k) continue;
        for (int i = l; i >= 0; i--) {
            for (int j = r; j >= 0; j--) {
                if (i >= el)
                    dp[i][j] |= dp[i - el][j];
                if (j >= el)
                    dp[i][j] |= dp[i][j - el];
            }
        }
    }
    int ans = 0;
    for (int i = 0; i <= l; i++)
        for (int j = 0; j <= r; j++)
            if (dp[i][j])
                ans = max(ans, i + j + k);

    cout << n - ans << endl;
}