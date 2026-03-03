# Autonomous-csv-data-analyst
🚀 Autonomous CSV Data Analyst Agent
An AI-powered autonomous agent that analyzes CSV/Excel datasets using natural language queries and generates insights with visualizations in a secure sandboxed environment.
📌 Project Overview
The Autonomous CSV Data Analyst Agent enables business users to upload a dataset and ask complex questions in plain English, such as:
What are the sales trends per region?
What is the average monthly revenue?
Show correlation between marketing spend and sales.
The agent automatically:
Converts natural language queries into executable Python (Pandas) code
Executes the code safely inside a sandbox
Performs self-correction if errors occur
Generates insights and visualizations
Returns results and downloadable graph outputs
🧠 Core Features
✅ Natural Language → Python (Pandas) conversion
✅ Autonomous code execution via Python REPL
✅ Self-correction mechanism for runtime errors
✅ Graph generation using Matplotlib
✅ Secure sandboxed execution using Docker
✅ Transparency via intermediate reasoning steps
🏗️ System Architecture
User Query
⬇
LangChain Agent
⬇
Python REPL Tool (Pandas Execution)
⬇
Sandboxed Environment (Docker)
⬇
Result + Visualization (Matplotlib)
🛠️ Tech Stack
Python
Pandas
Matplotlib
LangChain Agents
Docker (Sandboxing)
🔐 Security Implementation
To prevent malicious or unsafe code execution:
Restricted Python environment
Limited accessible libraries
Isolated working directory
Docker-based sandbox container
Prompt injection testing
📊 Example Workflow
Upload CSV file
Ask question:

Show monthly sales trend with 3-month rolling average
Agent generates Pandas code
Code executes in sandbox
Graph (.png) is saved and returned
📅 Implementation Plan (4 Weeks)
Week 1: Built Pandas Agent and query execution
Week 2: Implemented graph generation
Week 3: Added sandboxing & security controls
Week 4: UI integration & final testing
🎯 Learning Outcomes
AI Agent architecture
Prompt engineering
Secure LLM deployment
Autonomous code execution
Production-focused system design
📌 Future Improvements
Multi-file dataset support
Advanced statistical modeling
Role-based access control
Cloud deployment
Real-time dashboard integration
👨‍💻 Author
Rik Saha
B.Tech CSE
AI & Data Enthusiast
