with open(r'test.txt', 'a') as f:
    f.write('乔')

import pickle

a = [19, 'qiao', 'ming', [185, 76]]
# with open(r'test01.txt', 'wb') as f:
#     pickle.dump(a, f)

with open(r'test01.txt', 'rb') as f:
    b = pickle.load(f)
    print(b)
