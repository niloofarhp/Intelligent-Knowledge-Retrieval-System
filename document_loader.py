import glob, os
import easyocr
from langchain.document_loaders import DirectoryLoader, TextLoader, PyMuPDFLoader
from langchain.docstore.document import Document 
from langchain.text_splitter import CharacterTextSplitter
from PIL import Image
import numpy as np 

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

def load_image_documents(images_path):
    reader = easyocr.Reader(['en'])  # Adjust languages as needed
    image_docs = []
    img_files = glob.glob(os.path.join(images_path, "**/*.png"), recursive=True)
    for img_f in img_files:
        img = Image.open(img_f).convert("RGB")
        img_np = np.array(img)
        ocr_result = reader.readtext(img_np, detail=0)
        extracted_text = " ".join(ocr_result)

        doc = Document(
            page_content=extracted_text,
            metadata={
                "source": img_f,
                "type": "image"
            }
        )
        image_docs.append(doc)

    return image_docs

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)
