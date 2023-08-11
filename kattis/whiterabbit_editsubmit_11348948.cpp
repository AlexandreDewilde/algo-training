#include <bits/stdc++.h>
#define int long long
#define double long double
#define P(x) {if (debug) cout << x << endl;}
#define H(x) P(#x << ": " << (x))
#define FR(i,a,b) for (int i=(a); i<(b); i++)
#define F(i,n) FR(i,0,n)
#define DR(i,a,b) for (int i=(b); i-->(a);)
#define D(i,n) DR(i,0,n)
#define S(s) (int)(s).size()
#define ALL(v) v.begin(), v.end()
#define MI(a,v) a = min(a,v)
#define MA(a,v) a = max(a,v)
#define V vector
#define pb push_back
#define mt make_tuple
using namespace std;

int safeMod(int a, int m) {return (a % m + m) % m;}

void euclid(int a, int b, int &x, int &y, int &d) {
    if (b == 0) x=1, y=0, d=a;
    else euclid(b, a%b, y, x, d), y -= a/b*x;
}

int inv(int a, int m) { // aˆ-1 (mod m)
    int x,y,d; euclid(a,m,x,y,d);
    return (x + m) % m;
}

const double EPS = 1e-12; // -> const int EPS = 0
int solveLinear(V<V<int>> A, V<int> b, V<int>& x) {
    int n = S(A), m = S(A[0]), rank = 0, br, bc;
    V<int> col(m); iota(ALL(col), 0);
    F(i,n) {
        int v, bv = 0;
        FR(r,i,n) FR(c,i,m) if ((v = abs(A[r][c])) > bv)
            br = r, bc = c, bv = v;
        if (bv <= EPS) {
            FR(j,i,n) if (fabs(b[j]) > EPS) return -1;
            break;}
        swap(A[i], A[br]), swap(b[i], b[br]), swap(col[i], col[bc]);
        F(j,n) swap(A[j][i], A[j][bc]);
        //~ bv = 1/A[i][i]; // -> bv = inv(A[i][i], mod)
        bv = inv(A[i][i], 13);
        FR(j,i+1,n) {
            int fac = A[j][i] * bv; // reduce fac in [0, mod[
            fac = safeMod(fac, 13);
            b[j] -= fac * b[i]; // reduce b[j] in [0, mod[
            b[j] = safeMod(b[j], 13);
            FR(k,i+1,m) A[j][k] -= fac*A[i][k], A[j][k] = safeMod(A[j][k],13); // Same here
        }
        rank++;
    }
    x.assign(m, 0);
    for (int i = rank; i--;) {
        b[i] *= inv(A[i][i], 13);
        b[i] = safeMod(b[i], 13);
        x[col[i]] = b[i]; // mult. by inv. and reduce
        
        F(j,i) b[j] -= A[j][i] * b[i], b[j] = safeMod(b[j],13); // reduce b[j] in [0, mod[
    }
    return rank; // (multiple solutions if rank < m)
}

signed main() {
    int N, A, R, T; cin >> N >> A >> R >> T;

    vector<vector<int>> paths;
    map<pair<int,int>,int> mappings;
    vector<int> b(T);
    for (int i = 0; i < T; i++) {
        vector<int> path;
        int d, p; cin >> d >> p;
        b[i] = d;
        for (int i = 0; i < p; i++) {
            int o; cin >> o;
            path.push_back(o);
        }
        for (int i = 1; i < p; i++) {
            int x = path[i-1]; int y = path[i];
            if (x > y) swap(x, y);
            if (!mappings.count({x,y})) {
                mappings[{x,y}] = mappings.size();
            }
        }
        paths.push_back(path);
    }

    vector<vector<int>> matrix(T, vector<int>(mappings.size()));

    for (int it = 0; it < T; it++) {
        vector<int> path = paths[it];
        for (int i = 1; i < path.size(); i++) {
            int x = path[i-1]; int y = path[i];
            if (x > y) swap(x, y);
            matrix[it][mappings[{x,y}]] += 1;
            matrix[it][mappings[{x,y}]] %= 13;
        }
    }

    // for (int i = 0; i < matrix.size(); i++) {
    //     for (int j = 0; j < matrix[0].size(); j++)
    //         cout << matrix[i][j] << " ";
    //     cout << endl;
    // }
    vector<int> xx;
    solveLinear(matrix, b, xx);
    
    vector<vector<pair<int,int>>> g(N + 1, vector<pair<int,int>>());
    for (auto const &it : mappings) {
        auto [x, y] = it.first;
        int idx = it.second;
        // cout << x  << " " << y<< endl;
        g[x].push_back({y, xx[idx]});
        g[y].push_back({x, xx[idx]});
    }

    priority_queue<pair<int,int>> pq;
    vector<int> dst(N + 1, 1e9);
    dst[A] = 0;
    pq.push({0, A});
    while (pq.size()) {
        auto [d, x] = pq.top(); pq.pop();
        if (d > dst[x]) continue;
        for (auto [adj, w] : g[x]) {
            if (dst[adj] > dst[x] + w) {
                dst[adj] = dst[x] + w;
                pq.push({dst[adj], adj}); 
            }
        }
    }
    cout << dst[R] << endl;




}