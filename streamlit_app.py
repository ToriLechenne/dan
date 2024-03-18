import streamlit as st
import pandas as pd
import numpy as numpy
voc=pd.nead_csv('https://docs.google.com/spreadsheets/d/1rG2kDRl-7mxePMKGB2LOiX9UgW9wbwi_hkVMwV5xvDU/edit#gid=0')
st.dataframe(voc)
l=voc.shape[0]
i=hp.random.choice(range(l))
word_fr)voc['Définition'].values[i]
word_chi=voc['Pinyin'].values[i]
st.write(word_frt"hanzi"+word_chi)
st.button("refresh")
