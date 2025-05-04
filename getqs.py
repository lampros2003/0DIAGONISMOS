# extract the questions from evaluation.xlsx
import pandas as pd 
import os
import re
import json
import openpyxl


def get_questions_from_excel(file_path):
    df = pd.read_excel(file_path, sheet_name=None)

    sheet_names = df.keys()

    questions = []

    for sheet in sheet_names:
        data = df[sheet]

        if "Question" in data.columns:
            for question in data["Question"]:
                if isinstance(question, str):
                    questions.append(question.strip())

    return questions