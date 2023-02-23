# flu

##설명
기상정보로 감기예상환자 예측

![image](https://github.com/zzanggeonui//streamlit_flu/blob/main/%EA%B0%90%EA%B8%B0%EC%A7%84%EB%A3%8C%20%ED%99%98%EC%9E%90.png)

##주소

http://ec2-43-201-85-127.ap-northeast-2.compute.amazonaws.com:8503/

## Dataset

기상청 기상정보 데이터
https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36
국민건강보험공단 일별 감기진료 데이터
https://www.data.go.kr/data/15083145/fileData.do?recommendDataYn=Y

## 작업 설명

- jupyter notebook을 통해 데이터프레임 가공 및 데이터 분석을 진행하였습니다
- 머신러닝을 통해 수치 예측을 진행하였습니다
- putty를 통해 AWS EC2 인스턴스에 연결하여 서버를 배포 및 관리하였습니다.
- github action을 활용하여 CI/CD를 구현하였습니다.


## ai 인공지능
 Linear Regressionr로 수치예측 진행

 ![image](https://github.com/zzanggeonui//streamlit_flu/blob/main/%EB%A9%94%EC%9D%B8%ED%99%94%EB%A9%B4.png)
