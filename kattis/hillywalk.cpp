#include <bits/stdc++.h>

using namespace std;

#define int long long

double eval(int a, int b, int c, double x) {
    return a * x * x * x / 3. + b * x * x / 2. + c * x;
}

double integral(int a, int b, int c, double start, double end) {
    cout<< eval(a, b,c, end) << endl;
    cout << a << " "<< b << " " << c << " " << end << " " << start << endl; 
    return eval(a, b,c, end) - eval(a, b, c, start);
}

signed main() {
    int n; cin >> n;
    set<tuple<double,double,bool,int,int>> s;
    for (int i = 0; i < n; i++) {
        int a, b; cin >> a >> b;

        double rho = 4 * a * a + 4 * (b - a * a);
        if (rho < 0) continue;
        double start = (-2 * a + sqrt(rho)) / -2.;
        double end = (-2 * a - sqrt(rho)) / -2;
        // cout <<  start << " " << end << endl;
        s.emplace(make_tuple(start,end,false,a,b));
    }

    int current = 0;
    int ca = 0;
    int ca2 = 0;
    int cb = 0;
    double last_int = 0;
    double ans = 0;
    while (s.size()) {
        auto first = s.begin();
        auto [start, end, remove, a, b] = *first;
        s.erase(first);
        if (remove) {
            if (current >= 2) {
                // cout << last_int <<  " " << start << endl;
                ans += integral(-current, 2 * ca, cb - ca2, last_int, start);
                last_int = start;
            }
            current--;
            ca -= a;
            ca2 -= a*a;
            cb -= b;
            continue;
        }
        current++;
        if (current == 2) last_int = start;
        ca += a;
        ca2 += a*a;
        cb += b;

        s.emplace(make_tuple(end, start, true, a, b));
    }
    printf("%.6lf\n", ans);
}