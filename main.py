from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI(title="Kerala Scheme Eligibility API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

with open("kerala_schemes.json", "r") as f:
    data = json.load(f)

schemes = data["kerala_schemes"]

# ---------------------------------------------------
# User Input Model
# ---------------------------------------------------

class UserProfile(BaseModel):
    age: int | None = None
    gender: str | None = None
    income: float | None = None
    ration_card: str | None = None
    education: str | None = None
    housing_status: str | None = None
    marital_status: str | None = None
    child_age: int | None = None


# ---------------------------------------------------
# Eligibility Checker
# ---------------------------------------------------

def check_eligibility(user: dict, scheme: dict):
    eligibility = scheme.get("eligibility", {})

    # Age check
    if "min_age" in eligibility and user.get("age") is not None:
        if user["age"] < eligibility["min_age"]:
            return False

    if "max_age" in eligibility and user.get("age") is not None:
        if user["age"] > eligibility["max_age"]:
            return False

    # Gender check
    if "gender" in eligibility and user.get("gender"):
        if user["gender"] not in eligibility["gender"]:
            return False

    # Income check
    if "income_max" in eligibility and user.get("income") is not None:
        if user["income"] > eligibility["income_max"]:
            return False

    # Ration card check
    if "ration_card" in eligibility and user.get("ration_card"):
        if user["ration_card"] not in eligibility["ration_card"]:
            return False

    # Education check
    if "education" in eligibility and user.get("education"):
        if eligibility["education"] not in user["education"]:
            return False

    # Housing status
    if "housing_status" in eligibility and user.get("housing_status"):
        if user["housing_status"] not in eligibility["housing_status"]:
            return False

    # Marital status
    if "marital_status" in eligibility and user.get("marital_status"):
        if user["marital_status"] != eligibility["marital_status"]:
            return False

    # Child age
    if "child_age_max" in eligibility and user.get("child_age") is not None:
        if user["child_age"] > eligibility["child_age_max"]:
            return False

    return True


# ---------------------------------------------------
# API ENDPOINTS
# ---------------------------------------------------

@app.get("/")
def home():
    return {"message": "Kerala Scheme Eligibility API Running 🚀"}


@app.post("/check-eligibility")
def eligibility_checker(user: UserProfile):
    user_dict = user.dict()

    eligible_schemes = []

    for scheme in schemes:
        if check_eligibility(user_dict, scheme):
            eligible_schemes.append({
                "id": scheme["id"],
                "name": scheme["name"],
                "benefit": scheme["benefit"],
                "category": scheme["category"]
            })

    return {
        "total_eligible": len(eligible_schemes),
        "eligible_schemes": eligible_schemes
    }


@app.get("/roadmap/{scheme_id}")
def get_roadmap(scheme_id: str):
    for scheme in schemes:
        if scheme["id"] == scheme_id:
            return {
                "scheme_name": scheme["name"],
                "benefit": scheme["benefit"],
                "roadmap": scheme["roadmap"],
                "official_url": scheme.get("official_url", None)
            }

    raise HTTPException(status_code=404, detail="Scheme not found")