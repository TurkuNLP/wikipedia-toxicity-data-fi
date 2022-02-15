import json
import sys

lang=sys.argv[1]

for line in sys.stdin:
    comment=json.loads(line)
    for k in list(comment.keys()):
        if "text_" in k and k!="text_"+lang:
            del comment[k]
    assert "text_"+lang in comment
    comment["text"]=comment["text_"+lang]
    del comment["text_"+lang]
    print(json.dumps(comment,ensure_ascii=False,sort_keys=True))
        
