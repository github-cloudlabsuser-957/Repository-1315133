**MetaRAGicians Chatbot**

Welcome to the MetaRAGicians Chatbot! This repository contains code for a simple RAG chatbot built using azure cloud environment. This README will guide you through the process of setting up and running the code.

### Overview
Retrieval Augmented Generation (RAG) is one of the key techniques used to build chatbots for answering questions on domain data. RAG consists of two components: a retrieval model and an answer generation model based on LLM. The retrieval model fetches context relevant to the user’s query. The query and the retrieved context are then inputted to the LLM with the appropriate prompt to generate the answer. 

### Requirements
- Python 3.x
- pip (Python package installer)

### Setup
1. Clone this repository to your local machine:

```
git clone https://github.com/github-cloudlabsuser-957/Repository-1315133.git
```

2. Navigate to the cloned directory:

```
cd Repository-1315133
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

### Usage
1. Run the chatbot script:

```
streamlit run metaRAGicians.py
```

2. Once the chatbot is running, open the link in a browser and you can interact with it using natural language commands. 
   Eg:
- "What is the whitepaper Huawei and orange about"
- "What tools are mentioned to gather insights on  digital transformation ?"

3. You can upload documents and ask questions based on that document , chatbot will retrieve information from the uploaded documents.
   
### Configuration
- You can customize the API Endpoints and Key by modifying the `.env` file.
- You can change the cloud database end point into custom database and use for different usecases.

### Contributing
Contributions to this project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

### Credits
This chatbot was created by team MetaRAGicians. Special thanks to the developers of the libraries and tools used in this project.

### Support
If you encounter any issues or have questions about the chatbot, please open an issue on GitHub or contact odl_user_1313538@cloudlabssandbox.onmicrosoft.com .

Happy task management with the RAG Chatbot! 🚀
