import glob, os
from langchain.document_loaders import DirectoryLoader, TextLoader, PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def load_documents(base_path):
    documents = []
    text_loader_kwargs = {'encoding': 'utf-8'}
    folders = glob.glob(os.path.join(base_path, "*"))

    for folder in folders:
        doc_type = os.path.basename(folder)

        # Load .md and .txt files
        for ext in ["*.md", "*.txt"]:
            loader = DirectoryLoader(
                folder,
                glob=f"**/{ext}",
                loader_cls=TextLoader,
                loader_kwargs=text_loader_kwargs
            )
            docs = loader.load()
            for doc in docs:
                doc.metadata["doc_type"] = doc_type
            documents.extend(docs)

        # Load .pdf files using PyMuPDFLoader
        pdf_files = glob.glob(os.path.join(folder, "**/*.pdf"), recursive=True)
        for pdf_path in pdf_files:
            loader = PyMuPDFLoader(pdf_path)
            docs = loader.load()
            for doc in docs:
                doc.metadata["doc_type"] = doc_type
            documents.extend(docs)
    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)
