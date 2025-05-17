# Prompt Generator

A Streamlit application for generating prompts and scripts.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/prompt_gen.git
cd prompt_gen
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your API keys:
```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

5. Run the Streamlit app:
```bash
streamlit run script/web1.py
```

## Environment Variables

The following environment variables are required:

- `GROQ_API_KEY`: Your Groq API key
- `OPENAI_API_KEY`: Your OpenAI API key

## Project Structure

- `script/web1.py`: Main Streamlit application
- `script/script.py`: Script generation logic
- `script/goals.py`: Goals processing
- `script/product_info.py`: Product information handling

## Security Note

Never commit your `.env` file or expose your API keys. The `.env` file is already included in `.gitignore`. 