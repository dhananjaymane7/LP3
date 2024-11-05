import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv(r"F:\7. Seventh Seemester Degeree\ML Assignments\email_spam\emails.csv")
print(data.columns)

# Access the correct label column (replace 'Prediction' with the actual label column name)
y = data['Prediction'] 

# Display the first few rows of the dataset
print(data.head())

# Assuming 'text' is the column with email content and 'label' indicates spam or not
data['text'] = data['text'].astype(str)  # Ensure text is string
X = data['text']
y = data['label']  # Change to the appropriate column name for labels

# Feature extraction
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# K-Nearest Neighbors Classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Support Vector Machine Classifier
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

# Evaluate performance
print("KNN Classification Report:")
print(classification_report(y_test, y_pred_knn))
print("KNN Accuracy:", accuracy_score(y_test, y_pred_knn))

print("\nSVM Classification Report:")
print(classification_report(y_test, y_pred_svm))
print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
