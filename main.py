import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import requests
import html2text

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set path to your PDF file
PDF_PATH=os.getenv("PDF_PATH")

def get_pdf_text(pdf_path):
    response = requests.get(pdf_path)
    content = response.text
    content=html2text.html2text(content)
    return content

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_response(question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(question)

    prompt_template = """
    You will be provided your resume. Act as a person which has below resume and 
    Answer the question as detailed as possible from the provided context.
    If user is greeting you please greet them with respect.\n\n
    Context:\n {docs}?\n
    Question: \n{question}\n

    Answer:
    """

    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3,disable_streaming=False)
    prompt=ChatPromptTemplate.from_template(prompt_template)
    chain= prompt | llm | StrOutputParser()

    return chain.stream({
        "question":question,
        "docs":docs
    })

st.set_page_config(page_title="Ganesh Thorat", page_icon=r"logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.header(":violet[ChatBot] -  :blue[GenAI based] :orange[Resume]",divider='rainbow', help = "This bot is designed by Ganesh Thorat to address all of your questions about me")
st.subheader("Hello! There, How can I help you Today- 👩‍💻")
st.caption(":violet[Ask] :orange[anything] :violet[about] :violet[me] :blue[ᓚᘏᗢ]")

# Process the PDF file automatically
pdf_text = get_pdf_text(PDF_PATH)
text_chunks = get_text_chunks(pdf_text)
get_vector_store(text_chunks)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask about me (eg. Tell me about yourself)"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(get_response(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})