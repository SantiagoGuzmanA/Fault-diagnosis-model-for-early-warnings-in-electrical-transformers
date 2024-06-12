# Fault Diagnosis Model for Early Warnings in Electrical Transformers
# SRC

## Environment Configuration
### System Requirements
```
- Python 3.12.0
- Bookstores: sys, os, numpy, matplotlib, seaborn, pandas, math, time, scipy, sklearn
```

This directory contains all the Python source codes used for fault diagnosis in electrical transformers.

## File Description
- `Main.py and MainPandas.py`: Main script that coordinates data preprocessing, model training and result generation.
- `Analysis.py`: Functions for data analysis, main scripts, statistical models, main calculations.
- `Preprocessing.py`: Functions for data preprocessing, cleaning, transforming and preparing data.
- `Visualization.py` : Functions for displaying the data and results obtained from the scripts.
  
### Installation of Dependencies
To clone and run the contents of the Fault Diagnosis Model for Early Warnings in Electrical Transformers repository, you can follow the following steps. This includes cloning the repository, creating a virtual environment (to ensure that dependencies do not conflict with other projects), and installing the necessary dependencies.

**1. Clone the repository:**
Open a terminal or command line and run the following command to clone the repository:
```bash
git clone https://github.com/SantiagoGuzmanA/Fault-diagnosis-model-for-early-warnings-in-electrical-transformers.git
```

**2. Navigate to the project directory:**
Change to the project directory:
```bash
cd Fault-diagnosis-model-for-early-warnings-in-electrical-transformers
```

**3. Create a virtual environment:**
To ensure that dependencies are installed in an isolated environment, create a virtual environment:
```bash
python3 -m venv env
```

**4. Activate the virtual environment:**
```bash
.\env\Scripts\activate
```

5. Install dependencies:
Make sure that the requirements.txt file is located in the path Fault diagnosis model for early warnings in electrical transformers and contains the following lines:
```bash
sys
os
numpy
matplotlib
seaborn
pandas
scipy
sklearn
```
Then, install the dependencies using pip:
```bash
pip install -r "Fault diagnosis model for early warnings in electrical transformers/requirements.txt"
```

6. Run the project:
Once the dependencies are installed, you can run the main project script. It is the main input file to run the Main.py and MainPandas.py project. run:
```bash
python Main.py
python MainPandas.py
```
