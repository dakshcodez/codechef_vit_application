# SPECIAL SOUPS

def giveResult(matrix,n):
    res = 0
    for i in range(1,n):        #checking from 1st row onwards till bottom
        for j in range(3):      #checking all the columns
            if matrix[i][j] == 1:
                if matrix[i-1][j] != 1:
                    res+=1
    
    #handling edge cases
    if matrix[0][0] == 1:
        res += 1
    if matrix[0][1] == 1:
        res += 1
    if matrix[0][2] == 1:
        res += 1

    return res

def main():         #taking inputs
    t = int(input())
    for _ in range(t):
        n = int(input())
        ingredients = input().strip().split()
        
        matrix = []     #initializing a 2d matrix
        for i in range(n):          #forming the 2d array
            if ingredients[i]=='o':
                matrix.append([0,1,0])
            elif ingredients[i]=='t':
                matrix.append([1,0,0])
            elif ingredients[i]=='b':
                matrix.append([0,0,1])
            elif ingredients[i]=='p':
                matrix.append([1,1,0])
            elif ingredients[i]=='y':
                matrix.append([0,1,1])
            elif ingredients[i]=='c':
                matrix.append([1,0,1])
            elif ingredients[i]=='s':
                matrix.append([1,1,1])
        
        print(giveResult(matrix, n))
        
if __name__ == "__main__":
    main()