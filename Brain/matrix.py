'''
Created on Nov 27, 2015
matcal is a command line interface software that solves eventually all
problems involving matrices.....this includes
*Determinant
*Transpose
*inverse
*simultaneous equations 
*matrix multiplication
*matrix addition 
*matrix subtraction


etc
@author: Jnrshb
'''

def get_row_count(matrix):
    count = 0
    for row in matrix:
        count+=1
    return count

def get_col_count(matrix,row=1):
    """
    this function returns the number of columns in the specified row
    """
    count = 0
    for col in matrix[(row-1)]:
        count+=1
    return count
        
        
def is_valid(matrix):
    """
    checks if a given matrix is valid
    A matrix is valid when the number of columns in all the rows are equal
    """
    
    row = get_row_count(matrix)
    for i in range(row):
        for a in range(row):
            if int(get_col_count(matrix,row=i+1))!= int(get_col_count(matrix,row=a+1)):
                return False
    return True
    
def are_valid(lom):
    #returns True if all matrices in the given list of matrices are valid
    for matrix in lom:
        if  not is_valid(matrix):
            return False
    return True
            
def are_equal(lom):
    """
    returns True if the other of all the matrices 
    in the given list of matrices are equal
    """
    for matrix in lom:
        for i in lom:
            if order_of_matrix(i) != order_of_matrix(matrix):
                return False
    return True
    
def is_square_matrix(matrix):
    if is_valid(matrix):
        row= int(get_row_count(matrix))
        for i in range(row):
            if int(get_col_count(matrix,row=i+1))!= row:
                return False
        return True
    else:
        print "matrix is invalid"


def are_commutative(matrixA,matrixB):
    """"
    the commutative property is a condtion that must be met by two matrices before
    multiplication is possible.
    A 4x5 matrix multiplied by a 5x8 matrix yields a 4x8 matrix and this is possible
    because the commutative condition is met.
    let matrixA be 4x5
    let matrixB be 5x8
    matrixA * matrixB is valid for multiplication because the number of columns in matrixA
    equals the number of rows in matrixB...this property is called the commutative property
    therefore
    matrixB * matrixA is not possible since they are not commutative
    (5x8 * 4*5)
    """
    if are_valid([matrixA,matrixB]):
        x1 = get_row_count(matrixA)
        y1 =  get_col_count(matrixA)
        x2 = get_row_count(matrixB)
        y2 = get_col_count(matrixB)
        if y1 != x2:
            return False
        return True
    else:
        print "invalid matrix"

def order_of_matrix(matrix):
    """
    returns the order of a suare matrix
    """
    if is_valid(matrix):
        x = get_row_count(matrix)
        y = get_col_count(matrix)
        return (x,y)
    else:
        return "matrix is not valid"
        

    
def submatrix(matrix,index=(0,0)):
    r_matrix = [] #result matrix
    for row in range(int(get_row_count(matrix))):
        r_matrix.append([])
        for col in range(int(get_col_count(matrix))):
            if row != index[0] and col != index[1]:
                r_matrix[row].append(matrix[row][col])
    for i in r_matrix:
        if i == []:
            r_matrix.remove(i)
    return r_matrix
        
    
"""        
def submatrix(matrix):
   
    returns other square matrices derived from the main matrix
    number of sub matrices = number of columns in the matrix
    
    constant = 0
    submatrices = []
    if is_valid(matrix):
        nosm = int(get_col_count(matrix)) #number of sub matrices
        index_x = constant
        for i in range(nosm):
            submatrices.append(submatrix(matrix, index=(index_x,i)))
        return submatrices
    else:
        return "matrix is invalid"
    
"""      

def transpose(matrix):
    """
    returns the Transpose of a matrix
    """
    r_matrix = []
    if is_valid(matrix):
        nor = get_col_count(matrix) 
        for col in range(nor):
            r_matrix.append([])
            for i in range(int(get_row_count(matrix))):
                    r_matrix[col].append(matrix[i][col])
    else:
        return "matrix is invalid"
    return r_matrix

def det(matrix):
    """
    returns the determinant of a square matrix, supports only 2x2 matrix for now
    """
    index_x=0
    result = 0
    try:
        if is_square_matrix(matrix):
            pass
        else:
            raise SyntaxError
    except:
        return "matrix is not a square matrix"
    
    if is_square_matrix(matrix) and order_of_matrix(matrix)==(2,2) :
        x = 0
        y = 0
        a = matrix[x][y]*matrix[x+1][y+1]
        b = matrix[x][y+1]*matrix[x+1][y]
        result= a-b
        return result
    else:
        for i in range(get_col_count(matrix)):
            if i%2 != 0:
                result+= (-matrix[index_x][i])*det(submatrix(matrix,index=(index_x,i)))
            else:
                result+= (matrix[index_x][i])*det(submatrix(matrix,index=(index_x,i)))
            
        return result

def mat_mult(matrixA,matrixB):
    """
    returns the multiplication of two matrices
    the two matrices to be multiplied must be commutative as defined(are_commutative)
    the reulting matrix will be in the order of;
        (number of rows of matrixA) by (number of columns of matrixB)
    """
    r_matrix = [] #result matrix
    result = 0 #result of the calculation of each element of the resulting matrix
    if are_commutative(matrixA,matrixB):
        nor = get_row_count(matrixA) #number of rows of r_matrix
        noc = get_col_count(matrixB) #number of columns of r_matrix
        for row in range(nor):
            r_matrix.append([])
            j = 0
            col = 0 
            i = 0
            while j<int(get_col_count(matrixA)):
                result+= matrixA[row][j]*matrixB[col][i]
                j+=1
                col+=1
                if  j==int(get_col_count(matrixA)) and i < int(noc):
                    """
                    *resets the value of j so that the same row in matrixA can iterate through
                     the next column of matrixB untill the last column
                    *reset result to 0
                    *increase i by 1 to indicate the next column of matrixB to be iterated
                     by matrixA 
                    """
                    r_matrix[row].append(result) 
                    result = 0
                    j = 0
                    col =0
                    i+=1 
                    if i == int(noc):
                        """
                         if the columns have all being iterated through
                         break out of the while loop into the for loop
                         and pick the next row of matrixA
                        """
                        break
    return r_matrix
    
def scalar_mult(scalar,matrix):
    try:
        float(scalar)
        
    except:
        return "%s is not a number"%scalar
    r_matrix = []
    for row in range(int(get_row_count(matrix))):
        r_matrix.append([])
        for col in range(int(get_col_count(matrix))):
            r_matrix[row].append(scalar*matrix[row][col])
            
    return r_matrix
       
        

def cofactors(matrix):
    """
    returns the cofactors of a matrix
    """
    r_matrix = [] #result matrix
    if is_valid(matrix) and is_square_matrix(matrix):
        nor = get_row_count(matrix)
        noc = get_col_count(matrix)
        for row in range(nor):
            r_matrix.append([])
            for col in range(noc):
                r_matrix[row].append(det(submatrix(matrix,index=(row,col))))
        
    else:
        return "invalid matrix"
    return r_matrix
    
def addition(matrixA,matrixB):
    r_matrix = []
    if are_valid([matrixA,matrixB]) and are_equal([matrixA,matrixB]):
        for row in range(int(get_row_count(matrixA))):
            r_matrix.append([])
            for col in range(int(get_col_count(matrixA))):
                r_matrix[row].append(matrixA[row][col]+matrixB[row][col])
        return r_matrix
    return "matrices are not valid for the addition operation"
    
def subtraction(matrixA,matrixB):
    r_matrix = []
    if are_valid([matrixA,matrixB]) and are_equal([matrixA,matrixB]):
        for row in range(int(get_row_count(matrixA))):
            r_matrix.append([])
            for col in range(int(get_col_count(matrixA))):
                r_matrix[row].append(matrixA[row][col]-matrixB[row][col])
        return r_matrix
    return "matrices are not valid for the subtraction operation"
        
def adjoint(matrix):
    if is_valid(matrix) and is_square_matrix(matrix):
        return transpose(cofactors(matrix))
def inverse(matrix):
    """
    returns the inverse of a matrix
    """
    if is_valid(matrix) and is_square_matrix(matrix):
        x = float(1/(det(matrix)))
        y = adjoint(matrix)
        result = scalar_mult(x,y)
        return result
    else:
        return "matrix is invalid" 
         
                