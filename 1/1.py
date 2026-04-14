import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Загружаем датасет
data = pd.read_csv('telecom_churn.csv')

# 2. Изучаем датасет
print("Количество строк и столбцов:", data.shape)
print("\nТипы данных:\n", data.dtypes)
print("\nПропуски:", data.isnull().sum().sum())
print("\nРаспределение целевой переменной 'churn':\n", data['churn'].value_counts(normalize=True))

# 3. Подготовка данных
X = data.drop('churn', axis=1)
y = data['churn']

categorical_features = ['state', 'phone number', 'international plan', 'voice mail plan']
numerical_features = [col for col in X.columns if col not in categorical_features]

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4. Обучение моделей
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
    "DecisionTreeClassifier": DecisionTreeClassifier(random_state=42),
    "KNeighborsClassifier": KNeighborsClassifier()
}

pipelines = {
    name: Pipeline(steps=[('preprocessor', preprocessor), ('classifier', model)])
    for name, model in models.items()
}

results = {}
for name, pipeline in pipelines.items():
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = {"accuracy": accuracy, "predictions": y_pred}

# 5. Сравнение accuracy моделей
accuracy_table = pd.DataFrame({
    'Model': list(results.keys()),
    'Accuracy': [results[name]['accuracy'] for name in results]
})

plt.figure(figsize=(8, 5))
sns.barplot(data=accuracy_table, x='Model', y='Accuracy')
plt.title('Сравнение accuracy моделей')
plt.ylim(0.8, 0.95)
plt.ylabel('Accuracy')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Матрица ошибок для лучшей модели
best_model_name = max(results, key=lambda x: results[x]['accuracy'])
best_model_predictions = results[best_model_name]['predictions']

cm = confusion_matrix(y_test, best_model_predictions)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Predicted False', 'Predicted True'],
            yticklabels=['Actual False', 'Actual True'])
plt.title(f'Матрица ошибок для {best_model_name}')
plt.xlabel('Предсказание')
plt.ylabel('Фактическое значение')
plt.tight_layout()
plt.show()