from itertools import product

def interaction(j00,j10,j01,j11):
    return j11-j10-j01+j00

def endpoint_nonidentifiability(a,b):
    # Two completions share endpoints but imply different isolated contrasts.
    A={(0,0):a,(1,1):b,(1,0):a,(0,1):b}
    B={(0,0):a,(1,1):b,(1,0):b,(0,1):a}
    xA=A[(1,0)]-A[(0,0)]; yA=A[(0,1)]-A[(0,0)]
    xB=B[(1,0)]-B[(0,0)]; yB=B[(0,1)]-B[(0,0)]
    assert A[(0,0)]==B[(0,0)] and A[(1,1)]==B[(1,1)]
    assert (xA,yA)!=(xB,yB)
    return A,B

def main():
    for a,b in [(0,1),(2,9),(-3,4)]:
        endpoint_nonidentifiability(a,b)
    assert interaction(0,1,2,3)==0
    assert interaction(0,1,2,7)==4
    print("Observer121 attribution identifiability checks passed.")

if __name__=="__main__":
    main()
