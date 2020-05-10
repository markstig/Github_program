# https://blog.csdn.net/Jerry_1126/article/details/85224586

# Show in one row
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d'%(i,j,j*j), end='\t')

print('-----------------------------')

for i in range(1, 10):
    for j in range(1, i+1):
        if i == j:
            print('%d*%d=%d'%(i,j,i*j), end = '\n')
        else:
            print('%d*%d=%d'%(i,j,i*j), end = '\t')

print('-----------------------------')

for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d'%(i,j,i*j), end='\t')
    print()

print('-----------------------------')
for i in range(1,10):
    print('\t'.join('{i}*{j}={m}'.format(i=i, j=j, m=i*j) for j in range(1, i+1)))


