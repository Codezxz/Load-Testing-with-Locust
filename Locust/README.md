# Locust-Load-Testing

Installation Instructions

Create a 'Virtual Environment' with 'venv' :

    python -m venv env

Activate your 'Virtual Environment' :

    Linux   : Source ./env/bin/activate

    Windows : env\Scripts\activate

Clone this Repository :

    'git clone https://github.com/Urbano-InfoTech/Locust-Load-Testing.git'

Install the dependencies :

    pip install -r requirements.txt

Navigate to the Folder containing the code :

    cd locustLoadTest/

Run the code (In seperate terminals):

    flask --app testApp.py run => 
    locust -f tesLocust.py =>
     
About : 
    
    This is a 'Load Testing' Framework that uses 'Locust Framework' and 'Flask'.
