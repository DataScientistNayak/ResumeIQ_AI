"""
Application Cache Utilities
"""

from __future__ import annotations

import google.generativeai as genai
import spacy
import streamlit as st
from sentence_transformers import SentenceTransformer

from config import GEMINI_API_KEY


SPACY_MODEL = "en_core_web_sm"
SENTENCE_MODEL = "all-MiniLM-L6-v2"
GEMINI_MODEL = "gemini-2.5-flash"


@st.cache_resource(show_spinner=False)
def load_spacy_model():
    """
    Load the spaCy model once.
    """

    return spacy.load(SPACY_MODEL)


@st.cache_resource(show_spinner=False)
def load_sentence_transformer():
    """
    Load the SentenceTransformer model once.
    """

    return SentenceTransformer(SENTENCE_MODEL)


@st.cache_resource(show_spinner=False)
def load_gemini_model():
    """
    Load the Gemini model once.
    """

    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY not found. Please add it to your .env file."
        )

    genai.configure(
        api_key=GEMINI_API_KEY,
    )

    return genai.GenerativeModel(
        GEMINI_MODEL
    )