
class Populator():
    def __init__(self):
        self.PATH_INPUT = "C:/Users/Fish/Documents/TUDORITA/AN 4 SEM 2/KBS/KBS2023_HEART_DEFECT_ONTOLOGY/resources/res_populator.csv"
        self.PATH_OUTPUT = "C:/Users/Fish/Documents/TUDORITA/AN 4 SEM 2/KBS/KBS2023_HEART_DEFECT_ONTOLOGY/resources/heart_defect_populated.racer"

    def populate(self):
        with open(self.PATH_INPUT, "r") as f_in, open(self.PATH_OUTPUT, "a") as f_out:
            # Read the CSV file
            lines = f_in.readlines()

            f_out.write("\n\n;Populated automatically\n\n")

            # Write the instances to the output file
            for line in lines: # assuming that the instances are in lines 1 to 14
                if line.strip() == "":
                    currentFormat = ''
                    f_out.write("\n")
                    continue
                if 'Instance,Category' in line:
                    currentFormat = 'instance'
                    continue
                if 'Related,HasSymptom' in line:
                    currentFormat = 'relatedHasSymptom'
                    continue
                if 'Related,Treatment' in line:
                    currentFormat = 'relatedHasTreatment'
                    continue
                if 'Related,DiagnosisMethod' in line:
                    currentFormat = 'relatedHasDiagnosisMethod'
                    continue
                
                value1, value2 = line.strip().split(",")
                
                if currentFormat == 'instance':
                    f_out.write("(instance {} {})\n".format(value1, value2))    
                if currentFormat == 'relatedHasSymptom':
                    f_out.write("(related {} {} has-symptom)\n".format(value1, value2))
                if currentFormat == 'relatedHasTreatment':
                    f_out.write("(related {} {} has-treatment)\n".format(value1, value2))
                if currentFormat == 'relatedHasDiagnosisMethod':
                    f_out.write("(related {} {} has-diagnosis-method)\n".format(value1, value2))
        