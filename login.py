import time
import hashlib

def verify_password(password, stored_password_hash):
    # Implement password verification logic here
    # Return True if the provided password matches the stored hash, False otherwise
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    x = int(password_hash, 16)
    return x == int(stored_password_hash)

def get_stored_password_hash(user):
    
    user_file = f"client/{user}pass.txt"
    try:
        with open(user_file, "r") as f:
            lines = f.readlines()
            stored_password_hash = lines[0].strip()
            return stored_password_hash
    except FileNotFoundError:
        pass

    return None

g = open('server/servervalues/g64.txt','r').read()
g = g.rstrip('\n')
g = int(g, 10)

n = open('server/servervalues/n64.txt','r').read()
n = n.rstrip('\n')
n = int(n, 10)

y = open('server/servervalues/y.txt','r').read()
y = y.rstrip('\n')
y = int(y, 10)

user = input('enter your username: ')
loc = 'server/userdata/'
file = loc + user + '.txt'

password = input('Enter password: ')

A = open(file, 'r').read()
A = A.rstrip('\n')
A = int(A, 10)

secret = 'client/' + user + 'pass.txt'

x = open(secret, 'r').read()
x = x.rstrip('\n')
x = int(x, 10)

starta = time.time()
q = (x + y) % (n - 1)
val1 = pow(g, q, n)

c = pow(g, y, n)

val = 'server/userdata/' + user + 'value.txt'
with open(val, "w") as e:
    print(val1, file=e)

challenge = 'server/userdata/' + user + 'challenge.txt'
with open(challenge, "w") as f:
    print(c, file=f)

enda = time.time()

val1 = 'server/userdata/' + user + 'value.txt'
with open(val1, 'r') as f:
    A = int(f.read().strip())

challenge = 'server/userdata/' + user + 'challenge.txt'
with open(challenge, 'r') as f:
    c = int(f.read().strip())

with open(file, 'r') as f:
    b = int(f.read().strip())

starta = time.time()
d = c * b
k2 = d % n

if A == k2:
    stored_password_hash = get_stored_password_hash(user)
    if verify_password(password, stored_password_hash):
        print("Correct Password")
        print("Successfully logged into system")
        print("==============================")
        with open('server/sensitive-data/data.txt', 'r') as f:
            data = f.read().strip()
            print(data)
        print("==============================")
else:
    print("Wrong Password!")
    print("Logged out!")



enda = time.time()
print('Time to complete calculations:')
print(enda - starta)
