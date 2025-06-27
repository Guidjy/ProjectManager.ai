from PyPDF2 import PdfReader
import re
import json


def extract_pdf_text(document):
    pdf_text=''
    
    if document:
        reader = PdfReader(document)
        for page in reader.pages:
            pdf_text += page.extract_text()
        return pdf_text
    else:
        return False
    

def extract_json_from_string(string):
    # searches for a JSON list in string form. Basically extracts this form the string: [ { ... } ]
    search_result = re.search(r'\[\s*{.*?}\s*]', string, re.DOTALL)
    
    if search_result:
        # gets the entire result that matched the regex pattern
        json_list = search_result.group(0)
        try:
            # converts the string result into a python dictionary
            data = json.loads(json_list)
            return data
        except json.JSONDecodeError as e:
            print('Failed to parse JSON: ', e)

    else:
        print("No JSON list found.")
    return []
    