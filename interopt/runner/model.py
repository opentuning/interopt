import ast
import os
import tempfile

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#from autogluon.tabular import TabularDataset, TabularPredictor
from catboost import CatBoostRegressor

def load_catboost_models(tab, benchmark_name, dataset, objectives, features):
    models = {}
    for objective in objectives:
        model_root = 'models'
        os.mkdir(model_root) if not os.path.exists(model_root) else None
        model_path = f'{model_root}/{benchmark_name}_{dataset}_{objective}.cbm'
        if os.path.exists(model_path):
            catboost_model = CatBoostRegressor()
            print(f"Loading model for {objective}")
            catboost_model.load_model(model_path)
        else:
            print(f"Training model for {objective}")
            catboost_model = train_model(tab, objective, benchmark_name, features)
            print(f"Saving model for {objective}")
            catboost_model.save_model(model_path)
        models[objective] = catboost_model

    return models

def load_autogluon_models(tab, benchmark_name, dataset, objectives, features):
    models = {}
    for objective in objectives:
        model_root = 'models'
        os.mkdir(model_root) if not os.path.exists(model_root) else None
        model_path = f'{model_root}/{benchmark_name}_{dataset}_{objective}'
        if os.path.exists(model_path):
            print(f"Loading model for {objective}")
            autogluon_model = TabularPredictor.load(model_path)
        else:
            print(f"Training model for {objective}")
            autogluon_model = train_model(tab, objective, benchmark_name, features)
            print(f"Saving model for {objective}")
            autogluon_model.save(model_path)
        models[objective] = autogluon_model

    return models


catboost = True

def load_models(tab, benchmark_name, dataset, objectives, features):
    if catboost:
        models = load_catboost_models(tab, benchmark_name, dataset, objectives, features)
    else:
        models = load_autogluon_models(tab, benchmark_name, dataset, objectives, features)
    return models

def train_model(input_tab, objective, benchmark_name, in_features):
    features = in_features.copy()
    tab = input_tab.copy()
    print(tab)
    tab.reset_index(inplace=True)
    if "permutation" in features:
        features.remove('permutation')
        tab['tuple_str'] = tab['permutation'].apply(ast.literal_eval)
        for i in range(5):
            tab[f'tuple_permutation_{i}'] = tab['tuple_str'].apply(lambda x: x[i])
        features.extend([f'tuple_permutation_{i}' for i in range(5)])

    # Assume 'df' is your DataFrame
    X = tab[features]

    y = tab[objective]
    # Convert the y vector into a log scale
    y = np.log(y)

    # Splitting the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize CatBoostRegressor
    if catboost:
        with tempfile.TemporaryDirectory() as tmpdirname:
            catboost_model = CatBoostRegressor(silent=True, train_dir=tmpdirname)

            # Fit model
            catboost_model.fit(X_train, y_train)
        y_pred = catboost_model.predict(X_test)
    else:
        # Autogluon expects the complete dataframe as input, e.g. both X and Y in one dataframe
        df_train = X_train.copy()
        df_train[objective] = y_train
        print(df_train.head(), df_train.shape, df_train.columns)
        autogluon_model = TabularPredictor(label=objective, path='models').fit(
            train_data=TabularDataset(df_train), presets='high_quality', time_limit=180)
        y_pred = autogluon_model.predict(X_test)
        df_test = X_test.copy()
        df_test[objective] = y_test
        autogluon_model.leaderboard(df_test)

    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Catboost" if catboost else "AutoGluon")
    print(f"Metrics for {objective}")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R-squared: {r2}")

    return catboost_model if catboost else autogluon_model
