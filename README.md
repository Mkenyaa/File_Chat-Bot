```markdown
# Streamlit App for Document Q&A

This Streamlit app allows users to upload JSON, CSV, and PDF files and enables Q&A with the uploaded documents using Langchain's RAG (Retrieval-Augmented Generation) approach. The app uses Chroma DB as the vector store and GPT-4 as the model. Users are prompted to enter their OpenAI API key.

## Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

## Setup Instructions

### Step 1: Clone the Repository

```sh
git clone https://github.com/Mkenyaa/File_Chat-Bot.git
cd your-repo
```

### Step 2: Create a Virtual Environment

Create a virtual environment to isolate the project's dependencies.

```sh
python -m venv myenv
```

### Step 3: Activate the Virtual Environment

Activate the virtual environment. The command depends on your operating system.

#### On Windows:
```sh
myenv\Scripts\activate
```

#### On macOS and Linux:
```sh
source myenv/bin/activate
```

### Step 4: Install the Necessary Packages

Install the required packages using pip.

```sh
pip install streamlit langchain openai chromadb PyMuPDF
```

### Step 5: Run the Streamlit App

Run the Streamlit app using the following command:

```sh
streamlit run main.py
```

## Usage

1. Open the Streamlit app in your web browser.
2. Enter your OpenAI API key in the sidebar.
3. Upload a JSON, CSV, or PDF file.
4. Ask a question about the document in the text input field.
5. The app will display the answer based on the content of the uploaded document.

## File Structure

```
your-repo/
├── main.py
├── README.md
└── myenv/
```

## Dependencies

- `streamlit`: For creating the web application.
- `langchain`: For handling the document loading, text splitting, embeddings, and QA chain.
- `openai`: For using the OpenAI API.
- `chromadb`: For using Chroma DB as the vector store.
- `PyMuPDF`: For handling PDF files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome!! Please open an issue or submit a pull request.

```