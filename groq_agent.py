from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
    )

agent.print_response("""
                     Write the below sub-section of a research based book chapter called 
                     'Fundamentals of Machine Learning in Neurology': Applications of Machine Learning in Neurology
                            5.1 Disease Prediction and Classification
                            - Case studies on Alzheimer's, Parkinson's, MS, etc.
                            5.2 Imaging Analysis
                            - Techniques for analyzing neuroimaging data using ML.
                            5.3 Personalized Medicine
                            - How ML can aid in tailoring treatments based on individual patient data.
                            5.4 Monitoring and Management
                            - Use of ML in tracking disease progression and treatment efficacy.
                     """)


