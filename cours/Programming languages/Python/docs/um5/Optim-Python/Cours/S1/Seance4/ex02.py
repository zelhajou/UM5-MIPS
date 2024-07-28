Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #La creation
>>> T=(10,20,50,1,2,3,10,10,20,40)
>>> type(T)
<class 'tuple'>
>>> T.count(10)
3
>>> T.index(50)
2
>>> L=list(T)
>>> L
[10, 20, 50, 1, 2, 3, 10, 10, 20, 40]
>>> E={10,20,40,50}
>>> E
{40, 10, 20, 50}
>>> type(E)
<class 'set'>
>>> E[0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    E[0]
TypeError: 'set' object does not support indexing
>>> A={10,20,10,30,10,50}
>>> A
{10, 20, 50, 30}
>>> A={10,15.6,"Ali",(7,8,0),"z"}
>>> A
{10, (7, 8, 0), 15.6, 'z', 'Ali'}
>>> A={10,15.6,"Ali",{7,8,0},"z"}
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    A={10,15.6,"Ali",{7,8,0},"z"}
TypeError: unhashable type: 'set'
>>> L
[10, 20, 50, 1, 2, 3, 10, 10, 20, 40]
>>> set(L)
{1, 2, 3, 40, 10, 50, 20}
>>> A={10,20,30,40,50,60}
>>> B={10,20,1,3,5,9}
>>> A|B
{1, 3, 5, 40, 9, 10, 50, 20, 60, 30}
>>> A&B
{10, 20}
>>> A-B
{40, 50, 60, 30}
>>> A^B
{1, 3, 5, 40, 9, 50, 60, 30}
>>> 10 in A
True
>>> {1,2} <=B
False
>>> {1,3} <=B
True
>>> A
{40, 10, 50, 20, 60, 30}
>>> B
{1, 3, 5, 9, 10, 20}
>>> A-B
{40, 50, 60, 30}
>>> B-A
{1, 3, 5, 9}
>>> A^B
{1, 3, 5, 40, 9, 50, 60, 30}
>>> A+B
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    A+B
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> A*4
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    A*4
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> A
{40, 10, 50, 20, 60, 30}
>>> len(A)
6
>>> max(A)
60
>>> min(A)
10
>>> sum(A)
210
>>> A+4
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    A+4
TypeError: unsupported operand type(s) for +: 'set' and 'int'
>>> A.add(4)
>>> A
{4, 40, 10, 50, 20, 60, 30}
>>> A.pop()
4
>>> A
{40, 10, 50, 20, 60, 30}
>>> A.pop()
40
>>> A
{10, 50, 20, 60, 30}
>>> A.remove(60)
>>> A
{10, 50, 20, 30}
>>> B={10,"A",(4,5),18.9}
>>> B
{(4, 5), 10, 18.9, 'A'}
>>> B[0]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    B[0]
TypeError: 'set' object does not support indexing
>>> A
{10, 50, 20, 30}
>>> A.remove(50)
>>> A.add(400)
>>> A
{10, 400, 20, 30}
>>> id(A)
51662920
>>> A.remove(400)
>>> id(A)
51662920
>>> A.add(300)
>>> id(A)
51662920
>>> B={10,20,{50,60},(4,8)}
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    B={10,20,{50,60},(4,8)}
TypeError: unhashable type: 'set'
>>> B={10,20,(50,60),(4,8)}
>>> B
{10, 20, (50, 60), (4, 8)}
>>> #Les dictionnaires
>>> D={"Ali":14,"Sara":18,"Hiba":19}
>>> D["Ali"]
14
>>> D["Hiba"]
19
>>> D["Ali"]=19
>>> D
{'Ali': 19, 'Sara': 18, 'Hiba': 19}
>>> D["Karim"]=20
>>> D
{'Ali': 19, 'Sara': 18, 'Hiba': 19, 'Karim': 20}
>>> D[101]=11
>>> D
{'Ali': 19, 'Sara': 18, 'Hiba': 19, 'Karim': 20, 101: 11}
>>> 
>>> D[("Ali","Python"]=18
  
SyntaxError: invalid syntax
>>> D[("Ali","Python")]=18
>>> D
{'Ali': 19, 'Sara': 18, 'Hiba': 19, 'Karim': 20, 101: 11, ('Ali', 'Python'): 18}
>>> D[["Ali","JAVA"]]=10
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    D[["Ali","JAVA"]]=10
TypeError: unhashable type: 'list'
>>> D
{'Ali': 19, 'Sara': 18, 'Hiba': 19, 'Karim': 20, 101: 11, ('Ali', 'Python'): 18}
>>> len(D)
6
>>> d.keys()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    d.keys()
NameError: name 'd' is not defined
>>> D.keys()
dict_keys(['Ali', 'Sara', 'Hiba', 'Karim', 101, ('Ali', 'Python')])
>>> D.values()
dict_values([19, 18, 19, 20, 11, 18])
>>> 
===  TA/27_12_21/ex01.py ===
>>> E
{1: ['Ali', 'Rabat'], 2: ['Sara', 'Rabat'], 3: ['Hind', 'Rabat'], 4: ['Mohamed', 'Rabat']}
>>> E={}
>>> type(E)
<class 'dict'>
>>> A=set()
>>> A
set()
>>> type(A)
<class 'set'>
>>> A.add(40)
>>> A
{40}
>>> type(A)
<class 'set'>
>>> E
{}
>>> E.add(70)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    E.add(70)
AttributeError: 'dict' object has no attribute 'add'
>>> E
{}
>>> 
===  TA/27_12_21/ex01.py ===
>>> E
{1: ['Ali', 'Rabat'], 2: ['Sara', 'Rabat'], 3: ['Hind', 'Rabat'], 4: ['Mohamed', 'Rabat']}
>>> M
{101: ['JAVA', 5], 102: ['PYTHON', 9], 103: ['C', 10], 105: ['C++', 5]}
>>> EX
{(1, 101): 15, (1, 102): 10, (2, 101): 16, (3, 101): 13}
>>> (15*5+10*9)/14
11.785714285714286
>>> 
===  TA/27_12_21/ex01.py ===
>>> moyenneEtudiant(E,EX,M,1)
11.785714285714286
>>> 
===  TA/27_12_21/ex01.py ===
>>> moyenneEtudiant(E,EX,M,10)
"etudiant n'existe pas"
>>> moyenneEtudiant(E,EX,M,2)
16.0
>>> 
===  TA/27_12_21/ex01.py ===
>>> afficherNote(EX,1)
15
10
>>> 
===  TA/27_12_21/ex01.py ===
>>> afficherNote(M,EX,1)
JAVA 15
PYTHON 10
>>> 
>>> #les chaines de caracteres
>>> #La creation
>>> s1="abcdefgh"
>>> s1
'abcdefgh'
>>> type(s1)
<class 'str'>
>>> s2='abcdefgh'
>>> type(s2)
<class 'str'>
>>> s2
'abcdefgh'
>>> s3='l'etudiant'
SyntaxError: invalid syntax
>>> s3="l'etudiant"
>>> s3
"l'etudiant"
>>> s3='l\'etudiant'
>>> s3
"l'etudiant"
>>> s="abcdefrtyughf"
>>> #l'acces
>>> s[0]
'a'
>>> s[-1]
'f'
>>> s[0:5]
'abcde'
>>> s[::-1]
'fhguytrfedcba'
>>> s*5
'abcdefrtyughfabcdefrtyughfabcdefrtyughfabcdefrtyughfabcdefrtyughf'
>>> s+"Bonjour"
'abcdefrtyughfBonjour'
>>> s
'abcdefrtyughf'
>>> 'f'in s
True
>>> "fr" in s
True
>>> "rf" in s
False
>>> 'z' in s
False
>>> s
'abcdefrtyughf'
>>> s[0]
'a'
>>> s[0]='d'
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    s[0]='d'
TypeError: 'str' object does not support item assignment
>>> list(s)
['a', 'b', 'c', 'd', 'e', 'f', 'r', 't', 'y', 'u', 'g', 'h', 'f']
>>> set(s)
{'t', 'u', 'g', 'b', 'r', 'e', 'y', 'h', 'd', 'a', 'c', 'f'}
>>> tuple(s)
('a', 'b', 'c', 'd', 'e', 'f', 'r', 't', 'y', 'u', 'g', 'h', 'f')
>>> s
'abcdefrtyughf'
>>> len(s)
13
>>> max(s)
'y'
>>> ord("y")
121
>>> chr(121)
'y'
>>> chr(123)
'{'
>>> ord('{')
123
>>> "hiba"<"Ali"
False
>>> "hiba"<"Hind"
False
>>> "hiba"<"hind"
True
>>> ord("h")
104
>>> ord("H")
72
>>> s
'abcdefrtyughf'
>>> s.upper()
'ABCDEFRTYUGHF'
>>> s.lower()
'abcdefrtyughf'
>>> L=('a', 'b', 'c', 'd', 'e', 'f', 'r', 't', 'y', 'u', 'g', 'h', 'f')
>>> L
('a', 'b', 'c', 'd', 'e', 'f', 'r', 't', 'y', 'u', 'g', 'h', 'f')
>>> "".join(L)
'abcdefrtyughf'
>>> " ".join(L)
'a b c d e f r t y u g h f'
>>> "\n".join(L)
'a\nb\nc\nd\ne\nf\nr\nt\ny\nu\ng\nh\nf'
>>> s='a\nb\nc\nd\ne\nf\nr\nt\ny\nu\ng\nh\nf'
>>> print(s)
a
b
c
d
e
f
r
t
y
u
g
h
f
>>> #Les tableaux
>>> from numpy import *
>>> zeros(8)
array([0., 0., 0., 0., 0., 0., 0., 0.])
>>> zeros((8,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> ones(8)
array([1., 1., 1., 1., 1., 1., 1., 1.])
>>> ones((8,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> ones((8,4),int)
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])
>>> ones((8,4),float)
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> ones((8,4))*5
array([[5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.]])
>>> zeros((8,4))+5
array([[5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.],
       [5., 5., 5., 5.]])
>>> eye(7)
array([[1., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 0., 1.]])
>>> identity(7)
array([[1., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 0., 1.]])
>>> array([[1,2,3],[4,5,6],[7,8,9]])
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> from numpy.random import *
>>> randint(10,50,(5,8))
array([[17, 43, 27, 40, 49, 39, 16, 17],
       [22, 26, 28, 13, 14, 12, 21, 46],
       [40, 18, 38, 32, 45, 30, 26, 47],
       [38, 24, 24, 29, 29, 15, 30, 25],
       [25, 11, 17, 10, 32, 11, 42, 16]])
>>> A=randint(10,50,(5,8))
>>> A
array([[33, 29, 21, 21, 43, 28, 28, 46],
       [26, 29, 11, 10, 42, 33, 46, 39],
       [47, 28, 40, 31, 34, 11, 39, 34],
       [29, 32, 40, 22, 44, 43, 13, 12],
       [37, 27, 17, 35, 44, 31, 39, 24]])
>>> A[0]
array([33, 29, 21, 21, 43, 28, 28, 46])
>>> A[0,0]
33
>>> A[0,3]
21
>>> A[0][3]
21
>>> A[0]
array([33, 29, 21, 21, 43, 28, 28, 46])
>>> A[:,0]
array([33, 26, 47, 29, 37])
>>> A[:3,:3]
array([[33, 29, 21],
       [26, 29, 11],
       [47, 28, 40]])
>>> A[1:5,1:5]
array([[29, 11, 10, 42],
       [28, 40, 31, 34],
       [32, 40, 22, 44],
       [27, 17, 35, 44]])
>>> A
array([[33, 29, 21, 21, 43, 28, 28, 46],
       [26, 29, 11, 10, 42, 33, 46, 39],
       [47, 28, 40, 31, 34, 11, 39, 34],
       [29, 32, 40, 22, 44, 43, 13, 12],
       [37, 27, 17, 35, 44, 31, 39, 24]])
>>> A[0,0]=200
>>> A
array([[200,  29,  21,  21,  43,  28,  28,  46],
       [ 26,  29,  11,  10,  42,  33,  46,  39],
       [ 47,  28,  40,  31,  34,  11,  39,  34],
       [ 29,  32,  40,  22,  44,  43,  13,  12],
       [ 37,  27,  17,  35,  44,  31,  39,  24]])
>>> A=randint(10,50,(5,5))
>>> A
array([[27, 12, 31, 22, 39],
       [17, 43, 28, 27, 12],
       [12, 19, 26, 24, 15],
       [25, 32, 28, 30, 40],
       [10, 10, 12, 36, 35]])
>>> from numpy.linalg
SyntaxError: invalid syntax
>>> from numpy.linalg import *
>>> A
array([[27, 12, 31, 22, 39],
       [17, 43, 28, 27, 12],
       [12, 19, 26, 24, 15],
       [25, 32, 28, 30, 40],
       [10, 10, 12, 36, 35]])
>>> det(A)
-1435781.000000001
>>> transpose(A)
array([[27, 17, 12, 25, 10],
       [12, 43, 19, 32, 10],
       [31, 28, 26, 28, 12],
       [22, 27, 24, 30, 36],
       [39, 12, 15, 40, 35]])
>>> inv(A)
array([[ 0.22236817,  0.23545791, -0.27646974, -0.26444214,  0.09219651],
       [-0.06137566, -0.02608754,  0.02417709,  0.08405739, -0.02909288],
       [-0.0679052 , -0.10920607,  0.16581777,  0.09429363, -0.06572103],
       [ 0.07046618,  0.09860626, -0.07950446, -0.13574842,  0.07688707],
       [-0.09519558, -0.12380161,  0.09700783,  0.1588362 , -0.04600911]])
>>> A
array([[27, 12, 31, 22, 39],
       [17, 43, 28, 27, 12],
       [12, 19, 26, 24, 15],
       [25, 32, 28, 30, 40],
       [10, 10, 12, 36, 35]])
>>> A*3
array([[ 81,  36,  93,  66, 117],
       [ 51, 129,  84,  81,  36],
       [ 36,  57,  78,  72,  45],
       [ 75,  96,  84,  90, 120],
       [ 30,  30,  36, 108, 105]])
>>> A
array([[27, 12, 31, 22, 39],
       [17, 43, 28, 27, 12],
       [12, 19, 26, 24, 15],
       [25, 32, 28, 30, 40],
       [10, 10, 12, 36, 35]])
>>> A*10
array([[270, 120, 310, 220, 390],
       [170, 430, 280, 270, 120],
       [120, 190, 260, 240, 150],
       [250, 320, 280, 300, 400],
       [100, 100, 120, 360, 350]])
>>> A/10
array([[2.7, 1.2, 3.1, 2.2, 3.9],
       [1.7, 4.3, 2.8, 2.7, 1.2],
       [1.2, 1.9, 2.6, 2.4, 1.5],
       [2.5, 3.2, 2.8, 3. , 4. ],
       [1. , 1. , 1.2, 3.6, 3.5]])
>>> A+A
array([[54, 24, 62, 44, 78],
       [34, 86, 56, 54, 24],
       [24, 38, 52, 48, 30],
       [50, 64, 56, 60, 80],
       [20, 20, 24, 72, 70]])
>>> A/A
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
>>> A-A
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
>>> A**A
array([[ -714244925,  -251658240, -2010103841,   977272832,  1583713495],
       [ 1681328401,   407106611,           0,  -714244925,  -251658240],
       [ -251658240,  -306639989,   603979776,           0,  1500973039],
       [ 1296002393,           0,           0,  1073741824,           0],
       [ 1410065408,  1410065408,  -251658240,           0,   618402555]],
      dtype=int32)
>>> A
array([[27, 12, 31, 22, 39],
       [17, 43, 28, 27, 12],
       [12, 19, 26, 24, 15],
       [25, 32, 28, 30, 40],
       [10, 10, 12, 36, 35]])
>>> A*A
array([[ 729,  144,  961,  484, 1521],
       [ 289, 1849,  784,  729,  144],
       [ 144,  361,  676,  576,  225],
       [ 625, 1024,  784,  900, 1600],
       [ 100,  100,  144, 1296, 1225]])
>>> dot(A,A)
array([[2245, 2523, 3063, 3726, 3907],
       [2321, 3569, 3359, 3449, 3099],
       [1709, 2373, 2432, 2661, 2571],
       [2705, 3568, 3719, 4426, 4379],
       [1834, 2280, 2330, 3118, 3355]])
>>> 
>>> A
array([[27, 12, 31, 22, 39],
       [17, 43, 28, 27, 12],
       [12, 19, 26, 24, 15],
       [25, 32, 28, 30, 40],
       [10, 10, 12, 36, 35]])
>>> A[:3,:3]*10
array([[270, 120, 310],
       [170, 430, 280],
       [120, 190, 260]])
>>> B=A[:3,:3]*10
>>> B
array([[270, 120, 310],
       [170, 430, 280],
       [120, 190, 260]])
>>> A
array([[27, 12, 31, 22, 39],
       [17, 43, 28, 27, 12],
       [12, 19, 26, 24, 15],
       [25, 32, 28, 30, 40],
       [10, 10, 12, 36, 35]])
>>> A[:3,:3]=B
>>> A
array([[270, 120, 310,  22,  39],
       [170, 430, 280,  27,  12],
       [120, 190, 260,  24,  15],
       [ 25,  32,  28,  30,  40],
       [ 10,  10,  12,  36,  35]])
>>> 