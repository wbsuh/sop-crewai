# CrewAI SOP Writer Template 

CrewAI is a template for creating business-specific Standard Operating Procedures (SOPs). This project aims to streamline the process of developing SOPs that align with the ICH E6(R3) guideline or any regulatory requirements to promote quality and risk management in clinical trials. 

## Requirements

To run this project, you need to have Python installed on your system. The required Python packages are listed in the `requirements.txt` file. You need a subscription to OpenAI to power the Agents.

## Installation

1. Clone the repository:
```
git clone git@github.com:wbsuh/sop-crewai.git
```

2. Navigate to the project directory:
```
cd sop-crewai
```
3. Create a virtual environment (optional but recommended)
```
python -m venv venv

```
4. Activate the virtual environment:

- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required packages:
```
pip install -r requirements.txt
```
6. In the directory create .env file and add the following:
```
OPENAI_API_KEY = "YOUR_OPENAI_KEYS"
OPENAI_MODEL_NAME = "gpt-4-0125-preview"
```

## How to Run 

1. Place your reference documents in the `Regulatory_Documents` directory. These documents should provide guidance and requirements for developing SOPs related to IT computerized systems in clinical trials or any other regulatory requirements of your choosing.

2. Run the SOP CrewAI script:
```
python main.py
```

3. The generated drafts will be saved in the `output` directory.

## Reference Documents

The `Regulatory_Documents` directory is where you should place your reference documents. These documents serve as a guide for developing SOPs that comply with the ICH E6(R3) guideline and other relevant regulations.

Examples of reference documents include:
- ICH E6(R3) guideline
- Regulatory requirements specific to your region or country
- Internal company policies and procedures

Make sure to review and update these reference documents regularly to ensure your SOPs remain up-to-date with the latest guidelines and best practices.

## Optional 
Included a template sopoutline markdown file to help you get started with the SOP development process. You can use this as a reference for the structure and content of your SOP. Modify it as needed to fit your specific needs and requirements.

## Limitations
Regulatory Documents for review cannot exceed OpenAI's token limit. If you have a large document, you may need to split it into smaller chunks and submit them separately. Recommendation is to use ChatGPT or Gemini to filter relevant details for the SOP and then use the SOP CrewAI script to generate the final SOP. The PDF to Markdown converter (pdf2md.py) can be used to convert the PDF to Markdown.