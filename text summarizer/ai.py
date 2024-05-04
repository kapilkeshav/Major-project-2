import transformers as hf

def ai_sum(text):
    summarizer = hf.pipeline("summarization")
    summarized = summarizer(text,min_length=150,max_length=350)
    return summarized[0]['summary_text']
