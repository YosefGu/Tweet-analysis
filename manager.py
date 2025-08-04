from src.file_handling.file_handling import File_Handling
from src.data_clean.cleaner import Cleaner
from src.analyst.analyst import Analyst

class Manager():

    @staticmethod
    def run():
        df = File_Handling.read_csv_to_df("data/tweets_dataset.csv")
        claener = Cleaner(df)
        claener.run()
        File_Handling.create_csv_from_df(claener.df)

        analyst = Analyst(claener.df)
        analyst.run()

        dict_to_save = {
            "total_tweets": analyst.total_tweets, 
            "average_length" : analyst.average_length, 
            "common_words": analyst.ten_common_words,
            "longest_tweets": analyst.longest_tweets,
            "uppercase_words" : analyst.uppercase_words
            }
        File_Handling.create_json_from_dict(dict_to_save)


    

if __name__ == "__main__":
    Manager().run()
    