import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd 

iris_df = pd.read_csv("iris-species.csv")
iris_df['Label'] = iris_df['Species'].map({'Iris-setosa': 0, 'Iris-virginica': 1, 'Iris-versicolor':2})

X = iris_df[['SepalLengthCm','SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = iris_df['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

svc_model = SVC(kernel='linear').fit(X_train, y_train)
score = svc_model.score(X_train, y_train)

def prediction(SepalLength, SepalWidth, PetalLength, PetalWidth):
	species = svc_model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
	species = species[0]
	if species == 0:
		return 'Iris-setosa'
	elif species ==1 :
		return 'Iris-virginica'
	else:
		return 'Iris-versicolor'

st.title('Iris Flower Species Prediction App')
s_length = st.slider("Sepal Length", 0.0, 10.0)
s_width = st.slider("Sepal Width", 0.0, 10.0)
p_length = st.slider("Petal Length", 0.0, 10.0)
p_width = st.slider("Petal Width", 0.0, 10.0)
if st.button("Predict"):
	species_type = prediction(s_length, s_width, p_length, p_width)
	st.write("Species Predicted: ", species_type)
	st.write("Accuracy of the model: ", score)