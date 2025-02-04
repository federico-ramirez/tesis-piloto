#from langchain.document_loaders import UnstructuredLoader
from langchain_community.document_loaders import UnstructuredFileLoader

def extract_text_with_langchain_pdf(pdf_file):
    
    loader = UnstructuredFileLoader(pdf_file)
    documents = loader.load()
    pdf_pages_content = '\n'.join(doc.page_content for doc in documents)
    
    return pdf_pages_content

def main():
    text_with_langchain_files = extract_text_with_langchain_pdf("proyectosed.pdf")
    print(text_with_langchain_files)

if __name__ == '__main__':
    main()