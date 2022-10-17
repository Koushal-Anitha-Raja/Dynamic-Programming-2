#TC: O(m*n) 
#SC: O(m*n)
def knapsack (val,wt,m,n):
    #creating a dp array and iterating the two dimensional tabular array
    #initialize all the first row and colums as zero
    dp= [[ 0 for _ in range (m+1)] for s in range  (n+1)]
    
    
    #for iterating the 2d array
    for i in range(n+1):
        for j in range(m+1):
            #until j is the same value copy the above element 
            if j<wt[i-1]:
                #copy the above row on the same column 
                dp[i][j]=dp[i-1][j]
            else:
                #this is the logic of knapsack for using the repeated sub problems
                dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
        #the final  two d tabulation will hold the value        
    return dp[-1][-1]
    
val=[1,4,5,7]
wt=[1,3,4,5]
m=7
n=len(val)
print(knapsack(val,wt,m,n))
