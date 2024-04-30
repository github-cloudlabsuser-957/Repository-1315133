import streamlit as st
import openai
from constant import PROMPT_TEST_CASES, PROMPT_BDD_SCENARIOS , PROMPT_TEST_SCRIPTS
from datetime import datetime
import os
import time
import pandas as pd
import docx2txt
from Text_parser import parse_text


## Set OpenAI API key for Azure
openai.api_type = "azure"
openai.api_base = "https://aimlgpt24.openai.azure.com/"
openai.api_version = "2024-02-15-preview"
openai.api_key = "3253c457a54345ea9251d23a67e16b58"



st.set_page_config(
    page_title="Engineering documentation,including manuals, reports,and technical specifications",
    page_icon="🔍",
    layout="wide"
)

custom_style = """
    body {
        background-color: #5B9AD5;
    }
    .stApp {
        max-width: 2000px;
        margin: 0 auto;
    }
"""

#st.markdown(f'<style>{custom_style}</style>', unsafe_allow_html=True)

def load_documents(BRD_text):
    return [{"text": BRD_text}]

def load_file(uploaded_file):
    content = uploaded_file.read()
    # print(content.decode("utf-8").splitlines())
    #cleaned_content = ' '.join(line.strip() for line in content.decode("utf-8").splitlines())
    return content.decode("utf-8")

def generate_testcase_scenario(BRD_text, Bdd_scenario_checkbox):

    final_tc = []
    final_tc_only=[]
    user_instruction = PROMPT_TEST_CASES

    processed_data=parse_text(BRD_text)
    # print(processed_data)
    # Using for loop
    for line in processed_data:
        user_input=line['story'] + line['acceptance_content']
        # print(user_input)
        complete_prompt = user_instruction + user_input

        if Bdd_scenario_checkbox:
            complete_prompt = PROMPT_BDD_SCENARIOS + line

        message_text = [
            {"role": "system", "content": "You are an AI assistant that helps people find information."},
            {"role": "user", "content": complete_prompt}
        ]

        #print(complete_prompt)


def display_text_with_style(header, text, background_color):
    st.subheader(header)
    styled_text = f"<div style='background-color:{background_color}; padding:20px; width:100%'>{text}</div>"
    st.markdown(styled_text, unsafe_allow_html=True)


def save_to_file(data, summary_type, output_folder="output"):
    current_directory = os.getcwd()
    req_path="\\".join(current_directory.split("\\")[:-1])
    output_path = os.path.join(req_path, output_folder)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{output_path}/customer_complaint_{summary_type.lower()}_{timestamp}.html"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(data.replace("\n\n","<br>"))

    st.success(f"File downloaded successfully! Check the '{output_folder}' folder.")  # Display success message
    return filename

def main():
    st.title("Upload Engineering Documentation")

    session_state = st.session_state
    if not hasattr(session_state, "testcases_generated"):
        session_state.testcases_generated = False
    if not hasattr(session_state, "bdd_scenarios_generated"):
        session_state.bdd_scenarios_generated = ""
    if not hasattr(session_state, "current_summary_type"):
        session_state.current_summary_type = ""

    BRD_text = ""
    bdd_scenarios_testcases = ""
    uploaded_file = st.file_uploader("**Upload a text file**", type=["txt"])

    if uploaded_file is not None:
        file_content = load_file(uploaded_file)
        BRD_text = st.text_area("**Please provide Business Requirement Document:**", value=file_content, height=300)
    else:
        BRD_text = st.text_area("**Please provide Business Requirement Document:**", height=300, value=BRD_text)


                #st.balloons()
        custom_text_area_style = """  
                    border-radius: 1px;
                    margin-top: 10px;
                    margin-bottom: 10px;
                    margin-right: 15px;
                    margin-left: 8px;
                    background-color: #F0FFFF;
                    padding-top: 10px;
                    padding-right: 10px;
                    padding-bottom: 10px;
                    padding-left: 10px;
                """


                #print("pre",bdd_scenarios_testcases)
        bdd_scenarios_testcases = " ".join(str(x+ "\n\n--------------------------------------------\n\n") for x in bdd_scenarios_testcases)

                #print("post",len(bdd_scenarios_testcases))

        session_state.bdd_scenarios_testcases = bdd_scenarios_testcases
        session_state.testcases_generated=True
        display_text_with_style("Context-aware search results:", bdd_scenarios_testcases, "#FFFFE0")

    #col3, col4 = st.columns(2, gap="small")

    if session_state.testcases_generated:
       # with col3:
        if st.button("Download Results", help="Click to download the generated results"):
            save_to_file(session_state.bdd_scenarios_testcases, session_state.current_summary_type)

if __name__ == "__main__":
    main()
