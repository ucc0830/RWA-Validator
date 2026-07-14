# SA-RWA Validator

## 프로젝트 개요

**SA-RWA Validator(Standardised Approach RWA Validator)**는 Basel III 신용리스크 표준방법(Standardised Approach)의 RWA(Risk Weighted Assets) 산출 결과를 독립적으로 재산출하고 검증하기 위한 Python 기반 데스크톱 프로그램이다.

본 프로그램은 은행 내부 검증 업무를 지원하는 것을 목표로 하며, 원장 시스템에서 추출한 산출 결과를 입력받아 규제 요건에 따라 재계산을 수행한 후 차이 분석 및 검증 보고서를 생성한다.

---

# 프로젝트 목표

* 표준방법(Standardised Approach) RWA 산출 결과 검증
* Rule 기반 검증 엔진 개발
* 규제 요건별 오류 원인 분석
* Excel 기반 입력 및 결과 보고서 생성
* 향후 자산군별 Validator 확장 가능 구조 설계

---

# 개발 범위

### v1.0

* Bank Exposure Validator

### 향후 개발 계획

* Corporate Exposure
* Retail Exposure
* Sovereign Exposure
* CIU Exposure(FUND)
* Residential Mortgage(주거용부동산)
* Commercial Real Estate(상업용부동산)
* Default Exposure(부도)
* CRM Validation

---

# 주요 기능

## 입력

* 원장 시스템 산출 결과 Excel 업로드

입력항목
* 기준월
* 그룹사코드
* 계좌번호
* 익스포저유형
* 계정코드
* 상품코드
* 법인번호
* 법인명
* 장기 외부등급
* 단기 외부등급
* 잔액
* 미사용한도
* 약정금액
* CCF
* EAD
* Risk Weight
* RWA

---

## 처리

프로그램은 입력 데이터를 기반으로 다음 절차를 수행한다.

1. 입력 데이터 검증
2. 규제 요건 판정
3. 독립 재산출
4. 원장 결과 비교
5. 오류 원인 분석
6. 결과 보고서 생성

---

## 출력

Excel Report 생성

* Summary
* Validation Result
* Rule Summary
* Detail Report

---

# 프로젝트 구조

```text
sa-rwa-validator/

main.py

app/
│
├── ui/
│
├── common/
│   ├── excel_reader.py
│   ├── excel_writer.py
│   └── logger.py
│
├── bank/
│   ├── validator.py
│   ├── calculator.py
│   ├── rules.py
│   └── model.py
│
├── corporate/
│
├── retail/
│
├── ciu/
│
├── report/
│
└── config/

input/
output/
tests/
```

---

# 개발 원칙

* 규제 요건(Rule) 기반 설계
* Validator 모듈 분리
* 확장 가능한 구조
* 입력 데이터(Read Only) 유지
* 결과 보고서 자동 생성
* AI를 활용한 개발 생산성 향상

---

# 개발 환경

* Python 3.12+
* pandas
* openpyxl
* CustomTkinter

---

# 버전 관리

| Version | Description                 |
| ------- | --------------------------- |
| v0.1    | 프로젝트 생성                     |
| v0.2    | Excel 업로드                   |
| v0.3    | Bank Validator              |
| v0.4    | Risk Weight Validation      |
| v0.5    | Excel Report                |
| v1.0    | Bank Exposure Validation 완료 |

---

# 최종 목표

표준방법(Standardised Approach) 전체 자산군에 대한 독립적인 RWA 검증 플랫폼을 구축하여 규제 요건별 검증 결과와 오류 원인을 자동으로 제공하는 업무 지원 도구를 개발한다.
