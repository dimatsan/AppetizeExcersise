# AppetizeExcersise


## Pre-conditions
1. Python 3 installed
2. Geolocation tracking permission allowed for https://the-internet.herokuapp.com/ in browser settings (for more info see misc details)


## Framework set up
1. Open CMD console (or any other preferred terminal) as administrator
2. Navigate to the empty testing project folder (or create one)
3. Extract files from GitHub into newly created project folder (should be 3 objects - "tests" folder, "page_objects" folder and requirements.txt
3. While in folder, run "python -m venv env" to create a new virtual environment setup
4. Run "call env/Scripts/activate" to activate virtual environment
5. Run "python -m pip install -r requirements.txt" to install necessary modules (the only module used for this project is SeleniumBase)
6. Run "sbase install chromedriver latest" to install driver
7. Run "pytest -s" to run the test suite with print out to console. (see appendix for additional options)

## Misc details

### Author's software configuration
Project was completed using Python v3.10 with SeleniumBase framework.

OS: Windows 10

Text editor: PyCharm 2020.3.3

### Additional framework features
- run tests with -s attribute to print in console
- add -n=num attribute for several instances
- add --headless attribute to run without browser window
- for quick report add --dashboard attribute and open generated dashboard.HTML file
- for detailed report add --html=report.html and open generated report.HTML file
- to run tests on different browsers add --browser=browser_name attribute (i.e. --browser=firefox).
- to run specific test suite add -k "test_suite_name";

In Geolocation test - I have added a small extra step that takes your coordinates and returns the actual location. Just for fun =) Can be easily removed if needed.
Regarding geolocation permission: I have attampted to include giving a permission to track location into the automation, but it seemed to be a quite complicated and complex piece of work, different for each browser, which makes giving this permission manually one time before running the automation much more reasonable and efficient, since this is an action you need to perform only once per each browser. If you think it would make more sense to include this step into an automation - I would appreciate your guidence on how to do it. 
