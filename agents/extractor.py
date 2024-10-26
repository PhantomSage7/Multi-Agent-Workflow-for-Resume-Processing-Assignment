import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from typing import TypedDict, List

class PersonalInfo(TypedDict):
    name: str
    phone_no: int
    email: str

class Education(TypedDict):
    degree: str
    university: str

class WorkExperience(TypedDict):
    company: str
    role: str
    description: str

class Resume(TypedDict):
    personal_info: PersonalInfo
    education: Education
    work_experience: WorkExperience

def extractor(prompt):
    """
    Extracts structured information from resume text using Gemini
    """
    genai.configure(api_key=os.getenv("KEY"))
    
    # Define the schema for structured output
    # schema = {
    #     "type": content.Type.OBJECT,
    #     "properties": {
    #         "personal_info": {
    #             "name": content.Schema(type=content.Type.STRING),
    #             "phone_no": content.Schema(type=content.Type.NUMBER),
    #             "email": content.Schema(type=content.Type.STRING),
    #         },
    #         "education": {
    #             "degree": content.Schema(type=content.Type.STRING),
    #             "university": content.Schema(type=content.Type.STRING),
    #         },
    #         "work_experience": {
    #             "company": content.Schema(type=content.Type.STRING),
    #             "role": content.Schema(type=content.Type.STRING),
    #             "description": content.Schema(type=content.Type.STRING),
    #         }
    #     }
    # }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash"
    )
    
    return model.generate_content(prompt, generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=Resume
    )).text