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
    st.markdown("""PYTHON, MATLAB, PTC CREO, ANSYS, and C. Libraries include PyTorch, 
    Tensor Flow (Keras), Spacy, Pandas, Numpy, Sk-learn, Matplotlib, Seaborn, and Plotly. """)
    st.header('What are my hobbies?')
    st.write("I like playing/ watching Cricket Sport.")
    st.write("Cooking is my stress reliever.")
    st.write("I enjoy watching movies with friends and family.")
    st.write("I engage in interesting conversations.")

if pages == 'Projects':
    st.title('Projects')
    st.header('Artificial Intelligence')
    st.write('I have worked on AI projects at Strive school and participated in Kaggle competitions.')
    st.subheader('Face Mask Detection based on Deep Learning and Computer Vision.')
    st.write('Tasks:')
    st.write('I have Prepared a custom dataset by saving and labeling the images of the mask, no mask, bad mask.')
    st.write('I have built a pre-trained ResTNet model on PyTorch and Fastai to predict the images of mask, no mask, '
             'and bad mask.')
    st.write('I have applied a bounding box that captures the face using Haar cascades classifiers')
    st.write('Finally, I have detected faces with masks, no masks, and bad masks on the webcam and videos.')
    st.write('Python libraries: PyTorch, Fastai,and OpenCV. Environments: Jupyter Notebook and Google Colab')
