# ============================================
# 나만의 프롬프트 관리 프로그램
# ============================================

# 카테고리 목록 (미리 정해둔 6개)
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 기본 프롬프트 데이터 (리스트 안에 딕셔너리 3개)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 IT 컨설턴트입니다. 전문적으로 조언해주세요.",
        "category": "페르소나",
        "favorite": False
    },
]

# 메뉴를 화면에 보여주는 함수
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

    # 프롬프트 한 개를 "번호. [카테고리] 제목 ⭐" 형태로 출력하는 도우미 함수
def print_one(index, p):
    star = " ⭐" if p["favorite"] else ""
    print(f"{index}. [{p['category']}] {p['title']}{star}")

    # 1. 프롬프트 추가
def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    # 제목이 빈칸이면 다시 입력받기
    title = input("제목: ").strip()
    while title == "":
        print("제목은 비워둘 수 없습니다.")
        title = input("제목: ").strip()

    # 내용이 빈칸이면 다시 입력받기
    content = input("내용: ").strip()
    while content == "":
        print("내용은 비워둘 수 없습니다.")
        content = input("내용: ").strip()

    # 카테고리 선택
    print("\n카테고리 선택:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}) {c}")
    choice = input("선택: ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        category = CATEGORIES[int(choice) - 1]
    else:
        category = "기타"  # 잘못 입력하면 기타로 처리

    # 새 프롬프트를 딕셔너리로 만들어 리스트에 추가
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("\n프롬프트가 추가되었습니다!")

    # 2. 프롬프트 목록
def show_list():
    print("\n=== 프롬프트 목록 ===")
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        print_one(i, p)
    print(f"\n총 {len(prompts)}개의 프롬프트")

    # 3. 카테고리별 조회
def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}) {c}")
    choice = input("선택: ").strip()

    if not (choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 선택입니다.")
        return

    category = CATEGORIES[int(choice) - 1]
    print(f"\n[{category}] 카테고리 프롬프트:")

    count = 0
    for p in prompts:
        if p["category"] == category:
            count += 1
            print_one(count, p)

    if count == 0:
        print("해당 카테고리에 프롬프트가 없습니다.")
    else:
        print(f"\n총 {count}개의 프롬프트")

        # 4. 프롬프트 검색
def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()

    print("\n검색 결과:")
    count = 0
    for p in prompts:
        # 제목 또는 내용에 검색어가 들어있으면
        if keyword in p["title"] or keyword in p["content"]:
            count += 1
            print_one(count, p)

    if count == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"\n{count}개의 프롬프트를 찾았습니다.")

        # 5. 프롬프트 상세 보기
def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    show_list()
    num = input("\n번호 입력: ").strip()

    if not (num.isdigit() and 1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]
    star = "⭐" if p["favorite"] else "없음"
    print("\n────────────────────────────")
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("────────────────────────────")
    print("내용:")
    print(p["content"])
    print("────────────────────────────")


# 6. 즐겨찾기 관리 (추가/해제)
def manage_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    show_list()
    num = input("\n프롬프트 번호 입력: ").strip()

    if not (num.isdigit() and 1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]
    # True면 False로, False면 True로 뒤집기
    p["favorite"] = not p["favorite"]

    if p["favorite"]:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다!")


# 7. 즐겨찾기 목록
def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    count = 0
    for p in prompts:
        if p["favorite"]:
            count += 1
            print_one(count, p)

    if count == 0:
        print("즐겨찾기된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {count}개의 즐겨찾기")

        # ============================================
# 프로그램 실행 (메인 반복문)
# ============================================
def main():
    while True:
        show_menu()
        sel = input("선택: ").strip()

        if sel == "1":
            add_prompt()
        elif sel == "2":
            show_list()
        elif sel == "3":
            show_by_category()
        elif sel == "4":
            search_prompt()
        elif sel == "5":
            show_detail()
        elif sel == "6":
            manage_favorite()
        elif sel == "7":
            show_favorites()
        elif sel == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


# 이 파일을 직접 실행할 때만 main() 실행
if __name__ == "__main__":
    main()