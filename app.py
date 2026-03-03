from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import pandas as pd
import matplotlib.pyplot as plt
import os
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, file: UploadFile = File(...), question: str = Form(...)):
    
    contents = await file.read()
    with open("uploaded.csv", "wb") as f:
        f.write(contents)

    df = pd.read_csv("uploaded.csv")

    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    answer = agent.run(question)

    image_path = None

    # If question mentions graph, generate one
    if "plot" in question.lower() or "graph" in question.lower():
        df.plot()
        image_path = "static/output.png"
        plt.savefig(image_path)
        plt.close()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "answer": answer,
        "image": image_path
    })