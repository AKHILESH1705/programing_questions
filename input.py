from sklearn import tree
clf= tree.DecisionTreeClassifier()
x=[[180,15,0],
   [167,42,1],
   [136,35,1],[174,15,0],
   [155,25,1]]
y=['men','woman' ,'woman', 'men', 'woman']
clf=clf.fit(x,y)
prediction=clf.predict([[180,15,0]])
print(prediction)