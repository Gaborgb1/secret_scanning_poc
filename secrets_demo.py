# secrets_demo.py

import os

def main():
    # Fake AWS credentials
    AWS_ACCESS_KEY_ID = 'ASDWF@FSDFSEXAMPLE'
    AWS_SECRET_ACCESS_KEY = 'w2JalrXUtSnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'

    # Fake private SSH key
    PRIVATE_SSH_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowsBAAKCAQEA3PvDw7ANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUdaf2BAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJbmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2FwaTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbYIBADANBgkqhkiG9w0BAQEFAASCAQAWMsNkt2z73yZGeEi+0LmDiM...
-----END RSA PRIVATE KEY-----
"""

    # Fake database connection string
    DB_CONNECTION_STRING = 'postgres://username:password@localhost:5432/mydatabase'

    # Fake API token
    API_TOKEN = '7e5dc5d63b2e40d6b5aa2eef327e0328'

    print("Demo function for testing GitHub secret scanning")

if __name__ == "__main__":
    main()
