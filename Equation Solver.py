print("-----------------------------------------")
print("Linear equation solver upto 3 variables")
print("*****************************************")
import numpy as np
x=y=z=0
print("Linear Equation of the form ax + by +cz = d")
print("-----------------------------------------")
#Asking for number of variables
n=int(input("For 2 variables enter 2, for 3 variables enter 3: "))
#Code for 2 variables
#Getting values from user
if n == 2:
    print("For 1st equation-")
    a1=float(input("Enter coefficient of x="))
    b1=float(input("Enter coefficient of y="))
    c1=float(input("Enter constant term="))
    print("-----------------------------------------")
    print("For 2nd equation-")
    a2=float(input("Enter coefficient of x="))
    b2=float(input("Enter coefficient of y="))
    c2=float(input("Enter constant term="))
    print("-----------------------------------------")
#Solutions
    if a1/a2 != b1/b2:
        A = np.array([[a1,b1],[a2,b2]])
        B = np.array([[c1],[c2]])
        X = np.linalg.inv(A).dot(B)
        print("The solution of these equation are- ")
        print("x=",X[0])
        print("y=",X[1])
    elif a1/a2 == b1/b2 and b1/b2 != c1/c2:
        print("The given set of equations has NO SOLUTION")
    elif a1/a2 == b1/b2 and b1/b2 == c1/c2:
        print("The given set of equation has INFINITE SOLUTION")
#Code for 3 variables
#Getting values from user
elif n == 3:
    print("For 1st equation-")
    a1=float(input("Enter coefficient of x="))
    b1=float(input("Enter coefficient of y="))
    c1=float(input("Enter coefficient of z="))
    d1=float(input("Enter constant term="))
    print("-----------------------------------------")
    print("For 2nd equation-")
    a2=float(input("Enter coefficient of x="))
    b2=float(input("Enter coefficient of y="))
    c2=float(input("Enter coefficient of z="))
    d2=float(input("Enter constant term="))
    print("-----------------------------------------")
    print("For 3rd equation-")
    a3=float(input("Enter coefficient of x="))
    b3=float(input("Enter coefficient of y="))
    c3=float(input("Enter coefficient of z="))
    d3=float(input("Enter constant term="))
    print("-----------------------------------------")
    A = np.array([[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]])
#Determining cofactors
    c11=(b2*c3)-(c2*b3)
    c12=(c2*a3)-(a2*c3)
    c13=(a2*b3)-(b2*a3)
    c21=(b3*c1)-(b1*c3)
    c22=(a1*c3)-(c1*a3)
    c23=(b1*a3)-(a1*b3)
    c31=(b1*c2)-(c1*b2)
    c32=(c1*a2)-(a1*c2)
    c33=(a1*b2)-(b1*a2)
#Creating adjoint
    AdjA=np.array([[c11,c12,c13],[c21,c22,c23],[c31,c32,c33]])
#Determining Null Matrix
    Null_Matrix=np.array([[0,0,0],[0,0,0],[0,0,0]])
#In case of inconsistent equations
    if np.linalg.det(A) == 0 and (AdjA == Null_Matrix).all():
        print("The given set of equations has NO SOLUTION")
#In case of consistent equation but with infinite solution
    elif np.linalg.det(A) != 0 and (AdjA == Null_Matrix).all():
        print("The given set of equation has INFINITE SOLUTION")
#In case of consistent equation and with unique solution
    else:
        X = np.array([[x],[y],[z]])
        B = np.array([[d1],[d2],[d3]])
        X=np.linalg.inv(A).dot(B)
        print("The solution of these equation are- ")
        print("x=",X[0])
        print("y=",X[1])
        print("z=",X[2])
else:
    print("Choose only between 2 and 3")
print("-----------------------------------------")
