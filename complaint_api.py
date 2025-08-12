# api/complaint_api.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from difflib import get_close_matches

app = FastAPI()

complaint_map = {
    "muffled": "Audio / Video Issue",
    "sound not clear": "Audio / Video Issue",
    "unclear sound": "Audio / Video Issue",
    "echo": "Audio / Video Issue",
    "noise cancellation": "Audio / Video Issue",
    "no audio": "Audio / Video Issue",
    "distorted sound": "Audio / Video Issue",
    "audio delay": "Audio / Video Issue",
    "video lag": "Audio / Video Issue",
    "screen flickering": "Audio / Video Issue",
    "dead pixels": "Audio / Video Issue",
    "bluetooth not connecting": "Bluetooth Issue",
    "pairing failure": "Bluetooth Issue",
    "short range": "Bluetooth Issue",
    "frequent disconnection": "Bluetooth Issue",
    "unstable connection": "Bluetooth Issue",
    "bluetooth not detected": "Bluetooth Issue",
    "interference": "Bluetooth Issue",
    "dents": "Damaged Item Issue",
    "scratches": "Damaged Item Issue",
    "broken": "Damaged Item Issue",
    "cracked": "Damaged Item Issue",
    "seal broken": "Packaging Issue",
    "outer packaging damaged": "Damaged Item Issue",
    "used product": "Damaged Item Issue",
    "water damage": "Damaged Item Issue",
    "swollen battery": "Damaged Item Issue",
    "item missing": "Missing Item Issue",
    "completely missing": "Missing Item Issue",
    "empty box": "Parts Missing",
    "warranty card missing": "Parts Missing",
    "charging cable missing": "Parts Missing",
    "manual missing": "Parts Missing",
    "accessory missing": "Parts Missing",
    "earbud missing": "Parts Missing",
    "not charging": "Faulty Item Issue",
    "poor battery life": "Faulty Item Issue",
    "device not turning on": "Faulty Item Issue",
    "not working": "Faulty Item Issue",
    "overheating": "Faulty Item Issue",
    "file transfer error": "Faulty Item Issue",
    "slow charging": "Faulty Item Issue",
    "inaccurate reading": "Faulty Item Issue",
    "wrong color": "Wrong / Incorrect Item Issue",
    "wrong model": "Wrong / Incorrect Item Issue",
    "wrong size": "Wrong / Incorrect Item Issue",
    "wrong capacity": "Wrong / Incorrect Item Issue",
    "different brand": "Wrong / Incorrect Item Issue",
    "missing features": "Wrong / Incorrect Item Issue",
    "ordered by mistake": "Ordered by Mistake",
    "wanted different brand": "Ordered by Mistake",
    "wrong specs ordered": "Ordered by Mistake",
    "wanted different model": "Ordered by Mistake",
    "wrong variant": "Ordered by Mistake",
    "box damaged": "Packaging Issue",
    "poor packaging": "Packaging Issue",
    "security seal missing": "Packaging Issue",
    "opened packaging": "Packaging Issue",
    "torn box": "Packaging Issue",
    "too bulky": "Size - Expectation Mismatch",
    "too small": "Size - Expectation Mismatch",
    "cable too short": "Size - Expectation Mismatch",
    "cable too long": "Size - Expectation Mismatch",
    "strap too tight": "Size - Expectation Mismatch",
    "strap too loose": "Size - Expectation Mismatch",
    "cheap quality": "Quality - Expectation Mismatch",
    "poor finish": "Quality - Expectation Mismatch",
    "looks duplicate": "Quality - Expectation Mismatch",
    "poor sound quality": "Quality - Expectation Mismatch",
    "poor video quality": "Quality - Expectation Mismatch",
    "design different": "Design - Expectation Mismatch",
    "buttons too stiff": "Design - Expectation Mismatch",
    "colour different": "Colour - Expectation Mismatch",
    "color different": "Colour - Expectation Mismatch",
    "led color mismatch": "Colour - Expectation Mismatch",
    "logo missing": "Other - Expectation Mismatch",
    "compatibility issue": "Other - Expectation Mismatch",
    "unsupported feature": "Other - Expectation Mismatch",
    "fraud cancellation": "Potential Fraud Canceled Order",
    "tech_potential_fraud_cancellation": "Potential Fraud Canceled Order",
    "potential fraud": "Potential Fraud Canceled Order"
}

@app.get("/classify")
def classify_complaint(keyword: str = Query(..., description="Complaint keyword or sentence")):
    keyword_lower = keyword.lower()
    found_categories = []

    for key, category in complaint_map.items():
        if key in keyword_lower:
            if category not in found_categories:
                found_categories.append(category)

    if found_categories:
        return JSONResponse({"complaint_types": found_categories})

    # Suggest closest matches if no exact match
    suggestions = get_close_matches(keyword_lower, complaint_map.keys(), n=3, cutoff=0.6)
    return JSONResponse({
        "complaint_types": ["Others - Miscellaneous"],
        "suggestions": suggestions
    })
