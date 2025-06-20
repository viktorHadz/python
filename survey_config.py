# survey_config.py - Configuration file for survey analysis

# Professional academic color palette
ACADEMIC_COLORS = ['#2C5F7A', '#4A90A4', '#87CEEB', '#B0C4DE', '#708090']

# Document styling constants
DOC_STYLES = {
    'title_color': (44, 95, 122),  # RGB for Word documents
    'title_color_hex': '#2C5F7A',  # Hex for matplotlib
    'heading_color': (74, 144, 164),  # RGB for Word documents  
    'heading_color_hex': '#4A90A4',  # Hex for matplotlib
    'chart_width': 5.5,  # inches
    'chart_dpi': 150
}

# Updated question categories based on the new CSV structure
QUESTION_CATEGORIES = {
    "Course & Academic Background": [
        "8. Are you studying an undergraduate or postgraduate course?",
        "9. What course are you studying?",
        "10. What qualifications do you have? Please select all that apply",
        "11. What is your highest previous qualification?",
        "12. Did you study your highest previous qualification in the UK, or outside of the UK?",
        "13. Previous year situation"
    ],
    
    "Learning & Assessment Preferences": [
        "14. Previously, how did you typically receive feedback on the work you submitted",
        "15. Preferred way of receiving feedback?",
        "16. Did you usually read your feedback? (Please select one option)",
        "17. Did you ever discuss the academic feedback?",
        "41. How many hours in total do you expect to study each week on top of your teaching hours?",
        "42. How do you prefer to study",
        "43. How you prefer to be assessed"
    ],
    
    "Course Motivation & Expectations": [
        "18. Which of the following applies to you?",
        "19. What are your reasons for choosing the course you have applied for?",
        "20. What was it about the course you found most appealing?",
        "61. What are you hoping to achieve at Teesside University London?",
        "62. What are you most looking forward to about starting your course?"
    ],
    
    "Academic Skills Confidence": [
        "21. Understanding reading material/applying this to assessments/technical tasks",
        "22. Please select one answer for each statement which best represents your feelings about your learning skills:",
        "23. Numeracy Skills",
        "24. Digital Skills -Using Teams to join virtual meetings/lectures/collaborating in gro",
        "25. Digital Skills - Using Teams to record a presentation",
        "26. Digital Skills - use of Microsoft Office such as Word and PowerP"
    ],
    
    "Transition Concerns": [
        "27. How do you feel about: Getting used to living in a new country",
        "28. How do you feel about: Coping with the level of study at University",
        "29. How do you feel about: Getting used to moving away from home for the first time",
        "30. How do you feel about: Commuting to attend my studies",
        "31. How do you feel about: Adequate Information about how to study at University",
        "44. How do you feel about: Integrating into the local community",
        "40. How do you feel about: Your overall feeling about starting your course"
    ],
    
    "Practical Concerns": [
        "32. How do you feel about: Managing Finances and /or debt",
        "33. How do you feel about: Finding Suitable Accommodation",
        "34. How do you feel about: Fitting my study around work commitments",
        "35. How do you feel about: Fitting my study around family commitments",
        "36. How do you feel about: Access to suitable Wi-Fi connection in my home",
        "37. How do you feel about: Access to suitable workspace in my home",
        "38. How do you feel about: Suitable / affordable childcare",
        "39. How do you feel about: Looking after my health and welfare"
    ],
    
    "Demographics": [
        "45. I identify as:",
        "46. How would you describe your ethnicity?",
        "47. What is your identified religion?",
        "56. What is your age group?",
        "57. What is your marital Status?",
        "58. Do you consider English to be your first language?",
        "59. Rating your language skills, how do you consider your fluency in English?"
    ],
    
    "Background & Living Situation": [
        "48. Are you a Care Leaver* with previous experience of being a child in care?",
        "49. Where is your permanent residency when you are NOT studying?",
        "50. Your place of accommodation while you study?",
        "51. Distance from where you are living when you start your studies?",
        "52. Will you be living:",
        "53. Do you plan to undertake paid work during your studies?",
        "54. Did your parents / guardians go to university?",
        "55. Brothers or sisters that are either studying at, or have been to, University?"
    ],
    
    "Support & Services": [
        "60. Do you have a question about starting at Teesside University London?",
        "63. Services you may access whilst studying on your course?"
    ]
}

# Questions that typically need horizontal charts (long text responses)
HORIZONTAL_CHART_QUESTIONS = [
    "19. What are your reasons for choosing the course you have applied for?",
    "20. What was it about the course you found most appealing?",
    "46. How would you describe your ethnicity?",
    "61. What are you hoping to achieve at Teesside University London?",
    "62. What are you most looking forward to about starting your course?",
    "63. Services you may access whilst studying on your course?"
]

# Questions to exclude from main analysis (metadata columns)
EXCLUDE_COLUMNS = [
    "1. Id", "2. Start time", "3. Completion time", "4. Email", 
    "5. Full name", "6. Email", "7. ID"
]

def get_chart_color(question_index, category_name):
    # Get appropriate color for a chart based on question index and category
    return ACADEMIC_COLORS[question_index % len(ACADEMIC_COLORS)]

def should_use_horizontal_chart(question, response_count, max_label_length):
    # Determine if a horizontal chart should be used
    return (question in HORIZONTAL_CHART_QUESTIONS or 
            response_count > 6 or 
            max_label_length > 30)