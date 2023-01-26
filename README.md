# bookmachine
## Steps to run
1. Install python3
2. Create a virtual Environment and install the requirements
    >python -m venv .venv

    >.\\.venv\Scripts\Activate.ps1   
    
    >PIP install -r .\requirements.txt

    If you're having issues with your packages, enter the virtual env and run:

    > pip freeze | xargs pip uninstall -y

    > pip install --force-reinstall --no-cache-dir  -r .\requirements.txt

3. Create a file called .env and populate it with your API Key.
    > NAI_USERNAME="ASDFASDFASDFASDFASDF"
    > NAI_PASSWORD="ASDFASDFASDFASDFASDF"

4. Edit the promts & defaults on Story Generator.py and run