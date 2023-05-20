import numpy as np
def main():
    docs=[[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]]
    docs=np.array(docs)
    
    Query = [1,1,0,0,1,0]
    Query = np.array(Query)
    print("doc1 = %.2f"%cos_similar(docs[0],Query))
    print("doc2 = %.2f"%cos_similar(docs[1],Query))
    print("doc3 = %.2f"%cos_similar(docs[2],Query))


def cos_similar(a,b):
    dt = np.dot(a,b)
    s = np.linalg.norm(a)*np.linalg.norm(b)
    return dt/s

if __name__ == "__main__":
    main()