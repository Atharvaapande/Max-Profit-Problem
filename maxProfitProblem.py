def max_profit(n):
    # DP array to store max earnings for each time unit
    dp = [0] * (n + 1)
    
    # To track the buildings constructed
    track = [["T:0 P:0 C:0"] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(n + 1):
        if i >= 5 and dp[i] < dp[i - 5] + 1500:
            dp[i] = dp[i - 5] + 1500
            track[i] = track[i - 5] + ["T"]
        if i >= 4 and dp[i] < dp[i - 4] + 1000:
            dp[i] = dp[i - 4] + 1000
            track[i] = track[i - 4] + ["P"]
        if i >= 10 and dp[i] < dp[i - 10] + 3000:
            dp[i] = dp[i - 10] + 3000
            track[i] = track[i - 10] + ["C"]
    
    # Count buildings
    t_count = track[n].count("T")
    p_count = track[n].count("P")
    c_count = track[n].count("C")

    print(f"Time Unit: {n}")
    print(f"Earnings: ${dp[n]}")
    print(f"Solution: T:{t_count} P:{p_count} C:{c_count}")

# Test Cases
max_profit(7)
max_profit(8)
max_profit(13)
