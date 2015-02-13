#================================================================================
#
# Group information
# 
# 
#
#================================================================================
import pandas as pd
import csv

def getPostalCodeDic(csvfname = 'CP.csv'):
    """
    Returns a dictionary by postal code
    """
    cpdic = {}
    reader = csv.DictReader(open(csvfname), delimiter=':')
    for row in reader:
        cpdic[row['CP']] =  row['arrondissement'].split('|')[-1]
    return cpdic
    

def postalcode_area_studies():
    """
    Group some charactesitics by postal code area (first 3 letters)
    """
    dfpawnshop = pd.read_csv(pawnmtl.csv)
    cpdic = getPostalCodeDic()
    for ik in cpdic.keys():
        print ik, cpdic[ik]
    
if __name__=='__main__':
    #getPostalCodeDic()
    postalcode_area_studies()
