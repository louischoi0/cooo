import requests

cookies = {
    'sid': 'd9e3fb3848994d29b2d2baf3a4094ed02b668caf',
    'PCID': '5525748675932096357655',
    'MARKETID': '5525748675932096357655',
    'x-coupang-accept-language': 'ko-KR',
    'x-coupang-target-market': 'KR',
    '_abck': '24AD795AABB66727F0742C089BC8584F~-1~YAAQxnXTF/+YBTaOAQAAEZugPAuQwCzZQta6IIIhYbvs4F48zTbdtDf2bAPyjsW4nnLY8xqd7JmOJcuERDMw2X1/ckmy35Q5Azxi6aTFQcIWW96X7qQajS6Civ2IY4qcRGSfdYQJSt52QQjpXdpqf8V+Ia/n315oDtpRubPoBCPYVirBfRJ5v0BP3vfdbQeofzEVqVKhg87dGpL5cBzTOpy5IV1Pn64aHS73iCqaFbJXj7jXKhMD93uy13Coylr3/gGnA4pWSr62o2AxFML3aVB+bAov0G2uRFxC6WmZTSv50vIKSCoJGNSQ5RjZljDkaiOjorbBHYtCCjGbh8nR+aRl4Mb3pGFURtTu6hl3vg2gPEFfRUrweAashuYHGkHKBnnv9565iSJG3uUpKJNQGoQe5vOY9IGuQnSfpLeBDUdNBC8k0lOzzW4=~-1~-1~-1',
    'cto_bundle': 'P1itH19jV2dvSkpTTExXcWhPbkR4clZYUmlPb2ZZY21lVVd1YnZJOW1XUnlvZkZkNE45ZHE1WE5xZSUyQiUyRk9DVEFBaGtlc3F4TXZwQUxZeHBqJTJGNjRGaGoycVZaZmVlREd2JTJCTWlWMHZuMyUyRnFKN3MzVXQzc3hHZXQ0ZkRJVSUyQiUyQmpwT0tYTmpSMk0lMkZhSXZGOCUyQnFGSzVoQWdnZllGaFNKT29lcENkJTJGdU4yakNLMHcxaEVIMkxzWEpPUSUyQlRmSjJKTk1ScUI0TzFS',
    'searchKeyword': '%EC%9E%A5%EC%96%B4',
    'searchKeywordType': '%7B%22%EC%9E%A5%EC%96%B4%22%3A0%7D',
    '_fbp': 'fb.1.1710153051358.230784221',
    'trac_src': '1042016',
    'trac_spec': '10304903',
    'trac_addtag': '900',
    'trac_ctag': 'HOME',
    'trac_lptag': '%EC%BF%A0%ED%8C%A1',
    'trac_itime': '20240314200208',
    'bm_sz': 'F81C75E501F205198F5C721FC31BAAEC~YAAQxnXTF56LBTaOAQAAcmqgPBddwSKV4uJyxsAdwoMM/93aty1CoQU3TiOn93UO4qo8i0iOBn8SG+tLECERt0aVHmMaNQme6X9pNxs27scfQMMdvzXbr6xAltTfkB959liAsdU+yoZ6oQRqX4oeY+hKVNTjBgFKpc+EkAfdRFa4/3WL26MycaV5xL4kshqmf2ofTK4sHPIAWoB2mltMN4PJKKbdzMjUOHKOueg00bSqpxjgVaGJXdDziA8SqE++VQYUbF/l3O9kXwCjTANtwTuB85tU4E4CD/s3V6QKnVieAfOEwUWZeN/geSuwYpD+zQuqZfHfaoicVbyuQ0v7FVoNU2DpfbBIV0y+Zvz+1UufINjZb5+R1s7i~4277296~4604472',
    'overrideAbTestGroup': '%5B%5D',
    'ak_bmsc': '04AF5BE42BA2ABCACB7799EF2F30433A~000000000000000000000000000000~YAAQxnXTFx+MBTaOAQAAM2ygPBfNIHDHUlXcFZbpBp0Lu6AC/62C0ugMoxvOAhYstp2KZOgpqUvDOwZc3VsslTmJOMpndZFwwPsjL35Fz2I4QQxPlBEyvIO3QK5hisYjSF/1duimY1oZ5zK4ofih0XNJ/y2kkUOpjtbxd/d0MZB7ZR0p8pqDkEH/QrTtY2lN8n+xSBUdkLPdnlNsfdC1D9J7NIgjta8v/QWuKgqHH2E/kLsj3DXPcnvc4LbdBR9E2DyTUuCAzZ5c3jQW2yU0n/m6PaV8CsevvVzs92fdI2XzISAd4sJNxgcTO3HUDu2znTxSP8+R5DqqtJSQK9Zkdtyi7Cv2ua47eGXUCkehJrntwsLBxS+KSL3nhBOgoEsgoNbzY9TjI9IKp4Uy6edOyygwD65JUiFBBkyCoD+yPdH0vqi52oZwr1XJp5mCIJeajiAx3IYX+C2apeo=',
    'bm_sv': '81242D9401426D54BFAD020C0D5C2847~YAAQxnXTFwyZBTaOAQAAQZugPBf6VczT2CLx8gC4iJsVwTE9iRagpo9KlXDvbEE5fV8kVc5pV0GrwSt9fm5/VsYsapPRuIhJ7c1qAU8YbqqvciaDAswip9Llkw3Rh6HbPTLRutcH3eQDl3IXYXBDbCp+/Gukli/S8guH63VEQdkMAVJighL/PoopmzlfokqvmqHtGSO3my0j/iDcy6YnPhskwN36rJFNE9TOaal41SbVCOEVVtYJrqHEfXBRAEQvQg==~1',
    'baby-isWide': 'small',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'sid=d9e3fb3848994d29b2d2baf3a4094ed02b668caf; PCID=5525748675932096357655; MARKETID=5525748675932096357655; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; _abck=24AD795AABB66727F0742C089BC8584F~-1~YAAQxnXTF/+YBTaOAQAAEZugPAuQwCzZQta6IIIhYbvs4F48zTbdtDf2bAPyjsW4nnLY8xqd7JmOJcuERDMw2X1/ckmy35Q5Azxi6aTFQcIWW96X7qQajS6Civ2IY4qcRGSfdYQJSt52QQjpXdpqf8V+Ia/n315oDtpRubPoBCPYVirBfRJ5v0BP3vfdbQeofzEVqVKhg87dGpL5cBzTOpy5IV1Pn64aHS73iCqaFbJXj7jXKhMD93uy13Coylr3/gGnA4pWSr62o2AxFML3aVB+bAov0G2uRFxC6WmZTSv50vIKSCoJGNSQ5RjZljDkaiOjorbBHYtCCjGbh8nR+aRl4Mb3pGFURtTu6hl3vg2gPEFfRUrweAashuYHGkHKBnnv9565iSJG3uUpKJNQGoQe5vOY9IGuQnSfpLeBDUdNBC8k0lOzzW4=~-1~-1~-1; cto_bundle=P1itH19jV2dvSkpTTExXcWhPbkR4clZYUmlPb2ZZY21lVVd1YnZJOW1XUnlvZkZkNE45ZHE1WE5xZSUyQiUyRk9DVEFBaGtlc3F4TXZwQUxZeHBqJTJGNjRGaGoycVZaZmVlREd2JTJCTWlWMHZuMyUyRnFKN3MzVXQzc3hHZXQ0ZkRJVSUyQiUyQmpwT0tYTmpSMk0lMkZhSXZGOCUyQnFGSzVoQWdnZllGaFNKT29lcENkJTJGdU4yakNLMHcxaEVIMkxzWEpPUSUyQlRmSjJKTk1ScUI0TzFS; searchKeyword=%EC%9E%A5%EC%96%B4; searchKeywordType=%7B%22%EC%9E%A5%EC%96%B4%22%3A0%7D; _fbp=fb.1.1710153051358.230784221; trac_src=1042016; trac_spec=10304903; trac_addtag=900; trac_ctag=HOME; trac_lptag=%EC%BF%A0%ED%8C%A1; trac_itime=20240314200208; bm_sz=F81C75E501F205198F5C721FC31BAAEC~YAAQxnXTF56LBTaOAQAAcmqgPBddwSKV4uJyxsAdwoMM/93aty1CoQU3TiOn93UO4qo8i0iOBn8SG+tLECERt0aVHmMaNQme6X9pNxs27scfQMMdvzXbr6xAltTfkB959liAsdU+yoZ6oQRqX4oeY+hKVNTjBgFKpc+EkAfdRFa4/3WL26MycaV5xL4kshqmf2ofTK4sHPIAWoB2mltMN4PJKKbdzMjUOHKOueg00bSqpxjgVaGJXdDziA8SqE++VQYUbF/l3O9kXwCjTANtwTuB85tU4E4CD/s3V6QKnVieAfOEwUWZeN/geSuwYpD+zQuqZfHfaoicVbyuQ0v7FVoNU2DpfbBIV0y+Zvz+1UufINjZb5+R1s7i~4277296~4604472; overrideAbTestGroup=%5B%5D; ak_bmsc=04AF5BE42BA2ABCACB7799EF2F30433A~000000000000000000000000000000~YAAQxnXTFx+MBTaOAQAAM2ygPBfNIHDHUlXcFZbpBp0Lu6AC/62C0ugMoxvOAhYstp2KZOgpqUvDOwZc3VsslTmJOMpndZFwwPsjL35Fz2I4QQxPlBEyvIO3QK5hisYjSF/1duimY1oZ5zK4ofih0XNJ/y2kkUOpjtbxd/d0MZB7ZR0p8pqDkEH/QrTtY2lN8n+xSBUdkLPdnlNsfdC1D9J7NIgjta8v/QWuKgqHH2E/kLsj3DXPcnvc4LbdBR9E2DyTUuCAzZ5c3jQW2yU0n/m6PaV8CsevvVzs92fdI2XzISAd4sJNxgcTO3HUDu2znTxSP8+R5DqqtJSQK9Zkdtyi7Cv2ua47eGXUCkehJrntwsLBxS+KSL3nhBOgoEsgoNbzY9TjI9IKp4Uy6edOyygwD65JUiFBBkyCoD+yPdH0vqi52oZwr1XJp5mCIJeajiAx3IYX+C2apeo=; bm_sv=81242D9401426D54BFAD020C0D5C2847~YAAQxnXTFwyZBTaOAQAAQZugPBf6VczT2CLx8gC4iJsVwTE9iRagpo9KlXDvbEE5fV8kVc5pV0GrwSt9fm5/VsYsapPRuIhJ7c1qAU8YbqqvciaDAswip9Llkw3Rh6HbPTLRutcH3eQDl3IXYXBDbCp+/Gukli/S8guH63VEQdkMAVJighL/PoopmzlfokqvmqHtGSO3my0j/iDcy6YnPhskwN36rJFNE9TOaal41SbVCOEVVtYJrqHEfXBRAEQvQg==~1; baby-isWide=small',
    'Upgrade-Insecure-Requests': '1',
}

params = {
    'q': '장어',
    'channel': 'recent',
}

response = requests.get('https://www.coupang.com/np/search', params=params, cookies=cookies, headers=headers)
