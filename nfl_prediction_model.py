from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier


numerical_features = ['week', 'down', 'yards_to_go']
categorical_features = ['posteam', 'defteam', 'offense_personnel', 'defense_personnel']


numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')


preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])


model = RandomForestClassifier(n_estimators=100, random_state=42)


pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
])


print("Pipeline configuration:")
print(pipeline)

# Note: You can add code here to load data and fit the model if needed
