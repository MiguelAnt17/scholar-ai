from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import sys
import os

# Add your src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from executor import ResearchAgentExecutor

app = Flask(__name__)
CORS(app)

# Initialize the research agent
try:
    research_agent = ResearchAgentExecutor()
    print("✅ Research agent initialized successfully!")
except Exception as e:
    print(f"❌ Failed to initialize research agent: {e}")
    research_agent = None

@app.route('/')
def index():
    # Serve your HTML interface
    with open('interface.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/search', methods=['POST'])
def search_papers():
    try:
        data = request.get_json()
        query = data.get('query', '')
        format_output = data.get('format', 'text')
        
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        
        if not research_agent:
            return jsonify({'error': 'Research agent not initialized'}), 500
        
        # Run the research agent
        result = research_agent.run(f"Search for papers about: {query}")
        
        # Parse the result to extract individual papers
        # This depends on your agent's output format
        papers = parse_agent_result(result)
        
        return jsonify({
            'query': query,
            'results': papers,
            'raw_result': result
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def parse_agent_result(result):
    """
    Parse the agent's text result into structured paper data
    Adjust this based on your agent's actual output format
    """
    papers = []
    
    # Split by separator (adjust based on your tools.py output format)
    sections = result.split('---')
    
    for section in sections:
        if 'Title:' in section:
            paper = {}
            lines = section.strip().split('\n')
            
            for line in lines:
                if line.startswith('Title:'):
                    paper['title'] = line.replace('Title:', '').strip()
                elif line.startswith('Authors:'):
                    authors_str = line.replace('Authors:', '').strip()
                    paper['authors'] = [author.strip() for author in authors_str.split(',')]
                elif line.startswith('Summary:'):
                    paper['summary'] = line.replace('Summary:', '').strip()
                elif line.startswith('URL of the PDF:'):
                    paper['pdf_url'] = line.replace('URL of the PDF:', '').strip()
                elif line.startswith('Keywords:'):
                    keywords_str = line.replace('Keywords:', '').strip()
                    paper['keywords'] = [kw.strip() for kw in keywords_str.split(',')]
            
            if 'title' in paper:
                papers.append(paper)
    
    return papers

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'agent_ready': research_agent is not None
    })

if __name__ == '__main__':
    print("🚀 Starting Scholar AI Web Interface...")
    print("📡 Server will be available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)