from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, Extra
from typing import Dict, List
from database import save_languages, load_languages
import json

app = FastAPI()

class LanguageSchema(BaseModel):
    language: str
    appeared: int
    created: list
    functional: bool
    # object_oriented: bool = Field(alias="object-oriented")
    object_oriented: bool
    relation: Dict[str, List[str]]

    class Config:
        json_encoders = {
            "object_oriented": "object-oriented"
        }

@app.get("/")
def root():
    return {"message": "Hello Go developers (but I created it with Python)"}

@app.get("/languages", response_model=List[LanguageSchema])
async def get_languages():
    languages = load_languages()
    return list(languages.values())

@app.get("/language/{id}", response_model=LanguageSchema)
async def get_languages_id(id:int):
    languages = load_languages()
    try:
        index = int(id)
        return [language_data for language_data in languages.values()][index]
    except (ValueError, IndexError):
        raise HTTPException(status_code=404, detail="Language not found")

@app.post("/language", response_model=LanguageSchema)
async def add_language(language_data: LanguageSchema):
    languages = load_languages()
    new_language = language_data.dict()
    # languages.update(new_language)
    languages[new_language['language']] = new_language
    save_languages(languages)
    return new_language

@app.patch("/language/{id}", response_model=LanguageSchema)
async def update_language(id:int, language_data: LanguageSchema):
    languages = load_languages()
    try:
        index = int(id)
        language_list = [language_data for language_data in languages.values()]
        if 0 <= index < len(language_list):
            updated_language = language_data.dict(exclude_unset=True)
            languages[language_list[index]["language"]] = updated_language
            save_languages(languages)
            return updated_language
        else:
            raise HTTPException(status_code=404, detail="Language not found")
    except (ValueError, IndexError):
        raise HTTPException(status_code=404, detail="Language not found")

@app.delete("/language/{id}", response_model=LanguageSchema)
async def delete_language(id:int):
    languages = load_languages()
    try:
        index = int(id)
        language_list = [language_data for language_data in languages.values()]
        if 0 <= index < len(language_list):
            deleted_language = language_list.pop(index)
            languages.clear()
            for language in language_list:
                languages[language["language"]] = language
            save_languages(languages)
            return deleted_language
        else:
            raise HTTPException(status_code=404, detail="Language not found")
    except (ValueError, IndexError):
        raise HTTPException(status_code=404, detail="Language not found")

@app.get("/palindrome", response_model=Dict[str,str])
async def palindrome(text:str):
    def check_palindrome(text):
        hps_text = ''.join(a.lower() for a in text if a.isalnum())
        return hps_text == hps_text[::-1]
    if check_palindrome(text):
        return {"message":"Palindrome"}
    else:
        raise HTTPException(status_code=400, detail="Not Palindrome")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)