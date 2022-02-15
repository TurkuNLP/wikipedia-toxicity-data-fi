import sys
import json

comments={}
with open("translated.jsonl") as f:
    for line in f:
        try:
            comment=json.loads(line.strip())
        except:
            print("Weird line",line)
            continue
        assert comment["id"] not in comments
        comments[comment["id"]]=comment

import tensorflow_datasets

classes = [
    'toxicity',
    'severe_toxicity',
    'identity_attack',
    'insult',
    'obscene',
    'threat',
]

d = tensorflow_datasets.load('wikipedia_toxicity_subtypes')
print(list(d.keys()))


with open(f'train_fi_deepl.jsonl', 'w') as out_train,\
     open(f'test_fi_deepl.jsonl', 'w') as out_test:
    for s,out in (('train',out_train), ('test',out_test)):
        for x in d[s]:
            text = x['text'].numpy().decode('utf-8')
            id=x["id"].numpy().decode("utf-8")
            values = [int(x[k].numpy()) for k in classes]
            
            newdict={"id":id, "text":comments[id]["text_fi"], "lang":"fi-deepl"}
            for v,lab in zip(values,classes):
                newdict["label_"+lab]=v
            print(json.dumps(newdict,ensure_ascii=False,sort_keys=True),file=out)
