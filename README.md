# social-media-stress-prediction
 This project presents a Stress Level Prediction System developed using deep learning techniques and deployed as a Streamlit web application. The system predicts an individual’s stress level based on parameters such as age, gender, job type, social media usage, notification frequency, working hours, sleep duration, screen time before sleep etc...
A trained deep learning model processes the scaled input data and outputs a numerical stress level score. The web-based interface allows users to easily input their daily habits and instantly receive stress predictions. This project demonstrates how artificial intelligence and deep learning can be applied effectively in mental health analytics and stress monitoring systems.


INTRODUCTION
Stress is a natural psychological and physiological response to challenges and demands. While moderate stress can be motivating, prolonged or excessive stress leads to serious health issues such as anxiety, depression, cardiovascular diseases, and reduced work performance. In today’s digital environment, factors such as excessive screen exposure, constant notifications, long working hours, and poor sleep habits significantly contribute to stress.
Traditional stress evaluation methods are largely subjective and depend on clinical assessments or self-reported questionnaires. These methods are not scalable and cannot provide real-time insights into an individual’s stress condition. With the advancement of machine learning and deep learning, it has become possible to analyze behavioral data and predict stress levels accurately.
This project introduces a deep learning-based stress prediction system that estimates stress levels using lifestyle and work-related parameters. By deploying the model through Streamlit, the system becomes accessible as an interactive web application. The project highlights the importance of data-driven mental health assessment and demonstrates the practical use of AI in stress analysis.
This study analyzes the relationship between sleep quality, workload, and stress, providing empirical evidence for stress modeling


 LITERACY SURVEY:-
Stress and Lifestyle Factors
Author(s): Lazarus and Folkman
Year: 1984
This work introduces the transactional model of stress and coping, emphasizing how lifestyle and environmental factors influence stress responses.
Machine Learning in Mental Health Assessment
Author(s): Shatte et al.
Year: 2019
The authors review machine learning applications in mental health, highlighting predictive models for stress and emotional well-being.
Impact of Sleep and Workload on Stress
Author(s): Åkerstedt et al.
Year: 2014
This study analyzes the relationship between sleep quality, workload, and stress, providing empirical evidence for stress modeling.
Deep Learning for Behavioral Prediction
Author(s): Goodfellow et al.
Year: 2016
The book explains deep learning techniques and their ability to model complex behavioral patterns, forming the basis for stress prediction systems.
Rapid Deployment of ML Applications Using Streamlit
Author(s): Streamlit Inc.
Year: 2019
This reference presents Streamlit as a framework for deploying machine learning models with interactive web interfaces.
     
 SYSTEM ANALYSIS
3.1 EXISTING SYSTEM
Existing stress assessment systems rely mainly on psychological questionnaires, interviews, and clinical evaluations. These methods are subjective and depend heavily on user honesty and emotional state at the time of assessment. They are also time-consuming and require trained professionals.
Some digital wellness applications track limited parameters such as screen time or sleep but fail to combine multiple factors into a unified stress assessment. These tools lack predictive capabilities and often provide generic insights rather than personalized analysis.
Traditional systems are not scalable and cannot adapt to changing behavioral patterns. They also do not provide quantitative stress scores based on data analysis. These disadvantages highlight the need for an automated, intelligent, and data-driven stress prediction system.

3.2 DISADVANTAGES
1. Data Quality and Labeling Issues
Psychological states (e.g., anxiety, depression, loneliness) are complex and subjective, yet ML/DL models often rely on self-reported surveys, proxy labels, or inferred behaviors, which may be inaccurate, inconsistent, or biased. Poor-quality labels lead to unreliable predictions.
2. Ethical and Privacy Concerns
Analyzing social media data raises serious privacy, consent, and surveillance issues. Users may not be aware their posts, messages, or interactions are being used to infer mental health conditions, potentially violating ethical standards and data protection regulations.
3. Bias and Lack of Representativeness
Social media users are not representative of the general population. ML/DL models may inherit demographic, cultural, and socioeconomic biases, leading to skewed results and unfair conclusions especially for underrepresented groups.

4. Limited Interpretability of Deep Learning Models
Deep learning models often function as “black boxes”, making it difficult for psychologists, clinicians, and policymakers to understand why a particular prediction was made. This lack of explainability limits trust and real-world applicability.
3.3 PROPOSED SYSTEM
The proposed system introduces a deep learning-based approach to stress level prediction. By analyzing multiple lifestyle and work-related parameters, the system captures complex interactions that contribute to stress.
The Streamlit-based interface ensures ease of use and accessibility. Users can input their daily habits and instantly receive stress level predictions. The use of a scaler ensures consistent preprocessing and improved prediction accuracy.

3.4 ADVANTAGES :-
Machine Learning and Deep Learning
1.	Early Detection of Mental Health Risks
Machine learning and deep learning models can identify early signs of stress, anxiety, depression, or emotional imbalance from social media usage patterns, enabling timely intervention.
2.	Handling Large and Complex Data
Social media generates vast amounts of structured and unstructured data. ML and DL techniques efficiently analyze large datasets, including text, images, and behavioral patterns, which are difficult to process manually.
3.	Improved Prediction Accuracy
Deep learning models capture complex, non-linear relationships between social media behavior and psychological states, resulting in higher accuracy compared to traditional statistical methods.
4.	Real-Time Monitoring
ML-based systems can continuously monitor user behavior and update psychological assessments in real time, allowing dynamic and up-to-date mental health analysis.
5.	Personalized Insights
These models provide personalized psychological assessments based on individual usage patterns, helping tailor mental health recommendations and interventions.
6.	Automation and Scalability
Once trained, ML and DL systems can automatically analyze data for thousands or millions of users, making the approach scalable and cost-effective.
7.	Objective and Data-Driven Analysis
Machine learning reduces human bias by relying on data-driven insights rather than subjective self-reports or manual evaluations.
8.	Multimodal Data Analysis
Deep learning can integrate multiple data types such as text posts, emojis, images, engagement metrics, and time-based activity, offering a holistic psychological assessment.
9.	Support for Mental Health Research
The insights generated help psychologists and researchers better understand the relationship between social media usage and mental health trends across different populations.
10.	Decision Support for Policy and Well-being Applications
The results can guide institutions, educators, and healthcare professionals in designing mental health awareness programs and digital well-being policies.

 
