# FILES BELONGS TO @rocks_fighters 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "19763428"))
API_HASH = os.getenv("API_HASH", "979536ef62d662beb1a0a788bae912ea")
SESSION = os.getenv("SESSION", "BQA6OEBg8RW73LBNNnZXGbzSVQFwX_-1HOHUXG596PxxO3x9HVeBrSR-Aex-EYbjYr0gxdi8a3ZtllqSO3YizB3OviwnITkpW11iNpmhnYK3FPHKzmspT8mmbBHwMTOLkX71gjoqjcQmHwGQET8h3WHZGCusQb8Q5xvVp0Tyffxp8mMnDYG_6FAn26ThApZzBtFDK8HjAiW88Lr_j8HMAHuRnA0DNg7oyWjtBtkZ5FsbY0bEE9O9ldGvewCWXegwRF-u89p2caK9a9T1hoyWnP0oZPg7ir2h22uxM8F4pzoorQjCRXggnrd_qoaF2eidlKsqscrKcCDBbyAxH3HePDzbAAAAATQeQZcA")
OWNER = os.getenv("OWNER", "1452370643")
SUPPORT = os.getenv("SUPPORT", "-1001733594693)
SUDO_USERS = os.getenv("SUDO_USERS", "5314932005","2116857965","5533069787")
