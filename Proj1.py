#print("Manasa")
b,c,d= 2,3,"Great"
#print("{}" "{}".format("Value is ",  b))

Manasa = [1,2,3,"Great",7]
print(Manasa[0]) #1
print(Manasa[-1]) #7
print(Manasa[1:3]) #2,3
print(Manasa[:4]) #All values
(Manasa.insert(4, "together"))
print(Manasa)
Manasa.append("End")
print(Manasa)

Manasa[3] = "GREAT"
print(Manasa)
del Manasa[0]
print(Manasa)

Man = (1,2,3,"HH", 6.7)
print(Man[3])

dic = {0: 1, "a": 0.9, "b": "Great"}
print(dic[0])
print(dic["a"])
print(dic["b"])

gg = {}
gg["gender"] = "Female"
gg[1] = "tt"
gg[7]= 0.8
print(gg)