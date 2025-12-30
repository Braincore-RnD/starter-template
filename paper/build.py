import subprocess
import os
import sys
import platform

def run_command(command):
    print(f"Running: {' '.join(command)}")
    try:
        # On Windows, shell=True is sometimes required for commands to be found if they are not .exe
        use_shell = platform.system() == "Windows"
        subprocess.check_call(command, shell=use_shell)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {' '.join(command)}")
        print("Continuing sequence (step might be optional or non-fatal if no citations)...")
        # We don't exit here immediately to allow full cycle, 
        # but for pdflatex errors it usually stops.
        # For bibtex with empty refs, it might error but we re-run pdflatex anyway.

import time

def check_pdf_lock(filename):
    """
    Checks if the PDF file is locked by another process.
    Loops until the file is released.
    """
    pdf_file = f"{filename}.pdf"
    if not os.path.exists(pdf_file):
        return

    print(f"Checking if {pdf_file} is writable...")
    while True:
        try:
            # Try to rename the file to itself to check for exclusive access
            # Or simply try to open it in append mode
            with open(pdf_file, 'a+'):
                pass
            break
        except PermissionError:
            print(f"!! {pdf_file} is currently open in another application.")
            print("   Please close the PDF viewer to continue...")
            time.sleep(2)
        except Exception as e:
            print(f"Unexpected error checking file lock: {e}")
            break

def main():
    # Ensure we are in the directory of the script (the paper directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    filename = "main"
    
    # Check if PDF is locked before starting
    check_pdf_lock(filename)
    
    # Standard LaTeX build sequence
    # 1. pdflatex (initial run)
    # 2. bibtex (process references)
    # 3. pdflatex (apply references)
    # 4. pdflatex (resolve cross-references)
    
    commands = [
        ["pdflatex", "-interaction=nonstopmode", f"{filename}.tex"],
        ["bibtex", filename],
        ["pdflatex", "-interaction=nonstopmode", f"{filename}.tex"],
        ["pdflatex", "-interaction=nonstopmode", f"{filename}.tex"]
    ]
    
    print(f"Starting compilation for {filename}.tex on {platform.system()}...")
    
    for cmd in commands:
        try:
            run_command(cmd)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    print(f"\nBuild finished! Check {filename}.pdf")

if __name__ == "__main__":
    main()
