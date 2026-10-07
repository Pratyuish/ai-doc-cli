import os
import argparse
import sys
from openai import OpenAI

def generate_docstring(code: str) -> str:
    """Sends code to the OpenAI API to generate a professional docstring."""
    # The SDK automatically looks for the OPENAI_API_KEY environment variable
    client = OpenAI()
    
    prompt = f"Analyze the following Python code and return ONLY a professional Google-style docstring for it. Do not return any other text:\n\n{code}"
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Using the most cost-effective tier
            messages=[
                {"role": "system", "content": "You are an expert software engineer specialized in code documentation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="AI-powered Python Code Documentation CLI Tool.")
    parser.add_argument("file", help="Path to the Python file you want to document")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Analyzing {args.file}...")
    with open(args.file, "r") as f:
        file_content = f.read()
        
    docstring = generate_docstring(file_content)
    
    print("\n--- Generated Documentation ---")
    print(docstring)
    print("--------------------------------")

if __name__ == "__main__":
    main()
