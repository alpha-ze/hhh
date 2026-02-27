"""
AI Agent for Form Filling Assistance
This agent analyzes webpage screenshots and provides step-by-step guidance
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import base64

agent_app = FastAPI(title="Form Filling Agent")

class ScreenshotRequest(BaseModel):
    scheme_id: str
    screenshot: str  # base64 encoded image
    current_step: int
    user_data: dict

class AgentResponse(BaseModel):
    instructions: list[str]
    field_mappings: dict
    next_action: str
    warnings: list[str]

@agent_app.post("/analyze-form")
async def analyze_form(request: ScreenshotRequest):
    """
    Analyzes the screenshot and provides form filling guidance
    In production, this would use GPT-4 Vision or similar AI model
    """
    
    # Mock response - In production, integrate with OpenAI GPT-4 Vision API
    # or Google Gemini Vision API to analyze the screenshot
    
    scheme_guidance = {
        "STHREE_001": {
            "step_1": {
                "instructions": [
                    "Look for the 'Apply Now' or 'New Application' button",
                    "Click on 'Sthree Suraksha Pension Scheme'",
                    "You should see a login/registration page"
                ],
                "field_mappings": {},
                "next_action": "Click the 'Apply' button to proceed",
                "warnings": ["Ensure you have your Aadhaar card ready"]
            },
            "step_2": {
                "instructions": [
                    "Enter your 12-digit Aadhaar number in the Aadhaar field",
                    "Click 'Send OTP' button",
                    "Check your registered mobile for OTP",
                    "Enter the 6-digit OTP received"
                ],
                "field_mappings": {
                    "aadhaar_number": "Enter your Aadhaar number here",
                    "otp": "Enter OTP from SMS"
                },
                "next_action": "Click 'Verify' after entering OTP",
                "warnings": ["OTP is valid for 10 minutes only"]
            },
            "step_3": {
                "instructions": [
                    "Fill personal details: Name, Date of Birth, Address",
                    "Upload Ration Card (Yellow/Pink) - Max 2MB PDF/JPG",
                    "Upload Bank Passbook first page - Max 2MB",
                    "Fill bank details: Account number, IFSC code",
                    "Upload recent passport photo - Max 200KB"
                ],
                "field_mappings": {
                    "name": "Auto-filled from Aadhaar",
                    "dob": "Auto-filled from Aadhaar",
                    "address": "Verify and update if needed",
                    "ration_card": "Upload document",
                    "bank_passbook": "Upload document"
                },
                "next_action": "Click 'Save & Continue' after filling all fields",
                "warnings": [
                    "Ensure all documents are clear and readable",
                    "Bank account must be in your name"
                ]
            }
        },
        "PENSION_001": {
            "step_1": {
                "instructions": [
                    "Visit your local Gram Panchayat office during working hours (10 AM - 5 PM)",
                    "Ask the receptionist for 'Social Security Pension Application Form'",
                    "Collect the form - it's usually free of charge",
                    "You can also download the form from the Kerala government website if available"
                ],
                "field_mappings": {},
                "next_action": "Collect the application form",
                "warnings": [
                    "Carry your Aadhaar card for identification",
                    "Note down the office phone number for follow-up"
                ]
            },
            "step_2": {
                "instructions": [
                    "Fill your full name as per Aadhaar card",
                    "Enter your date of birth and age (must be 60+)",
                    "Write your complete address with pin code",
                    "Fill bank account details: Account number, IFSC code, Branch name",
                    "Attach photocopies of: Aadhaar card, Ration card, Bank passbook first page",
                    "Paste one recent passport-size photograph"
                ],
                "field_mappings": {
                    "name": "As per Aadhaar card",
                    "age": "Must be 60 years or above",
                    "address": "Current residential address",
                    "bank_details": "Active bank account in your name",
                    "ration_card": "Yellow or Pink card"
                },
                "next_action": "Complete the form and attach all documents",
                "warnings": [
                    "Use black or blue pen only",
                    "Do not leave any mandatory fields blank",
                    "Ensure photocopies are clear and readable"
                ]
            },
            "step_3": {
                "instructions": [
                    "Review the completed form for any errors",
                    "Verify all attached documents are properly stapled",
                    "Submit the form to the Panchayat Secretary",
                    "Get an acknowledgement receipt with application number",
                    "Note down the expected processing time (usually 30-45 days)"
                ],
                "field_mappings": {},
                "next_action": "Submit application and collect receipt",
                "warnings": [
                    "Keep the acknowledgement receipt safe",
                    "Note the application number for tracking",
                    "Ask for the helpline number for status updates"
                ]
            }
        },
        "EMPLOY_001": {
            "step_1": {
                "instructions": [
                    "Click on 'Register' if new user",
                    "Enter Aadhaar number for authentication",
                    "Complete OTP verification",
                    "Create username and password"
                ],
                "field_mappings": {
                    "aadhaar": "12-digit Aadhaar number",
                    "mobile": "Registered mobile number"
                },
                "next_action": "Complete registration and login",
                "warnings": ["Remember your username and password"]
            },
            "step_2": {
                "instructions": [
                    "Upload your SSLC certificate or higher education certificate",
                    "Upload income certificate (must show income below ₹1 lakh)",
                    "Ensure documents are in PDF format, max 2MB each",
                    "Fill employment preferences and skills"
                ],
                "field_mappings": {
                    "education_certificate": "SSLC or higher",
                    "income_certificate": "From Tahsildar office"
                },
                "next_action": "Upload all required documents",
                "warnings": ["Income certificate must be recent (within 6 months)"]
            },
            "step_3": {
                "instructions": [
                    "Review your application details",
                    "Submit the application",
                    "Monthly aid will be automatically credited to your bank account",
                    "You will receive SMS notifications for each payment"
                ],
                "field_mappings": {},
                "next_action": "Submit and wait for approval",
                "warnings": ["Ensure your bank account is active and linked to Aadhaar"]
            }
        },
        "HOUSING_001": {
            "step_1": {
                "instructions": [
                    "Navigate to Life Mission portal",
                    "Click 'New Application'",
                    "Select your district from dropdown",
                    "Enter Aadhaar for verification",
                    "Upload Ration Card and income certificate"
                ],
                "field_mappings": {
                    "district": "Select from dropdown",
                    "aadhaar": "12-digit number",
                    "ration_card_type": "Yellow or Pink"
                },
                "next_action": "Submit application for lottery",
                "warnings": ["Application is subject to lottery selection"]
            },
            "step_2": {
                "instructions": [
                    "Wait for district-level lottery announcement",
                    "Check your application status regularly on the portal",
                    "You will receive SMS if selected in lottery",
                    "Selected candidates will be contacted for further verification"
                ],
                "field_mappings": {},
                "next_action": "Wait for lottery results",
                "warnings": [
                    "Lottery is conducted quarterly",
                    "Keep your mobile number active for notifications"
                ]
            }
        },
        "UNWED_001": {
            "step_1": {
                "instructions": [
                    "Locate your District Women & Child Development Office",
                    "Visit during office hours (10 AM - 5 PM, Monday to Friday)",
                    "Carry your child's birth certificate as primary proof",
                    "Ask for 'Snehasparsham Scheme Application Form'",
                    "The staff will guide you through the process"
                ],
                "field_mappings": {},
                "next_action": "Visit WCD office and collect form",
                "warnings": [
                    "Carry original documents for verification",
                    "This is a confidential process - your privacy is protected"
                ]
            },
            "step_2": {
                "instructions": [
                    "Fill the application form with your personal details",
                    "Attach child's birth certificate (original + photocopy)",
                    "Attach your Aadhaar card (photocopy)",
                    "Attach income certificate from Tahsildar",
                    "Provide bank account details for direct benefit transfer",
                    "Submit to the WCD officer for verification"
                ],
                "field_mappings": {
                    "child_birth_certificate": "Mandatory document",
                    "aadhaar": "Your Aadhaar card",
                    "income_certificate": "Must show income below ₹25,000/month",
                    "bank_account": "In your name"
                },
                "next_action": "Submit application with all documents",
                "warnings": [
                    "Child must be below 18 years of age",
                    "Income certificate must be recent",
                    "Medical aid is also provided under this scheme"
                ]
            }
        }
    }
    
    scheme_id = request.scheme_id
    step_key = f"step_{request.current_step}"
    
    if scheme_id not in scheme_guidance:
        return AgentResponse(
            instructions=["AI guidance not yet configured for this scheme. Please follow the roadmap steps."],
            field_mappings={},
            next_action="Follow the instructions provided",
            warnings=[]
        )
    
    if step_key not in scheme_guidance[scheme_id]:
        return AgentResponse(
            instructions=["Continue with the current step as described in the roadmap"],
            field_mappings={},
            next_action="Follow on-screen instructions",
            warnings=[]
        )
    
    guidance = scheme_guidance[scheme_id][step_key]
    
    return AgentResponse(
        instructions=guidance["instructions"],
        field_mappings=guidance["field_mappings"],
        next_action=guidance["next_action"],
        warnings=guidance["warnings"]
    )

@agent_app.get("/")
def agent_home():
    return {"message": "Form Filling Agent API Running 🤖"}
