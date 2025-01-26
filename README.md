# Reorder PDF
Transpose, zip, interlace groups of multipage pdf files

Currently can only do Transpose. Number of pages per file must be equal. 

To use: 
- git clone https://github.com/jensdanb/reorder_pdf 
- Install python. 
- Check that it works and the version you have. 
- Make a Python Virtual Environment (google a guide) in the project folder. 
- Inside the project folder, install pypdf with command "pip install pypdf". 
- If using conda or other in-house python manager, use your manager to get pypdf. 
- Make a folder in the project, in same folder as "main.py", named "input", and one named "output". 
- Copy the pdf files you want to reorder into the input folder.
- Open the project directory in your command line and run "python3 main.py" or "python main.py"
- If no error messages, you will find your output files in the output folder. 
