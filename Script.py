import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')


df['Date Rptd'] = pd.to_datetime(df['Date Rptd'], errors='coerce')
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], errors='coerce')
df['TIME OCC'] = pd.to_numeric(df['TIME OCC'], errors='coerce')
df['Vict Age'] = pd.to_numeric(df['Vict Age'], errors='coerce')
df['LAT'] = pd.to_numeric(df['LAT'], errors='coerce')
df['LON'] = pd.to_numeric(df['LON'], errors='coerce')

# Drop rows with missing critical values
df = df.dropna(subset=['Crm Cd', 'Crm Cd Desc', 'AREA NAME', 'Vict Age', 'Vict Sex', 'LAT', 'LON'])

# ---------------------------- Visualization 1: Top 10 Crimes ----------------------------
crime_counts = df['Crm Cd Desc'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=crime_counts.values, y=crime_counts.index, palette='viridis')
plt.title('Top 10 Most Common Types of Crimes')
plt.xlabel('Number of Incidents')
plt.ylabel('Crime Type')
plt.tight_layout()
plt.show()

# ---------------------------- Visualization 2: Crime Distribution by Area ----------------------------
area_counts = df['AREA NAME'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=area_counts.values, y=area_counts.index, palette='magma')
plt.title('Crime Distribution by Area')
plt.xlabel('Number of Incidents')
plt.ylabel('Area Name')
plt.tight_layout()
plt.show()

# ---------------------------- Visualization 3: Crime Trends Over Time ----------------------------
df['Year'] = df['DATE OCC'].dt.year
df['Month'] = df['DATE OCC'].dt.month
time_trends = df.groupby(['Year', 'Month']).size().reset_index(name='Incidents')
plt.figure(figsize=(12, 6))
sns.lineplot(data=time_trends, x='Month', y='Incidents', hue='Year', marker='o')
plt.title('Crime Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Incidents')
plt.legend(title='Year')
plt.tight_layout()
plt.show()

# ---------------------------- Visualization 4: Victim Age Distribution ----------------------------
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Vict Age', bins=20, kde=True)
plt.title('Distribution of Victim Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# ---------------------------- Visualization 5: Victim Gender Distribution ----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Vict Sex', palette='pastel')
plt.title('Victim Sex Distribution')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
