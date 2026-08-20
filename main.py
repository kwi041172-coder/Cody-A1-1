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