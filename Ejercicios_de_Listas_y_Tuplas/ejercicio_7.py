abecedario_es = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = []
for i in range(2,len(abecedario_es),+3):
   num.append(i)

for numero in reversed(num):
   del abecedario_es[numero]

# del abecedario_es[2::3]
print(abecedario_es)