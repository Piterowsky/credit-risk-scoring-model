import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files('laotse/credit-risk-dataset', path='./data', unzip=True)