import string
import random
random.seed()
l=string.ascii_uppercase + string.ascii_lowercase + string.digits
N=input("I create random passwords, how long do you want your password to be? ")
N=int(N)
print("The password generated for you is:")
print("".join([random.choice(l) for i in range(N)]))
L=l+string.punctuation
print(string.punctuation)
print("A password with symbols of the same size can be:")
print("".join([random.choice(L) for i in range(N)]))
