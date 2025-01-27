# Reorder PDF
Transpose, zip, interlace groups of multipage pdf files

Currently can only do Transpose. Number of pages per file must be equal. 

Dependencies: 
- PyPdf. Source: https://pypi.org/project/pypdf/

To use: 
- git clone this address, or make a new folder and copy main.py into it.  
- Install a recent version of Python. 
- Make a Python Virtual Environment ("venv" - google a guide) in the project folder (the one where main.py is). 
- Inside the project folder, activate the venv and install pypdf with command "pip install pypdf". 
- If using conda or other in-house python manager, use your manager to get pypdf. 
- Make a folder named "input", and one named "output". They must be in same folder as main.py
- Copy the pdf files you want to reorder into the input folder.
- Run main.py. 
- If no error messages, you will find your output files in the output folder. 
