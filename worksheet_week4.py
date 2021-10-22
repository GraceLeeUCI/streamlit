#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 01:11:16 2021

@author: jihyunlee
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.title("Math 10 - Homework 4")

st.markdown("Grace Lee , Emi Cervantes, Yuzhen Lang")

uploaded_file = st.file_uploader("Upload a CSV file" , type = 'CSV')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df = df.applymap(lambda x: np.nan if x == " " else x)
    
    def can_be_numeric(c):
        try: 
            pd.to_numeric(df[c])
            return True
        except:
            return False
 
    good_cols = [c for c in df.columns if can_be_numeric(c)]
    
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)
    
    x_axis = st.selectbox("Choose a value for x-axis",good_cols)
    y_axis = st.selectbox("Choose a value for y-axis",good_cols)
    
    
    num_rows = st.slider("Select # of row(s)", 0,len(df.index)-1,(0,len(df.index)))
          
    my_table = pd.DataFrame({
       f'{x_axis}': df[x_axis],
       f'{y_axis}': df[y_axis],
    })
    st.table(my_table)   #for Q12
            
    st.write(f'Plotting ({x_axis},{y_axis}) for rows {num_rows}')
    
    
    my_graph = alt.Chart(df.loc[num_rows[0]:num_rows[1]]).mark_circle().encode(
        x=x_axis, y=y_axis,tooltip=[x_axis,y_axis])
    
    st.altair_chart(my_graph, use_container_width=True)
    
    
if st.button('Grade Homework'):
     st.write('10/10 :)')
     


    
    