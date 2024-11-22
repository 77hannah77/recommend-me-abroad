import re

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
