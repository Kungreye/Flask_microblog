import json
import requests
from flask_babel import _
from app import app


# In Microsoft Translator Text API V3, all data sent and received using the API is in JSON format. 
# XML will no longer be accepted or returned in V3.

def translate(text, source_language, dest_language):
    
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    
    URL = 'https://api.cognitive.microsofttranslator.com/translate'
    params = {'api-version': '3.0',
             'from': '{}'.format(source_language),
              'to': '{}'.format(dest_language)}
    requestBody = [{'Text': text}]  # dict format
    headers = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Content-Type': 'application/json'
        }

    # requests.post(url, params=params, data=json.dumps(data), headers=headers) 
    # r is JSON array in Azure v3.0 (unlike in v2.0 where we can directly get the translated result).
    r = requests.post(URL,
        params = params, 
        data = json.dumps(requestBody, ensure_ascii=False).encode('utf-8'),
        headers = headers)
    
    # requests uses dict to send form-encode data like HTML form.
    # When send data that is not form-encoded, pass in a JSON str instead of a dict.
    # That data in JSON str will be posted directly.    



    if r.status_code != 200:
        return _('Error: the translation service faild.')
    

    #print("r.content.decode('utf-8-sig')= ", r.content.decode('utf-8-sig'))
    #print("json.loads(r.content.decode('utf-8-sig'))= ",json.loads(r.content.decode('utf-8-sig')))
    return json.loads(r.content.decode('utf-8-sig'))[0]['translations'][0]['text']


# For text: 'Jon seems to be brooding recently. But that is understandible.'
# Translated text is included in the returned JSON Array:

#   r.content.decode('utf-8-sig')=  [{"translations":[{"text":"乔恩最近似乎在沉思。但那是 understandible。","to":"zh-Hans"}]}]
#   json.loads(r.content.decode('utf-8-sig'))=  [{'translations': [{'text': '乔恩最近似乎在沉思。但那是 understandible。', 'to': 'zh-Hans'}]}]

# To obtain translated text exclusively, we suffix it with " ..[0]['translations'][0]['text']   ".
# So, in routes.py, manually create the single dict {'text': translate('~')},
# to correspond to reponse['text'] in the base.html <script>function translate()</script>. 


'''
    r.content, as a bytes object, contains the raw body of the response.
    It is first converted to UTF-8 JSON string. (MS use utf-8 with ByteOrderMark, so utf-8-sig)
    Then the UTF-8 JSON string is sent to json.loads, and decoded from JSON str into Python str.
    Finally, the Python str is returned to the caller.
'''





'''
# Miguel's based on Microsoft Translator Text API V2.

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    
    #print("r.content.decode('utf-8-sig')= ", r.content.decode('utf-8-sig'))
    #print("json.loads(r.content.decode('utf-8-sig'))= ",json.loads(r.content.decode('utf-8-sig')))
    return json.loads(r.content.decode('utf-8-sig'))


#   For text: 'Jon seems to be brooding recently. But that is understandible.'
#   In this func & api_version, the translated text is directly returned:

#   r.content.decode('utf-8-sig')=  "乔恩最近似乎在沉思。但那是 understandible。"
#   json.loads(r.content.decode('utf-8-sig'))=  乔恩最近似乎在沉思。但那是 understandible。

#   So, in routes.py, manually create the single dict {'text': translate('~')},
#   to correspond to reponse['text'] in the base.html <script>function translate()</script>.

'''