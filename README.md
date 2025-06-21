# RAG LLM - Amazon Archaeology Knowledge Base

A Streamlit application for querying an Amazon archaeology knowledge base using OpenAI's Vector Store and Retrieval-Augmented Generation (RAG).

## 🏛️ Overview

This project provides a complete RAG (Retrieval-Augmented Generation) system for querying archaeological knowledge about the Amazon rainforest. It includes:

- **Streamlit Web App**: Interactive interface for querying the knowledge base
- **Vector Store Management**: Tools to upload and manage knowledge base documents
- **Cleanup Utilities**: Scripts to manage OpenAI vector stores and files
- **Knowledge Base**: Pre-generated research documents on Amazon archaeology

## 🚀 Features

- **Interactive Web Interface**: Query your knowledge base through a user-friendly Streamlit app
- **Multiple Vector Stores**: Support for multiple knowledge bases
- **Configurable Models**: Adjust temperature, search parameters, and model selection
- **Chat History**: Maintain conversation history during your session
- **File Upload Management**: Easy upload of knowledge base documents
- **Cleanup Tools**: Manage and clean up vector stores and files

## 📋 Prerequisites

- Conda or Miniconda installed
- Python 3.11 (managed by conda)
- OpenAI API key with access to:
  - GPT models (gpt-4o, gpt-4o-mini, gpt-3.5-turbo)
  - Vector Store API (beta feature)
  - Files API

## 🛠️ Installation

### Option 1: Quick Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd OpenAI_to_Z
   ```

2. **Run the setup script**
   ```bash
   ./setup.sh
   ```

3. **Set up environment variables**
   ```bash
   # Edit .env file and add your OpenAI API key
   nano .env  # or use your preferred editor
   ```

### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd OpenAI_to_Z
   ```

2. **Create conda environment**
   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the environment**
   ```bash
   conda activate rag-llm-env
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env and add your OpenAI API key
   ```

## 📚 Usage

### 1. Activate Environment

```bash
conda activate rag-llm-env
```

### 2. Upload Knowledge Base

First, upload your knowledge base documents to OpenAI Vector Store:

```bash
# Upload the existing knowledge base
python src/upload_knowledge_base.py --dir data/Knowledge_base --name "amazon_archaeology_kb"

# Upload research reports
python src/upload_knowledge_base.py --dir data/Deep_Research_reports --name "research_reports"

# Upload with custom extensions
python src/upload_knowledge_base.py --dir data/Knowledge_base --name "my_kb" --extensions md txt

# Dry run to see what would be uploaded
python src/upload_knowledge_base.py --dir data/Knowledge_base --name "my_kb" --dry-run
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### 4. Query Your Knowledge Base

1. Select a vector store from the sidebar
2. Adjust model settings (temperature, search results, etc.)
3. Enter your question in the text area
4. Click "Ask" to get an answer based on your knowledge base

### 5. Cleanup (Optional)

Manage your vector stores and files:

```bash
# List all vector stores
python src/cleanup_vector_stores.py --list-stores

# Clean up a specific vector store
python src/cleanup_vector_stores.py --cleanup-store "my_knowledge_base"

# Clean up all vector stores matching a pattern
python src/cleanup_vector_stores.py --cleanup-all-pattern "OpenAI_challenge_"

# Delete all files (dry run first)
python src/cleanup_vector_stores.py --delete-all-files --dry-run

# Delete all files for real
python src/cleanup_vector_stores.py --delete-all-files

# Delete only assistant files
python src/cleanup_vector_stores.py --delete-all-files --purpose assistants
```

### 6. Deactivate Environment

```bash
conda deactivate
```

## 📁 Project Structure

```
OpenAI_to_Z/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies (for pip)
├── environment.yml                 # Conda environment specification
├── setup.sh                        # Setup script
├── env.example                     # Environment variables template
├── README.md                       # This file
├── src/
│   ├── vector_store_manager.py     # Vector store management class
│   ├── upload_knowledge_base.py    # Knowledge base upload script
│   └── cleanup_vector_stores.py    # Cleanup utilities
├── data/
│   ├── Knowledge_base/             # Pre-generated knowledge base documents
│   └── Deep_Research_reports/      # Research reports
└── notebooks/                      # Original Jupyter notebooks
```

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_ORG_ID`: Your OpenAI organization ID (optional)
- `OPENAI_BASE_URL`: Custom OpenAI API URL (optional)

### Model Settings

In the Streamlit app, you can configure:

- **Chat Model**: Choose between gpt-4o-mini, gpt-4o, or gpt-3.5-turbo
- **Temperature**: Control response creativity (0.0 = focused, 1.0 = creative)
- **Search Results (k)**: Number of relevant passages to retrieve (1-10)

## 💡 Example Questions

Try these example questions with the Amazon archaeology knowledge base:

1. "What are the locations of known archaeological sites in the Amazon Rainforest?"
2. "What is the location of Kuhikugu (GPS coordinate)?"
3. "What techniques have been used to discover new archaeological sites in the Amazon rainforest in recent years?"
4. "What is the impact of the presence of Amazonian dark earth on vegetation?"
5. "What open-access LIDAR datasets cover portions of the Brazilian Amazon?"

## 🎯 Features in Detail

### Vector Store Manager

The `VectorStoreManager` class provides:

- **Create/Get Vector Stores**: Automatically create or retrieve existing vector stores
- **File Upload**: Upload and index documents with progress tracking
- **Search**: Query vector stores for relevant passages
- **RAG Integration**: Generate answers using retrieved context
- **Cleanup**: Delete vector stores and associated files

### Streamlit App Features

- **Multi-Store Support**: Switch between different knowledge bases
- **Real-time Chat**: Interactive conversation interface
- **Parameter Tuning**: Adjust model parameters on the fly
- **Chat History**: Maintain conversation context
- **Example Questions**: Quick access to sample queries

## 🔒 Security Notes

- Never commit your `.env` file with API keys
- The `.env` file is already in `.gitignore`
- Use environment variables for sensitive configuration
- Consider using OpenAI organization IDs for team management

## 🐛 Troubleshooting

### Common Issues

1. **API Key Not Found**
   - Ensure `.env` file exists and contains `OPENAI_API_KEY`
   - Check that the API key is valid and has necessary permissions

2. **Vector Store Not Found**
   - Upload a knowledge base first using the upload script
   - Check that your API key has Vector Store access

3. **File Upload Errors**
   - Ensure files are in supported formats (PDF, MD, TXT)
   - Check file sizes (very large files may timeout)
   - Verify file permissions

4. **Model Errors**
   - Ensure your OpenAI account has access to the selected model
   - Check API usage limits and billing

5. **Conda Environment Issues**
   - Ensure conda is properly installed and in your PATH
   - Try recreating the environment: `conda env remove -n rag-llm-env && conda env create -f environment.yml`

### Debug Mode

For debugging, you can run the upload script with verbose output:

```bash
python -u src/upload_knowledge_base.py --dir data/Knowledge_base --name "debug_kb"
```

## 📈 Performance Tips

- Use `gpt-4o-mini` for faster responses
- Adjust `search_k` based on your needs (lower = faster, higher = more comprehensive)
- Clear chat history periodically to free memory
- Use appropriate file extensions to avoid processing unnecessary files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for providing the Vector Store API
- Streamlit for the web framework
- The archaeological research community for the knowledge base content

## 📞 Support

For issues and questions:

1. Check the troubleshooting section above
2. Review the OpenAI API documentation
3. Open an issue in the repository

---

**Note**: This application requires OpenAI API access with Vector Store capabilities. Ensure your account has the necessary permissions and billing setup.