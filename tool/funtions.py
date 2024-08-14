from transformers import AutoTokenizer , AutoModelForSeq2SeqLM 

model = AutoModelForSeq2SeqLM.from_pretrained('')
tokenizer = AutoTokenizer.from_pretrained("")


def summarize(text):
    inputs = tokenizer(text, max_length=1024 , truncation = True , return_tensors = 'pt')
    
    summary_ids = model.generate(inputs['input_ids'] , max_length = 150 , min_length = 40 , early_stopping = True)
    
    summary = tokenizer.decode(summary_ids[0] , skip_special_tokens = True)
    
    return summary