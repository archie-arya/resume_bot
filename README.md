# 🧠 Resume Screening Bot with LangChain + Ollama

This project automates resume screening by parsing PDF resumes and scoring them against a given job description using an LLM (LLaMA 3.2 via Ollama). It uses:

- PyMuPDF for extracting text from resumes (PDFs)
- LangChain to prompt LLMs
- Ollama to run open-source LLMs locally (LLaMA 3.2, DeepSeek, etc.)

---

## Project Structure

```
resume_bot/
├── data/
│   ├── input/             # Put your resumes (PDFs) here
│   └── output/            # Output CSV will be saved here
├── scripts/
│   ├── parse_pdf.py       # PDF parsing logic using PyMuPDF
│   └── score_with_llama.py  # Main script: score resumes using LLM
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Prerequisites

- Python 3.9
- [Ollama](https://ollama.com/download) installed and running locally
- Git (optional, for cloning)

---

###  1. Clone the Repo

```bash
git clone https://github.com/archie-arya/resume_bot.git
cd resume_bot
```

---

### 2. Set Up Virtual Environment

```bash
python3.9 -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you encounter issues with `PyMuPDF`, install it directly:

```bash
pip install PyMuPDF
```

---

### 4. Pull LLaMA 3.2 with Ollama

```bash
ollama pull llama3
```

> You can also use other models like `deepseek-coder`, `mistral`, etc. Just change the model name in `score_with_llama.py`.

---

## Usage

### 1. Add Resumes

Put your resume files (PDFs) in:

```
data/input/
```

---

### 2. Run the Script

```bash
python scripts/score_with_llama.py
```

This will:

- Parse all PDFs in `data/input/`
- Score them using the LLM
- Save results in `data/output/resume_report.csv`

---

## Output Format

The CSV will contain:

```
filename,text_preview,score,reason
resume1.pdf,Preview of resume text...,8,Good match for BigQuery and Python
resume2.pdf,Preview of another resume...,5,Lacks Airflow experience
```

---

## Customization

- To change the **job description**, edit this string inside `score_with_llama.py`:

```python
job_description = """Data Engineer role requiring BigQuery, Airflow, Python, and cloud experience."""
```

- To switch models, change:

```python
Ollama(model="llama3.2")
```

to e.g.,

```python
Ollama(model="mistral")
```

---

## Testing

Try running the script on sample resumes and tweak your prompt template or job description to refine scoring accuracy.

---

## FAQ

### 1. I get `Could not parse LLM output` errors.
> Ensure your model is pulled (`ollama pull llama3`) and the prompt format matches expected output (`Score: <score>; Reason: <reason>`).

### 2. I want to run this in Docker or Airflow.
> This repo is built for local execution. For Docker or Airflow integration, reach out or open an issue.

---

### Contributions

PRs and feedback welcome! Please open an issue for bugs or feature requests.

---

## License

MIT License.
