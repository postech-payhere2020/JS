from easycodefpy import Codef, ServiceType
from ast import literal_eval
import sqlite3
import pandas as pd
from pandas import Series, DataFrame
import json
import sys 

demo_client_id = ''
demo_client_secret = ''

client_id = ''
client_secret = ''

public_key = sys.argv[0]

# 코드에프 인스턴스 생성
codef = Codef()
codef.public_key = public_key

# 데모 클라이언트 정보 설정
# - 데모 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
# - 데모 서비스로 상품 조회 요청시 필수 입력 항목
codef.set_demo_client_info(demo_client_id, demo_client_secret)

# 정식 클라이언트 정보 설정
# - 정식 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
# - 정식 서비스로 상품 조회 요청시 필수 입력 항목
codef.set_client_info(client_id, client_secret)


# 요청 파라미터 설정
# - 각 상품별 파라미터를 설정(https://developer.codef.io/products)
parameter = { # POSTECH 여기 parameter 수정
    "organization" : "0004",
    "reqIdentityList" : []
}

# 코드에프 정보 조회 요청
# - 서비스타입(0:정식, 1:데모, 2:샌드박스)
# 개인 보유계좌 조회 (https://developer.codef.io/products/bank/common/p/account)
product_url = "/v1/kr/public/nt/business/status" # POSTECH 여기 URL 수정


res = codef.request_product(product_url, ServiceType.SANDBOX, parameter)
print("paramter:",parameter,'\n')
print("result:",res,'\n')

#뒷 내용 ipynb 파일에 있습니다