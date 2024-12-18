#include <iostream>
#include <fstream>

using namespace std;

long long o, d, m;

// Function to simulate the loan repayment process
bool sim(long long o, long long d, long long m, long long x) {
    long long paid = 0;
    long long i = 0;

    while (paid < o) {
        long long c = (o - paid) / x;
        if (c <= m) {
            if (paid + m * (d - i) >= o) {
                return true;
            } else {
                return false;
            }
        }
        paid += c;
        i++;
        if (c * (d - i) + paid < o) {
            return false;
        }
        if (i > d) {
            return false;
        }
    }
    return true;
}

int main() {
    ifstream fin("loan.in");
    ofstream fout("loan.out");

    fin >> o >> d >> m;

    long long v1 = 1;
    long long v2 = o;
    long long mid = (v1 + v2) / 2;

    // Binary search for the maximum x
    while (v1 < v2 - 1) {
        if (sim(o, d, m, mid)) {
            v1 = mid;
        } else {
            v2 = mid;
        }
        mid = (v1 + v2) / 2;
    }

    fout << v1 << endl;

    fin.close();
    fout.close();

    return 0;
}
