from pypdf import PdfReader
from google import genai
from docx import Document
from bs4 import BeautifulSoup
API_KEY = ""

# name = 'CMSC470-Syllabus.pdf'
# name = "syllabus_416_25.pdf"
name = "3220 SP25 Syllabus_UpdatedJan23.docx"
# name = "Advanced Data Structures and Algorithms.html"
texts = ""

extension = name.split(".")[1]

if extension == "pdf":
    reader = PdfReader(name)
    for page in reader.pages:
        texts += page.extract_text()


elif extension == "docx":
    document = Document(name)
    for paragraph in document.paragraphs:
        texts += paragraph.text

elif extension == "html":
    with open(name, "r") as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, "html.parser")
    texts = soup.get_text()


client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="In the message text after, I will upload a syllabus to a college course. After I do so, please output the grade weights as percentages"
    + " followed by a percent sign contained inside in a json format also include drops as a separate directory with only the number in the value: " + texts 
)


print(response.text)