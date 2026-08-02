import re

STOPWORDS = {
    "the","a","an","and","or","of","to","for","with",
    "in","on","at","is","are","be","from","by","as"
}

def extract_keywords(text):

    words = re.findall(r"[A-Za-z+#\.]{2,}", text.lower())

    words = [w for w in words if w not in STOPWORDS]

    return sorted(list(set(words)))