import numpy as np
import pandas as pd
import joblib
# Import validation measures
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Robert J\VS Code\PythonWorks\Datathon\final_depression_dataset_1.csv")

df.dataframeName = 'final_depression_dataset_1.csv'
df.info()
# Clean Data
df = df.drop(columns=["City", "Name", "Working Professional or Student", "Profession"])

# Convert "Depression" column from "Yes" or "No" to 1 and 0
df['Depression'] = df['Depression'].map({'Yes': 1, 'No': 0})

# # Get unique values within all remaining fields using numpy in a SQL-like method
# unique_values = {col: np.unique(df[col].values) for col in df.columns}
# for col, values in unique_values.items():
#     print(f"Unique values in {col}: {values}")


# Gender - Depression: Add data labels
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x='Gender', hue='Depression')
plt.title('Count of Depression by Gender')
plt.xlabel('Gender')
plt.ylabel('Count of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
ax.set_xticks(range(len(df['Gender'].unique())))
ax.set_xticklabels(df['Gender'].unique())
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.tight_layout()
plt.show()

# Age - Depression: Leave as is
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Age', hue='Depression')
plt.title('Count of Depression by Age')
plt.xlabel('Age')
plt.ylabel('Count of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Academic Pressure - Depression: Add counts
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x='Academic Pressure', hue='Depression')
plt.title('Count of Depression by Academic Pressure')
plt.xlabel('Academic Pressure')
plt.ylabel('Count of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
ax.set_xticks(range(len(df['Academic Pressure'].unique())))
ax.set_xticklabels(df['Academic Pressure'].unique())
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.tight_layout()
plt.show()

# Work Pressure - Depression: Add counts
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x='Work Pressure', hue='Depression')
plt.title('Count of Depression by Work Pressure')
plt.xlabel('Work Pressure')
plt.ylabel('Count of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
ax.set_xticks(range(len(df['Work Pressure'].unique())))
ax.set_xticklabels(df['Work Pressure'].unique())
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.tight_layout()
plt.show()


# Study Satisfaction - Depression: Add data labels
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x='Study Satisfaction', hue='Depression')
plt.title('Count of Depression by Study Satisfaction')
plt.xlabel('Study Satisfaction')
plt.ylabel('Count of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
ax.set_xticks(range(len(df['Study Satisfaction'].unique())))
ax.set_xticklabels(df['Study Satisfaction'].unique())
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.tight_layout()
plt.show()

# Job Satisfaction - Depression: Stacked bar chart
plt.figure(figsize=(10, 6))
job_satisfaction_counts = df.groupby(['Job Satisfaction', 'Depression']).size().unstack()
job_satisfaction_counts = job_satisfaction_counts.div(job_satisfaction_counts.sum(axis=1), axis=0)
ax = job_satisfaction_counts.plot(kind='bar', stacked=True)
plt.title('Percentage of Depression by Job Satisfaction')
plt.xlabel('Job Satisfaction')
plt.ylabel('Percentage of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
ax.set_xticks(range(len(df['Job Satisfaction'].unique())))
ax.set_xticklabels(df['Job Satisfaction'].unique())
plt.tight_layout()
plt.show()

# Sleep Duration - Depression: Stacked bar chart
plt.figure(figsize=(10, 6))
sleep_duration_counts = ['Less than 5 hours', '5-6 hours', '7-8 hours', 'More than 8 hours']
sleep_duration_counts = df.groupby(['Sleep Duration', 'Depression']).size().unstack().reindex(sleep_duration_counts)
sleep_duration_counts = sleep_duration_counts.div(sleep_duration_counts.sum(axis=1), axis=0)
ax = sleep_duration_counts.plot(kind='bar', stacked=True)
plt.title('Percentage of Depression by Sleep Duration')
plt.xlabel('Sleep Duration')
plt.ylabel('Percentage of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
ax.set_xticks(range(len(sleep_duration_counts.index)))
ax.set_xticklabels(sleep_duration_counts.index)
plt.tight_layout()
plt.show()

# Dietary Habits - Depression: Stacked bar chart with ordered x-axis
plt.figure(figsize=(10, 6))
dietary_habits_order = ['Healthy', 'Moderate', 'Unhealthy']
dietary_habits_counts = df.groupby(['Dietary Habits', 'Depression']).size().unstack().reindex(dietary_habits_order)
dietary_habits_counts = dietary_habits_counts.div(dietary_habits_counts.sum(axis=1), axis=0)
ax = dietary_habits_counts.plot(kind='bar', stacked=True)
plt.title('Percentage of Depression by Dietary Habits')
plt.xlabel('Dietary Habits')
plt.ylabel('Percentage of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
ax.set_xticks(range(len(dietary_habits_order)))
ax.set_xticklabels(dietary_habits_order)
plt.tight_layout()
plt.show()


# Work/Study Hours - Depression: Stacked bar chart
plt.figure(figsize=(10, 6))
work_study_hours_counts = df.groupby(['Work/Study Hours', 'Depression']).size().unstack()
work_study_hours_counts = work_study_hours_counts.div(work_study_hours_counts.sum(axis=1), axis=0)
ax = work_study_hours_counts.plot(kind='bar', stacked=True)
plt.title('Percentage of Depression by Work/Study Hours')
plt.xlabel('Work/Study Hours')
plt.ylabel('Percentage of Depression')
plt.legend(title='Depression', loc='upper right', labels=['No', 'Yes'])
plt.xticks(rotation=45)
ax.set_xticks(range(len(df['Work/Study Hours'].unique())))
ax.set_xticklabels(df['Work/Study Hours'].unique())
plt.tight_layout()
plt.show()



