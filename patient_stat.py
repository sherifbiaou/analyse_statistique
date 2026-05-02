import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LogisticRegression
import os
# Chargement des données
import csv

#chargement de la donnée
df=pd.read_csv('patients_data.csv')
st.markdown("<h1 style='color:blue'>Analyse des données des patients</h1>", unsafe_allow_html=True)
st.write(df)

# Nettoyage des données
df.dropna(inplace=True)
df['age'] = df['age'].astype(int)
df['temperature'] = df['temperature'].astype(float)
df['systolic_bp'] = df['systolic_bp'].astype(float)
df['diastolic_bp'] = df['diastolic_bp'].astype(float)
df['smoker'] = df['smoker'].str.lower()

# Analyse statistique de base
#age
age_mean = df['age'].mean()
age_median = df['age'].median()
age_std = df['age'].std()
#temperature
temp_mean = df['temperature'].mean()
temp_median = df['temperature'].median()
temp_std = df['temperature'].std()
#bp
bp_mean = df[['systolic_bp', 'diastolic_bp']].mean()
bp_median = df[['systolic_bp', 'diastolic_bp']].median()
bp_std = df[['systolic_bp', 'diastolic_bp']].std()


#distribution
sex_distribution = df['sexe'].value_counts(normalize=True)
smoker_proportion = df['smoker'].value_counts(normalize=True)

# Analyse croisée
bp_by_smoker = df.groupby('smoker')[['systolic_bp', 'diastolic_bp']].mean()
temp_by_diag = df.groupby('diagnosis')['temperature'].mean()
top_diagnoses = df['diagnosis'].value_counts().head(5)

# Application Streamlit

# Statistiques de base

st.sidebar.title("—Statistiques de base—")


def stat_age(titre_age='statistique AGE',sous_age='statistiques',st_mo ='age_mean',st_me='temp_mean',st_std_t = 'age_std'):
  st.sidebar.markdown('<span style="font-size: 26px; color:yellow">◊-statistiques de la variable AGE </span>', unsafe_allow_html=True)
  st.sidebar.text(f"L'age moyen : {age_mean:.2f} ans")
  st.sidebar.text(f"L'age median : {age_median:.2f} ans")
  st.sidebar.text(f"L'ecart-type entre les ages est : {age_std:.2f} ans")
 

stat_age()
st.sidebar.text_input("COMMENTAIRE SUR L'AGE")

def stat_temp(titre_temp='STAT TEMPERATURE',st_mo ='temp_mean',st_me='temp_mean',st_std_t = 'temp_std'):
  st.sidebar.markdown('<span style="font-size: 26px; color:yellow">◊-statistiques de la variable TEMPERATURE </span>', unsafe_allow_html=True)
  st.sidebar.text(f"La temperature moyen : {temp_mean:.2f} °C")
  st.sidebar.text(f"La temperature median : {temp_median:.2f} °C")
  st.sidebar.text(f"L'ecart-type entre les temperatures est : {temp_std:.2f} °C")
 
stat_temp()
st.sidebar.text_input("COMMENTAIRE SUR LA TEMPERATURE CORPORELLE")


def stat_tension(titre_age='STAT TENSION ',st_sys_mo='bp_mean',st_sys_me='bp_median',st_sys_std='bp_std',st_dia_mo='bp_mean',st_dia_me='bp_median',st_dia_std='bp_std'):
     st.sidebar.markdown('<span style="font-size: 26px; color:yellow">◊-statistiques  des variables de la tension </span>', unsafe_allow_html=True)
     st.sidebar.text(f"Tension systolique moyenne : {bp_mean['systolic_bp']:.2f} mmHg")
     st.sidebar.text(f"Tension systolique median : {bp_median['systolic_bp']:.2f} mmHg")
     st.sidebar.text(f"Ecart-type entre les tensions systoliques  : {bp_std['systolic_bp']:.2f} mmHg")
     st.sidebar.text(f"Tension diastolique moyenne : {bp_mean['diastolic_bp']:.2f} mmHg")
     st.sidebar.text(f"Tension diastilique median : {bp_median['diastolic_bp']:.2f} mmHg")
     st.sidebar.text(f"Ecart-type entre les tensions diastolitiques  : {bp_std['diastolic_bp']:.2f} mmHg")

stat_tension()
st.sidebar.text_input("COMMENTAIRE SUR LES TENSIONS")

# Répartition par sexe
st.markdown('<span style="font-size: 28px; color:yellow">◊-Répartition par sexe</span>', unsafe_allow_html=True)
st.write(sex_distribution)

# Proportion de fumeurs
st.markdown('<span style="font-size: 28px; color:yellow">◊-Proportion de fumeurs</span>', unsafe_allow_html=True)
st.write(smoker_proportion)

# Moyenne tension artérielle : fumeurs vs non-fumeurs
st.markdown('<span style="font-size: 28px; color:yellow">◊-Moyenne tension artérielle : fumeurs vs non-fumeurs</span>', unsafe_allow_html=True)
st.write(bp_by_smoker)

# Température moyenne par diagnostic
st.markdown('<span style="font-size: 28px; color:yellow">◊-Température moyenne par diagnostic•</span>', unsafe_allow_html=True)
st.write(temp_by_diag)

# Top 5 des diagnostics
st.markdown('<span style="font-size: 28px; color:yellow">◊-Top 5 des diagnostics</span>', unsafe_allow_html=True)
st.write(top_diagnoses)

# Visualisations
st.markdown('<span style="font-size: 28px; color:yellow">◊—Visualisations</span>', unsafe_allow_html=True)

fig1, ax = plt.subplots()
sns.histplot(df['age'], bins=20, kde=True, ax=ax)
st.pyplot(fig1)

st.write("Histogramme des ages")
st.text_input("espace interpretation 1")

fig2, ax = plt.subplots()
sns.histplot(df['temperature'], bins=20, kde=True, ax=ax)
st.pyplot(fig2)

st.write("Histogramme des temperatures")
st.text_input("espace interpretation 2")

fig3, ax = plt.subplots()
df['diagnosis'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig3)

st.write("Histogramme des diagnostiques")
st.text_input("espace interpretation 3")

fig4, ax = plt.subplots()
sns.boxplot(x='diagnosis', y='temperature', data=df, ax=ax)
st.pyplot(fig4)

st.write(" diagramme en boite des variables diagnostiques et temperateurs")
st.text_input("espace interpretation 4")
