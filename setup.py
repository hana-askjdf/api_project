#패키징화 하기- setup.py파일이 있으면 pip로 설치 가능 
from setuptools import setup

setup(
    name ="myAPI", #언더바 하면 하이픈으로 바뀜
    version = 0.0.1,  # relese - 엄청난 변화가 있을때 | major - 기능추가/ 몇몇 변화  | minor - 버그수정, 패키지보안할때 올림
    description="my api library",
    url = "https://github.com/hana-askjdf/api_project.git", # 도큐먼트나 홈페이지 링크를 주로 넣음 
    author = "chn", #개발자이름
    author_email="sssssss@gamil.com",
    packages= ["my_api"], #어떤 패키지 넣을건지
    install_requires = [
        "requests"
        ] #의존성있는 패키지 리스트
    
)
