

def manhattan(a,b):
    #d_x=b[0]-a[0]
    #d_y=b[1]-a[1]
    #distance=abs(d_x)+abs(d_y)
    #return distance
    return minkowski(a,b,1)


def euclidean(a,b):
    #d_x=b[0]-a[0]
    #d_y=b[1]-a[1]
    #distance=(d_x**2+d_y**2)**0.5
    #return distance
    return minkowski(a,b,2)

def minkowski(a,b,p):
    d_x=b[0]-a[0]
    d_y=b[1]-a[1]
    distance=(abs(d_x)**p+abs(d_y)**p)**(1/p)
    return distance