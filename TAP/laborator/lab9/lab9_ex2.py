a = " kitten"
b = " sitting"
n, m = len(a), len(b)
M = [ [0 for j in range(m)] for i in range(n)]
M[0] = [ j for j in range(m) ]
for i in range(1, n): #for(int i = 1; i < n; i++)
 M[i][0] = i
 for j in range(1, m): #for(int j = 1; i < m; j++)
 if a[i] == b[j]:
 M[i][j] = M[i-1][j-1]
 else:
 M[i][j] = 1 + min(M[i-1][j-1], M[i-1][j], M[i][j-1])
edit = [ None ] * M[n-1][m-1] #array with M[n][m] edits
i, j, k = n - 1, m - 1, M[n-1][m-1] - 1
while k >= 0 and i > 0 and j > 0:
 if a[i] == b[j]:
 i, j = i - 1, j - 1
 else:
 if M[i][j] == 1 + M[i - 1][j - 1]:
 edit[ k ] = "replace " + a[i] + " --> " + b[j]
 i, j, k = i - 1, j - 1, k - 1
 elif M[i][j] == 1 + M[i][j - 1]:
 edit[k] = "add " + b[j]
 j, k = j - 1, k - 1
 elif M[i][j] == 1 + M[i-1][j]:
 edit[k] = "delete " + a[i]
 i, k = i - 1, k - 1
while k >= 0 and i > 0:
 if M[i][j] == 1 + M[i-1][j]:
 edit[k] = "delete " + a[i]