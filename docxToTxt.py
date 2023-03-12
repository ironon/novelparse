import docx
import os
import re
global allText
episode = r"(Episode|Episodes|episode|episodes) ([^[\s\D]+)"
output = "./output"
imgtag = "<img src=INSERTIMG></img>"
global template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()
if not os.path.exists("./alltext.txt"):
    path = "./input"
    allText = ""
    

    for file in os.scandir(path):
        doc = docx.Document(file.path)
        for docpara in doc.paragraphs:
            allText = allText + "\n" + docpara.text
            print(docpara.text.encode('utf-8'))
        
    # print(allText.encode("utf-8"))
    with open("alltext.txt", "w", encoding="utf-8") as f:
        f.write(allText)
else:
    with open("./alltext.txt", "r", encoding="utf-8") as f:
        allText = f.read()

# print(allText.encode("utf-8"))
indexes = re.finditer(episode, allText)

pastIndex = 0
for i, entry in enumerate(indexes):
    currentIndex = entry.span()[0]
    # if index == len(indexes) - 1:
    text = allText[pastIndex:currentIndex]
    pastIndex = currentIndex
    chapter = int(entry.group(2))-1
    with open(os.path.join(output, "txt", f"{chapter}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(output, "html", f"{chapter}.html"), "w", encoding="utf-8") as f:
        addedtext = ""
        if os.path.exists(f"./imgs/{chapter}.jpg"):
            addedtext = imgtag.replace("INSERTIMG", f"./images/{chapter}.jpg")
            print(addedtext)

        f.write(template.replace("INSERT STUFF HERE", text+addedtext))






