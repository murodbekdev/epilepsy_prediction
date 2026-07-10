import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.onehot_cols = []
        self.label_cols = []
        self.num_cols = []

        self.encoder = OneHotEncoder(
            sparse_output = False,
            handle_unknown = "ignore"
        )

        self.scaler = StandardScaler()

    # 1. Identify columns

    def find_columns(self, X_train):
        self.num_cols = X_train.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()
        cat_cols = X_train.select_dtypes(include=["object", "category"]).columns.tolist()

        for col in cat_cols:
            if X_train[col].nunique() <=5:
                self.onehot_cols.append(col)
            else:
                self.label_cols.append(col)
    
    # 2. Encoding 
    def encode(self, X_train, X_test):
        
        X_train_enc = X_train[self.num_cols].copy()
        X_test_enc = X_test[self.num_cols].copy()

        # Label Encoding 
        for col in self.label_cols:
            X_train_enc[col] = X_train[col].astype("category").cat.codes

            categories = (
                X_train[col]
                .astype("category")
                .cat.categories
            )
            X_test_enc[col] = pd.Categorical(
                X_test[col],
                categories = categories
            ).codes

            # One-Hot Encoding
        if len(self.onehot_cols) > 0:
            
            train_ohe = self.encoder.fit_transform(
                X_train[self.onehot_cols]
            )
            test_ohe = self.encoder.transform(
                X_test[self.onehot_cols]
            )
            # Align columns
            train_ohe = pd.DataFrame(
                train_ohe,
                columns = self.encoder.get_feature_names_out(self.onehot_cols),
                index = X_train.index
            )
            test_ohe = pd.DataFrame(
                test_ohe,
                columns = self.encoder.get_feature_names_out(self.onehot_cols),
                index = X_test.index
            )
            X_train_enc = pd.concat(
                [X_train_enc, train_ohe],
                axis=1
            )
            X_test_enc = pd.concat(
                [X_test_enc, test_ohe],
                axis=1
            )
        return X_train_enc, X_test_enc
    # 3. Scaling 
    def scale(self, X_train_enc, X_test_enc):
        X_train_scaled = X_train_enc.copy()
        X_test_scaled = X_test_enc.copy()

        X_train_scaled[self.num_cols] = self.scaler.fit_transform(
            X_train_scaled[self.num_cols]
        )
        X_test_scaled[self.num_cols] = self.scaler.transform(
            X_test_scaled[self.num_cols]
        )
        return X_train_scaled, X_test_scaled
    
        
    
