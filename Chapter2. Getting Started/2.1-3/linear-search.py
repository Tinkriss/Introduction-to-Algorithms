
def search(array, v):
    for i in range(0, len(array), 1):
       if array[i] == v:
           return i;
    return None;

print(search([1,2,3,4,5,6], 6));
print(search([1,2,3,4,5,6], 1));
print(search([1,2,3,4,5,6], 7));