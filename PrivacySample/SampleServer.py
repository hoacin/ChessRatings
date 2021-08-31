import json
import phe as paillier

#Initializing Moves Predictor and storing coefs
import sys
from phe.paillier import EncryptedNumber
sys.path.append('')
from AI.MovesPredictor import MovesPredictor
mp=MovesPredictor()
coefs = mp.getCoef()
intercept = float(mp.getIntercept())


#Normally this would come from REST API call, but we just load the sample JSON file
def getDataFromUser():
    data=getDataFromFile()
    keydata=data['public_key']
    publicKey = paillier.PaillierPublicKey(n=int(keydata['n']))
    enc_nums_rec = [paillier.EncryptedNumber(publicKey,int(x[0],int(x[1]))) for x in data['values']]
    result = sum([coefs[i]*enc_nums_rec[i] for i in range(3)])
    result += intercept
    return  result, publicKey


def getDataFromFile():
    with open('PrivacySample/SampleOutputFiles/DataForServer.json', 'r') as file:
        d=json.load(file)
        return json.loads(d)

#Step 3
def serializeData():
    result, publicKey = getDataFromUser()
    encrypted_data = {}
    encrypted_data['public_key'] = {'n': publicKey.n}
    encrypted_data['values'] = (str(result.ciphertext()),result.exponent)
    serialized = json.dumps(encrypted_data)
    with open('PrivacySample/SampleOutputFiles/AnswerFromServer.json', 'w') as file:
        json.dump(serialized,file)
    
serializeData() # - Step 3, remaining steps are in SampleClient.py!



