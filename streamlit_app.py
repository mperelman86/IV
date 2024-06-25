import streamlit as st
import pandas as pd
import math
from math import sqrt

# Load CSV data
df_stats = pd.read_csv('stats.csv',encoding='latin-1')  # CSV with name, attack, defense, hp
df_levels = pd.read_csv('cp_mod.csv',encoding='latin-1')  # CSV with level, percent

col1, col2 = st.columns([1, 2])

with col1:
    # UI for selecting name, attack2, defense2, hp2, level2
    name2 = st.selectbox('Select Character Name', df_stats['Name'])
    attack2 =st.slider('Input Additional Attack', 0, 15, 15)
    defense2 = st.slider('Input Additional Defense', 0, 15, 15)
    hp2 = st.slider('Input Additional HP', 0, 15, 15)
    #level2 = st.slider('Select Level', 0, 51, 25)
    col1, col2 = st.columns([1, 3])
    if st.button('Calculate CP Across Levels'):
        run_calc = True
    else:
        run_calc = False

if run_calc:
    results = []
    for level in range(1,51):
    # Find records in the CSVs
        character_stats = df_stats[df_stats['Name'] == name2].iloc[0]
        level_percent = df_levels[df_levels['Level'] == level].iloc[0]['CPM']
    
        # Calculation
        total_attack = ((character_stats['Attack'] + attack2) * level_percent)
        total_defense = (sqrt((character_stats['Defense'] + defense2 ) * level_percent))
        total_hp = (sqrt((character_stats['HP'] + hp2) * level_percent))
    
        cp = math.floor((total_attack * total_defense * total_hp) / 10)
        results.append({'Level': level, 'CP': cp})
        
        
    results_df = pd.DataFrame(results)
    results_df.set_index('Level', inplace=True)
    with col2:
        st.table(results_df) 
        #st.sidebar.write("CP Values by Level", results_df)
        #st.markdown(results_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
        #st.write(results_df)
