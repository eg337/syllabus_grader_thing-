from pypdf import PdfReader
from google import genai

API_KEY = ""

#name = 'CMSC470-Syllabus.pdf'
name = "syllabus_416_25.pdf"
texts = ""
reader = PdfReader(name)
for page in reader.pages:
    texts += page.extract_text()


with open("plaintext.txt", "w") as f:
    for text in texts:
        f.write(text)

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="In the message text after, I will upload a syllabus to a college course. After I do so, please output the grade weights as percentages followed by a percent sign contained inside in a json format: " + texts 
)


print(response.text)