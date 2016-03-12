class PrimeFactorizer:

    def __init__(self, num):
        self.factor = {}
        for i in xrange(2, num + 1): 
            if (num < i):
                break
            while(num % i == 0):
                #print num
                num /= i
                self.factor[i] = self.factor.get(i, 0) + 1

###import psyco; psyco.full()
##from math import sqrt, ceil
##import numpy as np
##
##class PrimeFactorizer:
##    #your code here
##    def __init__(self, num):
##        self.num = num
##        
##    #6k-1 and 6k+1 <= sqrt(n) and not divisible by n; k =1,2,3...
##    def isprime(self, n):
##        n *= 1.0
##        if n%2==0 and n!=2 or n%3==0 and n!=3:
##            return False
##        for b in range(1,int((n**0.5+1)/6.0+1)):
##            if n%(6*b-1)==0:
##                return False
##            if n %(6*b+1)==0:
##               return False
##        return True
##
##    def primesfrom2to(self, n):
##        # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
##        """ Input n>=6, Returns a array of primes, 2 <= p < n """
##        sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
##        sieve[0] = False
##        for i in xrange(int(n**0.5)/3+1):
##            if sieve[i]:
##                k=3*i+1|1
##                sieve[      ((k*k)/3)      ::2*k] = False
##                sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
##        return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]
##
##    @property
##    def factor(self):
##
##        #check if the input number is a prime
##        a = self.num
##        prime = []
##        result = {}
##
##        if PrimeFactorizer.isprime(self, a):
##            return {a:1}
##
##        prime = PrimeFactorizer.primesfrom2to(self, int(sqrt(a)+1))
##    
##        #now check the prime factors of num
##        for e in prime:
##            count = 0
##            q, r = divmod(a,e)
##            while r == 0:
##                result[e] = count + 1
##                count += 1
##                q, r = divmod(q, e)
##        return result

#p = PrimeFactorizer(13)
#print p.factor()            
print PrimeFactorizer(9999971*9999973).factor

        #generate prime factors till num
##        i = range(2, a)
##        for x in i:
##            comp=[]
##            for y in range(i.index(x), len(i)):
##                q = x * i[y]
##                if q <= max(i):
##                    comp.append(q) 
##                else:
##                    break
##            for z in comp:
##                i.remove(z)
##        prime = i
