import os 
import time

if os.path.basename(os.getcwd()) ==  "KBS2023_HEART_DEFECT_ONTOLOGY":
    os.chdir("utils")
elif os.path.basename(os.getcwd()) == "FuzzyDL":
    print(os.path.basename(os.getcwd()))
    os.chdir("/../utils")

from pracer.racer_client import RacerClient
import re

class Ontology():

    def __init__(self,RACER_QUERIES):
        super().__init__()
        self._racer = None
        self.RACER_PARAM = ['127.0.0.1', 8088] 
        self.JAVA_PARAM = ['java', '-jar'] 
        self.RACER_QUERIES = RACER_QUERIES
        self.FILE_FUZZY = ''
        self.FILE_RACER = 'C:/Users/Fish/Documents/TUDORITA/AN 4 SEM 2/KBS/KBS2023_HEART_DEFECT_ONTOLOGY/resources/heart_defect_raw.racer'
        self.PATH_FUZZY = 'C:/Users/Fish/Documents/TUDORITA/AN 4 SEM 2/KBS/KBS2023_HEART_DEFECT_ONTOLOGY/utils/FuzzyDL/FuzzyDL.jar'
        self.time = 0
    @property
    def racer(self) -> RacerClient:

        self.time+=1
        if self._racer is None:
            self._racer = RacerClient(self.RACER_PARAM[0],self.RACER_PARAM[1])
            self._racer.connect()
            self._racer.full_reset()
            print("[RACER]: connected...")
            if self.time >= 100:
                raise Exception(" racer timeout ...")

        return self._racer


    def racer_load_file(self):
        with open(self.FILE_RACER,"r") as file: 
            for line in file: 
                try: 
                    result = self.racer.racer_call(line[1:-2])   
                    OK_STATUS = result.get_value()[1:3]
                    ANSWER_STATUS = result.get_value()[1:7]   
                    if OK_STATUS != "ok" and ANSWER_STATUS != "answer":
                        raise Exception(f'invalid command in file {line}')   
                except Exception as e:
                    print("[ERROR]: ",e)

    def racer_run_queries(self):
        for query in self.RACER_QUERIES:
            print("[QUERY]: ",query[1:-1],' ?')
            result = self.racer.racer_call(query[1:-1])
            self.racer_interpret_result(result.get_value(),query)
            
    def racer_interpret_result(self,result,query):
        try: 
            OK_STATUS = result[1:3]
            ANSWER_STATUS = result[1:7]   
            if OK_STATUS != "ok" and ANSWER_STATUS != "answer":
                raise Exception(f'invalid command - {query}')
            
            matches = re.findall(r"[A-Za-z_]+", result)
            print("[ANSWER]: ")
            for match in matches[1:]: 
                print(f'\t\t{match}')

        except Exception as e:
            print("[ERROR]: ",e)

    def run(self):
        try:
            self.racer_load_file()
            self.racer_run_queries()
            
        except Exception as e:
            print("[ERROR]: ",e)