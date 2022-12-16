import numpy as np
import pickle
import json
import config
# import pymongo


class FISH_WEIGHT():
    def __init__(self, user_data):
        self.user_data = user_data
        self.model_file_path = config.MODEL_FILE_PATH
        self.project_file_path = config.PROJECT_DATA_FILE_PATH
        # self.mongo_connect_url = config.MONGO_DB_CONNECTION_URL
        # self.db_name = config.DATABASE_NAME
        # self.mongo_client = pymongo.MongoClient(self.mongo_connect_url)
        # self.db = self.mongo_client[self.db_name]
        # self.collection_user = self.db['user_input']

###############################################################################################

    def load_data(self):
        with open(self.model_file_path, 'rb') as f:
            self.model = pickle.load(f)

        with open(self.project_file_path, 'r') as f:
            self.project_data = json.load(f)

###############################################################################################

    def get_fish_names(self):
        self.load_data()
        fishes = list(self.project_data['Species'].keys())
        return fishes

###############################################################################################

    def get_fish_weight(self):
        
        self.load_data()
        
        Species = self.user_data['Species']
        Species = self.project_data['Species'][Species]

        test_array = np.zeros(len(self.project_data['Columns']))

        test_array[0] = Species
        test_array[1] = eval(self.user_data['Length1'])
        test_array[2] = eval(self.user_data['Length2'])
        test_array[3] = eval(self.user_data['Length3'])
        test_array[4] = eval(self.user_data['Height'])
        test_array[5] = eval(self.user_data['Width'])

        predicted_weight = np.around(self.model.predict([test_array]), 3)[0]
        # print(predicted_weight)

        return predicted_weight

###############################################################################################

if __name__ == "__main__":
    obj = FISH_WEIGHT()
    obj