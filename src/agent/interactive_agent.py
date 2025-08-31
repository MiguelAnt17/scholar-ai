from executor import ResearchAgentExecutor

def main():
    print("🔬 Research Agent - Interactive Mode")
    print("Type 'quit' to exit\n")
    
    try:
        # Initialize the agent
        print("Initializing agent...")
        agent = ResearchAgentExecutor()
        print("✅ Agent ready!\n")
        
        while True:
            # Get user input
            query = input("🔍 Enter your research query: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not query:
                print("Please enter a valid query.")
                continue
            
            print(f"\n🔬 Searching for papers about: '{query}'")
            print("-" * 60)
            
            try:
                result = agent.run(query)
                print(f"📄 Results:\n{result}")
            except Exception as e:
                print(f"❌ Error processing query: {e}")
            
            print("\n" + "=" * 60 + "\n")
            
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        print("Make sure Ollama is running and the llama3 model is installed.")

if __name__ == "__main__":
    main()