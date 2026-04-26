N = input()

logged_in = False
Error = 0

for i in range(N):
    s = input()

    if s == "login":
        logged_in = True
    if s == "logout":
        logged_in = False

    if s == 'private' and not logged_in:
        Error += 1

print(Error)
