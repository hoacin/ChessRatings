from os import linesep
import phe as paillier
import json

def loadKeys():
    with open('PrivacySample/SampleOutputFiles/ClientKeyPair.json', 'r') as file:
        keys=json.load(file)
        public_key=paillier.PaillierPublicKey(n=int(keys['public_key']['n']))
        private_key = paillier.PaillierPrivateKey(public_key,keys['private_key']['p'],keys['private_key']['q'])
        return public_key, private_key
    
def serializeData(public_key, data):
    encrypted_data_list = [public_key.encrypt(x) for x in data]
    encrypted_data = {}
    encrypted_data['public_key'] = {'n':public_key.n}
    encrypted_data['values']=[(str(x.ciphertext()),x.exponent) for x in encrypted_data_list]
    #We are sending public key and encrypted values
    serialized = json.dumps(encrypted_data)
    return serialized

#step number 1 - initialization
def generateAndStoreKeyPair():
    #Storing private key would probably not by in public place in production ;)
    public_key, private_key = paillier.generate_paillier_keypair()
    keys={}
    keys['public_key']={'n': public_key.n}
    keys['private_key'] = {'p': private_key.p, 'q': private_key.q}
    with open('PrivacySample/SampleOutputFiles/ClientKeyPair.json', 'w') as file:
        json.dump(keys,file)

#step number 2 - asking the server
def askServer():
    publickey, privatekey = loadKeys()
    white = int(input("Enter white rating: "))
    black = int(input("Enter black rating: "))
    year = int(input("Enter game year: "))
    data = [white,black,year]
    serialized = serializeData(publickey,data)
    with open('PrivacySample/SampleOutputFiles/DataForServer.json', 'w') as file:
        json.dump(serialized,file)

#step number 4 - reading response
def readAnswer():
    #This json would normally come as a be response from REST API
    with open('PrivacySample/SampleOutputFiles/AnswerFromServer.json', 'r') as file:
        serialized=json.load(file)
        answer_json = json.loads(serialized)
        answer_key = paillier.PaillierPublicKey(n=int(answer_json['public_key']['n']))
        answer = paillier.EncryptedNumber(answer_key,int(answer_json['values'][0]),int(answer_json['values'][1]))
        publickey, privatekey = loadKeys()
        if (publickey == answer_key):
            decryptedAnswer = privatekey.decrypt(answer)
            print('******************************')
            print(f'Decrypted answer: {decryptedAnswer}')
            print('******************************')

#generateAndStoreKeyPair() # - Step 1
#askServer() # - Step 2
#Step 3 takes place in SampleServer.py!
readAnswer() # - Step 4


