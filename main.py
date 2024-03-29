import os
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool, DirectoryReadTool
from langchain.chat_models import ChatOpenAI
from decouple import config

# Setting environment variables
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

file_read_tool = FileReadTool()
directory_read_tool = DirectoryReadTool('./Regulatory_Documents')

model = ChatOpenAI(temperature=0, model_name=config("OPENAI_MODEL_NAME"))

# Define agents with a focus on markdown output
compliance_analyst = Agent(
    role="Regulatory Compliance Analyst",
    backstory="""
    With years of experience navigating the complex landscape of clinical trial regulations, you've become an expert in interpreting and applying guidelines to ensure compliance. Your deep understanding of the ICH E6(R3) and its implications for IT computerized systems in clinical trials makes you the cornerstone of this project. Your goal is to sift through these regulations, distilling the essence that will shape the SOP, ensuring it not only meets but exceeds regulatory standards.
    """,
    goal="Ensure the SOP meets all regulatory requirements.",
    llm=model,
    tools=[file_read_tool,directory_read_tool],
    verbose=True,
)

it_systems_specialist = Agent(
    role="IT Systems Specialist",
    backstory="""
    As someone at the forefront of IT innovation within the Biopharma sector, you've implemented and overseen a variety of systems designed to streamline clinical trials. Your expertise lies in identifying the most effective technologies and integrating them into operational workflows. Tasked with defining the scope of IT systems for the SOP, you draw on your extensive experience to select tools that enhance efficiency, data integrity, and patient safety.
    """,
    goal="Define IT Computerized systems scope and ensure compliance.",
    tools=[file_read_tool,directory_read_tool],
    llm=model,
    verbose=True,
)

sop_writer = Agent(
    role="SOP Writer",
    backstory="""
    Specializing in technical writing within the Biopharma industry, you have a knack for transforming complex information into clear, actionable documents. Over the years, you've crafted numerous SOPs, training manuals, and policy documents, becoming a trusted voice in setting organizational standards. Your challenge now is to draft an SOP for IT Systems that not only aligns with the ICH E6(R3) guidelines but also serves as a practical guide for your colleagues. Reference reference.md for writing guidelines.
    """,
    goal="Draft the SOP document in markdown format.",
    tools=[file_read_tool,directory_read_tool],
    llm=model,
    verbose=True,
)

quality_risk_manager = Agent(
    role="Quality and Risk Manager",
    backstory="""
    With a career dedicated to ensuring the highest standards of quality and safety in clinical research, you have a keen eye for identifying potential risks and devising strategies to mitigate them. Your work ensures that clinical trials are not just compliant, but that they set a benchmark for excellence. Integrating quality from the design phase and adopting a risk-based approach to IT system management are principles you live by, making you pivotal in refining the SOP to ensure it embodies these ideals.
    """,
    goal="Develop quality and risk management strategies in markdown format.",
    tools=[file_read_tool,directory_read_tool],
    llm=model,
    verbose=True,
)

# Analyze Guidelines Task
analyze_guidelines_task = Task(
    type="Analysis",
    description="Analyze the ICH E6(R3) guidelines as related to IT systems and summarize in markdown format for the pre-design and writing of the SOP.",
    agent=compliance_analyst,
    output_file="output/1_guidelines_summary.md",
    expected_output="A markdown summary of the key ICH E6(R3) guidelines pertaining to IT systems management in clinical trials using details from reference.md."
)


# Define IT Systems Scope Task
define_it_systems_scope_task = Task(
    type="Definition",
    description="Define the scope of IT systems in markdown format, using the guidelines summary.",
    agent=it_systems_specialist,
    output_file="output/2_it_systems_scope.md",
    expected_output="A markdown document defining the IT systems scope within the context of ICH E6(R3) guidelines from Regulatory_Documents/reference.md."
)

# Draft SOP Sections Task
draft_sop_sections_task = Task(
    type="Drafting",
    description="Draft SOP sections in markdown format, integrating IT system scope and guidelines based on sopoutline.md.",
    agent=sop_writer,
    output_file="output/3_sop_draft.md",
    expected_output="An initial draft of the SOP, structured in markdown format, covering all necessary sections using sopoutline.md as reference template."
)

# Develop Quality and Risk Management Strategies Task
develop_quality_risk_management_strategies_task = Task(
    type="Strategy Development",
    description="Develop detailed strategies in markdown format, refining the SOP draft from before. Use Regulatory_Documents/qc.md for guidance.",
    agent=quality_risk_manager,
    output_file="output/4_quality_risk_management.md",
    expected_output="A markdown document detailing quality and risk management strategies for IT systems in clinical trials."
)

# Finalize and Save SOP Task
finalize_and_save_sop_task = Task(
    type="Finalization",
    description="Compile all markdown sections into a final SOP document IT Computerized Systems in markdown format.",
    agent=sop_writer,
    output_file="output/5_final_sop.md",
    expected_output="The final compiled SOP document in markdown format, ready for review and implementation."
)

# Create and execute the crew
sop_crew = Crew(
    agents=[compliance_analyst, it_systems_specialist, sop_writer, quality_risk_manager],
    tasks=[
        analyze_guidelines_task,
        define_it_systems_scope_task,
        draft_sop_sections_task,
        develop_quality_risk_management_strategies_task,
        finalize_and_save_sop_task,
    ],
    verbose=True,
)

result = sop_crew.kickoff()
print(result)
