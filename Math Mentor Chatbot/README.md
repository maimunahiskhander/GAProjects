# Math Mentor Chatbot

Prepared by: Maimunah Binte Iskhander, 7 Dec 2023

### Overview

This project introduces a specialized chatbot designed to assist students in solving PSLE (Primary School Leaving Examination) multiple choice mathematics questions. The chatbot leverages advanced natural language processing techniques, employing Retrieval Augmented Generation (RAG) and Llama-index for enhanced information retrieval and answer accuracy. It runs on a fine-tuned version of the GPT-3.5-turbo engine, specifically optimized for mathematical problem-solving. This custom solution aims to provide an interactive and effective tool for students preparing for the PSLE in Singapore, offering them a novel way to engage with challenging math concepts and practice questions.

### Problem Statement

Our AI-powered chatbot addresses the need for accessible and timely academic support, offering instant and personalized assistance to upper primary students. It fills the gaps in traditional learning by providing on-demand explanations, solutions, and concept clarifications, enhancing student engagement and understanding in mathematics

### Evaluation Criteria

Given that we are using a chatbot, the evaluation metrics will be the RAGAS score, answer relevancy and faithfulness.

### Datasets

80 multiple choice questions without diagrams from past PSLE papers.

### Data Dictionary

| Variable Name         | Data Type           | Description                                   |
|-----------------------|---------------------|------------------------------------------|
| `image`             | object              | image no     |
| `question`               | object              | question stem with four options       |
| `solution`            | object              | detailed solution             |
| `classification`     | object           | cognitive level classification (AO1/AO2/AO3)  |
| `topic`            | object              | topic the question belongs to              |



### Submissions
Files submitted: 
* [`01_Data_Prep.ipynb`](./code/01_Data_Prep.ipynb): This notebook covers data collection, cleaning and preprocessing.
* [`backend-processing.ipynb`](./streamlit/backend-processing.ipynb): This notebook delves into the 'behind the scenes' of building the index for the chatbot as well as its training and evaluation.
* [`app.py`](./streamlit/app.py): This notebook contains the code to run the streamlit application that employs the fine-tuned engine. It acts as an interface for the chatbot.
* [`ai_meets_math_slides.pdf`](./slides/ai_meets_math_slides.pdf): Presentation slides for the project.

### Summary
The fine-tuned GPT-3.5-Turbo model was chosen to be the final engine for the chatbot.

| Model | RAGAS Score | Answer Relevancy | Faithfulness |
|:----------------:|:-----------:|:------------------:|:--------------:|
| GPT-3.5-Turbo | 0.7685 | 0.8517 | 0.7000 |
| Fine-tuned | 0.8150 | 0.8922 | 0.7500 |

### Conclusion

In this project, we successfully developed an AI-powered chatbot designed to enhance the learning experience of upper primary students in mathematics. By addressing the critical need for timely and personalized academic support, our chatbot has demonstrated its capability to bridge the gaps in traditional educational methods. Key features such as on-demand explanations, problem-solving assistance, and concept clarification have significantly contributed to improving student engagement and understanding in mathematics.

### Areas for Improvement

1.  **Enhance Data Repository**: By adding more diverse and comprehensive data, we can further train the model to understand and respond to a wider array of mathematical queries. This expansion will improve the model's accuracy and predictive capabilities, making it more robust and reliable.
    
2.  **Incorporate Word Problems**: Customizing the model to handle word problems will add a critical dimension to the chatbot, enabling it to assist with more complex and real-world mathematical scenarios. This feature will help students develop their problem-solving skills in a more practical context.
    
3.  **Interactive UI Elements**: Introducing interactive elements like buttons for common prompts can make the chatbot more user-friendly and intuitive. This will streamline the interaction process, allowing students to quickly access frequently needed assistance.
    
4.  **Broaden the Range of Topics**: Expanding the chatbot's knowledge base to cover a broader range of mathematical topics will make it a more comprehensive educational tool. This expansion will cater to a wider spectrum of student needs and curricular requirements.
    
5.  **Incorporate Student Feedback**: Regularly integrating feedback from students will ensure that the chatbot evolves in line with the users' needs and preferences. This feedback loop will be instrumental in continuously refining the chatbot's effectiveness and user experience.
    
6.  **App Integration**: Developing a dedicated mobile or web application for the chatbot can enhance accessibility and convenience. An app would provide a centralized platform for students to access the chatbot and could include additional features like progress tracking, personalized learning paths, and interactive learning resources.


