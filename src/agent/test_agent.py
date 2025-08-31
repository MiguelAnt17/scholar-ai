from executor import ResearchAgentExecutor

def main():
    print("🔬 Starting Research Agent...")
    
    try:
        # Initialize the agent
        agent = ResearchAgentExecutor()
        print("✅ Agent initialized successfully!")
        
        # Test queries
        queries = [
            "quantum computing applications",
            "deep learning for natural language processing",
            "climate change and machine learning"
        ]
        
        for query in queries:
            print(f"\n🔍 Searching for: '{query}'")
            print("-" * 50)
            
            result = agent.run(query)
            print(f"📄 Results:\n{result}")
            print("=" * 50)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure Ollama is running and llama3 model is installed.")

if __name__ == "__main__":
    main()