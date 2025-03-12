import spacy

nlp = spacy.load("ko_core_news_md")

def chunk_text_by_sentence(text, max_chunk_size=512):
    doc = nlp(text)
    chunks = []
    current_chunk = ""

    for sent in doc.sents:
        if len(current_chunk) + len(sent.text) <= max_chunk_size:
            current_chunk += " " + sent.text
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sent.text

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks