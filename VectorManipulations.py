import math
class Vector:
  # TODO: Finish the Vector class.
    def __init__(self, input_vector):
        self.input_vector = input_vector
    
    def add(self, add_vector):
        """ Returns sum of the 2 vectors"""
        if len(self.input_vector) != len(add_vector.input_vector):
                raise ValueError("Lengths of both the vectors are different")
        return Vector([ip1 + ip2 for ip1, ip2 in zip(self.input_vector, add_vector.input_vector)])
     
    def subtract(self, sub_vector):
        """ Returns subtraction of the 2 vectors"""
        if len(self.input_vector) != len(sub_vector.input_vector):
                raise ValueError("Lengths of both the vectors are different")
        return Vector([ip1 - ip2 for ip1, ip2 in zip(self.input_vector, sub_vector.input_vector)])

    def dot(self, dot_vector):
        """ Returns dot or inner product of the 2 vectors"""
        if len(self.input_vector) != len(dot_vector.input_vector):
                raise ValueError("Lengths of both the vectors are different")
        return sum(ip1 * ip2 for ip1, ip2 in zip(self.input_vector, dot_vector.input_vector)) 
        
    def norm(self):
        """ Returns norm (magnitude) of this vector"""
        return math.sqrt(sum( ip**2 for ip in self.input_vector ))
    
    def toString(self):
        """ returns the vector as a string """
        s = str(tuple(self.input_vector))
        i = 0
        while i < len(s):
            if s[i] == " ":
                s = s[:i] + s[i+1:]
            i = i + 1
        return s
    def equals(self, result):
        """equals function for testing the results"""
        return bool(self.toString() == result.toString())

a = Vector([1,2])
b = Vector([3,4])
c = Vector([1,2,3])
print a.add(b)
print a.subtract(b)
##print a.dot(b)
##print a.norm()
print a.subtract(b).toString()
print c.toString()

