import base64
from Crypto.Cipher import AES
from urllib import parse

AES_SECRET_KEY = 'helloBrook2abcde'  # 此处16|24|32个字符
IV = 'helloBrook2abcde' 

# padding算法
BS = len(AES_SECRET_KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]


class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_ECB

    # 加密函数
    def encrypt(self, text):
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
        # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(self.ciphertext).decode("utf-8")

    # 解密函数
    def decrypt(self, text):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        plain_text = cryptor.decrypt(decode)
        return unpad(plain_text).decode("utf-8")


if __name__ == '__main__':
    aes_encrypt = AES_ENCRYPT()
    text = "Python"
    e = aes_encrypt.encrypt(text)
    d = aes_encrypt.decrypt(e)
    print(text)
    print(e)
    print(d)


    req = {
    "e": {
        "uri": "/person/initMultiUpload",
        "data": {
            "parentFolderId": "11463310842361563",
            "fileName": "conf.xml",
            "fileSize": 369,
            "sliceSize": 10485760,
            "fileMd5": "bfb07d9b177e301db54230699a735f15",
            "sliceMd5": "bfb07d9b177e301db54230699a735f15"
        },
        "rsaKey": {
            "success": True,
            "res_code": 0,
            "res_message": "成功",
            "expire": 1664611939159,
            "pkId": "6ac78d11ffc249eca6d88b3255674f4f",
            "pubKey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCTKNFGKCgarBLFsr+/zKh+7U3dfgqkKoVixyVcTF7QS1fSoUueN0FCaroQN60AVupLa33Wi69uMYDF8KD492c16ta+etsHWkyEaoEJf+CRrQ6jMeolWWmTf9PNHCAIowQExrKlc/wL7wMcDs1QNsQs1C7TwEp44xnYmfTBTeTG/wIDAQAB",
            "ver": "2"
        }
    },
    "t": "98836244-5478-4b77-9266-9a40006c5876",
    "r": "61e214f6-40a1-4570-8a78-2eb64215f128",
    "l": "061cecfd897548208c76c04b6e7fb",
    "c": 1664601588762,
    "d": "GET",
    "u": [
        "parentFolderId=11463310842361563",
        "fileName=conf.xml",
        "fileSize=369",
        "sliceSize=10485760",
        "fileMd5=bfb07d9b177e301db54230699a735f15",
        "sliceMd5=bfb07d9b177e301db54230699a735f15"
    ],
    "f": "parentFolderId=11463310842361563&fileName=conf.xml&fileSize=369&sliceSize=10485760&fileMd5=bfb07d9b177e301db54230699a735f15&sliceMd5=bfb07d9b177e301db54230699a735f15",
    "p": {
        "words": [
            808857955,
            1701013092,
            943273781,
            876098096
        ],
        "sigBytes": 16
    },
    "h": "008a3fec222a4b408fec574c42b71548735e1829ceaee18b25b25cd4286dc964220220351a5fefe9f3a5dd46d7f33db79b2ad142fbe4019f0a5c2f7e414f8c521311b55aa81007eca991de7ae2b09e635917e20ccb76a7293184f08039c4d5fac0155923647e57aeb97de6b6d500111593aad7f280c370c013f55ae309e1f39cf07c954d0114db8039df9437d8a4d00a5c8c7b8bf3eacb5abc76521d2e8cef5387dc636fd1bd9528833d22743b21b45a",
    "m": {
        "SessionKey": "98836244-5478-4b77-9266-9a40006c5876",
        "Operate": "GET",
        "RequestURI": "/person/initMultiUpload",
        "Date": 1664601588762,
        "params": "008a3fec222a4b408fec574c42b71548735e1829ceaee18b25b25cd4286dc964220220351a5fefe9f3a5dd46d7f33db79b2ad142fbe4019f0a5c2f7e414f8c521311b55aa81007eca991de7ae2b09e635917e20ccb76a7293184f08039c4d5fac0155923647e57aeb97de6b6d500111593aad7f280c370c013f55ae309e1f39cf07c954d0114db8039df9437d8a4d00a5c8c7b8bf3eacb5abc76521d2e8cef5387dc636fd1bd9528833d22743b21b45a"
    },
    "A": [
        "SessionKey=98836244-5478-4b77-9266-9a40006c5876",
        "Operate=GET",
        "RequestURI=/person/initMultiUpload",
        "Date=1664601588762",
        "params=008a3fec222a4b408fec574c42b71548735e1829ceaee18b25b25cd4286dc964220220351a5fefe9f3a5dd46d7f33db79b2ad142fbe4019f0a5c2f7e414f8c521311b55aa81007eca991de7ae2b09e635917e20ccb76a7293184f08039c4d5fac0155923647e57aeb97de6b6d500111593aad7f280c370c013f55ae309e1f39cf07c954d0114db8039df9437d8a4d00a5c8c7b8bf3eacb5abc76521d2e8cef5387dc636fd1bd9528833d22743b21b45a"
    ],
    "v": "SessionKey=98836244-5478-4b77-9266-9a40006c5876&Operate=GET&RequestURI=/person/initMultiUpload&Date=1664601588762&params=008a3fec222a4b408fec574c42b71548735e1829ceaee18b25b25cd4286dc964220220351a5fefe9f3a5dd46d7f33db79b2ad142fbe4019f0a5c2f7e414f8c521311b55aa81007eca991de7ae2b09e635917e20ccb76a7293184f08039c4d5fac0155923647e57aeb97de6b6d500111593aad7f280c370c013f55ae309e1f39cf07c954d0114db8039df9437d8a4d00a5c8c7b8bf3eacb5abc76521d2e8cef5387dc636fd1bd9528833d22743b21b45a",
    "g": "4cc33b15f9701c9991f20784351056c69233ecd4",
    "y": {
        "default_key_size": 1024,
        "default_public_exponent": "010001",
        "log": False,
        "key": {
            "n": {
                "0": 233096959,
                "1": 161434644,
                "2": 149101016,
                "3": 222037159,
                "4": 70046766,
                "5": 215286636,
                "6": 251862030,
                "7": 121618622,
                "8": 80130725,
                "9": 9056320,
                "10": 63773728,
                "11": 110704637,
                "12": 32122201,
                "13": 181463603,
                "14": 159375505,
                "15": 138848272,
                "16": 185031244,
                "17": 225175469,
                "18": 124204522,
                "19": 252317583,
                "20": 238125253,
                "21": 224967414,
                "22": 172714877,
                "23": 181405038,
                "24": 179966007,
                "25": 57938982,
                "26": 44125086,
                "27": 218412413,
                "28": 89934942,
                "29": 139865202,
                "30": 235578410,
                "31": 248831447,
                "32": 265070718,
                "33": 207301627,
                "34": 135965714,
                "35": 219439746,
                "36": 37672,
                "t": 37,
                "s": 0
            },
            "e": 65537,
            "d": None,
            "p": None,
            "q": None,
            "dmp1": None,
            "dmq1": None,
            "coeff": None
        }
    },
    "b": "B4gZua3/0IyDjSX9SzxHYR5cufycf/yyHWZOB7rq1QFIuexT144cMKrrGOSyJklUjk/MXCMJWE+jxyhRWUrcgIRWo7B0sjw3YryAAjvFM2V9otTYEIIgAvzvAL+PhNgl7RA0R+SN0f0AI8DI7oMAPxl2wghj1+bW8GVZrb1/eec=",
    "w": {}
}