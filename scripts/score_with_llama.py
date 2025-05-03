import fitz  # PyMuPDF
import os
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def parse_pdf(file_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def score_resume(resume_text: str, job_description: str):
    """Scores a resume based on job description using Langchain."""
    prompt = PromptTemplate.from_template("""
You are a resume screening expert. Given a job description and a resume, score the resume from 1 to 10 and give a one-line reason.

Job Description:
{job}

Resume:
{resume}

Respond in format: Score: <score>; Reason: <reason>
""")

    chain = prompt | Ollama(model="mistral") | StrOutputParser()
    result = chain.invoke({"resume": resume_text, "job": job_description})

    try:
        score_line = result.strip().split(";")
        score = int(score_line[0].split(":")[1].strip())
        reason = score_line[1].split(":")[1].strip()
        return score, reason
    except:
        return 0, "Could not parse LLM output"


def parse_and_score_resumes():
    input_dir = 'data/input'
    output_dir = 'data/output'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'resume_report.csv')

    job_description = """Data Engineer role requiring BigQuery, Airflow, Python, and cloud experience."""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("filename,text_preview,score,reason\n")

        for file_name in os.listdir(input_dir):
            if file_name.endswith('.pdf'):
                file_path = os.path.join(input_dir, file_name)
                try:
                    text = parse_pdf(file_path)
                    preview = text[:300].replace("\n", " ").replace(",", " ")
                    score, reason = score_resume(text, job_description)
                    reason = reason.replace(",", " ")
                    f.write(f"{file_name},{preview},{score},{reason}\n")
                    print(f"✅ Parsed and scored {file_name}: {score}")
                except Exception as e:
                    f.write(f"{file_name},ERROR,0,Error parsing: {str(e)}\n")
                    print(f"❌ Failed to process {file_name}: {e}")

if __name__ == "__main__":
    parse_and_score_resumes()
