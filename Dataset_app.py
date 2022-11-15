import streamlit as st
import pandas as pd
import seaborn as sns

# 1. Title and Subheader
st.title('Data Analysis')
st.subheader("Data Analysis using Python and streamlit")

# 2. Upload Dataset
upload=st.file_uploader('Please upload your CSV file Below')
if upload is not None:
    dat=pd.read_csv(upload)

# 3. Show Dataset    
if upload is not None:
    if st.checkbox("Preview"):
        if st.button('First 5 records'):
            st.write(dat.head())
        if st.button("Last 5 records"):
            st.write(dat.tail())
            
# 4. Check DataType of Each Column
if upload is not None:
    if st.checkbox('Datatype'):
        st.text("Datatype")
        st.write(dat.dtypes)
        
# 5. Find Shape of Our Dataset (Number of Rows And Number of Columns)
if upload is not None:
    dat_shap=st.radio("Please select Dimension",('Rows','Columns'))
    if dat_shap=='Rows':
        st.text('Count:')
        st.write(dat.shape[0])
    if dat_shap=='Columns':
        st.text('Count:')
        st.write(dat.shape[1])
        
    
# 6. Find Null Values in The Dataset
if upload is not None:
    boo=dat.isnull().values.any()
    if boo==True:
        if st.checkbox('Check for null values'):
            sns.heatmap(dat.isnull())
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
    else:
        st.success("No missing values found!!")


# 7. Find Duplicate Values in the dataset
if upload is not None:
    dup=dat.duplicated().any()
    if dup==True:
        st.warning('Dataset contain some duplicated value')
        t=st.selectbox('Do you want to remove duplicate values',('No','Yes'))
        if t=='Yes':
            dat=dat.drop_duplicates()
            st.text('Duplicate data are now removed')
        if t=='No':
            st.text('No date where removed')
    else:
        st.success("No duplicate values found!!")    


# 8. Get Overall Statistics
if upload is not None:
    if st.checkbox('Get overall statistics'):
        st.write(dat.describe())

# 9. About Section
if st.button('About'):
    st.text('This page was created using Streamlit')

# 10. By
if st.checkbox('Created By:'):
    st.success('Sanjith VGS')


#  download updated file