import streamlit as st
import pandas as pd
from math import sqrt

# Load CSV data
df_stats = pd.read_csv('stats.csv',encoding='latin-1')  # CSV with name, attack, defense, hp
df_levels = pd.read_csv('cp_mod.csv',encoding='latin-1')  # CSV with level, percent

# UI for selecting name, attack2, defense2, hp2, level2
name2 = st.selectbox('Select Character Name', df_stats['name'])
attack2 = st.number_input('Input Additional Attack', min_value=0)
defense2 = st.number_input('Input Additional Defense', min_value=0)
hp2 = st.number_input('Input Additional HP', min_value=0)
level2 = st.selectbox('Select Level', df_levels['level'])

if st.button('Calculate'):
    # Find records in the CSVs
    character_stats = df_stats[df_stats['name'] == name2].iloc[0]
    level_percent = df_levels[df_levels['level'] == level2].iloc[0]['percent']

    # Calculation
    total_attack = ((character_stats['attack'] + attack2) * level_percent)
    total_defense = (sqrt(character_stats['defense'] + defense2) * level_percent)
    total_hp = (sqrt(character_stats['hp'] + hp2) * level_percent)

    result = (total_attack + total_defense + total_hp) / 10

    st.write('Calculated Value:', result)
