import os


CSV_FILE_PATH = os.path.join(os.getcwd(), 'CSV_files\Fish.csv')
MODEL_FILE_PATH = os.path.join(os.getcwd(), 'Linear_reg.pkl')
PROJECT_DATA_FILE_PATH = os.path.join(os.getcwd(), 'Fish_project_data.json')

MONGO_DB_CONNECTION_URL = "mongodb://localhost:27017"
DATABASE_NAME = "Fish_weight"
PORT_NUMBER = 8080

# print(MONGO_DB_CONNECTION_URL)