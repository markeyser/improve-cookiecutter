# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the iris dataset
iris = datasets.load_iris()

# Convert to DataFrame
iris_df = pd.DataFrame(
    data=np.c_[iris["data"], iris["target"]],
    columns=iris["feature_names"] + ["target"],
)

# Print first 5 rows of the dataset
print(iris_df.head())

# Get the statistical summary of the DataFrame
print(iris_df.describe())

# Check for null values
print(iris_df.isna().sum())

# Data visualization using seaborn pairplot
sns.pairplot(iris_df, hue="target")
plt.show()

# Correlation matrix
corr_mat = iris_df.corr()
sns.heatmap(corr_mat, annot=True)
plt.show()

# Split the dataset into features and target variable
X = iris_df.iloc[:, :-1]
y = iris_df.iloc[:, -1]

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the logistic regression model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred))

# Print the confusion matrix
print(confusion_matrix(y_test, y_pred))

# Print the accuracy score
print(accuracy_score(y_test, y_pred))

# Predicting on new data
new_data = np.array([[5.1, 3.4, 1.5, 0.2]])
new_data = scaler.transform(new_data)
new_pred = model.predict(new_data)

# Print the new prediction
print("Prediction for new data: ", new_pred)
