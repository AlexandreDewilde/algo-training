#include <bits/stdc++.h>

using namespace std;
#define int long long

// from cp algorithms https://cp-algorithms.com/geometry/check-segments-intersection.html
struct pt {
    double x, y;
    pt() {}
    pt(double _x, double _y) : x(_x), y(_y) {}
    pt operator-(const pt& p) const { return pt(x - p.x, y - p.y); }
    double cross(const pt& p) const { return x * p.y - y * p.x; }
    double cross(const pt& a, const pt& b) const { return (a - *this).cross(b - *this); }
};

int sgn(const double& x) { return x >= 0 ? x ? 1 : 0 : -1; }

bool inter1(double a, double b, double c, double d) {
    if (a > b)
        swap(a, b);
    if (c > d)
        swap(c, d);
    return max(a, c) <= min(b, d);
}

bool check_inter(const pt& a, const pt& b, const pt& c, const pt& d) {
    if (fabs(c.cross(a, d)) < 1e-9 && fabs(c.cross(b, d)) < 1e-9)
        return inter1(a.x, b.x, c.x, d.x) && inter1(a.y, b.y, c.y, d.y);
    return sgn(a.cross(b, c)) != sgn(a.cross(b, d)) &&
           sgn(c.cross(d, a)) != sgn(c.cross(d, b));
}

signed main() {
    int t; cin >> t;
    while (t--) {
        int l, w; cin >> l >> w;
        double x, y, ws; cin >> x >> y >> ws;

        vector<pt> pts;
        for (int i = 0; i <= w; i++) {
            pts.push_back(pt(0, i));
            pts.push_back(pt(l, i));
        }

        for (int i = 1; i < l; i++) {
            pts.push_back(pt(i, 0));
            pts.push_back(pt(i, w));
        }

        vector<vector<bool>> can(pts.size(), vector<bool>(pts.size()));
        for (int i = 0; i < pts.size(); i++) {
            for (int j = 0; j < pts.size(); j++) {
                if (i==j)
                    can[i][j] = false;
                else
                    can[i][j] = !(check_inter(pts[i], pts[j], pt(x, y), pt(x + ws, y + ws)) || check_inter(pts[i], pts[j], pt(x, y + ws), pt(x + ws, y)));
            }
        }

        int ans = -(w+1) * w * (w - 1) / 3 - l * (l + 1) * (l - 1) / 3;
        for (int i = 0; i < pts.size(); i++) {
            for (int j = i + 1; j < pts.size(); j++) {
                for (int k = j + 1; k < pts.size(); k++) {
                    if (can[i][j] && can[j][k] && can[i][k])
                        ans++;
                }
            }
        }
        cout << ans << endl;
    }
}