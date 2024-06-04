import os
import streamlit as st
from langchain_core.prompts.prompt import PromptTemplate
from langchain.memory.buffer import ConversationBufferMemory
from langchain.openai.openai import OpenAI
from langchain.llm.llmchain import LLMChain
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-api-key"

# Streamlit setup
st.title("Presentation Generator")
prompt = st.text_input("Enter a topic for your presentation:")

# Prompt templates
title_template = PromptTemplate("I need a title for a presentation about {topic}.")
slide_template = PromptTemplate("Generate a slide about {title} based on {wikipedia_research}.")

# Conversation buffers
title_buffer = ConversationBufferMemory()
slide_buffer = ConversationBufferMemory()

# OpenAI setup
openai = OpenAI(temperature=0.9)

# LLMChain setup
title_llm = LLMChain(openai, title_template, title_buffer)
slide_llm = LLMChain(openai, slide_template, slide_buffer)

# Wikipedia setup
wiki = WikipediaAPIWrapper()

if prompt:
    # Generate title
    title = title_llm.generate({"topic": prompt})

    # Fetch Wikipedia data
    wikipedia_research = wiki.fetch(prompt)

    # Generate slides
    slides = []
    for i in range(5):  # Generate 5 slides
        slide = slide_llm.generate({"title": title, "wikipedia_research": wikipedia_research})
        slides.append(slide)

    # Display results
    st.subheader("Presentation Title")
    st.write(title)
    st.subheader("Slides")
    for i, slide in enumerate(slides, start=1):
        st.write(f"Slide {i}")
        st.write(slide)