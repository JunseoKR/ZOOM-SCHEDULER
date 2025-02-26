![ZOSC](https://user-images.githubusercontent.com/70479192/150922564-46bbba37-f467-429f-8a58-ad6de3abd3f3.png)

- - -

<br/>

<h1><b><div align="center">
  🎉 2021 제3회 한국코드페어 SW공모전 본선 10등 🎉
</div></b></h1>
  
<h2><b><div align="center">
  H28 응애 나 애기준서 팀 👶
</div></b></h2>

<br/>

- - -

<br/>

# ZOOM SCHEDULER [ ZOSC ]

## 🏫 Taejang High School / 태장고등학교

<br/>

### 전면등교로 인해 2021년 8월 이후로 서비스 종료되었습니다.
### 서비스 기간 : 2020년 ~ 2021년 (2년)

<br/>

## ZOSC 기능

### 1. 온라인 수업 자동 참여

- 수업시간이 되면 자동으로 수업에 입장합니다.

### 2. 집중도 분석

- 집중도 상태를 파악하여 알려드립니다.

### 3. 자가진단

- 교육청 자가진단을 ZOSC에서 한번에 끝낼 수 있습니다.


<br/>

<br/>

## 💻 프로젝트 소개

### 배경

- 2020년 코로나-19 바이러스 대유행으로 온라인 수업(ZOOM)으로 대체되면서 온라인 수업에 대한 불편함이 증가함.
- 온라인 수업으로 인해 발생하는 학력격차, 학생-교사 간 소통 단절과 같은 문제들을 해결하는데 도움이 되기 위함.
- 온라인 수업으로 인해 발생하는 학생-교사 간 소통과 교사의 관리 분절 문제를 해결하기 위함.

### 목적 / 목표

- 온라인 수업을 보조하는 기능들을 통해 불편함을 해소하고 흐트러진 학습 태도를 교정
- 지속적이고 점진적인 업데이트를 통해 확장 기능들을 추가

### 기능

#### 1. 온라인 수업 자동 참여
  - 서버에서 JSON 데이터를 응답받은 후 백그라운드 타이머를 설정하여 지정된 수업시간에 회의를 실행하도록 함.

#### 2. 집중도 분석
  - 실행 프로세스 목록을 불러와 서버에 등록되어 있는 프로세스 목록과 대조하여 감지, 감지 데이터를 DB에 업로드함
  - DB에 저장된 감지 데이터들을 분석하여 앱, 웹에서 자신의 집중도를 확인 가능

#### 3. 자가진단
  - 앱 내에서 자가진단을 요청(제출)하면, Selenium 모듈을 통해 백그라운드로 처리함.

<br/>
<br/>
<br/>

- - -

## 🔗 프로젝트 구조

### 전체 구조

![전체 구조](https://user-images.githubusercontent.com/70479192/167988020-990e3824-e24e-4ea1-a441-7085c9dd4ff8.jpg)

<br/>

### Class 구조

![Class 구조](https://user-images.githubusercontent.com/70479192/167988129-73069ab7-bed6-4c2e-975b-fe143682f646.jpg)


<br/>
<br/>
<br/>

- - -

## 📄 프로젝트 보고서
### SW공모전 본선 보고서

<br/>

![ZOSC 보고서](https://user-images.githubusercontent.com/70479192/167986241-44a9a238-367f-4c8b-bfb9-e9a7e4234002.jpg)

<h2><a href='https://drive.google.com/file/d/1-c5rdFHXZJQZJyS0UNvzL1iMwIsELFLL/view?usp=sharing' target='_blank'><div align="center">
  📄 프로젝트 보고서
</div></a></h2>

<h3><b><div align="center">
  ⭐ 자세한 프로젝트 내용은 보고서를 확인해 주세요. ⭐
</div></b></h3>

<br/>
<br/>
<br/>

- - -

## 🛠 기술 스택

### Front
- Python
- PyQt5

### Back
- JavaScript
- Node.js
- MySQL
