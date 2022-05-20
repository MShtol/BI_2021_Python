#!/usr/bin/env python
# coding: utf-8

# # CREATING DATABASE WITH SQLITE3

# This database is created on the basis of precessed ADAPTABLE antimicrobial peptide(AMP) database

# In[148]:


import numpy as np
import sqlite3
import pandas as pd


# In[186]:


def excel_to_sql(excel_path, db_path, table_name):
    """
    This function creates database from .xlsx file containing AMP ID, Sequence, Length and 30 features
    for each AMP.
    """
    df =  pd.read_excel(excel_path).drop(
        'Unnamed: 0', axis=1).rename(
        columns={'ID':'adaptable_ID',"HIV-1_Integrase":"HIV_1_Integrase"})
    connection = sqlite3.connect(db_path)
    querry_create_table = f"""CREATE TABLE {table_name}(
'db_ID' INTEGER PRIMARY KEY,
'adaptable_ID' TEXT,
'Sequence' TEXT,
'Length' INTEGER, 
'Lipid_Bilayer' INTEGER,
'Fusion_inhibitor' INTEGER,
'Integrase' INTEGER,
'biofilm' INTEGER,
'HIV_1_Integrase' INTEGER,
'Hepatitis_C_virus_HCV' INTEGER,
'inner_membrane' INTEGER,
'Virus_entry' INTEGER,
'gp41' INTEGER,
'Herpes_simplex_virus_1_HSV_1' INTEGER,
'gram_neg_bacterial_cell_wall' INTEGER,
'Virus_replication' INTEGER,
'Protease_inhibition' INTEGER,
'Multifunction' INTEGER,
'West_Nile_virus_WNV' INTEGER,
'antimicrobial' INTEGER,
'antibacterial' INTEGER,
'antigram_pos' INTEGER,
'antigram_neg' INTEGER,
'antifungal' INTEGER,
'antiyeast' INTEGER,
'antiviral' INTEGER, 
'antiprotozoal' INTEGER,
'antiparasitic' INTEGER,
'antiplasmodial' INTEGER, 
'antitrypanosomic' INTEGER,
'antileishmania' INTEGER,
'insecticidal' INTEGER,
'anticancer' INTEGER,
'antitumor' INTEGER
)"""
    try:
        connection.execute(querry_create_table)
    except:
        connection.close()
        return 'DB allready exists'
    
    df.to_sql(table_name,connection, if_exists='append', index=False)
    connection.close()
    return 'DB succesfully created'


# In[ ]:


class Amp:
    """
    This class creates AMP object. It looks usefull because of sparcity of data for each AMP.
    E.g. ypu can find papers with a number of peptides with only couple of this features been tested.
    """

    def __init__(self, adaptable_ID, Sequence, Length=0, Lipid_Bilayer=0,
                 Fusion_inhibitor=0, Integrase=0, biofilm=0, HIV_1_Integrase=0,
                 Hepatitis_C_virus_HCV=0, inner_membrane=0, Virus_entry=0, gp41=0,
                 Herpes_simplex_virus_1_HSV_1=0, gram_neg_bacterial_cell_wall=0,
                 Virus_replication=0, Protease_inhibition=0, Multifunction=0,
                 West_Nile_virus_WNV=0, antimicrobial=0, antibacterial=0, antigram_pos=0,
                 antigram_neg=0, antifungal=0, antiyeast=0, antiviral=0, antiprotozoal=0,
                 antiparasitic=0, antiplasmodial=0, antitrypanosomic=0, antileishmania=0,
                 insecticidal=0, anticancer=0, antitumor=0):
        """
        This function iniciates object with all 30 features =0 by default.
        Length is recalculated inside. but parameter is left for sake of uniformity,
    
        """
        self.adaptable_ID = adaptable_ID
        self.Sequence = Sequence
        self.Length = len(Sequence)
        self.Lipid_Bilayer = Lipid_Bilayer
        self.Fusion_inhibitor = Fusion_inhibitor
        self.Integrase = Integrase
        self.biofilm = biofilm
        self.HIV_1_Integrase = HIV_1_Integrase
        self.Hepatitis_C_virus_HCV = Hepatitis_C_virus_HCV
        self.inner_membrane = inner_membrane
        self.Virus_entry = Virus_entry
        self.gp41 = gp41
        self.Herpes_simplex_virus_1_HSV_1 = Herpes_simplex_virus_1_HSV_1
        self.gram_neg_bacterial_cell_wall = gram_neg_bacterial_cell_wall
        self.Virus_replication = Virus_replication
        self.Protease_inhibition = Protease_inhibition
        self.Multifunction = Multifunction
        self.West_Nile_virus_WNV = West_Nile_virus_WNV
        self.antimicrobial = antimicrobial
        self.antibacterial = antibacterial
        self.antigram_pos = antigram_pos
        self.antigram_neg = antigram_neg
        self.antifungal = antifungal
        self.antiyeast = antiyeast
        self.antiviral = antiviral
        self.antiprotozoal = antiprotozoal
        self.antiparasitic = antiparasitic
        self.antiplasmodial = antiplasmodial
        self.antitrypanosomic = antitrypanosomic
        self.antileishmania = antileishmania
        self.insecticidal = insecticidal
        self.anticancer = anticancer
        self.antitumor = antitumor


def add_amp(amp, db_path, table_name):
    """
    This function adds one new AMP to the database.
    As `amp` is used Amp object
    """
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    amp_dict = amp.__dict__
    qmarks = ', '.join('?' * len(amp_dict))
    querry = "INSERT INTO %s VALUES (Null, %s)" % (table_name, qmarks)
    cur.execute(querry, tuple(amp_dict.values()))
    connection.commit()
    connection.close()


def del_amp(adaptable_ID, db_path, table_name):
    """
    This function deletes ine AMP from the database by adaptable_ID value
    """
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    querry = "DELETE FROM %s WHERE adaptable_ID ='%s'" % (table_name, adaptable_ID)
    cur.execute(querry)
    connection.commit()
    connection.close()

    
def select_len(db_path, table_name, start=10, end=50):
    """
    This function selects from the DB rows with Length value between `start` and `end`
    Returns dataframe with selected rows
    """
    connection = sqlite3.connect(db_path)
    querry = "SELECT * FROM %s WHERE (Length >= %s AND Length < %s)" % (table_name, start, end)
    selected = connection.execute(querry).fetchall()
    with open('columns.txt') as f:
        colnames = f.read().split()
    select_df = pd.DataFrame(selected,columns=colnames).drop(columns='db_ID')
    connection.close()
    return select_df


def select_by_features(db_path, table_name, features):
    """
    This function selects from the DB rows that posses requiered features.
    Features can be passed as list of column names (except IDs, Sequence and Length).
    Returns dataframe with selected rows
    """
    connection = sqlite3.connect(db_path)
    querry = f"SELECT * FROM {table_name} WHERE (" + ' = 1 AND '.join(features) + ' = 1)' 
    print(querry)
    selected = connection.execute(querry).fetchall()
    with open('columns.txt') as f:
        colnames = f.read().split()
    select_df = pd.DataFrame(selected,columns=colnames).drop(columns='db_ID')
    connection.close()
    return select_df


# **Test**
# Creating DB

# In[ ]:


excel_path = 'adaptable_100.xlsx'
# excel_path = 'adaptable.xlsx'
db_path = 'adaptable.db'
table_name = 'amp'
excel_to_sql(excel_path, db_path, table_name)


# Creating new AMP and adding it to the database

# In[ ]:


new_amp = Amp('FAKE','OMAEWAMOUSHINDEIRU')

add_amp(new_amp, db_path, table_name)


# Deleting from DB

# In[ ]:


del_amp('asd', db_path, table_name)


# Selecting subset by length

# In[193]:


select_len(db_path, table_name, 15, 20)


# Selecting by features

# In[189]:


features = ['antimicrobial',
'antibacterial',
'antigram_pos',
'antigram_neg',
'antifungal',
'antiyeast']
select_by_features(db_path, table_name, features)

