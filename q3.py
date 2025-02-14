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
        
        #forming a hash map for the ingredients
        hash_map = {'o': [0,1,0], 't':[1,0,0], 'b':[0,0,1], 'p':[1,1,0], 'y':[0,1,1], 'c':[1,0,1], 's':[1,1,1]}

        matrix = []     #initializing a 2d matrix
        for i in range(n):          #forming the 2d array
            matrix.append(hash_map[ingredients[i]])
        
        print(giveResult(matrix, n))
        
if __name__ == "__main__":
    main()