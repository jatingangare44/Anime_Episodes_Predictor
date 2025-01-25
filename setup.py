from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Anime-Episodes-Prediction"
AUTHOR_USER_NAME = "jatingangare44"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie-Runtime-Prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/jatingangare44/Anime-Episode-Predictor",
    author_email="jating22it@student.mes.ac.in",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
