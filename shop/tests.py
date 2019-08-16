from django.test import TestCase

# Create your tests here.

a=[1,4,5]
b=sum(a)
z=len(a)+2
c=(z*(z+1)/2)
print("",c-b)

# list1=[]
# for i in range(0,len(a)+1):
#     list1.append(i)
# print(list1)
def missing_numbers(num_list):
    print(range(num_list[0], num_list[-1] + 1))
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    print(original_list)
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))


print(missing_numbers([1,2, 4, 5]))
