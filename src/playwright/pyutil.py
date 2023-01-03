# extract the view count
def get_view_count(view_string):
    view_string = view_string.replace("조회수", "")
    view_string = view_string.replace(" ", "")
    view_string = view_string.replace("회", "")

    if "천" in view_string:
        view_string = view_string.replace("천", "")
        return float(view_string) * 1000
    elif "만" in view_string:
        view_string = view_string.replace("만", "")
        return float(view_string) * 10000
    elif "억" in view_string:
        view_string = view_string.replace("억", "")
        return float(view_string) * 100000000
    else:
        return float(view_string)

# extract the upload date
def get_upload_date(upload_string):
    upload_string = upload_string.replace(" ", "")
    upload_string = upload_string.replace("전", "")

    # 분 단위
    if "분" in upload_string:
        upload_string = upload_string.replace("분", "")
        return int(upload_string)
    elif "시간" in upload_string:
        upload_string = upload_string.replace("시간", "")
        return int(upload_string) * 60
    elif "일" in upload_string:
        upload_string = upload_string.replace("일", "")
        return int(upload_string) * 60 * 24
    elif "개월" in upload_string:
        upload_string = upload_string.replace("개월", "")
        # 30일로 계산
        return int(upload_string) * 30
    elif "년" in upload_string:
        upload_string = upload_string.replace("년", "")
        # 365일로 계산
        return int(upload_string) * 365
    else:
        return 0

# 조회수
# 1.2천회
# 1.2만회
# 1.2억회
# 218만회

# 게시일
# 1년 전
# 1개월 전
# 1일 전
