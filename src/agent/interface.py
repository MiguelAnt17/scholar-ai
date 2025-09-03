from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add src directory to Python path
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.append(src_path)

# Import from the agent directory
from executor import ResearchAgentExecutor

app = Flask(__name__)
CORS(app)

# Initialize the research agent
research_agent = None

def initialize_agent():
    global research_agent
    try:
        research_agent = ResearchAgentExecutor()
        print("✅ Research agent initialized successfully!")
        return True
    except Exception as e:
        print(f"❌ Failed to initialize research agent: {e}")
        print("Make sure Ollama is running and llama3 model is installed.")
        return False

@app.route('/')
def index():
    """Serve the HTML interface"""
    # Same HTML content as above...
    return "HTML content here..."  # Use the same HTML from the previous artifact

# Same routes as above...

if __name__ == '__main__':
    print("🚀 Starting Scholar AI Web Interface...")
    print("📡 Initializing research agent...")
    
    agent_ready = initialize_agent()
    
    if agent_ready:
        print("✅ Agent initialized successfully!")
    else:
        print("⚠️  Agent initialization failed, but server will start anyway.")
    
    print("🌐 Server starting at: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)