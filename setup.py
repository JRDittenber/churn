from setuptools import setup, find_packages


req_file = 'requirements.txt'

def get_rq(file_path): 
    """This function will open the requirments.txt file, read it, remove
    the newline character ('\n') and pass it to the 
    install_requires() funtion in setup()      
    """
    with open(file_path) as file_obj: 
        reqs = file_obj.read().splitlines()
        return reqs
    
setup(
    
    name = 'Customer Churn Analysis',
    
    version = '0.1.0',
    
    author = 'J. Dittenber',
    
    author_email= 'jeff.dittenber@hotmail.com',
    
    description= 'This project will automate the analysis, model generation/deployment and monitoring of Customer Churn Data',
    
    packages=find_packages(),
    
    include_package_data=True, 
    
    python_requires = ">=3.8",
    
    install_requires = get_rq(req_file)    
    
       
    
)

