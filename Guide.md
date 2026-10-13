[가이드문서]

1. SA-RWA-Validator 폴더를 만듭니다.

2. VS Code에서 파일 → 폴더 열기로 해당 폴더를 엽니다.

3. 상단 메뉴에서 터미널 → 새 터미널을 선택합니다.

4. 터미널에 아래 명령을 순서대로 입력합니다.

5. python --version

6. python -m venv .venv

7. .\.venv\Scripts\Activate.ps1

8.
SA-RWA-Validator/
├── main.py
├── README.md
├── REQUIREMENTS.md
├── requirements.txt
├── config/
│   └── required_columns.py
├── core/
│   ├── excel_reader.py
│   ├── validator_engine.py
│   └── report_generator.py
├── models/
│   └── exposure.py
├── rules/
│   ├── bank_rules.py
│   └── sovereign_rules.py
├── validators/
│   ├── bank_validator.py
│   └── sovereign_validator.py
├── ui/
│   └── main_window.py
├── input/
├── output/
└── tests/

[STEP 1]
나는 IT 비전공자이며 VS Code와 Python만 설치된 상태에서 바이브코딩으로 SA-RWA Validator를 개발하려고 한다.
이 프로그램은 Basel III 신용리스크 표준방법(Standardised Approach)의 RWA 산출 결과를 Excel로 입력받아 독립적으로 재계산하고, 원장 값과 비교한 결과를 Excel로 출력하는 데스크톱 프로그램이다.
다음 원칙을 지켜라.

1. Python, pandas, openpyxl, CustomTkinter를 사용한다.
2. 업무 규칙은 rules/, 검증 로직은 validators/, 전체 실행 흐름은 core/, 화면은 ui/에 분리한다.
3. 최초 구현 대상은 Bank Exposure와 Sovereign Exposure다.
4. Corporate, Retail 등 다른 자산군은 이번 범위에서 구현하지 않는다.
5. 원본 Excel 데이터는 수정하지 않고 검증 결과만 별도로 생성한다.
6. Windows 환경에서 실행할 수 있어야 한다.
7. IT 비전공자가 이해할 수 있도록 각 파일의 역할을 설명한다.
8. 코드를 작성하기 전에 요구사항, 예상 폴더 구조, 구현 순서를 제안한다.
9. 아직 코드는 작성하지 말고, 불명확하거나 규제 확인이 필요한 사항을 구분한다.

응답은 다음 순서로 작성하라.
- 프로젝트 목표
- 기능 요구사항
- 비기능 요구사항
- 폴더 구조
- 단계별 개발 계획
- 미확정 사항 및 위험요인

프롬프트 입력 후 해야 할 조치
- AI가 제안한 폴더 구조를 확인합니다.
- Bank와 Sovereign이 이번 구현 범위에 포함되었는지 확인합니다.
- 규제 기준과 관련해 AI가 임의로 가정한 내용이 있다면 미확정 사항으로 남깁니다.
- 이 단계에서는 코드를 생성하지 않습니다.

[UPDATE DOC 1]
방금 확정한 프로젝트 목표, 기능 요구사항, 비기능 요구사항, 개발 범위와 미확정 사항을 REQUIREMENTS.md 파일로 작성해라.
요구사항마다 고유 ID를 부여해라. 예를 들어 FR-001은 기능 요구사항, NFR-001은 비기능 요구사항, BR-001은 업무 규칙, TC-001은 테스트 케이스를 의미한다.
각 항목에는 ID, 요구사항, 우선순위, 검증 방법, 상태를 포함해라.
현재 확정되지 않은 규제 기준은 확정된 사실처럼 작성하지 말고 '확인 필요'로 표시해라. 파일을 실제로 생성하고, 생성한 파일 경로와 내용을 요약해라.

[STEP 2]
확정된 REQUIREMENTS.md를 기준으로 SA-RWA Validator의 최소 프로젝트 구조를 생성해라.

조건:
1. 현재 작업 폴더를 먼저 확인하고 기존 파일을 덮어쓰지 마라.
2. 필요한 폴더와 초기 Python 파일을 생성해라.
3. requirements.txt에는 프로그램 실행에 필요한 외부 패키지만 기록해라.
4. README.md에는 프로젝트 개요, 설치 방법, 실행 방법, 폴더 구조를 작성해라.
5. REQUIREMENTS.md의 요구사항 ID와 개발 범위를 유지해라.
6. 아직 구현되지 않은 기능은 구현 완료로 표시하지 마라.
7. 코드 작성 후 생성 또는 수정한 파일 목록과 각 파일의 역할을 설명해라.

패키지 설치 명령도 별도로 제시해라. requirements.txt와 업무 요구사항 문서는 혼동하지 마라.

python -m pip install -r requirements.txt
python -c "import pandas, openpyxl, customtkinter; print('패키지 설치 확인 완료')"

[STEP 3]
REQUIREMENTS.md를 확인하고 Excel 입력 기능을 구현해라.

요구사항:
1. core/excel_reader.py에 ExcelReader 클래스를 구현한다.
2. pandas와 openpyxl을 사용한다.
3. 파일 경로가 잘못되었거나 파일이 존재하지 않으면 이해할 수 있는 오류를 반환한다.
4. 필수 컬럼은 config/required_columns.py에서 관리한다.
5. 컬럼명 앞뒤 공백을 제거한다.
6. 필수 컬럼이 누락되면 누락된 컬럼명을 모두 표시한다.
7. 원본 Excel 파일은 변경하지 않는다.
8. 기존 폴더 구조를 유지하고 불필요한 파일을 생성하지 않는다.
9. 정상 입력과 오류 입력을 검증하는 테스트 코드를 작성한다.

먼저 수정할 파일과 구현 계획을 제시하고, 구현 후 실행할 테스트 명령을 알려라. README.md와 REQUIREMENTS.md도 변경된 기능에 맞게 업데이트해라. 테스트를 실제로 실행하지 않았다면 통과했다고 표현하지 마라.

[STEP 4]
REQUIREMENTS.md와 현재 프로젝트 파일을 먼저 읽어라.

Bank Exposure 검증 기능을 다음 구조로 구현해라.

- rules/bank_rules.py: Risk Weight, EAD, RWA 계산 규칙
- validators/bank_validator.py: 계산 결과와 원장 값 비교
- core/validator_engine.py: 추후 여러 Validator를 연결할 수 있는 구조

검증 항목:
1. 외부등급에 따른 Risk Weight
2. EAD = 잔액 + 미사용한도 × CCF
3. RWA = EAD × Risk Weight
4. 원장 값과 계산 값의 차이
5. 오류 원인 기록

주의사항:
- 기존 파일과 클래스의 구조를 먼저 확인한다.
- 확인되지 않은 규제 기준을 임의로 추가하지 않는다.
- 등급표와 산식은 업무 규칙 파일에서 관리한다.
- 입력값이 비어 있거나 숫자가 아닌 경우의 처리를 고려한다.
- PASS와 FAIL이 명확히 구분되어야 한다.
- 원본 데이터는 변경하지 않는다.

정상 케이스, Risk Weight 오류, EAD 오류, RWA 오류, 잘못된 입력값에 대한 테스트를 작성해라.

구현 후 수정 파일, 변경 이유, 실행할 테스트 명령을 제시하고 README.md와 REQUIREMENTS.md를 업데이트해라.

[STEP 5]
현재 프로젝트의 rules/bank_rules.py와 REQUIREMENTS.md를 먼저 읽어라.

rules/sovereign_rules.py를 구현해라.

이번 구현 범위:
1. Sovereign Exposure의 장기 외부등급별 Risk Weight 조회
2. EAD 재계산
3. RWA 재계산
4. 미등급 값과 지원하지 않는 등급 코드 처리
5. 잘못된 숫자와 결측값 처리

기존 프로젝트의 컬럼명을 그대로 사용한다.
- 장기 외부등급
- 잔액
- 미사용한도
- CCF
- EAD
- Risk Weight
- RWA

Bank 규칙과 중복되는 부분이 있어도 우선 기존 구조를 유지해라. 공통 모듈로의 리팩터링은 별도 제안만 하고 지금 실행하지 마라.

중요:
- Risk Weight 표는 코드에 넣기 전에 규제 근거 및 적용 범위를 REQUIREMENTS.md에 명시해라.
- 국내 통화 표시 국채 우대, ECA 등급, 단기등급 적용 등 미구현 항목을 명시해라.
- 확인되지 않은 사항은 가정으로 표시하고 확정된 규제 사실처럼 서술하지 마라.

구현 후 정상값, 미등급, 미지원 등급, 결측값에 대한 테스트를 작성하고 README.md와 REQUIREMENTS.md를 업데이트해라.

[STEP 6]
현재 rules/sovereign_rules.py와 validators/bank_validator.py를 읽어라.

validators/sovereign_validator.py에 SovereignValidator를 구현해라.

요구사항:
1. SovereignRules를 사용해 Risk Weight, EAD, RWA를 재계산한다.
2. 원장 값과 재계산 값을 비교한다.
3. Risk Weight와 금액 항목의 허용 오차를 명시적으로 관리한다.
4. 계산에 실패한 항목은 오류 원인을 기록한다.
5. 하나의 항목에 오류가 발생해도 다른 항목의 검증을 가능한 범위에서 계속 수행한다.
6. 결과에는 계좌번호, 원장 값, 계산 값, PASS/FAIL, 오류 원인을 포함한다.
7. 기존 Bank Validator의 결과 컬럼과 호환성을 유지한다.

테스트를 작성하고 실행 결과를 확인해라. REQUIREMENTS.md에는 Validator의 입력, 출력, 예외 처리 기준을 기록하고 README.md에는 현재 지원하는 Sovereign 검증 항목을 반영해라.


[STEP 7]
현재 core/validator_engine.py, validators/bank_validator.py, validators/sovereign_validator.py, config/required_columns.py를 먼저 읽어라.

검증 엔진이 Bank와 Sovereign을 모두 처리할 수 있도록 수정해라.

요구사항:
1. 입력 데이터의 익스포저유형을 기준으로 사용할 Validator를 선택한다.
2. Bank와 Sovereign에 대한 분류 기준을 명확히 정의한다.
3. 알 수 없는 익스포저유형은 조용히 Bank로 처리하지 말고 명시적인 오류 또는 FAIL 결과로 기록한다.
4. Bank와 Sovereign의 결과 컬럼 형식을 통일한다.
5. 입력 데이터의 행 순서와 계좌 식별정보를 유지한다.
6. 기존 Bank 검증 기능이 회귀하지 않도록 테스트한다.
7. Sovereign 코드가 엔진을 통해 실제 호출되는지 테스트한다.
8. 기존 프로젝트 구조를 변경하지 않는다.

구현 후 변경 파일 목록, 익스포저 분류 기준, 테스트 결과를 설명해라. README.md와 REQUIREMENTS.md에 엔진 연결 및 분류 기준을 반영해라.

[STEP 8]
현재 ui/main_window.py, main.py, core/excel_reader.py, core/validator_engine.py, core/report_generator.py를 읽어라.

SA-RWA Validator 데스크톱 프로그램을 실행 가능한 상태로 연결해라.

필요 기능:
1. 프로그램 시작
2. Excel 파일 선택
3. 입력 파일명 표시
4. 검증 실행 버튼
5. 검증 진행 결과 및 오류 메시지 표시
6. 검증 결과 Excel 파일 저장
7. 결과 저장 경로 안내

조건:
- CustomTkinter 기반 기존 화면 구조를 최대한 유지한다.
- 파일 선택 전에는 검증 실행을 막는다.
- Excel 입력 오류가 발생해도 프로그램이 갑자기 종료되지 않도록 처리한다.
- 검증 결과는 원본 파일에 덮어쓰지 않는다.
- 출력 폴더가 없으면 생성한다.
- 화면에서 발생한 오류를 사용자가 이해할 수 있는 메시지로 보여준다.
- 실행 진입점은 main.py로 통일한다.

코드 변경 후 실제 실행 절차와 GUI 테스트 방법을 알려라. README.md와 REQUIREMENTS.md도 갱신해라. 직접 실행하지 않은 테스트는 성공했다고 주장하지 마라.



이번 작업에서 변경한 코드를 기준으로 README.md와 REQUIREMENTS.md를 함께 업데이트해라.

[REQUIREMENTS.md 갱신 규칙]
1. 기존 요구사항 ID를 유지한다.
2. 새 요구사항이 생기면 기존 ID를 임의로 변경하지 않고 새 ID를 부여한다.
3. 요구사항별 상태를 '미착수', '구현 중', '구현 완료', '테스트 완료', '확인 필요' 중 하나로 관리한다.
4. 실제 구현 여부와 테스트 여부를 구분한다.
5. 변경된 요구사항, 테스트 방법, 테스트 결과를 반영한다.
6. 규제 기준이 확인되지 않은 항목은 '확인 필요'로 유지한다.
7. 더 이상 유효하지 않은 요구사항은 삭제하지 말고 변경 이력을 남긴다.

[README.md 갱신 규칙]
1. 프로젝트 목적과 현재 지원 기능을 업데이트한다.
2. 설치 및 실행 방법이 실제 코드와 일치하는지 확인한다.
3. 폴더 구조와 파일 설명을 최신 상태로 유지한다.
4. 구현되지 않은 기능은 완료된 기능처럼 소개하지 않는다.
5. 실행 방법과 테스트 명령을 명시한다.
6. 알려진 한계와 미지원 기능을 기록한다.

[변경 이력]
- 변경한 파일
- 변경 이유
- 새로 구현한 기능
- 수정한 요구사항 ID
- 실행한 테스트 및 실제 결과
- 남은 작업

기존 문서를 무조건 전부 다시 작성하지 말고, 변경된 부분을 중심으로 갱신해라. 업데이트 후 두 문서와 실제 코드 사이에 불일치가 없는지 점검하고 요약해라.