import json
import urllib3

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    r = http.request('POST', 'https://api.trello.com/1/cards?key=key&token=token&name=new cards&idList=6533174897737ec8f0849068&desc=https://www.amazon.com/Datacard-isopropanol-cleaning-534000-003-AlphaCard/dp/B01MF72GJS')
    

    longinformation = '''
        <center>
        <html style="background-color: #353A58;">
        <div style="top: 35%; left: 50%; transform: translate(-50%, -50%); position: absolute; z-index: 8; align-items: center; justify-content: center; display: flex !important; flex-direction: column !important;">
        <h1 style="width: 500px; font-size: 60px; margin-top: 100px; background-color: black; color: #AFFAD1; padding: 19px; border: 10px; border-radius: 15px;">DLH Inventory</h1>
        <img src="https://i.ibb.co/pfrFkcP/dlh.png" alt="DLH logo" style="width: auto; max-height: 400px;">
        <h1 style="background-color: black; color: #AFFAD1; padding: 13px; border-radius: 15px;">You have succesfully added ink cards to the Amazon ordering list!</h1>
        </div>
        </html>
        </center>
        '''

    return {
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'}, 
        "body": longinformation
    }
