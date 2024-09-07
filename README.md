# GenAI-Based-Resume: RAG-Based Chatbot

This repository contains a **Retrieval-Augmented Generation (RAG)** based chatbot that uses Generative AI to answer questions about **Ganesh Thorat's** resume. The chatbot is built using **Streamlit** and **LangChain**, leveraging **Google's Generative AI** for embeddings and natural language responses. It allows interviewers to interact with the chatbot and inquire about Ganesh's professional experience, skills, and more.

You can access the deployed version of the chatbot here: <a href="https://ganeshthorat.streamlit.app/" target="_blank">GenAI-Based Resume Chatbot</a>

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
The **GenAI-Based-Resume** chatbot is designed to simulate an interview process where the user (interviewer) can ask any questions regarding Ganesh Thorat's resume. The bot retrieves relevant information from the provided resume PDF, processes it with embeddings, and responds to queries in a human-like manner. 

This project uses **Retrieval-Augmented Generation (RAG)** to enhance the accuracy and relevance of answers by retrieving the most relevant chunks of the resume before generating a response using **Google's Gemini Pro** model.

## Features
- Interactive chatbot to answer questions about the resume.
- Integration with **FAISS** for efficient similarity search on the resume data.
- Uses **Google Generative AI** models for embeddings and conversational responses.
- Streaming response functionality for real-time interaction.
- Automatically processes resume in PDF format to create a knowledge base.

## Technologies Used
- **Python**
- **Streamlit** for the web application.
- **LangChain** for managing conversational flows and embeddings.
- **Google Generative AI** for LLM-based responses and embeddings.
- **FAISS** for similarity search.
- **HTML2Text** for converting PDF content.
- **dotenv** for managing environment variables.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ganesh-Thorat-01/GenAi-Based-Resume.git
   cd GenAi-Based-Resume
   ```

2. Set up your virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file in the root directory.
   - Add your Google API key and the URL to your resume PDF:
     ```
     GOOGLE_API_KEY=your_google_api_key
     PDF_PATH=your_resume_pdf_url
     ```

4. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

5. Open your browser at `http://localhost:8501` to interact with the chatbot.

## Usage

- Launch the chatbot and start by asking questions like "Tell me about your skills" or "What projects have you worked on?"
- The chatbot will retrieve relevant sections from the resume and provide an AI-generated response based on that context.

## File Structure

```bash
📦 GenAi-Based-Resume
├── faiss_index/           # Directory containing FAISS index for vector storage
├── .devcontainer/         # Dev container settings
├── .gitignore             # Ignore rules for Git
├── main.py                # Main Streamlit application script
├── requirements.txt       # Dependencies required to run the project
└── README.md              # Project documentation
```

### main.py

This script contains the logic for:
- Reading and splitting the resume PDF into chunks.
- Embedding the chunks using Google Generative AI.
- Storing and retrieving chunks with FAISS for similarity-based search.
- Handling user interactions in the chatbot interface.

## Contributing
Contributions are welcome! If you encounter any bugs or have suggestions, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For any questions or inquiries, you can reach out to:
- **GitHub**: [Ganesh-Thorat-01](https://github.com/Ganesh-Thorat-01)
- **Email**: thorat.ganeshscoe@gmail.com
---

*Made with ❤️ by Ganesh Thorat*

