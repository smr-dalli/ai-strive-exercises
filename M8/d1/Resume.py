import streamlit as st

title = st.sidebar.title('Navigation')
pages = st.sidebar.radio('', ['About', 'Projects', 'Education', 'Skills'])


if pages == 'About':
    st.title('My Introduction')
    st.header('What am I doing?')
    st.markdown("""I am pursuing a master's in "Computational Methods in Engineering" at Leibniz University with a 
    strong background in Mechanical Engineering. Over the time, I have found my interest in the field of Artificial 
    Intelligence, I have enrolled in a 6 months Artificial Intelligence Bootcamp to advance my skills on AI.""")
    st.header('What am I looking for?')
    st.markdown("""I am actively looking for an internship in the field of Artificial Intelligence or AI on 
    Engineering.""")
    st.header('What are my interests?')
    st.markdown("""My interests are in the field of Machine Learning, Deep Learning, Computer Vision, Numerical 
    methods in fluid mechanics, Mechanics of Solids, Mechanics of advanced materials, Engineering dynamics and 
    vibrations, Finite elements, and Automobile Engineering.""")
    st.header('What are my competencies?')
    st.markdown("""
    * Software & Languages: PYTHON, MATLAB, PTC CREO, ANSYS, and C.
    * Libraries: PyTorch, Tensor Flow (Keras), Spacy, Pandas, Numpy, Sk-learn, Matplotlib, Seaborn, and Plotly. """)
    st.header('What are my hobbies?')
    st.markdown("""
    * I like playing/ watching Cricket Sport.
    * Cooking is my stress reliever.
    * I enjoy watching movies with friends and family.
    * I engage in interesting conversations.""")


if pages == 'Projects':
    st.title('Projects')
    st.markdown(""" 
    ## Artificial Intelligence Bootcamp, Strive School, Germany.
    I have worked on AI projects at Strive school and participated in Kaggle competitions.
    ### Face Recognition and Face Mask Detection
    **Focused on: Deep Learning and Computer Vision.**
    * Prepared a custom dataset by labeling the images of the mask, no mask, and bad mask.
    * Built a pre-trained ResNet model on PyTorch and Fastai to predict the images of mask, no mask, and bad mask.
    * Applied a bounding box that captures the face using Haar cascades classifiers.
    * Finally, detected faces with masks, no masks, and bad masks on the webcam and videos.
    * Python libraries: PyTorch, Fastai, OpenCV, Pandas, Numpy, and Matplotlib. 
    * Environments: Jupyter Notebook and Google Colab. 
    
    ### Jane Street Market Prediction (Kaggle competition)
    **Focused on: Machine Learning and Feature Engineering.**
    * Imported the data and pre-processed it to make clean data (Data Cleaning).
    * Discovered the patterns and plot the data by doing exploratory data analysis (EDA).
    * Applied the feature engineering techniques to extract new features from the data.
    * Fit the Machine Learning models to predict the data and also to calculate the accuracy.
    * Python libraries: Scikit-learn, XGBoost, Pandas, Numpy, Pycaret, Missingno, and Matplotlib. 
    * Environments: Jupyter/ Kaggle/ Google Colab Notebook.
    
    ### Web Scrapping the top 1000 books of Goodreads website
    **Focused on: Web Scrapping, Exploratory Data Analysis (EDA), Visualization, and Web App.**
    * Scrapped the 1000 best books from the Goodreads website and created a database.
    * Pre-processed and normalized the values of the features to a range between 0 to 1.
    * Analysed the features by grouping and aggregating to perform better computational insights.
    * Visualised the data to find out the patterns and trends among the features.
    * Created a web page and made it user friendly to upload the csv files and do the EDA. 
    * Python libraries: Beautiful Soup, Requests, Streamlit, Pandas, Numpy, Math, and Matplotlib. 
    
    ### More Projects on Deep Learning, Machine Learning,Computer Vision, and Feature Engineering:
    * Lane line detection for 'Self Driving Cars' using OpenCV.
    * Convolutional Neural Network (CNN) for binary classification of the images of cats and dogs using Tensor Flow and PyTorch.
    * CNN for multilabel classification of the handwritten/ fashion mnist datasets using PyTorch.
    * Predicting the tabular data and calculating the accuracy of the model using Tensor Flow.
    * Transfer learning pre-trained models such as ResNet and DenseNet for image classification.
    * Prediction on the titanic dataset and find the best Scikit-learn models based on accuracy.
    * Prediction the tabular data by using Scikit-learn models such as Random Forest, Decision tree, Gradient boosting, Support vector machines, Linear models, etc. 
    
    ## Academic Projects, Leibniz University, Germany.
    * Implemented code for the determination of stresses and strains in a laminated structure made of unidirectional fibre-reinforced composite materials using MATLAB.
    * Developed and analysed a model for moisture effects on the 1D structure.
    * Worked on Initial value, Boundary value problems, also Static and Dynamic analysis.
    * Calculated the stiffness constants of fibre-reinforced material through numerical homogenization conducted with the FEM using ANSYS software.
    * Analysis of anisotropic material response and bending of a wooden beam.
    * Solved stationery/transient advection-diffusion-equation using finite difference.
    * Calculated the level of contamination concentration (E.coli bacteria) transferred from a sanitary source to the water well using MATLAB.
    * Calculated the probability of failure of a model depending on the input variables and parameters using Monte Carlo simulation and determined the sensitivity analysis.
    
    ## More projects:
    * Drilling attachment for broken bolt removal at Rough Mill Strand.
    * Project on Hybrid Vehicle Challenge.

    
    
    
    
    
    
    
    
    """)

