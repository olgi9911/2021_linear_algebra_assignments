import numpy as np

def SolveLP(A, b, G):
    '''Solve the linear programming problem
        Max G(x)
        st. Ax <= b
             x >= 0
    '''
    # step 0: initialization
    maxg = 0;
    
    # step 1a: enumuate all combinations
    [m, n] = A.shape
    lst = EnumerateAll(np.arange(m-4), m-4, n)
    #print(lst)
    
    # step 1b: compute all the intersection points
    points = [];
    for idx in lst:
        Ai = A[idx, :]
        bi = b[idx]
        feasible = 1

        try: 
            xi = np.linalg.solve(Ai, bi)
            print(xi)
        except np.linalg.LinAlgError:
            # Ai is singular or not square.
            feasible = 0

        
        # step 2: check the feasibility of the itersection point
        if feasible == 1:
          for i in range(m):
              if np.dot(A[i,:], xi) > b[i]:  # violate a constraints
                  feasible = 0
        if feasible == 1:            # only add the feasible point
            points.append(xi)
        
    # step 3: evaluate the G function for all intersection points
    values = []
    for ptx in points:
        values.append(np.dot(G[0:n], ptx)+G[-1])
    
    # step 4: find the point with the largest value as the result
    maxg = max(values)
    maxidx = values.index(maxg)
    x = points[maxidx]
    
    return x, maxg

def EnumerateAll(mlist, m, n):
    ''' Enumerate all the n-tuple from mlist.
        where mlist contains m numbers.
        We assume m >= n.
    ''' 
    # this is just for demo purpose.
    # write your own code for question (3) here.
    if n==0:
        return [[]]
    lst=[]
    for i in range(0, m):
        m = m - 1
        first_element=mlist[i]
        recur_lst=mlist[i+1:]
        for p in EnumerateAll(recur_lst, m, n-1):
            lst.append([first_element]+p)
    return lst


#-------------------------------#
# main program starts from here.#
#-------------------------------#
# Put all the coefficients of the constrains into a matrix A and a vector b

A = np.array([[250,150,0,250],[16,16,0,0],[0,0,16,0],[0,0,0,15],[0,0,0,1], [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]) # x >= 0 === -x <= 0 (Don't forgot the non-negative constraint!)
b = np.array([12000, 800, 400, 200, 10, -1, -1, -1, -1])
G = np.array([80, 70, 60, 50])

# solve this problem
[x, maxg] = SolveLP(A, b, G)
print(x)
print(maxg)