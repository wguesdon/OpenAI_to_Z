@echo off
REM Setup script for RAG LLM - Amazon Archaeology Knowledge Base (Windows)

echo 🏛️ Setting up RAG LLM - Amazon Archaeology Knowledge Base
echo ==================================================

REM Check if .env file exists
if not exist .env (
    echo 📋 Creating .env file from template...
    copy env.example .env
    echo ⚠️  Please edit .env file and add your OpenAI API key
) else (
    echo ✅ .env file already exists
)

REM Check if conda environment exists
set ENV_NAME=rag-llm-env
conda env list | findstr /C:"%ENV_NAME%" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Conda environment '%ENV_NAME%' already exists
) else (
    echo 🐍 Creating conda environment '%ENV_NAME%' with Python 3.11...
    conda create -n %ENV_NAME% python=3.11 -y
    echo ✅ Conda environment created
)

echo.
echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file and add your OpenAI API key
echo 2. Activate conda environment: conda activate %ENV_NAME%
echo 3. Install dependencies: pip install -r requirements.txt
echo 4. Upload knowledge base: python src/upload_knowledge_base.py --dir data/Knowledge_base --name "my_kb"
echo 5. Run the app: streamlit run app.py
echo.
echo To deactivate the environment later: conda deactivate
echo.
pause 