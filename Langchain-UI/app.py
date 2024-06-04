import os
from apikey import apikey

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#from langchain.llms import OpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

# FastAPI app initialization
app = FastAPI()

# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a presentation video title about {topic}'
)

script_template = PromptTemplate(
    input_variables=['title', 'wikipedia_research'],
    template='write me a presentation script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research}'
)
# Menu template
menu_template = PromptTemplate(
    input_variables=['title'],
    template='create a menu for the presentation titled "{title}"'
)

# Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)
menu_chain = LLMChain(llm=llm, prompt=menu_template, verbose=True, output_key='menu')

wiki = WikipediaAPIWrapper()

# Request models
class PromptRequest(BaseModel):
    prompt: str

class ScriptRequest(BaseModel):
    title: str
    wikipedia_research: str

class MenuRequest(BaseModel):
    title: str


# Endpoints
@app.post("/generate-menu")
async def generate_menu(request: MenuRequest):
    try:
        # Generate menu logic here
        menu = menu_chain.run(request.title)
        return {"menu": menu}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/generate-title")
async def generate_title(request: PromptRequest):
    try:
        title = title_chain.run(request.prompt)
        return {"title": title, "title_history": title_memory.buffer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-script")
async def generate_script(request: ScriptRequest):
    try:
        script = script_chain.run(title=request.title, wikipedia_research=request.wikipedia_research)
        return {"script": script, "script_history": script_memory.buffer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/wikipedia-research")
async def wikipedia_research(request: PromptRequest):
    try:
        wiki_research = wiki.run(request.prompt)
        return {"wikipedia_research": wiki_research}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Example endpoint to process the whole flow
@app.post("/generate-presentation-content")
async def generate_presentation_content(request: PromptRequest):
    try:
        title = title_chain.run(request.prompt)
        wiki_research = wiki.run(request.prompt)
        script = script_chain.run(title=title, wikipedia_research=wiki_research)

        return {
            "title": title,
            "script": script,
            "title_history": title_memory.buffer,
            "script_history": script_memory.buffer,
            "wikipedia_research": wiki_research
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#Run the app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
