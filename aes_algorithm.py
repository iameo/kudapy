import hashlib
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def aes_encrypt(data, password):
    data = bytes(data, 'UTF-8')
    password = bytes(password, 'UTF-8')
    derived_key = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=32)
    iv = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=16)
    cipher = AES.new(derived_key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    #iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    #result = json.dumps({'iv':iv, 'ciphertext':ct})
    return ct



# encrypted_payload = aes_encrypt(data, password)
# print(encrypted_payload)



def aes_decrypt(encrypted_data, password):
    try:
        #b64 = json.loads(encrypted_data)
        #password = bytes(password, 'utf-8')
        #iv = b64decode(b64['iv'])
        #ct = b64decode(b64['ciphertext'])
        encrypted_data = bytes(encrypted_data, "utf-8")
        derived_key = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=32)
        iv = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=16)
        cipher = AES.new(derived_key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return pt
        #print("The message was: ", pt)
    except (ValueError, KeyError):
        print("Incorrect decryption")


# decrypted_payload = aes_decrypt(encrypted_payload, password)
# print(decrypted_payload)