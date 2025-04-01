The backend is built using **Flask** and handles the content processing, question-answering, and vector database interactions.

### Features
- Extracts webpage content from a given URL
- Implements Retrieval-Augmented Generation (RAG)
- Uses OpenAI APIs for text processing
- Stores embeddings in Pinecone for efficient retrieval

### Tech Stack
- Flask
- OpenAI API
- Pinecone (Vector Database)
- Selenium (for web scraping)

### Setup Instructions
```sh
# Clone the repository
git clone https://github.com/hiren1407/chatbot-backend.git
cd chatbot-backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
flask run
```

### Environment Variables
Create a `.env` file in the root directory and configure the following:
```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
