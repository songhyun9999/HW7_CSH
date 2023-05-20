import numpy as np
def main():
    arr = np.arange(1,5).reshape(2,2)
    eig_val,eig_vec = np.linalg.eig(arr)
    det = np.linalg.det(arr)
    #print("**********1-1**********")
    print("Eigenvalues : ",eig_val)
    print("Eigenvectors : ",eig_vec)
    print("Determinant: ",det)
    #print("**********1-2**********")
    vec1=[1,2,3]
    vec2=[4,5,6]
    print("cross product : ",np.cross(vec1,vec2))

    #print("**********1-3**********")
    a=[[1,2,-2],[2,1,-5],[1,-4,1]]
    a=np.array(a)
    b=[[-15],[-21],[18]]
    b=np.array(b)
    x=np.linalg.solve(a,b)
    print("solution : ")
    print(x)
    



if __name__ == "__main__":
    main()