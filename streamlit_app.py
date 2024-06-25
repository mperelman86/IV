import streamlit as st
import pandas as pd
from math import sqrt

# Load CSV data
df_stats = pd.read_csv('stats.csv',encoding='latin-1')  # CSV with name, attack, defense, hp
df_levels = pd.read_csv('cp_mod.csv',encoding='latin-1')  # CSV with level, percent

# UI for selecting name, attack2, defense2, hp2, level2
name2 = st.selectbox('Select Character Name', df_stats['Name'])
attack2 =st.slider('Input Additional Attack', min_value= 0, 15, 15)
defense2 = st.slider('Input Additional Defense', min_value= 0, 15, 15)
hp2 = st.slider('Input Additional HP', min_value= 0 15, 15)
level2 = st.slider('Select Level', min_value= 0, 51, 25)

if st.button('Calculate'):
    # Find records in the CSVs
    character_stats = df_stats[df_stats['Name'] == name2].iloc[0]
    level_percent = df_levels[df_levels['Level'] == level2].iloc[0]['CPM']

    # Calculation
    total_attack = ((character_stats['Attack'] + attack2) * level_percent)
    total_defense = (sqrt(character_stats['Defense'] + defense2) * level_percent)
    total_hp = (sqrt(character_stats['HP'] + hp2) * level_percent)

    result = (total_attack + total_defense + total_hp) / 10

    st.write('Calculated Value:', result)
