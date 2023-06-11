from google.cloud import kms_v1

def get_crypto_key(crypto_key_name):
    client = kms_v1.KeyManagementServiceClient()

    # request = kms_v1.GetCryptoKeyRequest(
    #     name=crypto_key_name,
    # )
    # response = client.get_crypto_key(request=request)

    response = client.get_crypto_key(name=crypto_key_name)
    if response:
        if(response.rotation_period.days >= 90):
            print("Key rotation period is good.")

def main():
    crypto_key_name = "projects/UPDATE_ME/locations/UPDATE_ME/keyRings/UPDATE_ME/cryptoKeys/UPDATE_ME"
    get_crypto_key(crypto_key_name)

# Executing as standalone script 
if __name__ == "__main__":
    main()