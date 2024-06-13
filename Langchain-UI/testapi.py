import requests
import streamlit as st

# Streamlit setup
st.title("Presentation Generator Test Interface")

# Input
topic = st.text_input("Enter a topic for your presentation:")

if topic:
    # Send requests to FastAPI app
    title_response = requests.post("http://localhost:8000/generate-title", json={"prompt": topic})
    wiki_response = requests.post("http://localhost:8000/wikipedia-research", json={"prompt": topic})
    script_response = requests.post("http://localhost:8000/generate-script", json={"title": title_response.json()["title"], "wikipedia_research": wiki_response.json()["wikipedia_research"]})
    menu_response = requests.post("http://localhost:8000/generate-menu", json={"title": title_response.json()["title"]})

    # Display results
    st.subheader("Presentation Title")
    st.write(title_response.json()["title"])
    st.subheader("Title Generation History")
    st.write(title_response.json()["title_history"])
    st.subheader("Wikipedia Research")
    st.write(wiki_response.json()["wikipedia_research"])
    st.subheader("Presentation Script")
    st.write(script_response.json()["script"])
    st.subheader("Script Generation History")
    st.write(script_response.json()["script_history"])
    st.subheader("Presentation Menu")
    st.write(menu_response.json()["menu"])