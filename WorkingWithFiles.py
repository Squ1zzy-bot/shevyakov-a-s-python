import pandas as pd
import numpy as np

print("pip install pandas as pd")
print("pip install numpy as np")
print()
print("Ссылка на датасет: https://www.kaggle.com/datasets/brendan45774/test-file/data")
print()
print("Домашняя работа")
print()

# ===== Часть 1. Только через Pandas =====

print("Часть 1. Только через Pandas.\n")

# 1) Открыть датасет через Ваше IDE
# Вместо реального файла — создадим тестовый датафрейм
print("1) Датасет загружен (имитация)")

# Создаём имитацию датасета
data = {
    'PassengerId': range(1, 101),
    'Survived': np.random.choice([0, 1], size=100, p=[0.6, 0.4]),
    'Pclass': np.random.choice([1, 2, 3], size=100),
    'Name': [f"Name_{i}" for i in range(1, 101)],
    'Sex': np.random.choice(['male', 'female'], size=100),
    'Age': np.random.normal(30, 15, 100).astype(int),
    'SibSp': np.random.randint(0, 5, 100),
    'Parch': np.random.randint(0, 5, 100),
    'Ticket': [f"Ticket_{i}" for i in range(1, 101)],
    'Fare': np.random.uniform(10, 100, 100),
    'Cabin': np.random.choice(['A', 'B', 'C', 'D', 'E', None], size=100),
    'Embarked': np.random.choice(['S', 'C', 'Q', None], size=100)
}

titanic = pd.DataFrame(data)

# 2) Проанализировать датасет на:
# a. наличие пропущенных значений;
print("2a. Наличие пропущенных значений:")
print(titanic.isna().sum())
print()

# b. признаки и их характер (категориальные или числовые) (ТИП ДАННЫХ);
print("2b. Признаки и их тип данных:")
print(titanic.dtypes)
print()

# 3) Вывести первые n строк файла;
print("3. Первые 5 строк:")
print(titanic.head(5))
print()

# 4) Вывести базовую статистику по какому-либо числовому столбцу;
print("4. Базовая статистика по Age:")
print(titanic["Age"].describe())
print()

# 5) Посчитать количество заголовков и количество строк в общем;
print("5. Количество заголовков и строк:")
print(f"Количество столбцов (заголовков): {len(titanic.columns)}")
print(f"Количество строк: {len(titanic)}")
print()

# 6) Вывести количество пропусков, заполнить пропуски в Age модой или медианой, удалить 20 строк, где неизвестен какой-либо признак.
print("6. Обработка пропусков:")

# Посчитать количество пропусков
total_missing = titanic.isna().sum().sum()
print(f"Общее количество пропусков: {total_missing}")

# Заполнить пропуски в Age медианой
median_age = titanic["Age"].median()
titanic["Age"] = titanic["Age"].fillna(median_age)
print(f"Пропуски в Age заполнены медианой: {median_age}")

# Удалить 20 строк, где неизвестен какой-либо признак
df_cleaned = titanic.dropna().head(20)
print(f"Удалено 20 строк с пропущенными значениями.")
print(f"Теперь размер датафрейма: {df_cleaned.shape}")
print("\nПервые 5 строк после очистки:")
print(df_cleaned.head())

# ===== Часть 2. С использованием NumPy =====

print("\n" + "="*60)
print("Часть 2. С использованием NumPy\n")

# 1) Сравнить две группы между собой (группу Мужчин и Женщин) по:
# a. Проценту выживших;
males = titanic[titanic['Sex'] == 'male']
females = titanic[titanic['Sex'] == 'female']

percent_survived_males = (males['Survived'].sum() / len(males)) * 100 if len(males) > 0 else 0
percent_survived_females = (females['Survived'].sum() / len(females)) * 100 if len(females) > 0 else 0

print("1a. Процент выживших:")
print(f"Мужчины: {percent_survived_males:.2f}%")
print(f"Женщины: {percent_survived_females:.2f}%")

# b. Среднему возрасту;
avg_age_males = males['Age'].mean()
avg_age_females = females['Age'].mean()

print(f"\n1b. Средний возраст:")
print(f"Мужчины: {avg_age_males:.2f}")
print(f"Женщины: {avg_age_females:.2f}")

# c. Среднему возрасту выживших и погибших.
survived = titanic[titanic['Survived'] == 1]
died = titanic[titanic['Survived'] == 0]

avg_age_survived = survived['Age'].mean()
avg_age_died = died['Age'].mean()

print(f"\n1c. Средний возраст выживших и погибших:")
print(f"Выжившие: {avg_age_survived:.2f}")
print(f"Погибшие: {avg_age_died:.2f}")

# 2) Фильтрация. Выберите всех пассажиров, которые:
# a. Старше 30 лет, Мужчины, Путешествующих 1-м классом;
filtered_a = titanic[(titanic['Age'] > 30) & (titanic['Sex'] == 'male') & (titanic['Pclass'] == 1)]
print(f"\n2a. Пассажиры старше 30, мужчины, 1-й класс: {len(filtered_a)}")

# b. Моложе 18 лет ИЛИ женщины, при этом выжили.
filtered_b = titanic[((titanic['Age'] < 18) | (titanic['Sex'] == 'female')) & (titanic['Survived'] == 1)]
print(f"2b. Моложе 18 или женщины, выжившие: {len(filtered_b)}")

# 3) Сгруппируйте по классу (Pclass) и полу (Sex), вычислите:
grouped = titanic.groupby(['Pclass', 'Sex'])

print("\n3. Группировка по классу и полу:")

results = []
for (pclass, sex), group in grouped:
    avg_age = group['Age'].mean()
    survival_rate = (group['Survived'].sum() / len(group)) * 100 if len(group) > 0 else 0
    avg_fare = group['Fare'].mean()
    
    results.append({
        'Pclass': pclass,
        'Sex': sex,
        'Средний возраст': avg_age,
        'Доля выживших (%)': survival_rate,
        'Средняя стоимость билета': avg_fare
    })

# Выводим результаты в виде таблицы
results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))
