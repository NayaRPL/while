print("perulangan  while")
#perulangna while sangat berkaitan dengan varian boolean, atau logical statment.
baris=5
i=1
while i <= baris:
    j=1
    while j<=i:
        print('%d'%(i*j), end ='')
        j+=1
    print()
    i+=1
print('while yang di kombinasikan dengan for')
baris = 5
for i in range(1, baris+1):
    j=1
    while j<=i:
           print('%d' % (i*j), end ='')
           j +=1
    print()
print("atau")
baris = 5
i=1
while i <= baris:
        for j in range (1,i+1):
            print('%d' % (i*j), end ='')
        print()
        i +=1
   
