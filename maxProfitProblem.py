def max_profit(n):
    # DP array to store max earnings for each time unit
    dp = [0] * (n + 1)

    # To track the buildings constructed
    track = [[] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        # Check if building a Theatre is optimal
        if i >= 5 and dp[i] < dp[i - 5] + 1500:
            dp[i] = dp[i - 5] + 1500
            track[i] = track[i - 5] + ["T"]

        # Check if building a Pub is optimal
        if i >= 4 and dp[i] < dp[i - 4] + 1000:
            dp[i] = dp[i - 4] + 1000
            track[i] = track[i - 4] + ["P"]

        # Check if building a Commercial Park is optimal
        if i >= 10 and dp[i] < dp[i - 10] + 3000:
            dp[i] = dp[i - 10] + 3000
            track[i] = track[i - 10] + ["C"]

    # Count buildings
    t_count = track[n].count("T")
    p_count = track[n].count("P")
    c_count = track[n].count("C")

    return f"Time Unit: {n}\nEarnings: ${dp[n]}\nSolution: T:{t_count} P:{p_count} C:{c_count}"

# Test Cases
test_results = {
    "Test Case 1": max_profit(7),
    "Test Case 2": max_profit(8),
    "Test Case 3": max_profit(13),
}

test_results
