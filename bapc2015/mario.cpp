#include <bits/stdc++.h>

#define int long long

using namespace std;

signed main() {
    int t; cin >> t;
    while (t--) {
        int n, w; cin >> n >> w;
        int l[n], r[n];
        int pos[n];
        int direction[n];
        for (int i = 0; i < n; i++) {
            cin >> l[i] >> r[i];
            pos[i] = l[i];
            direction[i] = 1;
        }
        int x = 0;
        int time = 0;
        while (x < w and time++ < w * w * 2) {
            vector<bool> forward(w * 4, false);

            for (int i = 0; i < n; i++) {
                if (direction[i] == 1)
                    forward[pos[i]] = true;
                pos[i] += direction[i];
                if (pos[i] == l[i] || pos[i] == r[i])
                    direction[i] *= -1;
            }
            if (forward[x]) x++;
            else if (!forward[x - 1]) x--;
        }
        if (x == w)
            cout << time << endl;
        else
            cout << "IMPOSSIBLE" << endl;



    }
}