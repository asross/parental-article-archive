import json
import glob
import re
from markdown import markdown

for p in ['michael', 'barbara']:
    with open(f"_data/{p}.json", "r") as f:
        data = json.load(f)
    for f in glob.glob(f"../llm_aided_ocr/cleaned_articles/{p}/*.json"):
        cleaned = json.load(open(f))
        for d in data:
            if d['id'] == cleaned['id']:
                print(f)
                #cleaned['text2'] = re.sub(r'^#+\s*', '', cleaned['text2'], flags=re.M)
                d['text_cleaned'] = markdown(cleaned['text2'])
                break
    with open(f"_data/{p}.json", "w") as f:
        json.dump(data, f, indent=4)
