import pandas as pd

class Analyst():

    def __init__(self, df : pd.DataFrame):
        self.df = df
        self.total_tweets = {"antisemitic": 0, "non_antisemitic": 0, "unspecified" : 0, "total": 0}
        self.average_length = { "antisemitic": 0, "non_antisemitic": 0, "total": 0 }
        self.uppercase_words = { "antisemitic": 0, "non_antisemitic": 0, "total": 0 }
        self.ten_common_words = []
        self.longest_tweets = {"antisemitic": [], "non_antisemitic": []}

    def run(self):
        dict_words = {}
        dict_tweets = {}

        for _ , row in self.df.iterrows():
            self.count_tweets_per_categories(row)
            self.count_uppercase_words(row)
            self.count_words_per_categories(row)

            # updating the dicts var with the current values
            dict_words = self.create_dict_words(row)
            dict_tweets = self.create_dict_tweets(row)

        self.find_common_words(dict_words)
        self.find_longest_tweets(dict_tweets)
        self.average_len_tweets()

       
    def count_tweets_per_categories(self, row):
        self.total_tweets["total"] += 1
        if row['Biased'] == 1:
            self.total_tweets["antisemitic"] += 1
        elif row['Biased'] == 0:
            self.total_tweets["non_antisemitic"] += 1
        else:
            self.total_tweets["unspecified"] += 1  
    
    def count_words_per_categories(self, row):
        count_words = len(row["Text"].split())
        self.average_length["total"] += count_words
        if row["Biased"] == 1:
            self.average_length["antisemitic"] += count_words
        elif row["Biased"] == 0:
            self.average_length["non_antisemitic"] += count_words
    
    def average_len_tweets(self):      
        self.average_length["antisemitic"] = round(self.average_length["antisemitic"] / self.total_tweets["antisemitic"], 2)
        self.average_length["non_antisemitic"] = round(self.average_length["non_antisemitic"] / self.total_tweets["non_antisemitic"], 2)
        self.average_length["total"] = round(self.average_length["total"] / self.total_tweets["total"], 2)
            
    def count_uppercase_words(self, row):
        count_upper = 0
        for word in row["Text"].split():
            if word.isupper():
                count_upper += 1
        self.uppercase_words["total"] += count_upper
        if row['Biased'] == 1:
            self.uppercase_words["antisemitic"] += count_upper
        elif row['Biased'] == 0:
            self.uppercase_words["non_antisemitic"] += count_upper

    def create_dict_words(self, row, words_dict={}):
        for word in row["Text"].split():
            word = word.lower()
            words_dict[word] = words_dict.get(word, 0) + 1
        return words_dict

    def find_common_words(self, words_dict):
        sorted_dict = sorted(words_dict.items(), key=lambda item : item[1], reverse=True)
        ten_keys = [key for key, value in sorted_dict[:10]]
        self.ten_common_words = ten_keys
        return
    
    def create_dict_tweets(self, row, dict_tweets={"antisemitic": {}, "non_antisemitic": {}}):
        if row["Biased"] == 1:
            dict_tweets["antisemitic"].update({row["Text"] : len(row["Text"].split())})
        elif row["Biased"] == 0:
            dict_tweets["non_antisemitic"].update({row["Text"] : len(row["Text"].split())})
        return dict_tweets

    def find_longest_tweets(self, dict_tweets):
        sorted_anti = sorted(dict_tweets["antisemitic"].items(), key= lambda item: item[1], reverse=True)
        self.longest_tweets["antisemitic"] = [key for key, value in sorted_anti[:3]]

        sorted_non_anti = sorted(dict_tweets["non_antisemitic"].items(), key= lambda item: item[1], reverse=True)
        self.longest_tweets["non_antisemitic"] = [key for key, value in sorted_non_anti[:3]]
        return