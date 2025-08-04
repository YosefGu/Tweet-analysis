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
        self.count_tweets_per_categories()
        self.average_len_tweets()
        self.count_uppercase_words()
        self.find_common_words()
        self.find_longest_tweets()
       
    def count_tweets_per_categories(self):
        for _, row in self.df.iterrows():
            self.total_tweets["total"] += 1
            if row['Biased'] == 1:
                self.total_tweets["antisemitic"] += 1
            elif row['Biased'] == 0:
                self.total_tweets["non_antisemitic"] += 1
            else:
                self.total_tweets["unspecified"] += 1  
    
    def average_len_tweets(self):
        antisemitic = 0
        non_antisemitic = 0
        total = 0
        for _, row in self.df.iterrows():
            count_words = len(row["Text"].split())
            total += count_words
            if row["Biased"] == 1:
                antisemitic += count_words
            elif row["Biased"] == 0:
                non_antisemitic += count_words
        self.average_length["antisemitic"] = round(antisemitic / self.total_tweets["antisemitic"], 2)
        self.average_length["non_antisemitic"] = round(non_antisemitic / self.total_tweets["non_antisemitic"], 2)
        self.average_length["total"] = round(total / self.total_tweets["total"], 2)
            
    def count_uppercase_words(self):
        for _, row in self.df.iterrows():
            count_upper = 0
            for word in row["Text"].split():
                if word.isupper():
                    count_upper += 1
            self.uppercase_words["total"] += count_upper
            if row['Biased'] == 1:
                self.uppercase_words["antisemitic"] += count_upper
            elif row['Biased'] == 0:
                self.uppercase_words["non_antisemitic"] += count_upper
            
    def find_common_words(self):
        words_dict = {}
        for _, row in self.df.iterrows():
            for word in row["Text"].split():
                word = word.lower()
                words_dict[word] = words_dict.get(word, 0) + 1
        sorted_dict = sorted(words_dict.items(), key=lambda item : item[1], reverse=True)
        ten_keys = [key for key, value in sorted_dict[:10]]
        self.ten_common_words = ten_keys
        return
    
    def find_longest_tweets(self):
        dict_tweest = {"antisemitic": {}, "non_antisemitic": {}}

        for _, row in self.df.iterrows():
            if row["Biased"] == 1:
                dict_tweest["antisemitic"].update({row["Text"] : len(row["Text"].split())})
            elif row["Biased"] == 0:
                dict_tweest["non_antisemitic"].update({row["Text"] : len(row["Text"].split())})                        
        
        sorted_anti = sorted(dict_tweest["antisemitic"].items(), key= lambda item: item[1], reverse=True)
        self.longest_tweets["antisemitic"] = [key for key, value in sorted_anti[:3]]

        sorted_non_anti = sorted(dict_tweest["non_antisemitic"].items(), key= lambda item: item[1], reverse=True)
        self.longest_tweets["non_antisemitic"] = [key for key, value in sorted_non_anti[:3]]
        return