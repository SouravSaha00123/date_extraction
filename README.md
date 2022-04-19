# Extract Date from Text

## Prerequisites
 [Python 3](https://www.python.org/downloads/),[NLTK](https://pypi.org/project/nltk/),[Regex](https://pypi.org/project/regex/),
 [Pytesseract](https://pypi.org/project/pytesseract/)
 
## How to run the model?
 The model is implemented in date_class.py. Download the date_pattern text file. Run the following lines to extract dates from text.
 `````````
sentences=sent_tokenize(text)
for sentence in sentences:
    formt = date_class(sentence,path = './date_pattern.txt')
    result = formt.date_extract()
    words=word_tokenize(sentence)
    for word in words:
        if result == 'yes':
            print('The date format ('+word+') is correct and is extracted by:\n'+formt)
            print(result)
 `````````
 Here, 'text' is the text used for date extraction.

## Contact
For any further query, comment or suggestion, you may reach out to me at ssaharaj@gmail.com
