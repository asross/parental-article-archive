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
                cleaned = re.sub(r'^#+\s*', '', cleaned['text2'], flags=re.M)
                d['text_cleaned'] = markdown(cleaned)
                break
    with open(f"_data/{p}.json", "w") as f:
        json.dump(data, f, indent=4)
