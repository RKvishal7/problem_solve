import math

import numpy as np
from numpy import dtype
# from scipy.linalg.cython_blas import ddof

'''a = np.array([[1,2,3,4,5],[6,7,8,9,10],[4,7,8,9,10]])
print(a)
print(a.shape)
print(a.dtype)'''

# zero and ones array
'''b = np.zeros((2,3),dtype =int)
print(b)
print(b.shape)
print(b.dtype)
c = np.ones((2,3),dtype=int)
print(c)
print(c.shape)
print(c.dtype)
print(b*c)
print(b+c)
print(b-c)
print(b/c)'''

#create identity matrix
'''m = np.identity(4,dtype=int)
print(m)
print(m.shape)
print(m.dtype)'''

#create a array with range
'''ar = np.arange(2,10,2)
print(ar)
print(ar.shape)
print(ar.dtype)'''

#create even and odd array
'''even = np.arange(2,10,2)
print(even.reshape(2,2),"\n",even.shape,sep=" ")
odd= np.arange(1,10,2)
print(odd.reshape(1,5),"\n",odd.shape,sep=" ")'''

# random number
'''r = np.random.rand(6)
print(r.reshape(2,3),"\n",r.shape,sep=" ")

int_r = np.random.randint(0,10,6)
print(int_r.reshape(2,3),"\n",int_r.shape,sep=" ")'''

# flatten array
'''arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(arr.shape)
print(arr.size)
arr1 = arr.flatten()
print(arr1)
print(arr1.shape)
print(arr1.size)'''

# access elements
'''t = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(t)
print(t[1,1])'''

# slice array
'''t = np.array([1,2,3,4,5])
print(t[1:4])
print(t[0:3])'''

#reverse array
'''t = np.array([1,2,3,4,5])
print(t[::-1])
print(np.flip(t))'''

# short array
'''q = np.array([1,2,6,4,5])
print(q)
print(np.sort(q))'''

# find max and min value
'''j = np.array([6,4,9,0,3,3,4])
print(j)
print(np.max(j))
print(np.min(j))'''

#find mean and sum value
'''h = np.array([8,9,3,3,5])
print(h)
print(np.mean(h))
print(np.sum(h))'''

#Standard deviation = √(average of (x - mean)²)
'''s = np.array([1,2,3,4,5])
print(np.std(s))'''

# besic araay calculation
'''a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
print(a%b)'''

#create a dimantional array and find dimentional and select row and column
'''i = np.array([[1,2,3,4,5],
             [2,4,6,8,9]])
print(i)
print("your array is ",i.ndim,"D.",sep="")
print("row ",i[0:5])
print("column ",i[:,0:5])'''

#  Diagonal elements and Transpose matrix
'''v = np.array([[1,2,3],
             [6,7,8],
            [4,7,8]])
print(v)
print("Diagonal elements :",np.diag(v))
print("reverse diagonal :",np.diag(np.fliplr(v)))
print("Transpose matrix :","\n",v.T)
print("dimention of array :",v.ndim)'''

#matric calculation
'''a = np.array([[1,2,5],
              [6,7,8]])
b = np.array([[3,4,5],
              [6,7,8]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)'''

#Brodcasting
'''a = np.array([[1,2,3],
             [4,5,5]])
b = np.array([6,7,8])
print(a+b)
print(a-b)
print(a*b)
print(a/b)'''
# Condition filtering
'''c = np.array([1,2,3])
print(c<0)
print(c>0)
print(c==2)
print(c[c<3])
print(c[(c>0)&(c<4)])
print(c[(c>0)|(c>3)])
print(c[(c%2==1)])
c[c<3] =0
print(c)
#and more '''

#. Filter even numbers
'''k = np.array([[1,2,3],
              [4,5,6]])
print(k[(k%2==0)])'''

# replace value
'''d  = np.array([1,2,3])
d[1] = 99
print(d)
d[d<2] = 0'''

#cocatence array
'''d1 = np.array([1,2,3])
d2 = np.array([4,5,6])
print(np.concatenate(([d1,d2])))
# 2D array
d3 = np.array([[1,2,3],
               [5,6,7]])
d4= np.array([[6,4,9],
              [7,8,0]])
print(np.concatenate((d3,d4),axis=0))#row wise
print(np.concatenate((d3,d4),axis=1))#column wise
print(np.vstack([d1,d2]))#row wise shortcut
print(np.hstack([d1,d2]))#column wise'''

#Split array
'''b1 = np.array([1,2,3,4,5,6])
print(np.split(b1,[1,2,3,4,5,6]))
b = np.split(b1,3)#shortcut = np.hsplit(a,3) or np.vsplit(b1,3)
c = np.array_split(b1,5)
print(c)
print(b)'''

#unique element
'''v = np.array([1,7,3,4,5])
print(np.unique(v, return_index=True ))# two value return value and index
h = np.array([[28,48,3,5,3],
              [3,4,53,5,35]])
print(np.unique(h))'''

#remove duplicate
'''v = np.array([1,2,3,4,5,5,2,5,3])
print(v)
# rd = []
# for i in v:
#     if i  not in rd  :
#         rd.append(i)
# print(rd)
_,v_idx = np.unique(v, return_index=True)
p= v[np.sort(v_idx)]
print(p)'''# unique element is the best method for removing duplicates

#frequency count
'''v = np.array([1,2,3,5,4,5])
value, count = np.unique(v, return_counts=True)
print(value,"\n",count,sep = "")
fq = dict(zip(value,count))#with dictionary method
print(fq)'''

# Index of max and Index of min
'''u = np.array([[1,2,30,4,5],
              [6,7,80,9,10]])
print(np.unravel_index(np.argmin(u),u.shape))
print(np.unravel_index(np.argmax(u),u.shape))'''

#value search
'''v = np.array([1,2,3,4,5,5,2,5,3])
print(4 in v)
print(np.where(v==4))'''

# boolean indexing = like value filtering
'''g = np.array([1,2,4,6,78,4,7,54])
h = g >50
print(h)
h = g[g>50]
print(h)
j = g[g%2==0]
print(j)'''

# Masking == if condition is true then change tha value
'''j= np.array([1,-2,-3,4,-5,5,2,5,-3])
mask1 = j[j<0] = 0
print(j)
mask2 = j[j%2==0]=-1
print(j)'''

#Handle NaN == empty value search and fill using masking
'''m = np.array([1,2,3,4,nan,4,5])
print(np.isnan(m))
b = m[np.isnan(m)]= np.nanmax(m)#masking
print(m)
print(b)'''

#  Copy vs view
'''h = np.array([1,2,3,4,5,5,2,5,3])
view_arr = h.view()
view_arr[5]=100
print(view_arr)#yaha par orignal array me change hua hai
copy_arr = h.copy()
copy_arr[5]=100
print(copy_arr)#yaha par array ka ak copy bana hai usme ye value change hua hai
print(view_arr.base)# original array dikhayega
print(copy_arr.base)# None return karega '''

#Random matrix and set seed
'''arr = np.random.rand(5,6)# result random value
print(arr)
arr1 = np.random.randint(0,10,(5,6))#reuslt is random integer value
print(arr1)
arr2 = np.random.randn(2,4)#result is randon negative or positive
print(arr2)
np.random.seed(50)
arr3 = np.random.rand(5,6)
print(arr3)'''

# Cumulative sum
'''v = np.array([[1,3,5],
              [2,4,6]])
print(np.cumsum(v))
print(np.cumsum(v,axis=0))
print(np.cumsum(v,axis=1))'''

#Cumulative product == like Cumulative sum but there multiple
'''h = np.array([[1,2,3],
              [4,5,6]])
print(np.cumprod(h))
print(np.cumprod(h,axis=0))
print(np.cumprod(h,axis=1))'''

#Histogram
'''j = np.array([1,2,3,4,6,7,8,4,4,6,7,6,5,4,3,3,5,6,7,9,9])
count , bins = np.histogram(j,bins=3)
print("count:",count)
print("bins:",bins)'''

# dot product
'''g = np.array([[1,2],
              [4,5]])
h = np.array([[10,0],
              [9,7]])
print(np.dot(g,h))'''

# square element , log value ,sin value , and cos value
'''arr1 = np.array([1,2,3,4,5])
print(np.square(arr1))
print(np.cbrt(arr1))
print(np.sqrt(arr1))
arr2 = np.array([1,2,3,4,5])
arr2 = np.array([[9,5,6],
                 [8,4,5]])
print(np.square(arr2))
print(np.sqrt(arr2))
print(np.cbrt(arr2))
print(np.cos(np.deg2rad(arr2)))'''

# exponential value(e^element)
'''arr1 = np.array([1,2,3,4,5])
print(np.exp(arr1))
arr2 = np.array([[4,5,7,],
                 [2,3,5]])
print(np.exp(arr2))'''

#normalize array(array - min value / (max-min))
'''t = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
normalize = (t- np.min(t)) / (np.max(t) - np.min(t))
print(normalize)'''

#standardize array
'''y = np.array([1,2,3,4,5])
stz = (y-np.mean(y))/np.std(y)
print(stz)
print(np.median(y))# formula = (n+1)/2'''

# row wise sum
'''t = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
print(np.sum(t,axis=0))#column wise
print(np.sum(t,axis=1))#row wise
print(np.mean(t,axis=0))#column wise mean
print(np.mean(t,axis=1))#row wise mean
print(np.median(t,axis=0))#column wise median
print(np.median(t,axis=1))#row wise median'''

#argmax and argmin
'''a = np.array([[1,2,3,4,5],
              [6,7,8,90,1]])
print(np.argmax(a))
print(np.argmin(a))'''

# 3D array ops = layer ,row ,column
'''arr = np.array([
    [[1,4,3],
     [2,5,6]],

    [[7,8,9],
     [10,11,12]]
])
print(arr.shape)#layaers, row , column
print(arr)
    # access elements
print(arr[0])#1st layer
print(arr[0][1][2])#specific elements
print(np.sum(arr,axis=0))#layers wise
print(np.sum(arr,axis=1))#row wise
print(np.sum(arr,axis=2))#column wise'''

#advanced slicing
'''#1d slicing
h = np.array([1,2,3,4,5])
print(h[0:5:2])#step slicing
print(h[h%2==0])#codition slicing
print(h[::-1])#reverce slicing
 #2d slicing
j = np.array([[1,2,3],
              [6,7,8]])
print(j[0:3,1:3])#step slicing
print(j[j-2==5])#condition slicing'''

#fancy indexing
'''g = np.array([1,2,3])
print(g[2])#for 1d
print(g[[0,1,2]])
q = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(q[[0,2],[2,1]])#specific element
print(q[[2,1]])#specific row and column'''

#broadcating rule = Different size ke arrays ko automatically match karke operation karna
'''d = np.array([[1,2,3],
               [4,5,6]])
f = np.array([7,8,9])
b = 2
print(d+f)
print(d*f)
print(d+b)'''

#Memory optimization
'''j = np.arange(1000000)#better than list
h = j.view()#avoid copy
print(j)
print(h)
j += 2
print(j)
arr = np.array([1,2,3,4,4])#dtype = int64 avoid , use dtype = np.int8,ya int32
print(arr.nbytes)'''

#  Sparse matrix concept == iss metrix me zero jyada hoti hai
'''from scipy.sparse import csr_matrix
v = np.array([[0,0,0],
               [0,9,0],
               [0,0,4]])
sparse_matrix = csr_matrix(v)
print(sparse_matrix)'''

#Linear algebra operation
'''n = np.array([[3,4],
              [6,7]])
m = np.array([[1,2],
              [4,5]])
print(n+m)
print(n-m)
print(np.dot(n,m))# or n @ m
print(n.transpose(),"\n",m.transpose(),end="\n")
print(np.linalg.inv(n),"\n",np.linalg.det(n),end="\n")
print(np.linalg.inv(m),"\n",np.linalg.det(m))
print(np.linalg.matrix_rank(n),"\n",np.linalg.matrix_rank(m))
print(np.linalg.solve(n,m))'''

#deternimate == |A| =(a*d - b*c), and inverse matrix == d -bA⁻¹ = (1/det) × [ d  -b
                                                                       #     -c  a ]
'''i = np.array([[1,2],
              [6,7]])
print(np.linalg.det(i))
print(np.linalg.inv(i))'''

# eigenvalue nd eigenvectors
'''j = np.array([[1,2],
              [4,5]])
value,vectors =np.linalg.eig(j)
print("eigenvalue :", value)
print("eigenvector :",vectors)'''

# to check the matrix is invertible or not invertible
'''h = np.array([[1,2],
               [2,4]])
c = np.linalg.det(h) == 0
if c == True:
    print("matrix is invertible")
else :
    print("matrix is not invertible")'''

#equation solving
'''A = np.array([[1,1,1],
              [2,1,1],
              [1,2,3]])
B = np.array([6,9,14])

X = np.linalg.solve(A,B)
print(X)'''

#matrix rank == kitni row ya column useful hai (bina relation ke )
'''S = np.array([[1,2],
              [3,4]])
print(np.linalg.matrix_rank(S))#row'''

#matrix trace = main diagonal element sum
'''k = np.array([[1,1,1],
              [2,1,1],
              [1,2,3]])

print(np.trace(k))#1+1+3=5'''

#. Kronecker product == A ke har element ki jagah → (B × wo element) ka block aayega
'''w = np.array([[1,2],
               [7,6]])
y = np.array([[3,4],
              [5,6]])
print(np.kron(w,y))'''

# tensor basics 👉 Scalar → Vector → Matrix → Tensor (list → table → cube → hypercube)
'''a = np.array(1)#0D array
b = np.array([2,2,3])#1D array
c = np.array([[1,2,3,4], #2D array
              [5,6,7,8]])
d = np.array([      #3D array
    [[1,2,3],
     [4,5,6]],

    [[7,8,9],
     [10,11,12]]
])
print(a,   "dimention :",a.ndim)
print(b,   "dimention :",b.ndim)
print(c,   "dimention :",c.ndim)
print(d,   "dimention :",d.ndim)'''

#vectoriization VS loop == 👉 Loop = ek-ek element par kaam , and  👉 Vectorization = poore array par ek sath kaam
"""v = np.array([1,2,3,4,5])
result = []
 #loop
for i in v:
    result.append(i+10)
print("loop :",result,"slowly")
 #vectorizatio

print("vectorization :", v+10,"fastly")"""

#performance test between vectorization and loop
import time
'''arr = np.arange(100000000)
 #vectorization
strt = time.time()
rest = arr**2
end = time.time()
print("vectorization time :", end - strt, "sec" )
 #loop
start = time.time()
rest2 = []
for i in arr:
    rest2.append(i**2)
end = time.time()
print("loop time :", end - start, "sec" )'''

# normal distribution == 👉 “Center me zyada data, side me kam → Normal Distribution”
import matplotlib.pyplot as pt
'''data = np.random.normal(loc=50,scale=10,size=1000)
print(data[:10])
pt.hist(data,bins=10)
pt.show()'''

# uniform distribution == 👉 Jisme sab values ke aane ka chance equal hota hai
'''arr1 = np.random.uniform(low=0,high=10,size=10)
print(arr1)
pt.hist(arr1,bins=10)
pt.show()'''

# correlation matrix and covariance matrix
'''data = np.array([[1,2,3],
                 [4,5,6],
                 [4,8,9]])
print(np.corrcoef(data))
print(np.cov(data))'''

'''x = np.array([1,2,3,4])
y = np.array([40,50,60,70])
print(np.cov(x,y))
print(np.std(x,ddof=1))
v = math.sqrt(5/4)
print(v)
print(np.std(x))'''

#PCA basics
'''from sklearn.decomposition import PCA
data = np.array([
    [1,2],
    [3,4],
    [5,6],
])
pca = PCA(n_components=2)
result = pca.fit_transform(data)
print(result)'''

# Image to Array
'''from PIL import Image

img = Image.open("vishal.jpg")
arr = np.array(img)

print(arr.shape)'''

#KNN(K- nearest neighbour)
from collections import Counter

def knn(X_train, y_train, x_test, k=3):
    distances = np.sqrt(np.sum((X_train - x_test)**2, axis=1))
    k_indices = np.argsort(distances)[:k]
    k_labels = y_train[k_indices]
    return Counter(k_labels).most_common(1)[0][0]

# Data
X_train = np.array([[1,2],[2,3],[3,4],[6,7],[7,8],[8,9]])
y_train = np.array([0,0,0,1,1,1])

x_test = np.array([5,5])

print(knn(X_train, y_train, x_test))