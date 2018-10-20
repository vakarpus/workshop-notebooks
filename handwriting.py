import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json
import key, sys
# Replace the subscription_key string value in key.py file with your valid subscription key.

# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

requestHeaders = {
    # Request headers.
    # Another valid content type is "application/octet-stream".
    'Content-Type': 'application/json',
    #'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': key.subscription_key,
}

# The URL of a JPEG image containing handwritten text.
body = {'url' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Cursive_Writing_on_Notebook_paper.jpg/800px-Cursive_Writing_on_Notebook_paper.jpg'}
#body = open(sys.argv[1], 'rb').read()
# For printed text, set "handwriting" to false.
params = {'handwriting' : 'true'}

try:
    # This operation requrires two REST API calls. One to submit the image for processing,
    # the other to retrieve the text found in the image. 
    #
    # This executes the first REST API call and gets the response.
    response = requests.request('POST', uri_base + '/vision/v1.0/RecognizeText', json=body, data=None, headers=requestHeaders, params=params)

    # Success is indicated by a status of 202.
    if response.status_code != 202:
        # if the first REST API call was not successful, display JSON data and exit.
        parsed = json.loads(response.text)
        print ("Error:")
        print (json.dumps(parsed, sort_keys=True, indent=2))
        exit()

    # The 'Operation-Location' in the response contains the URI to retrieve the recognized text.
    operationLocation = response.headers['Operation-Location']

    # Note: The response may not be immediately available. Handwriting recognition is an
    # async operation that can take a variable amount of time depending on the length
    # of the text you want to recognize. You may need to wait or retry this GET operation.

    print('\nHandwritten text submitted. Waiting 2 seconds to retrieve the recognized text.\n')
    time.sleep(2)

    # Execute the second REST API call and get the response.
    response = requests.request('GET', operationLocation, json=None, data=None, headers=requestHeaders, params=None)

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(response.text)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))

except Exception as e:
    print('Error:')
    print(e)

# ####################################
# ########### Python 2.7 #############
# import httplib, urllib, base64, time, json, sys
# import key
# ###############################################
# #### Update or verify the following values. ###
# ###############################################
# 
# # Replace the subscription_key string value with your valid subscription key.
# 
# # Replace or verify the region.
# #
# # You must use the same region in your REST API call as you used to obtain your subscription keys.
# # For example, if you obtained your subscription keys from the westus region, replace 
# # "westcentralus" in the URI below with "westus".
# #
# # NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# # a free trial subscription key, you should not need to change this region.
# uri_base = 'westcentralus.api.cognitive.microsoft.com'
# 
# headers = {
#     # Request headers.
#     # Another valid content type is "application/octet-stream".
#     #'Content-Type': 'application/json',
#     'Content-Type': 'application/octet-stream',
#     'Ocp-Apim-Subscription-Key': key.subscription_key,
# }
# 
# # The URL of a JPEG image containing handwritten text.
# #body = "{'url':'https://dl.dropboxusercontent.com/s/oln6ijsu5vz4ach/2017-08-03%2015.24.35.jpg'}"
# body = open(sys.argv[1], 'rb').read()
# 
# # For printed text, set "handwriting" to false.
# params = urllib.urlencode({'handwriting' : 'true'})
# 
# try:
#     # This operation requrires two REST API calls. One to submit the image for processing,
#     # the other to retrieve the text found in the image. 
#     #
#     # This executes the first REST API call and gets the response.
#     conn = httplib.HTTPSConnection(uri_base)
#     conn.request("POST", "/vision/v1.0/RecognizeText?%s" % params, body, headers)
#     response = conn.getresponse()
# 
#     # Success is indicated by a status of 202.
#     if response.status != 202:
#         # Display JSON data and exit if the first REST API call was not successful.
#         parsed = json.loads(response.read())
#         print ("Error:")
#         print (json.dumps(parsed, sort_keys=True, indent=2))
#         conn.close()
#         exit()
# 
#     # The 'Operation-Location' in the response contains the URI to retrieve the recognized text.
#     operationLocation = response.getheader('Operation-Location')
#     parsedLocation = operationLocation.split(uri_base)
#     answerURL = parsedLocation[1]
# 
#     # NOTE: The response may not be immediately available. Handwriting recognition is an
#     # async operation that can take a variable amount of time depending on the length
#     # of the text you want to recognize. You may need to wait or retry this GET operation.
# 
#     print('\nHandwritten text submitted. Waiting 2 seconds to retrieve the recognized text.\n')
#     time.sleep(2)
# 
#     # Execute the second REST API call and get the response.
#     conn = httplib.HTTPSConnection(uri_base)
#     conn.request("GET", answerURL, '', headers)
#     response = conn.getresponse()
#     data = response.read()
# 
#     # 'data' contains the JSON data. The following formats the JSON data for display.
#     parsed = json.loads(data)
#     print (json.dumps(parsed, sort_keys=True, indent=2))
#     conn.close()
# 
# except Exception as e:
#     print('Error:')
#     print(e)
# 
# ####################################

