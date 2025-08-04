import pandas as pd
import json

class File_Handling():

    @staticmethod
    def read_csv_to_df(path):
        try: 
            df = pd.read_csv(path)
            return df
        except Exception as e:
            print("Error: error reading csv", e)
            return {"Error" : e}
    
    @staticmethod
    def create_csv_from_df(df : pd.DataFrame):
        try: 
            df.to_csv("results/tweets_dataset_cleaned.csv")
        except Exception as e:
            print("Error: error createing csv file", e)
            return {"Error" : e}

    def create_json_from_dict(data_dict : dict):
        try: 
            with open("results/results.json", 'w') as f:
                json.dump(data_dict, f, indent=2)
        except Exception as e:
            print("Error: error createing results json file", e)
            return {"Error" : e}