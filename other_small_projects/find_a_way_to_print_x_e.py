def findSubStr01(substr, str):
    i=1
    while i > 0:
        index = str.find(substr)   #第一次出现的位置
        index2=str.find(substr,index+1)  #第二次出现的位置
        index3=str.find(substr,index2+1)  #第三次出现的位置
        print(index)
        print(index2)
        print(index3)
        i-=1

# print(findSubStr01('abc','abc a abc'))


def findSubStr(substr, str, i):
    count = 0
    num = 1
    while i > 0:
        print('This is the {} time: '.format(num))
        print('The str now is: {}'.format(str))
        index = str.find(substr)
        print('The index now is: {}'.format(index))
        if index == -1:
            return -1
        else:
            str = str[index+1:]   #第一次出现的位置截止后的字符串
            print('The changed str is {}'.format(str))
            i -= 1
            num += 1
            count = count + index + 1   #字符串位置数累加
            print('The orignial count number now is: {}'.format(count))
            print('----------------------------------')
    return count - 1

print(findSubStr('e','e e e', 3))