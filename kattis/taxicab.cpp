#include <bits/stdc++.h>

using namespace std;
#define V vector
#define S(s) (int)(s).size()
#define pb push_back
#define int long long
#define FR(i,a,b) for (int i=(a); i<(b); i++)
#define F(i,n) FR(i,0,n)
#define DR(i,a,b) for (int i=(b); i-->(a);)
const int INF = 1e18;

struct edge {int v,c,f,i;};
struct graph {
     // c=capacity, f=flow
    int n; V<V<edge>> g; V<int> d,cur;
    graph(int _n) : n(_n), g(n) {}
    void add(int u, int v, int c1=INF, int c2=0) {
        g[u].pb({v, c1, 0, S(g[v])});
        g[v].pb({u, c2, 0, S(g[u])-1});
    }
    int aug(int u, int t, int limf) {
        if (u == t) return limf;
        for (int &i=cur[u], f; i<S(g[u]); i++) {
            edge &e = g[u][i];
            if (e.c > e.f && d[e.v] == d[u]+1 &&
                (f = aug(e.v, t, min(limf, e.c-e.f)))) {
                e.f += f;
                g[e.v][e.i].f -= f;
                return f;
            }
        }
        return 0;
    }
    void reset() {F(u,n) for (edge &e : g[u]) e.f = 0;}
    int maxf(int s, int t) {
        reset(); // if maxf() is called more than once
        int mf=0, f;
        while (true) {
            d.assign(n, INF); d[s] = 0;
            queue<int> q; q.push(s);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (edge e : g[u])
                    if (e.c > e.f && d[e.v] == INF)
                        d[e.v] = d[u]+1, q.push(e.v);
            }
            if (d[t] == INF) break;
            cur.assign(n, 0);
            while (mf += (f = aug(s,t,INF)), f);
        }
        return mf;
    }
};


void solve() {
    int m; cin >> m;
    int n = m * 2 + 5;
    vector<tuple<int,int,int,int,int>> journeys;
    vector<vector<int>> capa(n, vector<int>(n));
    for (int i = 0; i < m; i++) {
        string s; int a,b,c,d;
        cin >> s;
        cin >> a >> b >> c >> d;
        int minutes = (s[3] - '0') * 10 + s[4] - '0';
        minutes += 60 * ((s[0]-'0')*10 + s[1] - '0');
        journeys.push_back(make_tuple(minutes, a,b,c,d));
        capa[i*2][i*2+1] = m;
        capa[2*m+2][i*2+1]++;
        capa[i*2][2*m+3]++;
        capa[2*m][i*2] = m;
        capa[i*2+1][2*m+1] = m;
    }

    graph g(n);
    for (int i = 0; i < m; i++) {
        auto [minutes, a, b, c, d] = journeys[i];
        int end = minutes + abs(a - c) + abs(b - d);
        for (int j = i + 1; j < m; j++) {
            auto [m2, aa, bb, cc, dd] = journeys[j];
            int ds = abs(aa - c) + abs(bb - d);
            if (end + ds < m2)
                capa[i*2+1][j*2] = m;
        }
    }
    capa[2*m+1][n-1] = INF;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (capa[i][j]) {
                g.add(i, j, capa[i][j], 0);
            }
        }
    }
    g.add(n - 1, 2 * m, 0);

    int lo = 0;
    int hi = m + 1;
    int ans = m;
    int size = g.g[n-1].size();
    edge &e = g.g[n-1][size - 1];
    while (hi >= lo) {
        int mid = lo + (hi - lo) / 2;
        e.c = mid;
        g.maxf(n - 3, n - 2);

        bool poss = true;
        for (edge x: g.g[n-3]) {
            if (x.f != 1) poss = false;
        }
        if (poss) {
            ans = mid;
            hi = mid - 1;
        }
        else {
            lo = mid + 1;
        }
    }
    cout << ans << endl;
}

signed main() {
    int t; cin >> t;
    while (t--) {
        solve();
    }
}