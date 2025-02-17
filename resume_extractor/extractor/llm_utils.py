import requests

GEMINI_API_KEY = "AIzaSyCLQwMfQYEErRNMuKXhqv6xs0mH2SnbLKg"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"

def get_structured_resume(text):
    prompt = f"""
    Extract and structure the following resume text into a **structured JSON format** with each section appearing separately.
    Ensure that all details are placed under their appropriate categories for easy parsing.

    The **structured JSON output** should strictly follow this format:

    ```json
    {{
        "Profile": {{
            "Name": "",
            "Phone": "",
            "Email": "",
            "LinkedIn": "",
            "GitHub": "",
            "Portfolio": ""
        }},
        "Work Experience": [
            {{
                "Company": "",
                "Role": "",
                "Duration": "",
                "Responsibilities": []
            }},
            {{
                "Company": "",
                "Role": "",
                "Duration": "",
                "Responsibilities": []
            }}
        ],
        "Projects": [
            {{
                "Project Name": "",
                "Project Link": "",
                "Description": "",
                "Technologies Used": []
            }},
            {{
                "Project Name": "",
                "Project Link": "",
                "Description": "",
                "Technologies Used": []
            }}
        ],
        "Technical Skills": {{
            "Programming Languages": [],
            "Backend Development": [],
            "Frontend Development": [],
            "Databases": [],
            "Development Tools": [],
            "AI/ML & Data Science": []
        }},
        "Education": [
            {{
                "University": "",
                "Degree": "",
                "Duration": "",
                "Relevant Coursework": []
            }}
        ],
        "Extracurricular Activities": [
            {{
                "Activity": "",
                "Description": ""
            }},
            {{
                "Activity": "",
                "Description": ""
            }}
        ]
    }}
    ```

    **Extraction Guidelines:**
    - Extract the **Projects** section so that each project appears as a **separate entry**.
    - Ensure that **Work Experience** entries are separated, each containing a **company, role, duration, and responsibilities**.
    - Extract **Technical Skills** into **distinct categories** (Programming Languages, Backend, Frontend, Databases, Development Tools, AI/ML).
    - Extract **Education** details into **a structured format** (University, Degree, Duration, Relevant Courses).
    - Extract **Extracurricular Activities** separately, listing each **competition, hackathon, or community activity as a new object**.

    **Ensure that each section appears separately in the JSON output, and no content is merged together.**

    **Resume text:**
    {text}
    """

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        json=payload
    )

    if response.status_code == 200:
        try:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except KeyError:
            return {"error": "Unexpected response format", "response": result}
    else:
        return {"error": f"API Error {response.status_code}: {response.json()}"}
