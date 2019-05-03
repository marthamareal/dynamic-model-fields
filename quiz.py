from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABczE3LVIIT3t-j_MXB-28_j2td3_1LmEvH9lqn3Ui-ONJI_a8OkKmqChZM0Ad3Mdp9rLMeHtk6OeCfybQp3GMvLUxRTz8MZYyQT4RALArmo0GXiORIzjNJV7ZbzjqgvMFTMDVLuBMTIuX96tXSj6NnhMwDTnx--LAZn5g-ZSMJstU23FY='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
    