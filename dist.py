import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails = []
for i in range(100) :
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(coin)
    print('X',i+1,'=',tails,', E =', sum(tails))
    final_tails.append(sum(tails))
print(final_tails)
plt.hist(final_tails, bins = 10)
plt.show()

# Random Variable X = [X1,X2,X3.......,X100]
# X1 =