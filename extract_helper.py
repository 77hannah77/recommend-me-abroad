import re
import pandas as pd

# 보고서 parsing 관련
def extract_section(content, start, end):
    if isinstance(content, str):
        match = re.search(rf'{re.escape(start)}(.*?){re.escape(end)}', content, re.DOTALL)
        if match:
            return match.group(1).strip()
    return None

def old_extract_motivation(content):
    # 두 부분 추출
    match1 = extract_section(content, "교환학생에 관심 갖게 된 계기 및 지원 동기", "출국 전 준비 사항과 주의 할 점")
    match2 = extract_section(content, "교환학생 프로그램을 통해 느낀 점, 배운 점", "기타\(사진, 건의사항, 등\)")

    # 결과 조합
    result = ""
    if match1:
        result += match1
    if match2:
        result += match2

    return result.strip()  # 결과를 공백으로 조합하여 반환

def new_extract_motivation(content):
    # 세 부분 추출
    match1 = extract_section(content, "8. 소감", "9. 프로그램 평가 및 기타 내용")
    match2 = extract_section(content, "9. 프로그램 평가 및 기타 내용", "10. 파견 예정 학생들에게 전하고 싶은 말")
    match3 = extract_section(content, "10. 파견 예정 학생들에게 전하고 싶은 말", "")

    # 결과 조합
    result = ""
    if match1:
        result += match1
    if match2:
        result += match2
    if match3:
        result += match3

    return result.strip()  # 결과를 공백으로 조합하여 반환

# csv 파일 관련
# 데이터를 읽어올 대상 열 선택
def select_content(row):
    if row['Attachment Present'] == "Yes":
        return row['Attachment Content']
    else:
        return row['Text Content']
    
# Version에 따라 함수 선택
def process_content(row):
    content = row['Selected Content']
    try:
        # 'Version' 열이 존재하면 값에 따라 처리
        if row['Version'] == 'old':
            return old_extract_motivation(content)
        elif row['Version'] == 'new':
            return new_extract_motivation(content)
    except KeyError:
        # 'Version' 열이 없을 경우 기본값 처리
        return old_extract_motivation(content)
