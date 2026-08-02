from utils.keyword_extractor import extract_keywords


def compare_keywords(
    resume_text,
    jd_text
):

    resume = set(
        extract_keywords(resume_text)
    )

    jd = set(
        extract_keywords(jd_text)
    )

    matched = sorted(
        list(
            resume.intersection(jd)
        )
    )

    missing = sorted(
        list(
            jd - resume
        )
    )

    return matched, missing