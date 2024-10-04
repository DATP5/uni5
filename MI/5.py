from sklearn import tree
X = [
        [0,1,0,0],
        [1,0,1,0],
        [0,0,1,1],
        [0,0,1,0],
        [0,0,0,1],
        
        [1,0,0,1],
        [1,0,0,0],
        [0,1,1,0],
        [0,1,1,0],
        [1,1,1,0],

        [1,1,0,1],
        [0,0,0,0]
        ]
Y = [0,1,1,0,0,0,1,1,0,1,0,0]
clf = tree.DecisionTreeClassifier()
clf.fit(X,Y)
tree.plot_tree(clf)
