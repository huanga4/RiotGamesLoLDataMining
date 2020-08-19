import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import plot_tree

'''
    Author: Philip Quinn
    Course: Data Mining I
    Purpose: Game outcome predictor
    Data Source: ./gameInfo.csv
    Description: gameInfo obtained from Riot API calls (10482 games).
    Trained for classification of a winning team. A more accurate model would be one that is time series   
'''

gameInfo = pd.read_csv('gamesInfo.csv')
features = []
classes = ["100", "200"]
for col in gameInfo.columns:
    if col != 'winner':
        features.append(col)
print(gameInfo.shape)

# Drop null values
gameInfo = gameInfo.dropna()
print(gameInfo.shape)

X = gameInfo.iloc[:, 1:-1].to_numpy()
Y = gameInfo.iloc[:, -1].to_numpy()


# Min max scaler
scaler = MinMaxScaler()
scaler.fit(X)
X = scaler.transform(X)

# Train test split 70/30
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

# Logistic Regression
lg = LogisticRegression(random_state=0, max_iter=10000).fit(X_train, y_train)
y_pred = lg.predict(X_test)
print(y_pred)
print("Logistic Regression Accuracy: " + str(round(sum(y_pred==y_test)/len(y_pred)*100, 2)) + "%")

# Generate results
cm = confusion_matrix(y_test, y_pred, labels=[100, 200])
print("Report: \n", classification_report(y_test, y_pred))
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion matrix of the Logistic Regression Classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + ['Team 1', 'Team 2'])
ax.set_yticklabels([''] + ['Team 1', 'Team 2'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Decision tree
dt = DecisionTreeClassifier()

# Train decision tree
dt.fit(X_train, y_train)

# Make predictions on test data
y_pred = dt.predict(X_test)
a = plot_tree(dt,
              feature_names=features,
              class_names=classes,
              filled=True,
              rounded=True,
              fontsize=14)

print("Decision Tree Accuracy: " + str(round(sum(y_pred==y_test)/len(y_pred)*100, 2)) + "%")

# Generate results
cm = confusion_matrix(y_test, y_pred, labels=[100, 200])
print("Report: \n", classification_report(y_test, y_pred))
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion matrix of the Decision Tree Classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + ['Team 1', 'Team 2'])
ax.set_yticklabels([''] + ['Team 1', 'Team 2'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Naive Bayes
gnb = GaussianNB()

# Train
gnb.fit(X_train, y_train)

# Predict on test data
y_pred = gnb.predict(X=X_test)
print("Naive Bayes Accuracy: " + str(round(sum(y_pred==y_test)/len(y_pred)*100, 2)) + "%")

# Generate results
cm = confusion_matrix(y_test, y_pred, labels=[100, 200])
print("Report: \n", classification_report(y_test, y_pred))
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion matrix of the Naive Bayes Classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + ['Team 1', 'Team 2'])
ax.set_yticklabels([''] + ['Team 1', 'Team 2'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Neural Network
nn = MLPClassifier(solver='lbfgs', alpha=0.0001, hidden_layer_sizes=(4, 2), random_state=1, max_iter=10000).fit(X_train, y_train)

y_pred = nn.predict(X_test)
print("Neural Network Accuracy: " + str(round(sum(y_pred==y_test)/len(y_pred)*100, 2)) + "%")

# Generate results
cm = confusion_matrix(y_test, y_pred, labels=[100, 200])
print("Report: \n", classification_report(y_test, y_pred))
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion matrix of the Neural Network Classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + ['Team 1', 'Team 2'])
ax.set_yticklabels([''] + ['Team 1', 'Team 2'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
