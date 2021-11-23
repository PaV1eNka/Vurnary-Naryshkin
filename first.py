def commit(a):
    return a[0], a[1], a[2]


s = "My first git-repo"
p = s.split()
print(commit(p))