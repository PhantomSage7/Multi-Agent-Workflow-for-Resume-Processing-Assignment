
# Multi-Agent Workflow for Resume Processing

## Assignment Overview
This project is part of the AI/ML Intern technical assignment focused on building a Large Language Model (LLM)-powered multi-agent workflow for automating resume processing. The system handles the entire process, from reading multi-page resumes to extracting and validating entities, with the ability to involve human feedback at each step.

---

## Objective
The goal of this project is to automate the processing of multi-page resumes using a multi-agent architecture, where each agent is responsible for different stages of the process. The key tasks include:

- **Resume Reading**: Parsing multi-page resumes in formats like PDF and DOCX.
- **Entity Extraction**: Identifying and extracting key information like personal details, education, experience, and skills.
- **Entity Validation**: Verifying the accuracy and completeness of extracted data.
- **Human Feedback Loop**: Allowing real-time human intervention to correct or refine the agents' outputs.
- **JSON Output**: Formatting the extracted and validated entities into a standardized JSON format for downstream use.

---

## Project Structure
\`\`\`
project-root/
│
├── agents/                    # Directory containing agent scripts
│   ├── __init__.py            # Package initializer
│   ├── extractor.py           # Agent responsible for extracting entities
│   ├── graph.py               # Handles monitoring with LangGraph
│   ├── reader.py              # Agent for reading resumes
│   ├── validator.py           # Agent for validating extracted entities
│
├── venv/                      # Virtual environment (not tracked by Git)
│
├── main.py                    # Orchestrator script for running the entire workflow
│
├── requirements.txt           # Required dependencies
│
└── resume.pdf                 # Sample resume file for testing
\`\`\`

---

## Setup and Installation

### Prerequisites
- Python 3.x
- Git
- Gemini API key

### Steps

1. **Clone the Repository**
   \`\`\`bash
   git clone https://github.com/PhantomSage7/Multi-Agent-Workflow-for-Resume-Processing-Assignment.git
   cd Multi-Agent-Workflow-for-Resume-Processing-Assignment

   \`\`\`

2. **Create and Activate a Virtual Environment**
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate    # For Windows
   \`\`\`

3. **Set up the .env file for the Gemini API key**
   - In the project root, create a \`.env\` file and add your Gemini API key with the following format:
     \`\`\`bash
     GEMINI_API_KEY=your_gemini_api_key_here
     \`\`\`

4. **Install Dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

5. **Run the Application**
   \`\`\`bash
   python main.py
   \`\`\`

---

## How It Works

### Agents
- **Resume Reader Agent (reader.py)**: Reads and processes multi-page resumes, transforming them into a structured format ready for further processing.
- **Extractor Agent (extractor.py)**: Extracts key entities such as name, contact info, education, and work experience. It also uses the **Gemini API** for enhanced entity extraction. The API key must be provided via the \`.env\` file and accessed within the \`extractor.py\` script using the \`GEMINI_API_KEY\` environment variable.
  
  Example usage in \`extractor.py\`:
  \`\`\`python
  import os
  from dotenv import load_dotenv

  load_dotenv()

  GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
  # Use GEMINI_API_KEY in API calls
  \`\`\`

- **Validator Agent (validator.py)**: Checks the extracted data for accuracy and completeness, flagging any issues that need correction.

### Workflow
1. **Human Feedback**: At each step, the system can pause and request feedback from users to correct or enhance the process.
2. **JSON Output**: After validation, the system compiles the processed data into a JSON file for further use.

---

## Human Feedback Loop
At any point, users can intervene by providing feedback, which the agents integrate into their processing. This is essential for refining and correcting the extracted information in real-time.

### How Users Can Provide Feedback
- The system will pause during critical steps and request input.
- Users can either confirm the extraction, modify it, or add missing information.
- The feedback is passed back to the relevant agent for processing.

---

## Monitoring with LangGraph and LangSmith
The system leverages LangGraph and LangSmith for monitoring and visualizing each call made to the LLMs within the agents. This enables tracking of the system's performance and allows for debugging and optimization.

- **LangGraph**: Visualizes the data flow and interaction between agents.
- **LangSmith**: Monitors the calls to LLMs, ensuring transparency and traceability.

---

## Assumptions and Design Decisions
- The project assumes that resumes are primarily in PDF format.
- A human-in-the-loop mechanism was integrated to handle ambiguous or incomplete data extraction.
- The agents are modular, making it easy to extend or add new features.

---

## Sample Output
A JSON file containing the extracted and validated resume data will be generated. Here is an example of the expected structure:
\`\`\`json
{
  "name": "John Doe",
  "contact": {
    "email": "johndoe@example.com",
    "phone": "+1234567890"
  },
  "education": [
    {
      "institution": "University of Example",
      "degree": "B.Sc. Computer Science",
      "years": "2015-2019"
    }
  ],
  "experience": [
    {
      "company": "Tech Corp",
      "role": "Software Engineer",
      "years": "2020-2023"
    }
  ],
  "skills": ["Python", "Machine Learning", "Data Analysis"]
}
\`\`\`

---

## Bonus Features
- **Robust Error Handling**: The system gracefully handles errors such as missing or malformed data.
- **Scalability**: The design is modular, allowing for easy addition of new agents or other functionalities.
- **User Interface**: The system can be extended to include a CLI or a simple GUI for user interaction.

---


## Monitoring Setup

1. **LangGraph**: Install LangGraph and configure it by following the [LangGraph Documentation](https://www.langchain.com/langgraph).
2. **LangSmith**: Follow the [LangSmith Documentation](https://www.langchain.com/langsmith) for setting up and integrating LangSmith with the agents.

---

## Resources
- [LangChain Documentation](https://python.langchain.com/docs/introduction/)
- [LangGraph Documentation](https://www.langchain.com/langgraph)
- [LangSmith Documentation](https://www.langchain.com/langsmith)
- [Python Code Style Guidelines (PEP 8)](https://pep8.org/)

---

## Conclusion
This project demonstrates the use of a multi-agent workflow for resume processing powered by LLMs, with a strong focus on modularity, scalability, and real-time human intervention. The monitoring tools ensure full transparency in the system’s operations, enabling both debugging and optimization.
