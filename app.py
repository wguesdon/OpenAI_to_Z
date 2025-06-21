import streamlit as st
import os
from dotenv import load_dotenv
from src.vector_store_manager import VectorStoreManager
from datetime import datetime

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="RAG LLM - Amazon Archaeology Knowledge Base",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .user-message {
        background-color: #f0f2f6;
        border-left-color: #1f77b4;
    }
    .assistant-message {
        background-color: #e8f4fd;
        border-left-color: #28a745;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'vector_store_id' not in st.session_state:
        st.session_state.vector_store_id = None
    if 'vs_manager' not in st.session_state:
        st.session_state.vs_manager = None

def load_api_key():
    """Load OpenAI API key from environment"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("❌ OPENAI_API_KEY not found in environment variables")
        st.info("Please set OPENAI_API_KEY in your .env file")
        return None
    return api_key

def get_vector_stores(vs_manager):
    """Get list of available vector stores"""
    try:
        stores = vs_manager.list_all_vector_stores()
        return stores
    except Exception as e:
        st.error(f"Error fetching vector stores: {e}")
        return []

def main():
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">🏛️ RAG LLM - Amazon Archaeology Knowledge Base</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Query your knowledge base using Retrieval-Augmented Generation</p>', unsafe_allow_html=True)
    
    # Load API key
    api_key = load_api_key()
    if not api_key:
        st.stop()
    
    # Initialize vector store manager
    if st.session_state.vs_manager is None:
        st.session_state.vs_manager = VectorStoreManager(api_key, cli_mode=False)
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Vector store selection
        st.subheader("📚 Vector Store")
        stores = get_vector_stores(st.session_state.vs_manager)
        
        if not stores:
            st.warning("No vector stores found. Please upload a knowledge base first.")
            st.info("Use the upload script to create a vector store:")
            st.code("python src/upload_knowledge_base.py --dir data/Knowledge_base --name 'my_kb'")
        else:
            store_names = [store['name'] for store in stores]
            selected_store_name = st.selectbox(
                "Select Vector Store:",
                store_names,
                index=0 if not st.session_state.vector_store_id else None
            )
            
            # Get the selected store ID
            selected_store = next((store for store in stores if store['name'] == selected_store_name), None)
            if selected_store:
                st.session_state.vector_store_id = selected_store['id']
                st.success(f"✅ Connected to: {selected_store_name}")
                st.info(f"ID: {selected_store['id']}")
                if selected_store.get('file_counts'):
                    st.info(f"Files: {selected_store['file_counts']}")
        
        st.divider()
        
        # Model configuration
        st.subheader("🤖 Model Settings")
        chat_model = st.selectbox(
            "Chat Model:",
            ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
            index=0
        )
        
        temperature = st.slider(
            "Temperature:",
            min_value=0.0,
            max_value=1.0,
            value=0.2,
            step=0.1,
            help="Higher values make output more creative, lower values more focused"
        )
        
        search_k = st.slider(
            "Search Results (k):",
            min_value=1,
            max_value=10,
            value=5,
            step=1,
            help="Number of relevant passages to retrieve"
        )
        
        st.divider()
        
        # Chat history management
        st.subheader("💬 Chat History")
        if st.button("Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
        
        if st.session_state.chat_history:
            st.info(f"Messages: {len(st.session_state.chat_history)}")
        
        st.divider()
        
        # Information
        st.subheader("ℹ️ About")
        st.markdown("""
        This app uses OpenAI's Vector Store for RAG (Retrieval-Augmented Generation).
        
        **Features:**
        - Query your knowledge base
        - Adjust model parameters
        - View chat history
        - Multiple vector store support
        """)

    # Main content area
    if not st.session_state.vector_store_id:
        st.warning("⚠️ Please select a vector store from the sidebar to start querying.")
        
        # Show available stores in main area
        if stores:
            st.subheader("📋 Available Vector Stores")
            for store in stores:
                with st.expander(f"📚 {store['name']}"):
                    st.write(f"**ID:** {store['id']}")
                    st.write(f"**Created:** {store['created_at']}")
                    if store.get('file_counts'):
                        st.write(f"**Files:** {store['file_counts']}")
    else:
        # Chat interface
        st.subheader("💬 Ask a Question")
        
        # Question input
        question = st.text_area(
            "Enter your question:",
            placeholder="e.g., What are the locations of known archaeological sites in the Amazon Rainforest?",
            height=100
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            ask_button = st.button("🔍 Ask", type="primary", use_container_width=True)
        
        with col2:
            if st.button("🎲 Example Questions", use_container_width=True):
                examples = [
                    "What are the locations of known archaeological sites in the Amazon Rainforest?",
                    "What is the location of Kuhikugu (GPS coordinate)?",
                    "What techniques have been used to discover new archaeological sites in the Amazon rainforest in recent years?",
                    "What is the impact of the presence of Amazonian dark earth on vegetation?",
                    "What open-access LIDAR datasets cover portions of the Brazilian Amazon?"
                ]
                question = st.selectbox("Choose an example:", examples)
        
        # Process question
        if ask_button and question.strip():
            if not st.session_state.vector_store_id:
                st.error("Please select a vector store first.")
            else:
                # Add user message to chat history
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": question,
                    "timestamp": datetime.now()
                })
                
                # Show user message
                with st.chat_message("user"):
                    st.write(question)
                
                # Generate response
                with st.chat_message("assistant"):
                    with st.spinner("🔍 Searching knowledge base..."):
                        try:
                            response = st.session_state.vs_manager.answer_question(
                                vector_store_id=st.session_state.vector_store_id,
                                question=question,
                                chat_model=chat_model,
                                temperature=temperature,
                                search_k=search_k
                            )
                            
                            # Add assistant response to chat history
                            st.session_state.chat_history.append({
                                "role": "assistant",
                                "content": response,
                                "timestamp": datetime.now()
                            })
                            
                            st.write(response)
                            
                        except Exception as e:
                            error_msg = f"Error generating response: {e}"
                            st.error(error_msg)
                            st.session_state.chat_history.append({
                                "role": "assistant",
                                "content": error_msg,
                                "timestamp": datetime.now()
                            })
        
        # Display chat history
        if st.session_state.chat_history:
            st.subheader("📜 Chat History")
            
            for i, message in enumerate(st.session_state.chat_history):
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.write(message["content"])
                        st.caption(f"🕐 {message['timestamp'].strftime('%H:%M:%S')}")
                else:
                    with st.chat_message("assistant"):
                        st.write(message["content"])
                        st.caption(f"🕐 {message['timestamp'].strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main() 