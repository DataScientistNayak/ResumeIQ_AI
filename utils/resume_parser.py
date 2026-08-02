import re

EMAIL_REGEX = r'[\w\.-]+@[\w\.-]+\.\w+'
PHONE_REGEX = r'(\+?\d[\d\s\-\(\)]{8,}\d)'
LINKEDIN_REGEX = r'https?://(www\.)?linkedin\.com/in/[^\s]+'
GITHUB_REGEX = r'https?://(www\.)?github\.com/[^\s]+'


SKILLS = [
    "python","java","c","c++","sql","mysql","postgresql","mongodb",
    "pandas","numpy","tensorflow","keras","pytorch","scikit-learn",
    "machine learning","deep learning","data analysis","power bi",
    "excel","tableau","git","github","docker","aws","azure","gcp",
    "flask","fastapi","streamlit","react","html","css","javascript",
    "langchain","langgraph","openai","gemini","nlp","opencv"
]


SECTIONS = [
    "education",
    "experience",
    "projects",
    "skills",
    "certifications",
    "achievements",
    "internship",
    "summary",
    "objective"
]


def extract_email(text):
    match = re.search(EMAIL_REGEX, text, re.I)
    return match.group() if match else "Not Found"


def extract_phone(text):
    match = re.search(PHONE_REGEX, text)
    return match.group().strip() if match else "Not Found"


def extract_linkedin(text):
    match = re.search(LINKEDIN_REGEX, text, re.I)
    return match.group() if match else "Not Found"


def extract_github(text):
    match = re.search(GITHUB_REGEX, text, re.I)
    return match.group() if match else "Not Found"


def extract_name(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return lines[0] if lines else "Unknown"


def extract_skills(text):

    text_lower = text.lower()

    found = []

    for skill in SKILLS:

        if skill in text_lower:
            found.append(skill.title())

    return sorted(list(set(found)))


def detect_sections(text):

    text_lower = text.lower()

    found = []

    for section in SECTIONS:

        if section in text_lower:
            found.append(section.title())

    return found


def parse_resume(text):

    return {

        "Name": extract_name(text),

        "Email": extract_email(text),

        "Phone": extract_phone(text),

        "LinkedIn": extract_linkedin(text),

        "GitHub": extract_github(text),

        "Skills": extract_skills(text),

        "Sections": detect_sections(text)
    }