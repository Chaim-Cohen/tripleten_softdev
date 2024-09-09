# importing pandas for EDA, streamlit for creating the app, plotly.express for both, and altair
import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt


# reading the file and storing it to 'df'
df=pd.read_csv('vehicles_us.csv')


# replace all the empty cells in the 'paint_color' column with 'unknown'
df['paint_color']=df['paint_color'].fillna('unknown')

# replace all the empty cells in the 'is_4wd' column with 'unknown'
df['is_4wd']=df['is_4wd'].fillna('unknown')

# replace all the empty cells in the 'model_year' column with the median values for that model
df['model_year'] = df['model_year'].fillna(df.groupby(['model'])['model_year'].transform('median'))

# convert median value to an integer instead of a float
df['model_year'] = df['model_year'].apply( lambda x: int(x))

# replace all missing values in 'cylinders' column with the median number of cylinders for that model
df['cylinders'] = df['cylinders'].fillna(df.groupby(['model'])['cylinders'].transform('median'))

# convert median value to an integer instead of a float
df['cylinders'] = df['cylinders'].apply( lambda x: int(x))

# replace all the empty cells in the 'odometer' column with the median values for that model
df['odometer'] = df['odometer'].fillna(df.groupby(['model'])['odometer'].transform('median'))


# create function for replacing wrong model names with right ones
def replace_wrong_model(wrong_models, right_model):
    for wrong_model in wrong_models:
        df['model']=df['model'].replace(wrong_models, right_model)

wrong_models='ford f150'
right_model='ford f-150'
replace_wrong_model(wrong_models, right_model)

wrong_models='ford f250'
right_model='ford f-250'
replace_wrong_model(wrong_models, right_model)

wrong_models=['ford f-250 sd', 'ford f250 super duty']
right_model='ford f-250 super duty'
replace_wrong_model(wrong_models, right_model)

wrong_models='ford f350'
right_model='ford f-350'
replace_wrong_model(wrong_models, right_model)

wrong_models='ford f350 super duty'
right_model='ford f-350 super duty'
replace_wrong_model(wrong_models, right_model)


# declare app title
st.title('Find Your Car!')

st.caption(':blue[Select your preferences here]')

# create slider to filter the dataset by model_year
model_year_range = st.slider(
    "Select model year range",
    value= (1908, 2019))

# create list of selected model_year range values
actual_model_year = list(range(model_year_range[0],model_year_range[1]+1))

# create checkbox to filter chosen data for cars priced under 50,000
under_50k = st.checkbox('Cars under 50k')

# create filter for the 'excellent_condition' checkbox
if under_50k:
    filtered_df=df[df.model_year.isin(actual_model_year)]
    filtered_df=filtered_df[df.price<=50000]
else:
    filtered_df=df[df.model_year.isin(actual_model_year)]

# demonstrate scatterplot of the data presented according to 'model_year' and 'price'
st.write('Here are your options compared by model_year and price')

fig = px.scatter(filtered_df, x='model_year', y='price')           
st.plotly_chart(fig)


# prepare and show a histogram of filtered_df to show spread of 'days_listed'
st.write('Distribution of number of days selected listings remained available')

fig_2 = px.histogram(filtered_df, x='days_listed')
st.plotly_chart(fig_2)


# offer sample listings that match selected parameters
st.write('Here is a sample of cars that match your criteria')
st.dataframe(filtered_df.sample(10))