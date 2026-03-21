from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (fine for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Request Model ----------
class CitationRequest(BaseModel):
    source_type: str
    author: str
    year: int
    title: str
    publisher: str = ""
    url: str = ""

# ---------- Author Formatter ----------
def format_authors(author_str: str):
    authors = [a.strip() for a in author_str.split(",")]
    
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} & {authors[1]}"
    else:
        return ", ".join(authors[:-1]) + f", & {authors[-1]}"

# ---------- GET (keep for testing) ----------
@app.get("/apa")
def generate_apa_get(
    source_type: str,
    author: str,
    year: int,
    title: str,
    publisher: str = "",
    url: str = ""
):
    authors = format_authors(author)

    if source_type == "book":
        citation = f"{authors} ({year}). *{title}*. {publisher}."
    elif source_type == "website":
        citation = f"{authors} ({year}). {title}. Retrieved from {url}"
    elif source_type == "journal":
        citation = f"{authors} ({year}). *{title}*."
    else:
        return {"error": "Invalid source type"}

    return {"citation": citation}

# ---------- POST (NEW — IMPORTANT) ----------
@app.post("/apa")
def generate_apa_post(data: CitationRequest):
    authors = format_authors(data.author)

    if data.source_type == "book":
        citation = f"{authors} ({data.year}). *{data.title}*. {data.publisher}."
    elif data.source_type == "website":
        citation = f"{authors} ({data.year}). {data.title}. Retrieved from {data.url}"
    elif data.source_type == "journal":
        citation = f"{authors} ({data.year}). *{data.title}*."
    else:
        return {"error": "Invalid source type"}

    return {"citation": citation}