from math import sqrt

# def prime_numbers(n):  #GIVES ALL NUMS
#     prime_nums = []
#     for p in range(2, n+1):
#         for i in range(2, p):
#             if p % i == 0:
#                 break
#         else:
#             prime_nums.append(p)
#         p+=1
#     return prime_nums
           

def prime_numbers(n):  #CHECKS IF NUM IS PIME W/ SQRT LIST
    prime_nums = []
    # z = int(sqrt(n))
    # print z
    for p in range(2, int(sqrt(n))+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            prime_nums.append(p)
        p+=1
    return prime_nums
            
print prime_numbers(20)


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



def prime_factors(n):
    prime_factors = []
    p = prime_numbers(n)
    for i in range (0, p[-1]):
        if n%p[i] ==0:
            print p[i]
            prime_factors.append(p[i])
            d = Decimal(n)/Decimal(p[i])
            while i in range (0, d+1):
                if d%p[i] ==0:
                    prime_factors.append(p[i])
                    i+=1
                    return prime_factors
                else:
                    i+=1
            # else:
            #     i+=1
            # print "check2"
            return prime_factors
        else:
            i+=1
    return prime_factors
    print "check3"

    def prime_factors(n):
    prime_factors = []
    p = prime_numbers(n)
    for i in range (0, p[-1]):
        if n%p[i] ==0:
            print p[i]  #check
            prime_factors.append(p[i])
            d = Decimal(n)/Decimal(p[i])
            print d  #check
            for i in range (0, ((prime_numbers(d))[-1])):  #NOT GIVING THE CORRECT #S
                print i  # check
                print d
                if d%p[i] ==0:
                    print p[i]  #check
                    prime_factors.append(p[i])
                    print p[i] #check
                    i+=1
                    return prime_factors
                else:
                    i+=1
            # else:
            #     i+=1
            # print "check2"
            return prime_factors
        else:
            i+=1
    return prime_factors
    print "check3"

print prime_factors(75)