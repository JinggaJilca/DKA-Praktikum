
# Menambah Elemen
x = [1,2,7]
print("Kondisi awal list atau array x: ", x)
x.append(5)
print("Kondisi array x append:", x)
x.extend([4,5,8])
print("Kondisi array x extend:", x)

# Installasi lewat terminal "pip install numpy"
import numpy as np

x = np.array([4,5,7,10])
y = np.array([5,6,7,8])

z = x + y
print(z)

# Penggabungan dengan concatenate numpy
z = np.concatenate((x,y))
print(z)

print(z.tolist()) #untuk menampilkan elemen dengan pemisah ,

# Penggunan ndim
a = np.array([85,90,75,30])
print("Dimensi Array a: ", a.ndim)
print("Sape a: ", a.shape)

b = np.array([[85,90,75,30], [56,78,23,23]])
print("Dimensi Array b: ", b.ndim)
print("Shape b: ", b.shape)


# Shape
i = np.array([[5, 10, 15, 13], [7, 8, 13, 12]])
j = np.array([[15, 78, 13, 14], [52, 48, 79, 14]])

if i.shape == j.shape:
    print("array i dn j sama")
else:
    print("array i dan j tdk sama")
    print("shape i =", i.shape)
    print("shape j =", j.shape)

# Size
x = np.array([[1, 2, 3], [4, 5, 6]]) 
print("Size x:", x.size) 

x = np.array([1, 2, 3, 4, 5, 6]) 
y = np.array([[5, 6], [7, 8], [9, 10]]) 
 
# Membandingkan ukuran kedua array 
if x.size == y.size: 
    print("Kedua array memiliki jumlah elemen yang sama.") 
else: 
    print("Kedua array memiliki jumlah elemen yang berbeda.")

# dtype, untuk tipe data
x = np.array([1, 2, 3]) 
print("Tipe data x:", x.dtype) 

x = np.array(["apple", "banana", "cherry"], dtype=np.str_) 
print("Tipe data x:", x.dtype) 

# ones
x = np.ones((3, 4)) 
 
print(x) 

# empty
x = np.empty((2, 2)) 
print(x) 

# linspace
x = np.linspace(0, 1, 5)  
print(x) 

# Random
x = np.random.randint(0, 10, size=(3, 4)) 
print(x) 


# Menambahkan elemen array
