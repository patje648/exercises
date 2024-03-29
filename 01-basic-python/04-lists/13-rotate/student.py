# Write your code here
def rotate(xs,n):
    for i in range(n):
        xs.append(xs[0])
        del xs[0]
    print(xs)