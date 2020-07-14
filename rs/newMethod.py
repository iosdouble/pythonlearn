# -*- coding: utf-8 -*-
"""
RSA加解密
"""
import base64
from M2Crypto import BIO, RSA

with open("public_key.pem", 'r') as f:
    pubkey = f.read()
with open("private_key.pem", 'r') as f:
    prikey = f.read()

# 加密
text = "ABCDEF".encode('utf-8')  # 明文
pub_bio = BIO.MemoryBuffer(pubkey.encode('utf-8'))  # 公钥字符串
pub_rsa = RSA.load_pub_key_bio(pub_bio)  # 加载公钥
secret = pub_rsa.public_encrypt(text, RSA.pkcs1_padding)  # 公钥加密
sign = base64.b64encode(secret)  # 密文base64编码
print(sign)

# 解密
b64_sign = "uhBqhevT0E5+WT++HX+pGzSy7YGskBQODuvoV+hf0k8cSyXG/GuAT4LKYaCiT9qiEGlbWxCIH51Qt1s0y2X56TbNja93AbzXiFWzsC2H6vwo3ZFcoj+YqUBsax+Gad0I6NME9lalpKsPtWqi4W/b3VbG5Mx+WBJ+L17GR7ZvWMo="  # base64密文
cipher = base64.b64decode(b64_sign)  # base64解码
pri_bio = BIO.MemoryBuffer(prikey.encode('utf-8'))  # 加载私钥
pri_rsa = RSA.load_key_bio(pri_bio)
plain = pri_rsa.private_decrypt(cipher, RSA.pkcs1_padding)  # 解密
print(plain.decode('utf-8'))

