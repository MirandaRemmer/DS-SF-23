from math import sqrt
from decimal import Decimal

def prime_numbers(n):
    prime_nums = []
    # z = int(sqrt(n))
    # print z
    for p in range(2, int(sqrt(n))+1):
        # print p
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            prime_nums.append(p)
        p+=1
    return prime_nums
           

           


# def prime_factors(n):
#     prime_factors = []
#     p = prime_numbers(n)
#     i = 0
#     while n%p[i] != 0:
#         i +=1
#     else:
#         prime_factors.append(p[i])
#         d = n/p[i]
#         while d%p[i] !=0:
#             i +=1
#         else:
#             prime_factors.append(p[i])
#             d = n/p[i]
#             while d%p[i]
#     return prime_factors
   



    # if n / num in prime_nums:
    #     prime_factors.append(d)



# def prime_factors(n):
#     prime_factors = []
#     p = prime_numbers(n)
#     # i = 0
#     # factorial = (n%p[i] ==0)
#     for i in range (0, p[-1]):
#         if n%p[i] ==0:
#         # if factorial == True:
#             prime_factors.append(p[i])
#             return prime_factors
#             d = Decimal(n)/Decimal(p[i])
#             print d
#             while d%p[i] ==0:
#                 prime_factors.append(p[i])
#                 i+=1
#             else:
#                 i+=1
#         else:
#             i+=1
#     return prime_factors




# def prime_tree(nt):
#     pt = prime_numbers(nt)
#     i = 0
#     dt = Decimal(nt)/Decimal(pt[i])
#     for i in range (0, pt[-1]):
#         print i
#         if dt%pt[i] ==0:
#             prime_factors.append(pt[i])
#             i+=1
#         else:
#             i+=1

# prime_tree(75)


#BEST ONE!!!

# def prime_factors(n):
#     prime_factors = []
#     p = prime_numbers(n)
#     for i in range (0, p[-1]):
#         d = Decimal(n)/Decimal(p[i])
#         if n%p[i] ==0:
#             print p[i]  #check
#             prime_factors.append(p[i])
#             if d%p[i] == 0:
#                 print d  #check
#                 prime_factors.append(p[i])
#                 return prime_factors
#             else:
#                 i+=1
#         else: 
#             i+=1

# print prime_factors(13195)


# def prime_factors(n):
#     prime_factors = []
#     p = prime_numbers(n)
#     print p[-1] #check
#     for i in range (0, p[-1]):
#         while n%p[i] != 0:
#             i+=1
#         ##WHILE REMAINDER DOESNT EQUAL ZERO, 
#         ##KEEP GOING THROIGH THE LIST.. 
#         ##WHEN IT REACHES A # THAT IS EVENLY DIVISIBLE, 
#         ##ADD IT TO THE LIST 
#         ##AND THEN USE THAT NUMBER TO CALCULTE IT'S FACTORS 
#         else:
#             prime_factors.append(p[i])
#             d = Decimal(n)/Decimal(p[i])
#             print d #check
#             df = prime_numbers(d)
#             print df
#             # while d%p[i]
#             for f in range (0, df[-1]):
#                 while d%df[i] !=0:
#                     i+=1
#             else:
#                 prime_factors.append(df[i])
#                 f+=1
#         i+=1
#     return prime_factors

# def prime_factors(n):   #ALMOST WORKS
#     prime_factors = []
#     p = prime_numbers(n)
#     print p[-1] #check
#     for i in range (0, p[-1]):
#         if n%p[i] != 0:
#             i+=1
#         ##WHILE REMAINDER DOESNT EQUAL ZERO, 
#         ##KEEP GOING THROIGH THE LIST.. 
#         ##WHEN IT REACHES A # THAT IS EVENLY DIVISIBLE, 
#         ##ADD IT TO THE LIST 
#         ##AND THEN USE THAT NUMBER TO CALCULTE IT'S FACTORS 
#         else:
#             prime_factors.append(p[i])
#             d = Decimal(n)/Decimal(p[i])
#             print "d:", d #check
#             for i in range (0, p[-1]):
#                 if d%p[i] !=0:
#                     break
#                 else:
#                     prime_factors.append(p[i])
#                     i+=1
#                     return prime_factors
#                 i+=1
#             return prime_factors
#     return prime_factors


# def prime_factors(n):
#     prime_factors = []
#     p = prime_numbers(n)
#     print p[-1] #check
#     for i in range (0, p[-1]):
#         if n%p[i] != 0:
#             i+=1
#         ##WHILE REMAINDER DOESNT EQUAL ZERO, 
#         ##KEEP GOING THROIGH THE LIST.. 
#         ##WHEN IT REACHES A # THAT IS EVENLY DIVISIBLE, 
#         ##ADD IT TO THE LIST 
#         ##AND THEN USE THAT NUMBER TO CALCULTE IT'S FACTORS 
#         else:
#             prime_factors.append(p[i])
#             d = Decimal(n)/Decimal(p[i])
#             print "d:", d #check
#             for i in range (0, p[-1]):
#                 if d%p[i] ==0:
#                     prime_factors.append(p[i])
#                     i+=1
#                     return prime_factors
#                 i+=1
#             #return prime_factors
#             i+=1
#             return prime_factors
#     return prime_factors


# print prime_numbers(13195)
# print prime_factors(13195)



def prime_factors(n):
    i=2
    factors = []
    while i*i <= n:
        if n%i:
            i += 1
        else:
            n//=i
            factors.append(i)
    if n>1:
        factors.append(n)
    return factors

print prime_factors(13195)
