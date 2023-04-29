# 
arr = [1,2,3,4]

def find_product(lst):
    result = []
    a=0
    while len(result) != len(lst):
         product = 1
         count = 0
         while(count<len(lst)):
             if count==a:
                count+=1
                continue
             else:
                 product *=lst[count]
                 count+=1
         a+=1
         result.append(product)
    return(result)


print(find_product(arr))

