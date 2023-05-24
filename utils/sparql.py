from SPARQLWrapper import SPARQLWrapper, JSON

class SPARQL():
    def __init__(self, SPARQL_QUERIES):
        self.sprQL = SPARQLWrapper("http://sparql.hegroup.org/sparql/")
        self.FILE_SPARQL = "C:/Users/Fish/Documents/TUDORITA/AN 4 SEM 2/KBS/KBS2023_HEART_DEFECT_ONTOLOGY/resources/heart_defect.sparql"
        self.query = \
        """
        """
        self.questions = [
            "[SPARQL]: Select subclasses of CHD ?",
            "[SPARQL]: List all concepts of CHD ? ",
        ]
        self.queries = SPARQL_QUERIES
    
    def load_file(self):
        with open(self.FILE_SPARQL,"r") as file:
            for line in file: 
                self.query += line

    def run_query(self,query):
        results = None
        query = self.query +'\n' + query
        try: 
            self.sprQL.setQuery(query)
            self.sprQL.setReturnFormat(JSON)
            results = self.sprQL.query().convert()
            print("[RESULT]:\n")
            for result in results["results"]["bindings"]:
                if "label" in result:
                    print("\t\t\t",result["label"]["value"])
                elif "x" in result:
                    print('\t\t\t',result['x']['value'])
                else:
                    print("\t\t\t",result)
                
        except Exception as e: 
            print("[ERROR]: ",e)
        return results
    
    def run(self):
        self.load_file()
        for index,q in enumerate(self.queries):
            print(self.questions[index])
            self.run_query(q)