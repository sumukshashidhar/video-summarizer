# video-summarizer
Extract Information from a Youtube video using subtitle files and the GPT3.5-Turbo API!

This is a Python script that processes WebVTT subtitle files, extracts the spoken text, and generates bullet points and a summary using OpenAI's GPT-3.5 turbo API.

## Features
- Extract spoken text from WebVTT subtitle files
- Generate bullet points and summary using OpenAI's GPT-3.5 turbo API
- Store the extracted spoken text and summary in separate files

## Prerequisites
Before using this script, please ensure that you have Python 3.6 or later installed. You will also need an OpenAI API key to access the GPT-3.5 turbo API. You can sign up for an API key [here](https://beta.openai.com/signup/).

To run this script, you will need to install the following Python packages:

- openai
- webvtt-py

You can install these packages using pip:

```bash
pip install openai webvtt-py
```

## Configuration
- Create a .env file in the project directory with the following content:
```makefile
OPENAI_API_KEY=your_api_key_here
```

- Ensure the input VTT file is available for processing.

## Usage
Update the input_vtt, output_text, and output_summary variables in the script with the appropriate file paths.

```python
Copy code
input_vtt = "input.vtt"
output_text = "processed_text.txt"
output_summary = "summary.txt"
```

Run the script:

```bash
python src/main.py
```
The script will process the VTT file, generate a summary, and store the extracted spoken text in the processed_text.txt file and the summary in the summary.txt file.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.