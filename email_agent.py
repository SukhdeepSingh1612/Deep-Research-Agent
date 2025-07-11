from agents import Agent
from agents import function_tool
from typing import Dict
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("sukhdeepnarulasingh@gmail.com") 
    to_email = To("sukhdeepsingh1612@gmail.com") 
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}

email_instructions = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="emailer agent",
    instructions=email_instructions,
    tools=[send_email],
    model="gpt-4o-mini"
    
)