#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import rsa
import json


def create_keys():
    # 生成公钥和私钥
    (pubkey, privkey) = rsa.newkeys(1024)
    pub = pubkey.save_pkcs1()
    print('生成公钥:' + str(pub))
    with open('public.pem', 'wb+')as f:
        f.write(pub)

    pri = privkey.save_pkcs1()
    print('生成私钥:' + str(pri))
    with open('private.pem', 'wb+')as f:
        f.write(pri)

def encrypt(content: str):
    # 用公钥加密
    print("原始内容: %s" % content)
    with open('public.pem', 'rb') as f:
        p = f.read()
    public_key = rsa.PublicKey.load_pkcs1(p)
    original_content = content.encode('utf8')
    crypt_content = rsa.encrypt(original_content, public_key)
    print("加密后的内容: %s" % crypt_content)
    return crypt_content


def decrypt(crypt_content):
    # 用私钥解密
    with open('private.pem', 'rb') as f:
        p = f.read()
    private_key = rsa.PrivateKey.load_pkcs1(p)
    original_content = rsa.decrypt(crypt_content, private_key).decode()

    print(original_content)


if __name__ == '__main__':
    create_keys()
    url = encrypt(json.dumps({"username": "wangchao104"}))
    decrypt(url)
