#include <bits/stdc++.h>

using namespace std;


int n, m;
int ans;
int in[37][2];
int w[37][37];
int out[37][2];
int chosen[37];

void apply(int i, int c, vector<int> &done) {

    done.push_back(i);
    chosen[i] = c;
    int nxt = out[i][c];
    int idx = in[nxt][0] == i;
    int in_next = in[nxt][idx];
    if (in_next == -1)
        return;
    int choice_idx = out[in_next][0] == nxt;
    if (chosen[in_next] == choice_idx)
        return;
    apply(in_next, choice_idx, done);
}

void unapply(vector<int> &done) {
    for (int i : done)
        chosen[i] = -1;
}

void check() {
    int dst = 0;
    int i = 0;
    int tot = 0;
    bool first = true;
    while (i != 0 || first) {
        first = false;
        dst += w[i][out[i][chosen[i]]];
        i = out[i][chosen[i]];
        // cout << i << " ";
        tot++;
    }
    if (tot == n) {
        ans = min(ans, dst);
    }
}

void solve(int i) {
    if (i == n) {
        check();
    }
    else if (chosen[i] == -1) {
        vector<int> done;
        if (out[i][0] != -1) {
            apply(i, 0, done);
            solve(i + 1);
            unapply(done);

        }

        done.clear();
        if (out[i][1] != -1) {
            apply(i, 1, done);
            solve(i+1);
            unapply(done);
        }
    }
    else {
        solve(i+1);
    }
}

int main() {
    int t; cin >> t;
    while (t--) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            in[i][0] = -1;
            out[i][0] = -1;
            chosen[i] = -1;
        }

        for (int i = 0; i < m; i++) {
            int a, b, d; cin >> a >> b >> d;
            if (in[b][0] == -1) {
                in[b][0] = a;
                in[b][1] = -1;
            }
            else {
                in[b][1] = a;
            }
            if (out[a][0] == -1) {
                out[a][0] = b;
                out[a][1] = -1;
            }
            else {
                out[a][1] = b;
            }
            w[a][b] = d;
        }
        ans = 1e9;
        solve(0);
        cout << ans << endl;
    }
}