import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Fungsi untuk menghubungkan ke MongoDB
def get_data_from_mongodb():
    client = MongoClient('mongodb+srv://rizkyfarizh:27072000@uts.uk2opke.mongodb.net/')  # Ganti dengan URL MongoDB Anda
    db = client['rambu']  # Ganti dengan nama database Anda
    collection = db['lalulintas']  # Ganti dengan nama koleksi Anda

    data = list(collection.find({}, {'class': 1, '_id': 0, 'day': 1, 'month': 1, 'year': 1}))  # Mengambil data tanpa '_id'
    return pd.DataFrame(data)

# Fungsi untuk membuat diagram
def plot_data(df, attribute, col1, col2):
    data_count = df[attribute].value_counts().sort_index()
    
    col1.bar_chart(data_count)
    col2.line_chart(data_count)

def main():
    st.title('MongoDB Data Visualization with Streamlit')
    
    # Mengambil data dari MongoDB
    data = get_data_from_mongodb()
    
    if not data.empty:
        st.write('Data from MongoDB:')
        st.write(data)
        
        # Pilihan atribut untuk visualisasi
        attributes = ['class', 'day', 'month', 'year']
        attribute = st.selectbox('Select attribute to visualize:', attributes)
        
        # Plotting data
        col1, col2 = st.columns(2)
        plot_data(data, attribute, col1, col2)
        
    else:
        st.write('No data found in the collection.')

if __name__ == '__main__':
    main()
