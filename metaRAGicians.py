import os
import json
from dotenv import load_dotenv

# Add OpenAI import
from openai import AzureOpenAI

import streamlit as st
st.title("MetaRAGicians")

def main():

    try:
        # Flag to show citations
        show_citations = False

        # Get configuration settings
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        azure_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        azure_search_key = os.getenv("AZURE_SEARCH_KEY")
        azure_search_index = os.getenv("AZURE_SEARCH_INDEX")

        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
            base_url=f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}/extensions",
            api_key=azure_oai_key,
            api_version="2023-09-01-preview")

        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-3.5-turbo"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

        # Get the prompt
        # text = input('\nEnter a question:\n')

        # Configure your data source
        extension_config = dict(dataSources = [
                {
                    "type": "AzureCognitiveSearch",
                    "parameters": {
                        "endpoint":azure_search_endpoint,
                        "key": azure_search_key,
                        "indexName": azure_search_index,
                    }
                }]
            )

        with st.chat_message("assistant"):
            with st.spinner('Retrieving...'):
                response = client.chat.completions.create(
                    model = azure_oai_deployment,
                    temperature = 0.5,
                    max_tokens = 1000,
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    extra_body = extension_config
                )
                response = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.write(response)


        if (show_citations):
            # Print citations
            print("Citations:")
            citations = response.choices[0].message.context["messages"][0]["content"]
            citation_json = json.loads(citations)
            for c in citation_json["citations"]:
                print("  Title: " + c['title'] + "\n    URL: " + c['url'])



    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()


