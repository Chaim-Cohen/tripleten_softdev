# Project

## Links
Link to GitHub repository: https://github.com/Chaim-Cohen/tripleten_softdev
URL of app on Render: https://https://tripleten-softdev.onrender.com

# Project Description

This project is an app interface to view data on cars for sale. The data can be filtered according to 2 different variables, which changes the data displayed in the various visualizations.
The project begins with a dataset (vehicles_us.csv) which was then analysed (EDA.ipynb), prepared for an app (app.py), committed to github and deployed as a web service on render.com.
The project incoporates pandas, streamlit, and plotly.express libraries for analyzing, preprocessing and preparing the data 
(in both EDA and in app.py). It also includes st.write, st.header, st.slider, st.plotly_chart, st.checkbox, st.sample, px.scatter, and px.histogram to visualize the data (in app.py).


# Application use instructions
The application opens to a page with several visualizations. There is a scatterplot of 'model_year' and 'price', there is a histogram of 'days_listed' (i.e, the duration of the car listing in the advertisment dataset), and a table with a sample of rows from the dataset.

The entire dataset included in all 3 visualizations by default. 

The user can then filter the dataset by 'model_year' using a 'slider', this will affect all the visualizations.
The user can also filter the dataset by 'price' with a checkbox, which retains all cars with a price below 50,000 USD. This will also affect all the visualizations.

The application can also be run on a local machine
To do this install: pandas, streamlit, plotly.express, and altair.
Then clone the github repository from: https://github.com/Chaim-Cohen/tripleten_softdev
Find file ‘app.py’ and run it with command “streamlit run app.py” from the terminal. 
