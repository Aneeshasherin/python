a={'a':1,'b':9,'c':8,}
b={'d':7,'e':4,'f':6}
c=a|b
d=dict(sorted(c.items()))
e=dict(sorted(c.items(), reverse=True))
print(d)
print(e)