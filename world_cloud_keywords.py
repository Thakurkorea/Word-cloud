# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:21:32 2024
Himalaya Cloud
@author: IT
"""


%reset -f
%clear
import os
if os.name == 'posix':
   os.system('clear')
else:
   os.system('cls')
   
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
file_pth='scopus_Himalaya.csv'


df= pd.read_csv( file_pth) # let's update english name 
df.columns

# Concatenate columns, split by both commas and semicolons, flatten, strip whitespace, and drop NaNs
all_keywords = pd.concat([df['Author Keywords'], df['Index Keywords']]) \
                 .str.split('[,;]', expand=True) \
                 .stack().str.strip().str.lower().dropna()  # we made lower case too

# Ensure all elements are strings (to prevent any non-string errors)
all_keywords = all_keywords[all_keywords.apply(lambda x: isinstance(x, str))]

# Create DataFrame and calculate word frequencies
all_keywords_df = pd.DataFrame(all_keywords, columns=['all_keywords'])
word_freq = all_keywords_df['all_keywords'].value_counts()

# Save word frequencies to CSV
word_freq.to_csv("Word_frequency.csv", header=["Frequency"])

# Generate word cloud from word frequencies
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()