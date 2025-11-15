import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Data Science Syllabus Viewer", layout="wide")

# ----------------------------
# TRAINER & BATCH DETAILS
# ----------------------------
TRAINER_NAME = "Om Bankar"
BATCH_NAME = "CBZ@ON-X-DSAAI-05~"
BATCH_MODE = "Online"
ATTENDANCE = "02"

# ----------------------------
# DAY–WISE SYLLABUS DATA
# ----------------------------
syllabus = {
    "Day 1": {
        "title": "Introduction to Data Science",
        "topics": [
            "Discussion of ETL pipeline",
            "How stored data is used for business problems",
            "Three types of Analytics – Descriptive, Predictive, Prescriptive",
            "Descriptive: Data Summarization & Visualization",
            "Tools for Data Summarization and Visualization",
            "Predictive: Sales prediction in McDonald's, weather forecasting",
            "Two major algorithms – Machine Learning, Deep Learning",
            "Math needed for ML & DL",
            "Examples: Classification, Regression",
            "Deep Learning examples: Image & Text processing"
        ]
    },

    "Day 2": {
        "title": "Getting Started with Python",
        "topics": [
            "Need for a programming language in DA & DS",
            "Why Python?",
            "Python libraries for DA & DS",
            "Python IDEs",
            "Setting up Google Colab",
            "Simple commands: print(), type(), etc."
        ]
    },

    "Day 3": {
        "title": "Variables and Data Types",
        "topics": [
            "Creating simple variables",
            "Rules for variable naming",
            "Numeric types: int, float, bool, complex",
            "Sequence types: strings, lists, tuples"
        ]
    },

    "Day 4": {
        "title": "Type Casting & Strings",
        "topics": [
            "Type Casting: int→float, str→int",
            "String methods",
            "Indexing & slicing",
            "String concatenation"
        ]
    },

    "Day 5": {
        "title": "Operators in Python",
        "topics": [
            "Arithmetic Operators",
            "Logical Operators",
            "Assignment Operators",
            "Comparison Operators"
        ]
    },

    "Day 6": {
        "title": "Conditional Statements",
        "topics": [
            "if statement",
            "elif statement",
            "if–else examples",
            "Student Grading System",
            "Customer Discount System"
        ]
    },

    "Day 7": {
        "title": "Lists – Functions & Comprehension",
        "topics": [
            "Understanding Lists",
            "Indexing & slicing",
            "List methods",
            "Example: Grocery items"
        ]
    },

    "Day 8": {
        "title": "Lists & Tuples",
        "topics": [
            "Mutability",
            "Syntax differences",
            "Memory usage",
            "Use cases",
            "List & Tuple methods"
        ]
    },

    "Day 9": {
        "title": "Loops in Python",
        "topics": [
            "for loop",
            "while loop",
            "break, continue, pass"
        ]
    },

    "Day 10": {
        "title": "Patterns & List Comprehension",
        "topics": [
            "Pattern printing",
            "List comprehension",
            "Turtle pattern examples"
        ]
    },

    "Day 11": {
        "title": "Sets",
        "topics": [
            "Understanding Sets",
            "Set methods: add, update, remove"
        ]
    },

    "Day 12": {
        "title": "Dictionaries",
        "topics": [
            "Dictionary structure",
            "Updating dictionaries",
            "Dictionary methods",
            "Extracting JSON from API"
        ]
    },

    "Day 13": {
        "title": "Functions",
        "topics": [
            "User-defined functions",
            "Return statements",
            "Input/output parameters",
            "Recursive functions"
        ]
    },

    "Day 14": {
        "title": "Arguments & Lambda",
        "topics": [
            "*args, **kwargs",
            "Lambda functions"
        ]
    },

    "Day 15": {
        "title": "Built-in Functions & Modules",
        "topics": [
            "abs, type, len, sum, zip",
            "datetime & strftime",
            "Modules: Chempy, Geopy, Scipy"
        ]
    },

    "Day 16": {
        "title": "OOP – Classes & Objects",
        "topics": [
            "OOP Concepts",
            "Classes & Objects",
            "Polymorphism"
        ]
    },

    "Day 17": {
        "title": "OOP – Inheritance, Encapsulation, Abstraction",
        "topics": [
            "Parent/child classes",
            "Types of inheritance",
            "Encapsulation",
            "Abstraction examples"
        ]
    },

    "Day 18": {
        "title": "Abstraction in OOP",
        "topics": [
            "Understanding Abstraction",
            "Car/ATM examples"
        ]
    },

    "Day 19": {
        "title": "Regular Expressions",
        "topics": [
            "Introduction to Regex",
            "search(), match(), sub(), split()",
            "Extracting phone numbers, subtitles"
        ]
    },

    "Day 20": {
        "title": "Error Handling",
        "topics": [
            "Types of errors",
            "try–except",
            "Raise exceptions",
            "Finally block"
        ]
    },

    "Day 21": {
        "title": "Anaconda & NumPy Intro",
        "topics": [
            "Why Anaconda",
            "Navigator interface",
            "Environments",
            "NumPy basics",
            "Array creation & slicing",
            "Simple grayscale image"
        ]
    },

    "Day 22": {
        "title": "NumPy – Creating & Slicing Arrays",
        "topics": [
            "np.array, zeros, ones, arange, linspace",
            "Random arrays",
            "Slicing 1D & 2D",
            "Negative indexing",
            "Speed & memory comparison"
        ]
    },

    "Day 23": {
        "title": "Pandas Introduction",
        "topics": [
            "Why Pandas",
            "Series & DataFrame",
            "Create DataFrames & Series"
        ]
    },

    "Day 24": {
        "title": "Pandas – Methods & Manipulation",
        "topics": [
            "head, tail, info, describe",
            "Selecting rows/cols",
            "Filtering & sorting",
            "Missing values",
            "Read CSV / Save CSV"
        ]
    },

    "Day 25": {
        "title": "Matplotlib Basics",
        "topics": [
            "Line, Bar, Hist, Box, Scatter plots",
            "Titles, labels, legends",
            "Saving plots"
        ]
    },

    "Day 26": {
        "title": "Seaborn Introduction",
        "topics": [
            "Bar, Line, Hist, Box, Scatter, Pairplot",
            "Themes & customization"
        ]
    },

    "Day 27": {
        "title": "EDA – Part 1",
        "topics": [
            "What is EDA",
            "Check types, missing values",
            "Basic statistics",
            "Distribution plots"
        ]
    },

    "Day 28": {
        "title": "EDA – Part 2 (Hands-On)",
        "topics": [
            "Full EDA activity",
            "Histograms, boxplots, countplots"
        ]
    },

    "Day 29": {
        "title": "Data Cleaning",
        "topics": [
            "Missing values",
            "Duplicates",
            "Inconsistent data",
            "Renaming columns"
        ]
    },

    "Day 30": {
        "title": "EDA Assignment",
        "topics": [
            "Perform full EDA",
            "Handle missing values",
            "Visualizations",
            "Observations"
        ]
    }
}

# ----------------------------
# STREAMLIT UI
# ----------------------------
st.title("📘 Data Science Syllabus Viewer")

selected_day = st.selectbox("Select Day", list(syllabus.keys()))

if selected_day:

    data = syllabus[selected_day]

    st.markdown("### 📚 Data Science Training Update")

    st.write(f"**Date:** {datetime.now().date()}")
    st.write(f"**Trainer Name:** {TRAINER_NAME}")
    st.write(f"**Batch Name:** {BATCH_NAME}")
    st.write(f"**Batch Mode:** {BATCH_MODE}")
    st.write(f"**Attendance:** {ATTENDANCE}")

    st.write(f"**Topic:**")
    st.subheader(selected_day)
    st.write(f"### {data['title']}")

    st.write("### Main Topic:")
    for t in data['topics']:
        st.write(f"- {t}")

    st.markdown("==" * 30)
