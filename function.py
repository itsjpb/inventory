import json
import urllib3 # type: ignore

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    r = http.request('POST', 'https://api.trello.com/1/cards?key=cf4871448e422d8b29372e4438d740cb&token=ATTAffa001e5ab0d1b20f40abe41c25dabb69ed12f876957fa5cf000f44983a472de23E6A847&name=new cards&idList=6533174897737ec8f0849068&desc=https://www.amazon.com/Datacard-isopropanol-cleaning-534000-003-AlphaCard/dp/B01MF72GJS')
    
    r.data
    
    # b'User-agent: *\nDisallow: /deny\n'
    return 'hello from lambda'
