#include <iostream>
#include <vector>

using namespace std;

int climbStairs(int n) {
    if (n <= 1) return 1; // Base case: 1 way to climb 0 or 1 stair
    vector<int> dp(n + 1); // dp[i] will store the number of ways to climb i stairs
    dp[0] = 1; // 1 way to climb 0 stairs (do nothing)
    dp[1] = 1; // 1 way to climb 1 stair (one step)
    for (int i = 2; i <= n; i++)
    {
        dp[i] = dp[i - 1] + dp[i - 2]; 
        // The number of ways to climb i stairs is the sum of the ways 
        //to climb (i-1) and (i-2) stairs
    }
    return dp[n];
}

int main() {
    int n;
    cout << "Enter number of stairs: ";
    cin >> n;
    cout << "Number of ways to climb " << n << " stairs: " << climbStairs(n) << endl;
    return 0;
}
