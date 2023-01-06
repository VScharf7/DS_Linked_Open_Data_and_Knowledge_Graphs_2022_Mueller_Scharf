#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:05:05 2022

@author: scharf
"""


import pandas as pd

df = pd.read_csv("/home/scharf/Desktop/sRNATarBase3_w_target_from_1_to_terminal.csv")

# define columns to use
# %%
#print(df.columns)

#  'SRNA_START',
 #      'SRNA_END', 'SRNA_STRAND', 'TARGET_TYPE', 'TARGET_LENGTH',
 #      'TARGET_START', 'TARGET_END', 'TARGET_STRAND', 'REGULATION', 'PMID',
 #      'SRNA_SEQ', 'TARGET_REGION', 'TARGET_SEQ'
 
df.drop(['ID', 'REGULATION', 'PMID', 'SRNA_SEQ', 'TARGET_SEQ'], inplace=True)
print(df.columns)
