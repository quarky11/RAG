from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
import os 


#python -m venv nama_env
#pip install -r requirements.txt

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    cleaned_chunks = [chunk.replace("\n", " ") for chunk in chunks]
    return cleaned_chunks


def get_vectorstore(text_chunks):
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    model = embeddings.embed_documents(text_chunks)
    #vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return model

pdf_docs = [os.path.expanduser("~/Downloads/Dokumen tanpa judul (1).pdf")]  # Expand '~' to your home directory
text = get_pdf_text(pdf_docs)  # Extract text
text_chunks = get_text_chunks(text)
embeding = get_vectorstore(text_chunks)


print (embeding)