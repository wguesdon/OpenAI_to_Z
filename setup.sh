#!/bin/bash

# Setup script for RAG LLM - Amazon Archaeology Knowledge Base

echo "🏛️ Setting up RAG LLM - Amazon Archaeology Knowledge Base"
echo "=================================================="

# Make Python scripts executable
echo "📝 Making scripts executable..."
chmod +x src/upload_knowledge_base.py
chmod +x src/cleanup_vector_stores.py

# Check if .env file exists
if [ ! -f .env ]; then
    echo "📋 Creating .env file from template..."
    cp env.example .env
    echo "⚠️  Please edit .env file and add your OpenAI API key"
else
    echo "✅ .env file already exists"
fi

# Check if conda environment exists
ENV_NAME="rag-llm-env"
if conda env list | grep -q "^$ENV_NAME "; then
    echo "✅ Conda environment '$ENV_NAME' already exists"
else
    echo "🐍 Creating conda environment '$ENV_NAME' with Python 3.11..."
    conda create -n $ENV_NAME python=3.11 -y
    echo "✅ Conda environment created"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your OpenAI API key"
echo "2. Activate conda environment: conda activate $ENV_NAME"
echo "3. Install dependencies: pip install -r requirements.txt"
echo "4. Upload knowledge base: python src/upload_knowledge_base.py --dir data/Knowledge_base --name 'my_kb'"
echo "5. Run the app: streamlit run app.py"
echo ""
echo "To deactivate the environment later: conda deactivate"
echo "" 