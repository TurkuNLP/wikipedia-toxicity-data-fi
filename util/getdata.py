import json
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

with open(f'all.tsv', 'w') as out:
    for s in ('train', 'test'):
        print('\t'.join(["section","id"]+classes + ['text']), file=out)
        for x in d[s]:
            text = x['text'].numpy().decode('utf-8')
            id=x["id"].numpy().decode("utf-8")
            values = [str(int(x[k].numpy())) for k in classes]
            print('\t'.join([s,id]+ values + [json.dumps(text)]), file=out)
