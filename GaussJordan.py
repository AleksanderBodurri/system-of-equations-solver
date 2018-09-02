
# 
# Logic Functions start here
#

def swap_list_positions(li, index1, index2):
    '''  (List, int, int) -> None
    Rearranges the position of the 2 elements in the list li specified by
    the two index inputs index1 and index2. Used in this Application to provide
    equation/row swapping logic
    
    REQ: index1 and index2 are within the index range of li
    
    >>> a = [1,2,3]
    >>> swap_list_positions(a,0,2)
    >>> print(a)
    [3, 2, 1]
    
    '''
    element_1 = li[index1]
    element_2 = li[index2]
    li[index1] = element_2
    li[index2] = element_1


def column_zero_check(li):
    ''' (List) -> None
    Checks to see if any column of a system of equations represented as the
    list li is entirely 0. In other words checks to see if any coefficent
    in the system is 0 for all equations. Returns False if any given column
    is found to be all zero. Returns True otherwise.
    REQ: li is a list of lists, each representing a single equation in a system

    a = [[0,2,3,4],[2,3,4,4],[2,3,1,0]]
    column_zero_check(a)
    True
    a = [[0,2,3,],[2,3,4,4],[2,3,1,0]]
    column_zero_check(a)
    True
    
    '''
    for variable_index in range(len(li[0])-1):
        column_sum = 0
        for equation in li:
            column_sum += equation[variable_index]
        column_sum -= li[0][variable_index]
        column_diff = 0-column_sum
        column_diff += li[0][variable_index]
        if column_sum == 0 and column_diff == 0:
            return False
    return True
    

def gauss_jordan_helper1(li, i, j):
    ''' (List, int, int) -> None
    First Step in Gauss Jordan Process. Checks value at li[i][j] to see if it
    is nonzero and continously swaps the row with the next row if the current
    li[i][j] is zero.
    REQ: li is a list of lists, each representing a single equation in a system
    REQ: i represents a row number (cannot exceed row length)
    REQ: j represents a column number (cannot exceed column length)
    >>> a = [[0,2,4,4],[4,8,1,6], [8,9,7,5]]
    >>> gauss_jordan_helper1(a,0,0)
    >>> print(a)
    [[4, 8, 1, 6], [0, 2, 4, 4], [8, 9, 7, 5]]
    '''
    first_pivot_found = False
    tries = len(li) - 1
    start_index = j + 1
    while not first_pivot_found:
        if li[i][j] != 0:
            first_pivot_found = True
        elif start_index <= tries:
            swap_list_positions(li, 0, start_index)
        if not first_pivot_found and start_index > tries:
            raise Exception("No Unique Solution")
        start_index += 1
    
def gauss_jordan_helper2(li, i, j):
    ''' (List, int, int) -> None
    Second step in Gauss Jordan process. Finds value of coefficient at the
    position specified by ints i and j. Store this value in a variable and
    then divides the entire row i by the stored value (thus making the
    coefficient at the specified i and j equal to 0)
    REQ: li is a list of lists, each representing a single equation in a system
    REQ: i represents a row number (cannot exceed row length)
    REQ: j represents a column number (cannot exceed column length)
    
    >>> a = [[0,2,4,4],[4,8,1,6], [8,9,7,5]]
    >>> gauss_jordan_helper1(a,0,0)
    >>> print(a)
    [[4, 8, 1, 6], [0, 2, 4, 4], [8, 9, 7, 5]]
    >>> gauss_jordan_helper2(a,0,1)
    >>> print(a)
    [[1.0, 2.0, 0.25, 1.5], [0, 2, 4, 4], [8, 9, 7, 5]]
    
    
    '''
    divide_by = li[i][j]    
    for index in range(len(li[i])):
        li[i][index] = li[i][index]/divide_by


def gauss_jordan_helper3(li, pivot_row_index, replaced_row_index, pivot_index):
    ''' (List, int, int, int) -> None
    Subtracts the row specified by replaced_row_index by the multiple of the
    row specified by pivot_row_index that will turn the value of the replaced 
    row at the pivot index into 0.
    REQ: li is a list of lists, each representing a single equation in a system
    REQ: pivot_row_index represents the row with the current pivot and thus
    cannot exceed row length
    REQ: replaced_row_index represents the row that is being transformed to
    have a 0 at the current pivot index and thus cannot exceed row length
    REQ: pivot_index is the column position if the current pivot and thus
    cannot exceed column length
    
    a = [[0,2,4,4],[4,8,1,6], [8,9,7,5]]
    gauss_jordan_helper1(a,0,0)
    >>> print(a)
    [[4, 8, 1, 6], [0, 2, 4, 4], [8, 9, 7, 5]]
    gauss_jordan_helper2(a,0,1)
    >>> print(a)
    [[1.0, 2.0, 0.25, 1.5], [0, 2, 4, 4], [8, 9, 7, 5]]
    >>> gauss_jordan_helper3(a,0,1,0)
    >>> print(a)
    [[1.0, 2.0, 0.25, 1.5], [0.0, 2.0, 4.0, 4.0], [8, 9, 7, 5]]
    >>> gauss_jordan_helper3(a,0,2,0)
    >>> print(a)
    [[1.0, 2.0, 0.25, 1.5], [0.0, 2.0, 4.0, 4.0], [0.0, -7.0, 5.0, -7.0]]

    '''
    new_row = []
    multiply_by = li[replaced_row_index][pivot_index]
    copy_pivot_row = [x * multiply_by for x in li[pivot_row_index]]
    for i in range(len(li[0])):
        li[replaced_row_index][i] = (
        li[replaced_row_index][i] - copy_pivot_row[i])


def gauss_jordan(li):
    ''' (List) -> None
    Performs the Gauss-Jordan algorithm on the given list to transform it into
    RREF form. See helper functions for Step by Step logic.
    REQ: li is a list of lists, each representing a single equation in a system
    
    >>> a = [[0,2,4,4],[4,8,1,6], [8,9,7,5]]
    >>> gauss_jordan(a)
    >>> print(a)
    [[1.0, 2.0, 0.25, 1.5], [0.0, 1.0, 2.0, 2.0],
    [0.0, 0.0, 1.0, 0.3684210526315789]]

    
    '''
    i = 0
    j = 0
    while j < len(li) and i < (len(li[0])-1):
        gauss_jordan_helper1(li, i, j)
        gauss_jordan_helper2(li, i, j)
        b = i
        while b+1 <= len(li)-1:
            gauss_jordan_helper3(li, i, b+1, j)
            b += 1
        i += 1
        j += 1


def solve_system(li):
    ''' (List) -> None
    Takes a list representing a system of equations that can be represented
    as a matrix that has been turned into RREF and back subsitutes values
    to find all solutions
    REQ: li is a list of lists, each representing a single equation in a system
    that has been turned into RREF by the Gauss-Jordan algorithm
    
    >>> a = [[4,4,1,24],[2,-4,1,0],[5,-4,-5,12]]
    >>> gauss_jordan(a)
    >>> print(a)
    [[1.0, 1.0, 0.25, 6.0], [-0.0, 1.0, -0.08333333333333333, 2.0],
    [-0.0, -0.0, 1.0, -0.0]]
    >>> solve_system(a)
    >>> print(a)
    [[1.0, 0, 0, 4.0], [-0.0, 1.0, 0, 2.0], [-0.0, -0.0, 1.0, -0.0]]
    
    '''
    for k in range(len(li)-1):
        z = li[-1-k][-1]
        for i in reversed(range(len(li)-1-k)):
            li[i][-1] = li[i][-1] - li[i][-2-k]*z
            li[i][-2-k] = 0


def round_values(li):
    ''' (List) -> None
    Takes in a list representing a solved system of equations and rounds all
    solutions to the nearest 2 decimal places
    REQ: li is a list of lists, each representing a single equation in a system
    that has been fully solved
    
    >>> a = [[1,2,4],[2,1,4]]
    >>> gauss_jordan(a)
    >>> print(a)
    [[1.0, 2.0, 4.0], [-0.0, 1.0, 1.3333333333333333]]
    >>> solve_system(a)
    >>> print(a)
    [[1.0, 0, 1.3333333333333335], [-0.0, 1.0, 1.3333333333333333]]
    >>> round_values(a)
    >>> print(a)
    [[1.0, 0, 1.33], [-0.0, 1.0, 1.33]]

    '''
    for equation in li:
        equation[-1] = round(equation[-1],2)
        
def pull_out_solution(li):
    ''' (List) -> None
    Takes in a list representing a solved system of equations that has had
    its solutions rounded to 2 decimal places and prints out the solutions
    for each variable
    
    >>> a = [[1,2,4],[2,1,4]]
    >>> gauss_jordan(a)
    >>> print(a)
    [[1.0, 2.0, 4.0], [-0.0, 1.0, 1.3333333333333333]]
    >>> solve_system(a)
    >>> print(a)
    [[1.0, 0, 1.3333333333333335], [-0.0, 1.0, 1.3333333333333333]]
    >>> round_values(a)
    >>> print(a)
    [[1.0, 0, 1.33], [-0.0, 1.0, 1.33]]
    >>> pull_out_solution(a)
    x_1 = 1.33
    x_2 = 1.33

    
    '''
    for variable_index in range(len(li)):
        if li[variable_index][-1] == 0.0:
            solution = 0.0
        else:
            solution = li[variable_index][-1]
        print("x_" +
              str(variable_index+1) + 
              " = " + str(solution))

#
#Logic functions end here
#


exit = False
while not exit:
    column_check = False
    while not column_check:
        equations = []
        valid_num_variable_input = False
        while not valid_num_variable_input:
            try:
                num_variables = int(input('How many variables/equations?: '))
                if num_variables <= 0:
                    raise ValueError("Input integer is too small")
                valid_num_variable_input = True
            except ValueError as error:
                print("Invalid input please input an integer greater than 0")
        
        for e in range(num_variables):
            eq = []
            for x in range(num_variables+1):
                eq.append(0)
            equations.append(eq)
        
        eq_num = 1
        for equation in equations:
            print(equation)                
            for variable in range(len(equation)):
                valid_input = False
                while not valid_input:
                    print("for equation number " + str(eq_num))
                    try:
                        if variable == num_variables:
                            equation[variable] = int(
                                input("Insert constant that equation is equal to \n"))
                        else:
                            equation[variable] = int(
                                input( "Insert coefficient for variable at position " +
                                       str(variable + 1) + "\n" ) )
                        valid_input = True
                    except ValueError as error:
                        print("Invalid input please input" +
                              " an integer greater than 0")
                print(equation)        
            eq_num += 1
        
        print(equation)
        
        if not column_zero_check(equations):
            print(equations)
            print("The equation you have input has a full column of zeros." + 
                  " If you would like to solve the equation you have input" +
                  " decrease your variable count by 1 before you start to" +
                  " input coefficients")
        else:
            column_check = True
    
    try:
        gauss_jordan(equations)
        solve_system(equations)
        round_values(equations)
        pull_out_solution(equations)
        key_input = input(
            "Input x to exit. Input any other character to try again \n")
        if key_input.upper() == "X":
            exit = True        
    except Exception as error:
        print("Given equation has no unique solutions")
    