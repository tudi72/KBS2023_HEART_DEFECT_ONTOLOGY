import os

import subprocess

class Fuzzy():
    def __init__(self,FUZZY_QUERIES,PATH_FUZZY="C:/Users/Fish/Documents/TUDORITA/AN 4 SEM 2/KBS/KBS2023_HEART_DEFECT_ONTOLOGY/utils/FuzzyDL/FuzzyDL.jar",PATH_FILE="C:/Users/Fish/Documents/TUDORITA/AN 4 SEM 2/KBS/KBS2023_HEART_DEFECT_ONTOLOGY/resources/res_fuzzy.txt"):
        self.commands = ["java","-jar",PATH_FUZZY,PATH_FILE]
        self.FUZZY_QUERIES = FUZZY_QUERIES
        self.PATH_FILE = PATH_FILE

    def sanity_check(self):
            result = subprocess.run(self.commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def load_query(self):
        for query in self.FUZZY_QUERIES:
            with open(self.PATH_FILE,"a") as f: 
                f.write(query)

    def load_file(self):
        data = None 
        error = None
        try:
            if os.path.basename(os.getcwd()) == "KBS2023_HEART_DEFECT_ONTOLOGY":
                os.chdir("utils/FuzzyDL")
            elif os.path.basename(os.getcwd()) == "utils": 
                os.chdir("FuzzyDL")
            elif os.path.basename(os.getcwd()) != "FuzzyDL": 
                 raise Exception("invalid fuzzy path...")
    
            result = subprocess.run(self.commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            data = result.stdout
            error = result.stderr
            if(error != ""):
                raise Exception(" emtpy data set...")
            print("[FUZZY]: ",data)
        except Exception as e:
            print("[ERROR]: ",error)
    
    def run(self):
        self.load_query()
        self.load_file()