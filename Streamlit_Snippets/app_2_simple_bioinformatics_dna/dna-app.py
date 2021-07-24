######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


######################
# Page Title

# Reference: The Data Professor (http://youtube.com/dataprofessor)

######################

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

Count the number of neucleotides ! 

***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query 1\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name 
sequence = ''.join(sequence) # list to string

st.write("""
***
""")

## Prints the input
st.header('INPUT')
st.text_area("Sequence", sequence, height=250)


## DNA count
st.header('OUTPUT')

### dictionary
st.subheader('Print Counter')
def counter(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = counter(sequence)
X # prints 


### text
st.subheader('Print in text form')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### DataFrame
st.subheader('Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'item'})
st.write(df)

### Bar Chart using Altair
st.subheader('Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='item',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
