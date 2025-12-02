d = {3: "apple", 1: "banana", 2: "cherry"}
ascending = dict(sorted(d.items()))
descending = dict(sorted(d.items(), reverse=True))
print("Ascending order:", ascending)
print("Descending order:", descending)
