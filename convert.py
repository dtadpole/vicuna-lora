#!/usr/bin/env python

import json

f = open("sharegpt_20230401_clean_lang_split.json")

obj = json.load(f)
print("loaded %s conversations" % len(obj))

output = []

for conv in obj:

  human=False
  inst={"instruction":"", "input":"", "output":""}

  for i in conv["conversations"]:

    if i["from"] == "human" and human == False:

      inst["instruction"] = i["value"]
      human=True

    elif i["from"] == "gpt" and human == True:

      inst["output"] = i["value"]
      human=False

      output.append(inst)
      inst={"instruction":"", "input":"", "output":""}

    else:

      pass

print("processed %s instructions" % len(output))


OUTPUT_FILENAME = "output.json"

json_object = json.dumps(output, indent=4)
with open(OUTPUT_FILENAME, "w") as outfile:
    outfile.write(json_object)

print("written to file %s" % OUTPUT_FILENAME)
