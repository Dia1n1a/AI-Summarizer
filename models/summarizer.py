from transformers import pipeline

_summarizer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=-1
        )
    return _summarizer


def summarize_text(text: str, max_length=80, min_length=20) -> str:
    text = text.strip()

    if len(text) < 40:
        summarizer = get_summarizer()
        result = summarizer(
            text,
            max_length=min(max_length, len(text)),
            min_length=10,
            do_sample=False
        )
        return result[0]["summary_text"]

    summarizer = get_summarizer()

    max_chunk_size = 400
    chunks = [
        text[i:i + max_chunk_size]
        for i in range(0, len(text), max_chunk_size)
    ]

    summaries = []

    for chunk in chunks:
        chunk = chunk.strip()
        if len(chunk) < 40:
            continue

        try:
            result = summarizer(
                chunk,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )
            summaries.append(result[0]["summary_text"])
        except Exception:
            continue

    if not summaries:
        return text[:max_length]

    return " ".join(summaries)
