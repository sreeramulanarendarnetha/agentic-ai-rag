from pinecone import Pinecone, ServerlessSpec
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

from config import (
    PDF_PATH,
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    PINECONE_CLOUD,
    PINECONE_REGION,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def load_and_split_pdf():
    print("1. Loading PDF...")

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    print(f"   Loaded {len(documents)} pages.")

    print("2. Splitting document into chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    print(f"   Created {len(chunks)} chunks.")

    return chunks


def create_pinecone_index():
    print("3. Setting up Pinecone...")

    pc = Pinecone(api_key=PINECONE_API_KEY)

    existing_indexes = [index["name"] for index in pc.list_indexes()]

    if PINECONE_INDEX_NAME not in existing_indexes:
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud=PINECONE_CLOUD,
                region=PINECONE_REGION,
            ),
        )

        print(f"   Created index: {PINECONE_INDEX_NAME}")
    else:
        print(f"   Index already exists: {PINECONE_INDEX_NAME}")


def create_embeddings():
    print("4. Loading free local embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("   Local embedding model ready.")

    return embeddings


def upload_to_pinecone(chunks, embeddings):
    print("5. Uploading embeddings to Pinecone...")

    PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name=PINECONE_INDEX_NAME,
        pinecone_api_key=PINECONE_API_KEY,
    )

    print("   Embeddings uploaded successfully.")


def main():
    print("=" * 60)
    print("PDF → Pinecone ETL PIPELINE")
    print("=" * 60)

    chunks = load_and_split_pdf()

    create_pinecone_index()

    embeddings = create_embeddings()

    upload_to_pinecone(chunks, embeddings)

    print("=" * 60)
    print("ETL PROCESS COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()