import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

#Defining Parameters
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

st.set_option('deprecation.showPyplotGlobalUse', False)

#Inputting Text
option = st.selectbox('Which text would you like to analyze?', ('My Text', 'Sonnets', 'Plays'))

if option == 'My Text':
  textInput = st.text_area('Enter your text here to analyze:', '''
  Shall I compare thee to a summer’s day?
  Thou art more lovely and more temperate:
  Rough winds do shake the darling buds of May,
  And summer’s lease hath all too short a date:
  Sometime too hot the eye of heaven shines,
  And often is his gold complexion dimm’d;
  And every fair from fair sometime declines,
  By chance or nature’s changing course untrimm’d;
  But thy eternal summer shall not fade
  Nor lose possession of that fair thou owest;
  Nor shall Death brag thou wander’st in his shade,
  When in eternal lines to time thou growest:
  So long as men can breathe or eyes can see,
  So long lives this and this gives life to thee.
  ''', height=400)

if option == 'Sonnets':
  sonnets = open("data/Sonnets.txt","r")
  textInput = sonnets.read()
  sonnets.close() 

#Splitting Input
tokenizedInput = (textInput.lower()).split()
#print(tokenizedInput)

nav = st.sidebar.radio("Stats",["Your Text", "Sonnets", "Plays"])

if st.button('Analyze This'):
  if nav == "Any Position":
      #Counting Letters - TOTAL
      letterCounts = []
      counter = 0

      for match in letterList:
        counter = 0
        for token in tokenizedInput:
          for letter in token:
            if match == letter:
              counter = counter + 1
        letterCounts.append(counter)

      #Crafting Graph - TOTAL
      plt.bar(letterList, letterCounts)
      plt.title('Most Used Letters - Any Position')
      plt.xlabel('Letter')
      plt.ylabel('Frequency')
      plt.show()
      st.pyplot()

  if nav == "Starting Letters":
      #Counting Letters - START
      startCounts = []
      counter = 0

      for match in letterList:
            counter = 0
            for token in tokenizedInput:
                  if match == token[0]:
                    counter = counter + 1
            startCounts.append(counter)

      #Crafting Graph - START
      plt.bar(letterList, startCounts)
      plt.title('Most Used Letters - Starting')
      plt.xlabel('Letter')
      plt.ylabel('Frequency')
      plt.show()
      st.pyplot()
