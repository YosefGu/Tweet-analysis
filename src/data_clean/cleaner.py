import pandas as pd

class Cleaner():

    def __init__(self, df : pd.DataFrame):
        self.df = df

    def run(self):
        self.remove_unclassfied_rows()
        self.save_relevent_columns()
        self.remove_semicolumn()
        return

    def remove_unclassfied_rows(self):
        self.df = self.df[self.df['Biased'].notna()].copy()
        return
    
    def save_relevent_columns(self):
        self.df = self.df[['Text', 'Biased']].copy()
        return 
    
    def remove_semicolumn(self):
        self.df['Text'] = self.df['Text'].str.replace(r"[.,-]", "", regex=True)
        return
    
    def convert_to_lower(self):
        self.df['Text'] = self.df['Text'].str.lower()
        return
    

    
   
