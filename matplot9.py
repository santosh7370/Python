# Visualize the clusters 
import matplotlib.pyplot as plt 
plt.scatter(X[:, 0], X[:, 1], c=row_labels) 
plt.ylabel('Feature 2') 
plt.xlabel('Feature 1') 
plt.show() 
