from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Step 2: Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 3: Train a simple Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 4: Make predictions
predictions = model.predict(X_test)

# Step 5: Show accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"🌸 Model Accuracy: {accuracy:.2f}")
