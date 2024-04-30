import docx2txt

def load_file(file_path):
    content = docx2txt.process(file_path)
    return content

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def parse_text(content):
    # print(content)
    processed_data=[]
    temp=''
    for line in content.split("\n"):
        # print(line)
        if isfloat(line.replace(" ","")):
            story=True
            if temp!='':
                processed_data.append({'story':story_content ,'acceptance_content':temp })
            temp=''
        elif line[:5]=="Given":
            if story:
                story_content=temp
                story=False
                temp=line
            else:
                acceptance_content=temp
                processed_data.append({'story':story_content ,'acceptance_content':acceptance_content })
                temp=line
        else:
            temp+=line
    processed_data.append({'story':story_content ,'acceptance_content':temp })
    return processed_data

def main():
    content=load_file('Firm Workflow user stories.docx')
    processed_data=parse_text(content)
    print(len(processed_data))
    with open('user_story_combinations.txt', 'w') as f:
        for line in processed_data:
            f.write(f"{line}\n")
    f.close()
    for item in processed_data:
        print(item['story'])
        print(item['acceptance_content'])
        print("--------------------------------------------------")

if __name__ == "__main__":
    main()
