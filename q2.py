# CHEF'S CHAOTIC COOKBOOK

def longestDecreasingSubsequence(arr):
    n = len(arr)
    dp = [1] * n #initialize the dp array

    for i in range(n):
        for j in range(i):
            if arr[i] < arr[j]:     #update the ith element in the dp array
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(longestDecreasingSubsequence(arr))

if __name__ == "__main__":
    main()