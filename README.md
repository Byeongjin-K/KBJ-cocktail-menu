# 🍸 나만의 칵테일 메뉴 (Personal Cocktail Menu)

찌니의 칵테일 비법 영상을 바탕으로 정리한 개인 칵테일 메뉴판입니다. 총 **35종** · 9개 카테고리.

## 📂 파일 구성

| 파일 | 용도 |
|---|---|
| **`index.html`** | 손님용 메뉴 — 칵테일 설명·풍미·도수·잔·가니쉬 (레시피 비공개) |
| **`recipes.html`** | 바텐더용 메뉴 — 정확한 레시피·계량·조주법·팁 포함 |
| `build_menu.py` | 두 HTML을 생성하는 빌드 스크립트 (편집/추가 시 사용) |

---

## 🌐 GitHub Pages 호스팅 가이드

### 1. GitHub 리포지토리 만들기

1. [github.com](https://github.com) 로그인
2. 우측 상단 **+** → **New repository**
3. Repository name: 원하는 이름 (예: `cocktail-menu`)
4. **Public** 선택 (Pages 무료 사용)
5. **Create repository**

### 2. 파일 업로드

브라우저에서 가장 쉽게:
1. 새 리포지토리 페이지의 **"uploading an existing file"** 클릭
2. `index.html`, `recipes.html`, `build_menu.py`, `README.md` 드래그 & 드롭
3. 아래 **Commit changes** 버튼

또는 Git CLI를 쓰신다면:
```bash
git clone https://github.com/[username]/[repo-name].git
cd [repo-name]
# 파일 복사 후
git add .
git commit -m "Add cocktail menu"
git push
```

### 3. GitHub Pages 활성화

1. 리포지토리 → **Settings** (상단 탭)
2. 왼쪽 사이드바 → **Pages**
3. **Source**: `Deploy from a branch`
4. **Branch**: `main` / `(root)` 선택 → **Save**
5. 1-2분 후 페이지 상단에 URL이 표시됨:
   `https://[your-username].github.io/[repo-name]/`

### 4. 접속 URL

- **손님용**: `https://[username].github.io/[repo-name]/`
- **바텐더용**: `https://[username].github.io/[repo-name]/recipes.html`

---

## 📱 손님에게 공유하기

### QR 코드 인쇄
1. [qr-code-generator.com](https://www.qr-code-generator.com/) 등에서 손님용 URL로 QR 생성
2. 작은 카드에 인쇄해 테이블에 두기

### 카톡/문자로 공유
- URL을 그대로 전송하면 카톡 미리보기에 메뉴 제목·설명이 표시됩니다 (OG 메타태그 포함)

### 홈 화면 추가 (iOS/Android)
- 브라우저에서 URL 접속 → 공유 → **홈 화면에 추가**
- 앱처럼 한 번에 열림 (PWA 메타태그 포함)

---

## ✏️ 메뉴 수정·추가하기

1. `build_menu.py`의 `COCKTAILS` 리스트에서 칵테일 데이터 편집
2. 파이썬 실행:
   ```bash
   python3 build_menu.py
   ```
3. `index.html`, `recipes.html`이 자동 재생성
4. GitHub에 push → 1-2분 후 사이트 반영

### 새 칵테일 추가 템플릿
```python
{
    "kr": "한글 이름", "en": "English Name", "cat": "vodka",  # 9가지 카테고리 중 하나
    "abv": 20,
    "recipe": [("재료1", "30 ml"), ("재료2", "15 ml")],
    "method": "Shake",
    "glass": "Cocktail",
    "garnish": "라임 웨지",
    "notes": "스토리·배경 설명...",
    "taste": "맛 묘사 (첫모금~끝맛 시퀀스로)...",
    "tip": "만들기 팁 (선택)",
    "tags": ["태그1", "태그2", "태그3"],
},
```

### 카테고리 종류
`vodka` · `whisky` · `rum` · `tequila` · `gin` · `multi` · `liqueur` · `signature` · `mocktail`

---

## 🎨 디자인 컨셉

빈티지 스피크이지 바 분위기:
- **다크 배경** + 앤틱 골드 액센트
- **세리프 타이포그래피**: Cormorant Garamond + Noto Serif KR + Italianno
- **모바일 우선** 반응형 + Sticky 카테고리 네비게이션
- **인쇄 친화적**: `@media print` 적용 (PDF 변환 시 흰 배경·골드 보더)

---

*Drink responsibly — savor slowly. ✦*
