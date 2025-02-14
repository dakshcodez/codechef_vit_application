# SMOKE AND MIRRORS

# finding reflection and printing it

def printReflection(matrix, rows, cols, pos):
    reflected_matrix = [[0] * rows for _ in range(cols)]    #the dimension of the reflected array will be cols x rows

    if pos == 0 or pos == 2:
        for col in range(cols):
            for row in range(rows):
                reflected_matrix[col][row] = matrix[rows-row-1][cols-col-1]     #found this using pen, paper and some insane level intuition
    
    elif pos == 1 or pos == 3:
        for col in range(cols):
            for row in range(rows):
                reflected_matrix[col][row] = matrix[row][col]   #same thing as above
    
    printMatrix(reflected_matrix, cols, rows)

#prints matrix

def printMatrix(matrix, rows, cols):
    for row in range(rows):
        for col in range(cols):
            print(matrix[row][col], end = " ")
        print()

def main():
    t = int(input())     #taking number of times loop runs
    for _ in range(t):
        rows , cols = map(int, input().split())     #assigining rows and columns
       
        matrix = []     #initialize matrix or 2d array
        for row in range(rows):
            row = input().strip().split()
            row = [int(x) for x in row]
            matrix.append(row)

        mirror_pos = int(input())       #taking input for the position of mirror
        
        printReflection(matrix, rows, cols, mirror_pos)

if __name__ == "__main__":
    main()