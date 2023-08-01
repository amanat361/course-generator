import os
import re
import json
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

script_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_path, 'textbook.pdf')

layout = LAParams(
    char_margin=1.0,
    line_margin=0.5,
    word_margin=0.1,
    boxes_flow=0.5,
    detect_vertical=False,
    all_texts=False
)

text = extract_text(input_file, laparams=layout)

text = '\n'.join(line for line in text.split('\n') if len(line) >= 10)

with open(os.path.join(script_path, 'textbook.txt'), 'w') as outfile:
    outfile.write(text)

# pdf_file = open(input_file, 'rb')

# pdf_json = {"pages": []}

# for page in range(1,100):
#     print(f"Processing page {page}")
#     text = extract_text(pdf_file, page_numbers=[page])
#     text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
#     text = re.sub(r'[\s]+', ' ', text)
#     pdf_json["pages"].append(text)
#     print(f"Page {page} processed\n")

# pdf_file.close()

# save json to file
# with open(os.path.join(output_dir, 'textbook.json'), 'w') as outfile:
#     json.dump(pdf_json, outfile, indent=4)