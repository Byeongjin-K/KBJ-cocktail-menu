"""
나만의 칵테일 메뉴판 v3
- 모바일 최적화 (sticky 카테고리 nav, 타이트한 패딩, 작은 폰트)
- GitHub Pages 배포 준비 (index.html + recipes.html)
- 카톡/SNS 공유용 OG 메타태그
"""

SECTIONS = [
    ("vodka",     "I",    "Vodka",        "보드카 베이스"),
    ("whisky",    "II",   "Whisky",       "위스키 베이스"),
    ("rum",       "III",  "Rum",          "럼 베이스"),
    ("tequila",   "IV",   "Tequila",      "데킬라 베이스"),
    ("gin",       "V",    "Gin",          "진 베이스"),
    ("multi",     "VI",   "Multi-Spirit", "여러 베이스 혼합"),
    ("liqueur",   "VII",  "Liqueur",      "리큐어 베이스"),
    ("signature", "VIII", "Signature",    "시그니처"),
    ("mocktail",  "IX",   "Mocktail",     "논알콜"),
]

COCKTAILS = [
    # ============ VODKA ============
    {
        "kr": "갓마더", "en": "Godmother", "cat": "vodka", "abv": 30,
        "recipe": [("보드카", "45 ml"), ("아마레또", "15 ml")],
        "method": "Build", "glass": "Old Fashioned", "garnish": None,
        "notes": "1970년대 미국 동부 사교계에서 사랑받기 시작한 클래식. 영화 〈대부〉를 연상시키는 '갓파더'(스카치 버전)와 한 쌍을 이루는 보드카 버전이다. 두 가지 재료뿐인 단순함이 오히려 격조를 만든다.",
        "taste": "보드카가 입안을 차갑고 깔끔하게 정돈한 뒤, 아마레또의 따뜻한 아몬드·살구 향이 천천히 펼쳐진다. 단맛은 끈적이지 않고, 견과류의 깊이감으로 마무리되며 입안에 오래 머문다.",
        "tip": "큰 얼음 한 덩이로 천천히 희석시키며 마시면 향이 더 살아난다. 식후, 늦은 밤, 잔잔한 음악과 함께.",
        "tags": ["묵직한 바디", "아몬드향", "달콤", "식후주", "어른스러운"],
    },
    {
        "kr": "코스모폴리탄", "en": "Cosmopolitan", "cat": "vodka", "abv": 19,
        "recipe": [("보드카(시트론)", "45 ml"), ("트리플 섹", "15 ml"),
                   ("크랜베리 주스", "30 ml"), ("라임 주스", "15 ml")],
        "method": "Shake", "glass": "Martini", "garnish": "라임 슬라이스 또는 오렌지 필",
        "notes": "1980년대 뉴욕에서 자리잡고, 드라마 〈섹스 앤 더 시티〉를 통해 전 세계의 아이콘이 된 핑크빛 마티니. 우아한 마티니 글라스에 담긴 새콤한 분홍색이 자리의 분위기를 단번에 끌어올린다.",
        "taste": "첫 모금에 크랜베리의 산뜻한 산미가 톡 쏘듯 퍼지고, 시트론 보드카의 레몬 향이 가볍게 올라온다. 트리플 섹의 오렌지 단맛이 균형을 잡으며, 라임이 끝맛을 깔끔하게 정리. 단순한 새콤달콤이 아니라 입체적인 시트러스 칵테일.",
        "tip": "시트론 보드카가 없다면 일반 보드카에 레몬즙 소량을 더해도 된다. 잔과 술을 미리 차게 식혀두면 풍미가 더 살아난다.",
        "tags": ["새콤달콤", "시트러스", "우아한", "분홍빛", "사진 잘 나오는"],
    },
    {
        "kr": "케이프코드", "en": "Cape Cod", "cat": "vodka", "abv": 9,
        "recipe": [("보드카", "45 ml"), ("크랜베리 주스", "120 ml"), ("라임", "1 wedge")],
        "method": "Build", "glass": "Highball", "garnish": "라임 웨지",
        "notes": "미국 동부 매사추세츠 케이프코드 반도의 크랜베리 산지에서 이름을 따온, 단순함의 미학을 보여주는 한 잔. '보드카 크랜베리'라는 별칭으로도 불리며, 미국 가정에서 가장 흔히 만드는 칵테일 중 하나다.",
        "taste": "크랜베리 주스의 자연스러운 새콤함이 주연. 보드카는 거의 자기 주장을 하지 않고 뒷받침만 하다가, 마지막에 라임 한 조각이 산뜻함을 더해 마무리한다. 알코올감이 거의 없어 주스를 마시듯 부드럽게 넘어간다.",
        "tip": "100% 크랜베리 주스보다는 약간 단맛이 가미된 시판 크랜베리 주스가 균형이 더 좋다.",
        "tags": ["가벼운", "베리향", "산뜻한", "데일리", "입문자용"],
    },
    {
        "kr": "블루라군", "en": "Blue Lagoon", "cat": "vodka", "abv": 11,
        "recipe": [("보드카", "30 ml"), ("블루 큐라소", "30 ml"), ("라임 즙", "20 ml"),
                   ("스프라이트", "Top up")],
        "method": "Shake → Build", "glass": "롱드링크 (Highball)", "garnish": "레몬 슬라이스 · 체리",
        "notes": "1960년 파리의 해리스 뉴욕 바에서 탄생. 이름은 1949년 영화 〈블루 라군〉에서 따왔다고 알려져 있다. 청록빛 바다처럼 빛나는 색이 먼저 시선을 사로잡는, 시각·미각 모두 화려한 트로피컬 칵테일.",
        "taste": "블루 큐라소가 사실은 오렌지 리큐어(색만 푸를 뿐)이라는 점이 첫 모금에서 드러난다. 오렌지의 달콤함이 입안에 퍼지고, 라임의 산미가 바로 단맛을 잡아준다. 스프라이트의 탄산이 입안을 청량하게 헹궈내며, 후미는 의외로 산뜻하고 가볍다.",
        "tip": "꼭 셰이킹으로 라임즙·블루큐라소·보드카를 먼저 섞고, 얼음 채운 잔에 따른 뒤 스프라이트로 마무리.",
        "tags": ["청량한", "달콤", "트로피컬", "푸른빛", "여름"],
    },
    {
        "kr": "카미카제", "en": "Kamikaze", "cat": "vodka", "abv": 25,
        "recipe": [("보드카", "30 ml"), ("트리플 섹", "30 ml"), ("라임 주스", "30 ml")],
        "method": "Shake", "glass": "샷 / Cocktail", "garnish": None,
        "notes": "이름은 일본어 '카미카제(神風, 신의 바람)'에서. 1970년대 미국 해군 술자리에서 비롯되었다는 설이 유력하다. 짧고 강렬하게 마시는 샷 스타일이지만 칵테일 잔으로 받으면 더 오래 음미할 수 있다.",
        "taste": "라임의 강한 산미가 첫 입에 폭발하듯 들어오고, 트리플 섹의 오렌지 단맛이 뒤따른다. 보드카는 알코올의 무게만 더하며 모습을 거의 드러내지 않는다. 1:1:1의 균형 덕분에 25도의 도수임에도 의외로 깔끔하게 넘어간다.",
        "tip": "잘 차게 셰이킹할수록 라임의 산미가 살아나고 알코올감이 누그러진다. 한 잔이 아쉬울 때, 모임의 분위기 전환용으로.",
        "tags": ["드라이", "강한", "강한 시트러스", "샷 스타일", "분위기 전환"],
    },
    {
        "kr": "블랙 러시안", "en": "Black Russian", "cat": "vodka", "abv": 28,
        "recipe": [("보드카", "45 ml"), ("깔루아", "15 ml")],
        "method": "Build", "glass": "Old Fashioned", "garnish": None,
        "notes": "1949년 벨기에 브뤼셀에서 미국 대사를 위해 만들어진 칵테일. 냉전 시대의 미국·러시아 긴장 관계가 이름에 묻어난다. 두 가지 재료의 단순함 속에 깊은 어둠과 위엄이 담긴 식후의 명작.",
        "taste": "깔루아의 진한 커피·카카오 향이 코를 먼저 자극하고, 보드카가 단맛을 깎아내며 어른스러운 무게감을 더한다. 디저트의 단맛이 아닌 드라이한 단맛으로, 묵직하지만 끈적이지 않게 마무리. 깊은 밤의 위로 같은 한 잔.",
        "tip": "우유나 크림을 띄우면 '화이트 러시안'으로 변신. 큰 얼음 한 덩이로 천천히 풀어가며 마실 것.",
        "tags": ["묵직한 바디", "커피향", "카카오", "식후주", "어두운 분위기"],
    },
    {
        "kr": "우우", "en": "Woo Woo", "cat": "vodka", "abv": 13,
        "recipe": [("보드카", "45 ml"), ("피치트리", "22.5 ml"),
                   ("크랜베리 주스", "105 ml"), ("복숭아 비터 (선택)", "3 dash"),
                   ("라임 웨지", "1 ea")],
        "method": "Stir", "glass": "적당한 잔 (Highball 권장)", "garnish": "라임 웨지 (짜서 넣기)",
        "notes": "1980년대 미국에서 유행한 가벼운 칵테일. \"우우~\"라는 감탄사가 절로 나올 만큼 달콤하고 마시기 쉽다는 데서 이름이 붙었다. 분홍빛 컬러가 사랑스러워 파티나 캐주얼한 모임에서 인기.",
        "taste": "복숭아의 농밀한 단맛이 코를 먼저 자극하고, 크랜베리의 산뜻한 산미가 즉시 균형을 잡는다. 보드카는 깊이감만 더하며 거의 드러나지 않고, 복숭아 비터가 향을 한층 입체적으로 만든다. 부드럽게 술이 들어가지만 도수는 의외로 있어 천천히 음미할 것.",
        "tip": "복숭아 비터를 빼도 충분히 맛있지만, 한 방울로 향의 깊이가 확연히 달라진다.",
        "tags": ["새콤달콤", "복숭아향", "베리향", "부드러운", "파티용"],
    },

    # ============ WHISKY ============
    {
        "kr": "갓파더", "en": "Godfather", "cat": "whisky", "abv": 32,
        "recipe": [("스카치 위스키", "45 ml"), ("아마레또", "15 ml")],
        "method": "Build", "glass": "Old Fashioned", "garnish": None,
        "notes": "1972년 영화 〈대부〉가 개봉하던 시기에 등장. 영화 속 코를레오네 집안의 시칠리아 뿌리(아마레또는 이탈리아산)를 떠올리게 한다는 점에서 이름이 붙었다. 위스키 입문자가 위스키의 매력에 빠지는 관문 같은 한 잔.",
        "taste": "스카치의 스모키한 향이 첫 모금부터 강하게 다가오고, 아마레또의 아몬드·바닐라 단맛이 그 거친 면을 부드럽게 감싼다. 시가의 연기, 가죽, 오크 통의 깊이감이 입안에 길게 남으며, 단맛은 디저트적이지 않고 따뜻하게 마무리.",
        "tip": "블렌디드 스카치(조니워커, 시바스 리갈 등)로 만드는 것이 정석. 큰 얼음 한 덩이를 추천.",
        "tags": ["스모키", "묵직한 바디", "견과류", "식후주", "위스키 입문"],
    },

    # ============ RUM ============
    {
        "kr": "다이키리", "en": "Daiquiri", "cat": "rum", "abv": 22,
        "recipe": [("화이트 럼", "60 ml"), ("라임 주스", "20 ml"), ("심플 시럽", "10 ml")],
        "method": "Shake", "glass": "Cocktail", "garnish": None,
        "notes": "1898년 쿠바의 다이키리 광산에서 일하던 미국 광산기사가 만들었다고 전해진다. 어니스트 헤밍웨이가 매일 같은 바에서 다이키리를 마셨다는 일화로 더 유명해졌다. '럼·라임·당'이라는 가장 기본적인 3요소의 균형이 모든 것을 결정한다.",
        "taste": "화이트 럼의 깨끗한 사탕수수 풍미가 베이스가 되고, 신선 라임의 톡 쏘는 산미가 즉시 입안을 깨운다. 심플 시럽의 단맛은 산미를 부드럽게 다듬는 역할만 할 뿐 결코 앞에 나서지 않는다. 단순하기에 어떤 재료의 부족함도 바로 드러난다.",
        "tip": "신선한 라임을 즉석에서 짜는 것이 핵심. 시판 라임 주스로는 그 맛이 나오지 않는다.",
        "tags": ["드라이", "강한 시트러스", "깔끔한", "클래식", "정통파"],
    },
    {
        "kr": "쿠바 리브레", "en": "Cuba Libre", "cat": "rum", "abv": 10,
        "recipe": [("화이트 럼", "45 ml"), ("라임 주스", "10 ml"), ("콜라", "Top up")],
        "method": "Build", "glass": "Highball", "garnish": "라임 웨지",
        "notes": "1900년 쿠바 독립 직후, 미국 군인들이 \"자유 쿠바(Cuba Libre)\"를 외치며 럼에 콜라를 섞어 마신 데서 비롯되었다. 흔히 '럼콕'이라 부르지만 라임 한 조각이 평범한 럼콕과 진짜 쿠바 리브레를 가른다.",
        "taste": "콜라의 익숙한 카라멜 단맛이 베이스이지만, 라임이 그 단맛에 산뜻한 깊이를 더해 갑자기 어른의 음료로 변신한다. 럼은 콜라 속에 녹아들어 부드러운 마무리를 만든다.",
        "tip": "콜라의 단맛에 비해 라임이 모자라면 평범한 럼콕이 된다. 라임 즙을 후하게 짜 넣는 것을 추천.",
        "tags": ["가벼운", "친숙한", "시트러스", "데일리", "여름"],
    },
    {
        "kr": "바카디", "en": "Bacardi Cocktail", "cat": "rum", "abv": 24,
        "recipe": [("바카디 화이트 럼", "60 ml"), ("라임 주스", "20 ml"), ("그레나딘 시럽", "10 ml")],
        "method": "Shake", "glass": "Cocktail", "garnish": None,
        "notes": "1900년대 초 바카디사가 자사 럼을 알리기 위해 만든 칵테일. 1936년 뉴욕 대법원이 \"바카디 칵테일은 반드시 Bacardi 브랜드 럼을 써야 한다\"는 판결까지 내린, 칵테일 역사상 유일무이한 법적 보호 칵테일.",
        "taste": "다이키리에 그레나딘이 더해진 셈인데, 그레나딘의 석류 단맛이 라임의 산미와 만나 핑크빛으로 빛나는 균형을 만든다. 화이트 럼의 가벼움 덕분에 화려한 색에 비해 마우스필은 단정하고 정직하다.",
        "tip": "정통 그레나딘(석류 시럽)을 쓰면 향이 한층 깊다. 시판 그레나딘은 단맛만 강한 경우가 많으니 주의.",
        "tags": ["새콤달콤", "베리·석류", "분홍빛", "클래식", "우아한"],
    },
    {
        "kr": "스카이 다이빙", "en": "Sky Diving", "cat": "rum", "abv": 23,
        "recipe": [("화이트 럼", "30 ml"), ("블루 큐라소", "20 ml"), ("라임 주스", "10 ml")],
        "method": "Shake", "glass": "Cocktail", "garnish": None,
        "notes": "1967년 일본 IBA(국제 바텐더 협회) 칵테일 공모전 수상작. 일본 바텐더 와다 마사요시의 작품으로, 하늘에서 뛰어내릴 때의 그 짙푸른 시야를 표현했다고 한다. 일본 클래식 칵테일의 정수.",
        "taste": "맑고 짙은 푸른빛이 시각의 첫 인상. 블루 큐라소의 오렌지 풍미가 가볍게 입안에 펼쳐지고, 라임의 산미가 그 단맛을 단단히 잡아준다. 화이트 럼은 거의 보이지 않게 깊이만 더한다.",
        "tip": None,
        "tags": ["산뜻한", "시트러스", "푸른빛", "클래식", "단정한"],
    },
    {
        "kr": "블루 헤븐", "en": "Blue Heaven", "cat": "rum", "abv": 12,
        "recipe": [("화이트 럼", "30 ml"), ("아마레또", "15 ml"),
                   ("블루 큐라소", "15 ml"), ("파인애플 주스", "90 ml")],
        "method": "Shake", "glass": "Hurricane", "garnish": "파인애플 · 체리",
        "notes": "파인애플과 푸른 하늘이 만나는 휴양지 풍경을 그린 트로피컬 칵테일. 1970~80년대 카리브 리조트에서 인기를 끌었으며, 사진으로 보면 음료 자체가 바캉스가 된다.",
        "taste": "파인애플 주스의 농밀한 새콤달콤함이 베이스가 되고, 아마레또의 아몬드 향이 트로피컬한 단맛에 견과류의 깊이를 더한다. 블루 큐라소가 시각적 청량감과 오렌지 풍미를 함께 가져오며, 럼은 부드럽게 모두를 연결한다.",
        "tip": "파인애플을 잔 가장자리에 꽂으면 비주얼이 완성된다.",
        "tags": ["트로피컬", "달콤", "파인애플향", "푸른빛", "휴양지 무드"],
    },

    # ============ TEQUILA ============
    {
        "kr": "마가리타", "en": "Margarita", "cat": "tequila", "abv": 23,
        "recipe": [("데킬라", "45 ml"), ("트리플 섹", "15 ml"), ("라임 주스", "15 ml")],
        "method": "Shake", "glass": "Margarita", "garnish": "소금 림 (Salt Rim)",
        "notes": "탄생 설은 여럿이지만, 1948년 멕시코의 한 호스티스가 가수 페기 리에게 헌정했다는 설이 가장 유력. 잔 가장자리의 소금이 단순한 장식이 아니라 풍미의 핵심이라는 점에서, 칵테일이 어떻게 '경험'이 될 수 있는지를 보여준다.",
        "taste": "첫 모금 전에 입술에 닿는 소금이 침샘을 자극하고, 라임의 강한 산미와 트리플 섹의 오렌지 단맛이 한꺼번에 들어온다. 데킬라의 풀·약초 향이 그 위로 떠오르며, 짭짤함이 단맛과 산미를 모두 끌어올린다.",
        "tip": "반쪽만 소금 림으로 만들면 소금 없이도 마실 수 있어 선택권이 생긴다. 멕시코 음식·해산물과 환상의 궁합.",
        "tags": ["짭짤한", "강한 시트러스", "약초향", "클래식", "음식 페어링"],
    },
    {
        "kr": "마타도르", "en": "Matador", "cat": "tequila", "abv": 14,
        "recipe": [("데킬라", "30 ml"), ("파인애플 주스", "60 ml"), ("라임 주스", "15 ml")],
        "method": "Shake", "glass": "Old Fashioned", "garnish": "파인애플",
        "notes": "스페인어로 '투우사'. 멕시코·중남미의 정열을 한 잔에 담은 트로피컬 칵테일이다. 데킬라가 어려워서 못 마신다는 사람도 마타도르는 거뜬히 마실 수 있을 만큼 부드럽다.",
        "taste": "파인애플 주스의 농밀한 단맛이 데킬라의 거친 풀향을 부드럽게 감싸고, 라임이 마지막에 산뜻함을 더한다. 데킬라의 캐릭터는 살아있되 공격적이지 않게 다듬어진, 균형 잘 잡힌 한 잔.",
        "tip": "100% 아가베 데킬라(블랑코)를 쓰면 풀향이 더 살아난다.",
        "tags": ["트로피컬", "부드러운", "파인애플향", "데킬라 입문", "황금빛"],
    },
    {
        "kr": "멕시콜라", "en": "Mexicola", "cat": "tequila", "abv": 10,
        "recipe": [("데킬라", "45 ml"), ("라임 주스", "15 ml"), ("콜라", "Top up")],
        "method": "Build", "glass": "Highball", "garnish": "라임 웨지",
        "notes": "쿠바 리브레가 럼콕이라면, 멕시콜라는 '데킬라콕'. 멕시코의 콜라 사랑(세계 1인당 콜라 소비량 1위)을 담은 칵테일이기도 하다. 럼콕보다 한층 거친 매력이 있다.",
        "taste": "콜라의 카라멜 단맛 뒤로 데킬라의 풀·흙 향이 살짝 비치는 독특한 조합. 라임의 산미가 콜라의 단맛을 잡아주며, 데킬라가 럼보다 강한 캐릭터로 입안에 흔적을 남긴다.",
        "tip": "데킬라 블랑코보다는 레포사도(오크통 숙성)가 콜라의 카라멜과 더 잘 어울린다.",
        "tags": ["가벼운", "친숙한", "데킬라의 흔적", "데일리", "캐주얼"],
    },

    # ============ GIN ============
    {
        "kr": "김렛", "en": "Gimlet", "cat": "gin", "abv": 27,
        "recipe": [("진", "60 ml"), ("라임 주스", "15 ml"), ("심플 시럽", "10 ml")],
        "method": "Shake / Stir", "glass": "Cocktail", "garnish": None,
        "notes": "19세기 영국 해군이 괴혈병 예방을 위해 라임 주스에 진을 섞어 마신 데서 유래. 군의관 토머스 김렛 경의 이름이 그대로 칵테일이 되었다. 레이먼드 챈들러의 〈긴 이별〉에 등장하는 \"진과 로즈 라임 코디얼 반반\"의 김렛은 하드보일드 문학의 상징과도 같다.",
        "taste": "진의 주니퍼·고수·감귤 등 보태니컬 향이 전면에 펼쳐지고, 라임의 산미가 그 향을 한층 또렷하게 부각시킨다. 단맛은 최소로만 들어가 진의 캐릭터를 가리지 않는다. 드라이하고 향이 강한, 진의 진수를 느낄 수 있는 한 잔.",
        "tip": "진의 향이 좋은 브랜드일수록 그 차이가 크게 난다.",
        "tags": ["드라이", "강한 보태니컬", "강한 시트러스", "클래식", "진 애호가용"],
    },
    {
        "kr": "화이트 레이디", "en": "White Lady", "cat": "gin", "abv": 25,
        "recipe": [("진", "30 ml"), ("트리플 섹", "20 ml"), ("레몬 주스", "10 ml"),
                   ("계란 흰자 (옵션)", "1 ea")],
        "method": "Shake", "glass": "Cocktail", "garnish": None,
        "notes": "1929년 런던 사보이 호텔의 전설적인 바텐더 해리 크래독이 정착시킨 클래식. 1차 세계대전 후 사교계의 우아한 여인들이 즐겨 마시며 이름을 얻었다. 계란 흰자가 만드는 비단 같은 거품층은 우아함의 정점.",
        "taste": "흰자 거품이 입술에 먼저 닿으며 부드러운 마우스필을 선사한다. 진의 허브향, 트리플 섹의 오렌지 단맛, 레몬의 산미가 정교한 삼각형을 이루며 균형 잡힌 풍미. 새콤하지만 결코 자극적이지 않고, 비단처럼 매끄럽게 넘어간다.",
        "tip": "흰자를 넣으면 '드라이 셰이크'(얼음 없이 먼저 흔들기) → 얼음 추가 → 본격 셰이크 순서. 신선한 계란만 사용할 것.",
        "tags": ["우아한", "시트러스", "비단 같은", "클래식", "거품"],
    },

    # ============ MULTI ============
    {
        "kr": "A.M.F", "en": "Adios Mother F***er", "cat": "multi", "abv": 20,
        "recipe": [("보드카", "15 ml"), ("진", "15 ml"), ("화이트 럼", "15 ml"),
                   ("데킬라", "15 ml"), ("블루 큐라소", "15 ml"),
                   ("스위트 앤 사워", "30 ml"), ("스프라이트", "Top up")],
        "method": "Build", "glass": "Hurricane", "garnish": "레몬",
        "notes": "롱아일랜드 아이스티의 푸른 사촌. \"안녕히 잘 가시오, 어머니\"라는 짓궂은 이름 그대로, 한 잔이면 정신이 작별을 고한다고 알려진 도수 폭탄. 미국 대학가에서 악명 높은 칵테일.",
        "taste": "달콤한 푸른빛에 속아 한 모금 머금으면, 스위트앤사워의 새콤달콤함과 스프라이트의 청량감이 먼저 다가온다. 5종의 증류주는 그 단맛에 완벽하게 숨어 알코올감이 거의 느껴지지 않는다. 한 잔을 다 비울 무렵 발이 풀리기 시작하는, 위장의 명수.",
        "tip": "달콤한 푸른빛에 속아 빠르게 마시면 위험. 천천히, 그리고 한 잔만.",
        "tags": ["강한", "달콤", "푸른빛", "위장의 명수", "주의 요망"],
    },
    {
        "kr": "롱아일랜드 아이스티", "en": "Long Island Iced Tea", "cat": "multi", "abv": 22,
        "recipe": [("보드카", "15 ml"), ("진", "15 ml"), ("화이트 럼", "15 ml"),
                   ("데킬라", "15 ml"), ("트리플 섹", "15 ml"),
                   ("레몬 주스", "15 ml"), ("콜라", "Top up")],
        "method": "Build", "glass": "Highball / Hurricane", "garnish": "레몬 웨지",
        "notes": "1972년 미국 뉴욕 롱아일랜드의 바텐더 로버트 (밥) 버트가 만들었다고 알려진 클래식. 5종의 증류주가 들어있음에도 아이스티처럼 보이도록 콜라와 레몬으로 위장한, 1920년대 금주법 시대 전통의 현대적 계승.",
        "taste": "겉모습은 평범한 아이스티지만, 첫 모금부터 묵직한 알코올감이 콜라·레몬의 단맛 뒤에서 슬쩍 모습을 드러낸다. 진의 허브, 데킬라의 흙냄새, 럼의 사탕수수가 각자 자리를 잡으며 복합적인 풍미. 마실수록 진해지는 알코올 자국이 인상적.",
        "tip": "재료가 많아 보여도 사실은 모든 증류주가 같은 양(15ml)이라 외우기 쉽다.",
        "tags": ["강한", "친숙한 외모", "복합적", "위장의 명수", "파티용"],
    },
    {
        "kr": "롱비치 아이스티", "en": "Long Beach Iced Tea", "cat": "multi", "abv": 22,
        "recipe": [("보드카", "15 ml"), ("진", "15 ml"), ("화이트 럼", "15 ml"),
                   ("데킬라", "15 ml"), ("트리플 섹", "15 ml"),
                   ("레몬 주스", "15 ml"), ("크랜베리 주스", "Top up")],
        "method": "Build", "glass": "Highball / Hurricane", "garnish": "레몬",
        "notes": "롱아일랜드의 콜라를 크랜베리 주스로 바꾼 사촌. 캘리포니아 롱비치의 분홍빛 노을을 닮았다. 우아한 외모로 손쉽게 마시게 되지만, 도수는 롱아일랜드와 똑같다는 점이 함정.",
        "taste": "크랜베리의 산뜻한 산미가 베이스가 되어 콜라보다 한층 가볍게 시작한다. 5종의 증류주는 베리의 향에 잘 녹아들어 알코올감이 더 잘 숨겨진다. 분홍빛에 속아 더 위험할 수 있는 한 잔.",
        "tip": "여성에게 권하기 좋은 외모지만, 도수를 반드시 미리 알려줄 것.",
        "tags": ["강한", "우아한", "분홍빛", "베리향", "함정"],
    },

    # ============ LIQUEUR ============
    {
        "kr": "깔루아 콕", "en": "Kahlua & Coke", "cat": "liqueur", "abv": 7,
        "recipe": [("깔루아", "45 ml"), ("콜라", "Top up")],
        "method": "Build", "glass": "Highball", "garnish": None,
        "notes": "가장 단순한 커피 칵테일. 깔루아는 멕시코산 커피 리큐어로, 콜라의 카라멜 향과 만나 자연스러운 조합을 이룬다. 칵테일 입문자, 단맛을 좋아하는 사람에게 안성맞춤.",
        "taste": "콜라의 카라멜·바닐라 향에 깔루아의 진한 커피 향이 얹히며 마치 커피맛 콜라 같은 첫인상. 단맛이 도드라지지만 끝맛에 커피의 약간 쌉쌀한 흔적이 남아 디저트로 마실 만하다.",
        "tip": "디저트와 함께, 혹은 디저트 대신. 도수가 낮아 식사 후 가볍게.",
        "tags": ["가벼운", "달콤", "커피향", "디저트", "입문용"],
    },
    {
        "kr": "깔루아 말차 밀크", "en": "Kahlua Matcha Milk", "cat": "liqueur", "abv": 5,
        "recipe": [("깔루아 말차", "30 ml"), ("우유", "90 ml"), ("말차 파우더", "1 tsp")],
        "method": "Build (Stir)", "glass": "Old Fashioned", "garnish": "말차 가루 (옵션)",
        "notes": "깔루아 브랜드에서 출시한 한정판 '말차 리큐어'를 이용한 동양 풍 칵테일. 일본 카페의 말차 라테가 부드럽게 어른의 음료로 변신한 모습. 디저트 자리에 잘 어울린다.",
        "taste": "우유의 부드러움이 입안을 감싸고, 말차의 쌉쌀한 풀향이 단맛을 깔끔하게 잡아준다. 깔루아 말차는 일반 깔루아보다 단맛이 절제되어 있어 라테 같은 균형이 자연스럽게 형성된다. 마지막 모금까지 묵직하고 크리미.",
        "tip": "'깔루아 말차'는 깔루아 브랜드의 말차 리큐어 제품(별개 상품). 말차 파우더는 미리 소량의 우유에 잘 풀어두면 덩어리 없이 부드럽다.",
        "tags": ["크리미", "말차향", "달콤", "디저트", "동양풍"],
    },
    {
        "kr": "카시스 오렌지", "en": "Cassis Orange", "cat": "liqueur", "abv": 7,
        "recipe": [("크렘 드 카시스", "30 ml"), ("오렌지 주스", "90 ml")],
        "method": "Build", "glass": "Highball", "garnish": "오렌지 슬라이스",
        "notes": "일본·한국 이자카야의 부동의 베스트셀러. 크렘 드 카시스는 검은 까치밥나무 열매(블랙커런트)로 만든 프랑스 디종 지방의 리큐어로, 오렌지 주스와의 조합이 가장 친숙하다. 술 못 마시는 사람도 부담 없이 즐길 수 있는 첫 칵테일.",
        "taste": "오렌지 주스의 산뜻한 단맛이 입안을 가득 채우고, 그 안에 카시스의 깊은 베리 향이 보랏빛 그림자처럼 깔린다. 알코올감은 거의 느껴지지 않고, 마치 고급 과일 주스를 마시는 듯한 부드러운 풍미.",
        "tip": "100% 오렌지 주스가 풍미가 더 깊다. 시각적으로는 카시스가 바닥에 가라앉게 두면 자연스러운 그라데이션이 만들어진다.",
        "tags": ["가벼운", "베리향", "과일향", "데일리", "이자카야"],
    },
    {
        "kr": "카시스 소다", "en": "Cassis Soda", "cat": "liqueur", "abv": 5,
        "recipe": [("크렘 드 카시스", "30 ml"), ("소다 워터", "120 ml")],
        "method": "Build", "glass": "Highball", "garnish": "레몬 트위스트",
        "notes": "카시스 오렌지의 더 가벼운 자매. 식전주(Aperitif)로 식욕을 자극하기에 좋고, 더운 여름 한낮에도 부담 없이 마실 수 있다.",
        "taste": "탄산이 코를 먼저 자극하고, 그 위로 카시스의 베리 향이 가볍게 퍼진다. 단맛이 절제되어 있어 음식 맛을 가리지 않으며, 레몬 트위스트의 시트러스 향이 마지막을 정리한다.",
        "tip": "탄산은 차게, 카시스도 차게 보관하면 거품이 오래 유지된다.",
        "tags": ["가벼운", "청량한", "베리향", "식전주", "여름"],
    },
    {
        "kr": "보치 볼", "en": "Bocce Ball", "cat": "liqueur", "abv": 8,
        "recipe": [("아마레또", "30 ml"), ("오렌지 주스", "90 ml"), ("소다 워터", "30 ml")],
        "method": "Build", "glass": "Highball", "garnish": "오렌지 슬라이스",
        "notes": "이탈리아 잔디 볼링 'Bocce'에서 이름을 따왔다. 아마레또(이탈리아의 아몬드 리큐어)와 오렌지의 만남은 카시스 오렌지의 이탈리아 사촌이라 할 만하다.",
        "taste": "오렌지 주스의 새콤달콤함이 베이스가 되고, 아마레또의 따뜻한 아몬드·살구 향이 부드럽게 얹힌다. 소다의 탄산이 가벼움을 더하며, 끝맛에 견과류의 깊이가 길게 남는다.",
        "tip": "아마레또는 디사론노 브랜드가 가장 보편적이고 향이 균형 잡혀 있다.",
        "tags": ["부드러운", "아몬드향", "오렌지", "데일리", "이탈리아"],
    },
    {
        "kr": "아페롤 스프리츠", "en": "Aperol Spritz", "cat": "liqueur", "abv": 9,
        "recipe": [("아페롤", "60 ml"), ("프로세코", "90 ml"), ("소다 워터", "30 ml")],
        "method": "Build", "glass": "Wine", "garnish": "오렌지 슬라이스",
        "notes": "이탈리아 베니스의 여름 풍경 그 자체. 1919년 이탈리아 파도바에서 탄생한 아페롤(약초·시트러스 리큐어)에 프로세코 스파클링 와인을 더한 식전주. '3-2-1' 비율로 외우면 쉽다.",
        "taste": "프로세코의 거품이 입안에서 톡 터지며 시작되고, 아페롤의 쌉쌀한 약초·오렌지·자몽 풍미가 그 위에 펼쳐진다. 단맛이 절제되어 있고 끝맛에 자몽 껍질 같은 쌉쌀함이 길게 남는다. 식욕을 자극하는, 식전주의 정석.",
        "tip": "큼직한 와인잔에 얼음을 가득 채우고 오렌지 슬라이스를 풍성하게.",
        "tags": ["청량한", "쌉쌀", "시트러스", "식전주", "여름 점심"],
    },
    {
        "kr": "아페롤 입문", "en": "Aperol Entrée", "cat": "liqueur", "abv": 22,
        "recipe": [("아페롤", "60 ml"), ("진", "30 ml"),
                   ("레몬 주스 (반개 착즙)", "~15 ml"), ("설탕 시럽", "7.5 ml"),
                   ("앙고스투라 비터", "1-2 dash")],
        "method": "Shake", "glass": "Cocktail", "garnish": "레몬 필",
        "notes": "아페롤 = 가벼운 식전주, 라는 고정관념을 깨는 한 잔. 진과 비터까지 더해 아페롤의 깊이를 본격적으로 드러낸다. 가벼운 스프리츠가 아닌, 식사 시작 전 진중하게 마실 만한 묵직한 칵테일.",
        "taste": "아페롤의 쌉쌀한 약초향이 진의 보태니컬과 만나 한층 복합적인 풍미를 만든다. 레몬의 산미가 그 무게를 가볍게 끌어올리고, 앙고스투라 비터의 향신료 노트가 끝맛에 깊이를 더한다. 한 모금마다 다른 향이 발견되는, 음미하는 칵테일.",
        "tip": "레몬 필은 잔 위에서 짜내 오일을 떨어뜨린 뒤 가니쉬로.",
        "tags": ["묵직한 바디", "쌉쌀", "복합적", "허브향", "진중한"],
    },
    {
        "kr": "블루 사파이어", "en": "Blue Sapphire", "cat": "liqueur", "abv": 10,
        "recipe": [("피치트리", "15 ml"), ("말리부", "15 ml"),
                   ("블루 큐라소", "15 ml"), ("스위트 앤 사워", "15 ml"),
                   ("스프라이트", "Top up")],
        "method": "Shake → Build", "glass": "Highball", "garnish": "레몬 · 체리",
        "notes": "푸른 보석처럼 빛나는 색이 시선을 사로잡는 트로피컬 칵테일. 피치 + 코코넛 + 블루 큐라소의 트리오는 시각·풍미 모두 화려하다.",
        "taste": "복숭아의 달콤한 향이 첫 모금을 부드럽게 열고, 말리부의 코코넛이 부드럽게 깔린다. 블루 큐라소의 오렌지 향과 스위트앤사워의 산미가 그 위에 입체감을 더하며, 스프라이트의 탄산이 끝맛을 청량하게 마무리.",
        "tip": "셰이킹한 내용물을 잔에 따른 뒤 스프라이트로 채워야 거품이 살아난다.",
        "tags": ["달콤", "트로피컬", "복숭아·코코넛", "푸른빛", "비주얼"],
    },

    # ============ SIGNATURE ============
    {
        "kr": "조엽수림", "en": "Shōyōjurin · 照葉樹林", "cat": "signature", "abv": 4,
        "recipe": [("헤르메스 말차", "30 ml"), ("우롱차", "Top up")],
        "method": "Build", "glass": "310ml Highball", "garnish": None,
        "notes": "'조엽수림(常緑闊葉樹林)'은 일본 남부의 짙은 녹색 활엽수림을 가리키는 식물학 용어. 그 깊고 단정한 숲의 색을 한 잔에 담은, 거의 차에 가까운 일본식 칵테일.",
        "taste": "우롱차의 구수하고 따뜻한 향이 베이스가 되고, 그 위로 헤르메스 말차의 진한 쌉쌀함이 천천히 떠오른다. 알코올감은 거의 없어 차를 마시듯 부드럽게 넘어가지만, 끝맛에 말차의 깊은 흙·풀향이 길게 남는다.",
        "tip": "우롱차는 차게 식혀서 사용. 일식·한식 어디에나 어울리고, 술이 약한 손님에게 권하기 좋다.",
        "tags": ["가벼운", "차향", "쌉쌀", "단정한", "일본풍"],
    },
    {
        "kr": "오션 워터", "en": "Ocean Water", "cat": "signature", "abv": 11,
        "recipe": [("화이트 럼", "30 ml"), ("코코넛 럼 (말리부)", "15 ml"),
                   ("블루 큐라소", "15 ml"), ("스프라이트", "Top up")],
        "method": "Build", "glass": "Highball", "garnish": "라임 웨지",
        "notes": "미국 패스트푸드 체인 Sonic의 푸른 음료 '오션 워터'에 코코넛 럼을 더해 칵테일화한 버전. 깔끔하고 시원해, 한여름 오후 해변에 놓아두면 어울릴 한 잔.",
        "taste": "코코넛 럼의 부드러운 단맛이 먼저 입안에 퍼지고, 블루 큐라소의 오렌지 향과 화이트 럼의 깔끔함이 그 뒤를 잇는다. 스프라이트의 탄산이 모든 것을 깨끗하게 헹궈내며 마무리.",
        "tip": "라임을 즙으로 짜 넣으면 단맛이 한층 정리된다.",
        "tags": ["청량한", "트로피컬", "코코넛", "푸른빛", "휴양지"],
    },
    {
        "kr": "꿈", "en": "Dream · 夢", "cat": "signature", "abv": 26,
        "recipe": [("보드카", "40 ml"), ("피치 리큐어", "10 ml"),
                   ("그랑 마니에르", "10 ml"), ("블루 큐라소", "1 tsp"),
                   ("레몬즙", "1 tsp")],
        "method": "Shake", "glass": "Martini", "garnish": None,
        "notes": "맑은 푸른빛이 꿈속을 떠다니는 듯한 인상을 주는 시그니처 칵테일. 그랑 마니에르(오렌지 코냑 리큐어)가 단순한 푸른 칵테일을 신비롭고 깊이 있게 변화시킨다.",
        "taste": "첫 모금에 피치의 달콤한 향과 그랑 마니에르의 진한 오렌지 코냑 풍미가 동시에 펼쳐진다. 보드카가 그 단맛을 절제시키며 드라이하게 마무리하고, 레몬 한 방울이 가벼운 산미로 향을 단정하게 잡는다.",
        "tip": "마티니 글라스에 담아야 푸른빛이 가장 아름답게 드러난다.",
        "tags": ["강한", "신비로운", "오렌지·복숭아", "푸른빛", "음미용"],
    },
    {
        "kr": "그린 필드", "en": "Green Field", "cat": "signature", "abv": 14,
        "recipe": [("헤르메스 말차 리큐어", "45 ml"), ("보드카", "15 ml"), ("우유", "15 ml")],
        "method": "Shake", "glass": "Martini", "garnish": None,
        "notes": "이름 그대로 진한 녹차밭의 한 컷을 옮긴 듯한 한 잔. 일본의 말차 리큐어 문화가 만든 크리미한 디저트 칵테일이다.",
        "taste": "말차 리큐어의 진한 쌉쌀함이 우유로 부드럽게 다듬어져 마치 말차 라테에 알코올을 더한 듯한 풍미. 보드카가 끝맛을 깔끔하게 정리하며 단맛이 무겁지 않게 마무리된다. 디저트 대신 마실 만한 만족감.",
        "tip": "말차 리큐어와 우유는 분리되기 쉬우니 충분히 강하게 셰이크. 잔도 미리 차게 식혀두면 더 좋다.",
        "tags": ["크리미", "말차향", "쌉쌀", "디저트", "일본풍"],
    },

    # ============ MOCKTAIL ============
    {
        "kr": "세인트 클레멘스", "en": "St. Clement's", "cat": "mocktail", "abv": 0,
        "recipe": [("오렌지 주스", "90 ml"), ("비터 레몬 (또는 토닉)", "90 ml")],
        "method": "Build", "glass": "Highball", "garnish": "오렌지 슬라이스",
        "notes": "영국 동요 'Oranges and Lemons, say the bells of St. Clement's'에서 이름을 따온 클래식 목테일. 알코올 없이도 칵테일의 풍미와 격조를 갖춘, 운전·임신·금주일 손님을 위한 정통 답안.",
        "taste": "오렌지의 자연스러운 단맛이 먼저 입안을 채우고, 비터 레몬의 쌉쌀한 산미가 그 단맛을 한층 어른스럽게 잡아준다. 단순한 주스와는 분명히 다른, 입체적이고 정돈된 풍미.",
        "tip": "비터 레몬이 없으면 토닉 워터로 대체. 토닉이 더 가볍고 비터 레몬이 더 쌉쌀하다.",
        "tags": ["산뜻한", "시트러스", "쌉쌀", "논알콜", "어른스러운"],
    },
    {
        "kr": "셜리 템플", "en": "Shirley Temple", "cat": "mocktail", "abv": 0,
        "recipe": [("그레나딘 시럽", "15 ml"), ("라임 즙", "10 ml"),
                   ("진저에일", "Top up")],
        "method": "Build", "glass": "Highball", "garnish": "마라스키노 체리",
        "notes": "1930년대 헐리우드 아역 스타 셜리 템플(당시 5-7세)을 위해 헐리우드의 한 바텐더가 만들어준 클래식 목테일. 어른들이 칵테일을 마실 때 아이도 함께 \"진짜\" 잔을 들 수 있게 해준다는 의미에서 사랑받아 왔다.",
        "taste": "진저에일의 톡 쏘는 생강 향이 시작이고, 그레나딘의 석류 단맛이 분홍빛으로 그 위에 퍼진다. 라임의 산미가 단맛을 정리하며 입안을 깔끔하게 만들고, 마지막에 마라스키노 체리를 한 알 깨물면 달콤한 마무리.",
        "tip": "얼음을 채운 잔에 그레나딘과 라임즙을 먼저 넣고, 진저에일을 부은 뒤 잘 저어준다.",
        "tags": ["달콤", "진저향", "분홍빛", "논알콜", "온 가족용"],
    },
]


# ============================================================
# CSS — desktop base + mobile optimization + sticky nav
# ============================================================

BASE_CSS = """
:root {
  --bg-deep: #15100c;
  --bg-card: #1f1813;
  --bg-card-elev: #2a2018;
  --text-primary: #f0e6d2;
  --text-muted: #b8a888;
  --text-faint: #7a6a55;
  --gold: #c8a96a;
  --gold-bright: #e4c785;
  --gold-deep: #8b7340;
  --crimson: #8b3a3a;
  --border-faint: rgba(200, 169, 106, 0.15);
  --border: rgba(200, 169, 106, 0.3);
}
* { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
html { scroll-behavior: smooth; scroll-padding-top: 70px; }
body {
  background: var(--bg-deep);
  background-image:
    radial-gradient(ellipse at top, rgba(139, 115, 64, 0.08) 0%, transparent 60%),
    radial-gradient(ellipse at bottom, rgba(139, 58, 58, 0.05) 0%, transparent 60%);
  color: var(--text-primary);
  font-family: 'Lora', 'Noto Serif KR', serif;
  line-height: 1.6;
  min-height: 100vh;
  position: relative;
  -webkit-font-smoothing: antialiased;
}
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='0.9' numOctaves='2' seed='2'/><feColorMatrix values='0 0 0 0 0.78  0 0 0 0 0.66  0 0 0 0 0.42  0 0 0 0.035 0'/></filter><rect width='200' height='200' filter='url(%23n)'/></svg>");
  pointer-events: none;
  z-index: 1;
  opacity: 0.7;
}

/* ---------- STICKY CATEGORY NAV ---------- */
.cat-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(21, 16, 12, 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-faint);
  overflow-x: auto;
  overflow-y: hidden;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}
.cat-nav::-webkit-scrollbar { display: none; }
.cat-nav-inner {
  display: flex;
  gap: 28px;
  padding: 14px 32px;
  white-space: nowrap;
  width: max-content;
  min-width: 100%;
  justify-content: center;
}
.cat-nav a {
  font-family: 'Cormorant Garamond', serif;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  font-size: 13px;
  color: var(--text-muted);
  text-decoration: none;
  padding: 6px 2px;
  border-bottom: 1.5px solid transparent;
  transition: color 0.2s ease, border-color 0.2s ease;
  font-weight: 500;
}
.cat-nav a:hover, .cat-nav a.active {
  color: var(--gold);
  border-bottom-color: var(--gold);
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 56px 48px 100px;
  position: relative;
  z-index: 2;
}

/* ---------- COVER ---------- */
.cover {
  text-align: center;
  padding: 60px 0 80px;
  position: relative;
  border-bottom: 1px solid var(--border-faint);
  margin-bottom: 64px;
}
.cover-ornament {
  font-family: 'Italianno', cursive;
  color: var(--gold);
  font-size: 72px;
  line-height: 1;
  margin-bottom: 18px;
  opacity: 0.85;
}
.cover-eyebrow {
  font-family: 'Cormorant Garamond', serif;
  font-size: 13px;
  letter-spacing: 0.6em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 24px;
  font-weight: 500;
}
.cover h1 {
  font-family: 'Noto Serif KR', 'Cormorant Garamond', serif;
  font-weight: 300;
  font-size: clamp(40px, 7vw, 88px);
  color: var(--text-primary);
  line-height: 1.05;
  letter-spacing: -0.02em;
  margin-bottom: 20px;
}
.cover h1 em {
  font-family: 'Italianno', cursive;
  font-style: normal;
  color: var(--gold-bright);
  font-weight: 400;
  font-size: 1.3em;
  line-height: 0.8;
  display: inline-block;
  transform: translateY(0.05em);
}
.cover-subtitle {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-size: 20px;
  color: var(--text-muted);
  letter-spacing: 0.08em;
  margin-top: 8px;
}
.cover-meta {
  margin-top: 40px;
  display: flex;
  justify-content: center;
  gap: 36px;
  flex-wrap: wrap;
  color: var(--text-faint);
  font-size: 12px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
}
.cover-meta span { display: flex; align-items: center; gap: 10px; }
.cover-meta span::before { content: '✦'; color: var(--gold); }
.cover-edition {
  margin-top: 28px;
  font-family: 'Italianno', cursive;
  color: var(--gold-bright);
  font-size: 30px;
  letter-spacing: 0.05em;
}
.cover-edition .label {
  font-size: 12px;
  letter-spacing: 0.4em;
  font-family: 'Cormorant Garamond', serif;
  color: var(--text-faint);
  text-transform: uppercase;
  display: block;
  margin-top: 6px;
}

/* ---------- SECTIONS ---------- */
.section { margin-bottom: 80px; scroll-margin-top: 70px; }
.section-header {
  text-align: center;
  margin-bottom: 44px;
  position: relative;
}
.section-header::before, .section-header::after {
  content: '';
  position: absolute;
  top: 50%;
  width: 80px;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
}
.section-header::before { left: calc(50% - 220px); }
.section-header::after { right: calc(50% - 220px); }
.section-number {
  font-family: 'Italianno', cursive;
  color: var(--gold);
  font-size: 44px;
  line-height: 0.8;
  margin-bottom: 6px;
}
.section-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 32px;
  font-weight: 500;
  letter-spacing: 0.15em;
  color: var(--text-primary);
  text-transform: uppercase;
}
.section-title-kr {
  font-family: 'Noto Serif KR', serif;
  color: var(--gold);
  font-size: 13px;
  font-weight: 400;
  letter-spacing: 0.4em;
  margin-top: 10px;
}

/* ---------- ABV BADGE ---------- */
.abv-badge {
  flex-shrink: 0;
  width: 54px;
  height: 54px;
  border: 1px solid var(--gold);
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: var(--gold);
  background: rgba(200, 169, 106, 0.05);
}
.abv-badge .pct {
  font-family: 'Cormorant Garamond', serif;
  font-size: 21px;
  font-weight: 600;
  line-height: 1;
}
.abv-badge .label {
  font-size: 9px;
  letter-spacing: 0.15em;
  margin-top: 2px;
  opacity: 0.75;
}
.abv-badge.zero { border-color: var(--text-faint); color: var(--text-faint); }
.abv-badge.high { border-color: var(--crimson); color: #d97b7b; background: rgba(139, 58, 58, 0.1); }

/* ---------- COCKTAIL CARDS ---------- */
.cocktail {
  background: var(--bg-card);
  border: 1px solid var(--border-faint);
  position: relative;
  transition: border-color 0.3s ease;
  page-break-inside: avoid;
}
.cocktail:hover { border-color: var(--border); }
.cocktail-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border-faint);
}
.cocktail-name {
  font-family: 'Noto Serif KR', serif;
  font-size: 25px;
  font-weight: 500;
  color: var(--text-primary);
  line-height: 1.2;
  margin-bottom: 4px;
}
.cocktail-name-en {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-size: 13px;
  letter-spacing: 0.2em;
  color: var(--gold);
  text-transform: uppercase;
}
.meta-tag {
  font-family: 'Cormorant Garamond', serif;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text-muted);
  padding: 4px 10px;
  border: 1px solid var(--border-faint);
  background: rgba(0,0,0,0.2);
}
.meta-tag.method { color: var(--gold); border-color: var(--border); }
.cocktail-notes {
  font-family: 'Noto Serif KR', serif;
  font-size: 14.5px;
  line-height: 1.75;
  color: var(--text-muted);
}
.cocktail-taste {
  font-family: 'Noto Serif KR', serif;
  font-size: 14.5px;
  line-height: 1.8;
  color: var(--gold-bright);
  padding: 14px 16px;
  border-left: 2px solid var(--gold);
  background: rgba(200, 169, 106, 0.04);
  margin: 18px 0;
}
.cocktail-taste::before {
  content: '— Taste —';
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-weight: 600;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  font-size: 10px;
  color: var(--gold);
  display: block;
  margin-bottom: 6px;
}

/* ---------- QUICK INDEX (전체 칵테일 목록) ---------- */
.quick-index {
  margin-bottom: 80px;
  padding: 40px 44px;
  border: 1px solid var(--border-faint);
  background: linear-gradient(180deg, rgba(200, 169, 106, 0.03), transparent);
  position: relative;
}
.quick-index::before, .quick-index::after {
  content: '';
  position: absolute;
  width: 22px;
  height: 22px;
  border: 1px solid var(--gold);
}
.quick-index::before { top: -1px; left: -1px; border-right: none; border-bottom: none; }
.quick-index::after  { bottom: -1px; right: -1px; border-left: none; border-top: none; }
.quick-index-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 12px;
  letter-spacing: 0.5em;
  text-transform: uppercase;
  color: var(--gold);
  text-align: center;
  margin-bottom: 32px;
}
.qi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 26px 36px;
}
.qi-cat-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 13px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border-faint);
}
.qi-cat-name-kr {
  font-family: 'Noto Serif KR', serif;
  font-size: 11px;
  font-weight: 400;
  color: var(--text-faint);
  letter-spacing: 0.2em;
  margin-left: 8px;
}
.qi-list { list-style: none; }
.qi-list li { margin-bottom: 4px; }
.qi-list a {
  font-family: 'Noto Serif KR', serif;
  color: var(--text-primary);
  text-decoration: none;
  font-size: 14.5px;
  display: block;
  padding: 4px 0;
  transition: color 0.2s ease, padding-left 0.2s ease;
}
.qi-list a:hover {
  color: var(--gold-bright);
  padding-left: 8px;
}
.cocktail { scroll-margin-top: 80px; }

/* ---------- BACK TO LIST BUTTON ---------- */
.back-to-list {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 18px;
  font-family: 'Cormorant Garamond', serif;
  font-size: 11px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--text-faint);
  text-decoration: none;
  padding: 6px 14px;
  border: 1px solid var(--border-faint);
  transition: color 0.2s ease, border-color 0.2s ease;
}
.back-to-list:hover {
  color: var(--gold);
  border-color: var(--border);
}
.back-to-list::before {
  content: '←';
  font-size: 13px;
}

/* ---------- FOOTER ---------- */
.footer {
  text-align: center;
  margin-top: 100px;
  padding-top: 44px;
  border-top: 1px solid var(--border-faint);
}
.footer-ornament {
  font-family: 'Italianno', cursive;
  color: var(--gold);
  font-size: 56px;
  line-height: 1;
  margin-bottom: 14px;
}
.footer p {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  color: var(--text-muted);
  font-size: 15px;
  letter-spacing: 0.1em;
}
.footer .small {
  margin-top: 14px;
  font-size: 10.5px;
  letter-spacing: 0.4em;
  text-transform: uppercase;
  color: var(--text-faint);
  font-style: normal;
}

/* ============================================================
   MOBILE — < 720px
   ============================================================ */
@media (max-width: 720px) {
  html { scroll-padding-top: 56px; }
  .container { padding: 24px 16px 60px; }

  .cat-nav { border-bottom: 1px solid var(--border); }
  .cat-nav-inner {
    padding: 10px 16px;
    gap: 20px;
    justify-content: flex-start;
  }
  .cat-nav a {
    font-size: 11.5px;
    letter-spacing: 0.15em;
    padding: 5px 2px;
  }

  .cover { padding: 32px 0 44px; margin-bottom: 36px; }
  .cover-ornament { font-size: 52px; margin-bottom: 12px; }
  .cover-eyebrow { font-size: 10px; letter-spacing: 0.4em; margin-bottom: 16px; }
  .cover h1 { font-size: 40px; margin-bottom: 14px; }
  .cover-subtitle { font-size: 15px; letter-spacing: 0.05em; }
  .cover-meta { gap: 14px 22px; margin-top: 28px; font-size: 10px; letter-spacing: 0.2em; }
  .cover-meta span::before { font-size: 9px; }
  .cover-edition { font-size: 24px; margin-top: 22px; }
  .cover-edition .label { font-size: 10px; letter-spacing: 0.3em; margin-top: 4px; }

  .section { margin-bottom: 52px; }
  .section-header { margin-bottom: 28px; }
  .section-header::before, .section-header::after { display: none; }
  .section-number { font-size: 32px; }
  .section-title { font-size: 24px; letter-spacing: 0.1em; }
  .section-title-kr { font-size: 11px; letter-spacing: 0.3em; }

  .cocktail-grid { grid-template-columns: 1fr !important; gap: 16px !important; }
  .cocktail { padding: 22px 18px !important; }
  .cocktail-head { gap: 10px; padding-bottom: 12px; }
  .cocktail-name { font-size: 21px; }
  .cocktail-name-en { font-size: 11px; letter-spacing: 0.15em; }
  .abv-badge { width: 46px; height: 46px; }
  .abv-badge .pct { font-size: 18px; }
  .abv-badge .label { font-size: 8px; }

  .cocktail-notes { font-size: 13.5px; line-height: 1.7; }
  .cocktail-taste { font-size: 13.5px; line-height: 1.7; padding: 12px 14px; margin: 14px 0; }
  .cocktail-taste::before { font-size: 9px; }

  .meta-tag { font-size: 10px; padding: 3px 8px; letter-spacing: 0.15em; }

  /* Quick Index — mobile */
  .quick-index { padding: 22px 18px; margin-bottom: 40px; }
  .quick-index-title { font-size: 11px; letter-spacing: 0.35em; margin-bottom: 22px; }
  .qi-grid { grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 18px 18px; }
  .qi-cat-name { font-size: 11.5px; letter-spacing: 0.2em; margin-bottom: 10px; padding-bottom: 7px; }
  .qi-cat-name-kr { font-size: 10px; letter-spacing: 0.15em; margin-left: 5px; }
  .qi-list li { margin-bottom: 2px; }
  .qi-list a { font-size: 13.5px; padding: 5px 0; }
  .qi-list a:hover { padding-left: 0; }
  .cocktail { scroll-margin-top: 60px; }
  .back-to-list { font-size: 10px; letter-spacing: 0.2em; padding: 5px 12px; margin-top: 14px; }

  .footer { margin-top: 60px; padding-top: 28px; }
  .footer-ornament { font-size: 42px; }
  .footer p { font-size: 14px; }
}

/* ---------- PRINT ---------- */
@media print {
  body { background: white; color: #1a1410; }
  body::before { display: none; }
  .cat-nav { display: none !important; }
  .container { padding: 20px; max-width: 100%; }
  .cocktail { background: white; border: 1px solid #c8a96a; color: #1a1410; }
  .cocktail-name, .recipe-list li { color: #1a1410; }
  .cover h1, .section-title { color: #1a1410; }
  .cocktail-notes, .cocktail-taste { color: #4a3a25; }
  .cocktail-taste { background: #fbf5e8; border-left-color: #8b7340; }
  .cocktail { page-break-inside: avoid; }
  .cover { page-break-after: always; }
  .back-to-list { display: none !important; }
}
"""

RECIPE_CSS = """
.cocktail { padding: 30px 30px 26px; }
.cocktail-head { margin-bottom: 18px; }
.cocktail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(440px, 1fr));
  gap: 30px;
}
.recipe-label {
  font-family: 'Cormorant Garamond', serif;
  font-size: 11px;
  letter-spacing: 0.4em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 12px;
}
.recipe-list { list-style: none; margin-bottom: 18px; }
.recipe-list li {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 6px 0;
  font-size: 14.5px;
  color: var(--text-primary);
  border-bottom: 1px dotted rgba(200, 169, 106, 0.1);
}
.recipe-list li:last-child { border-bottom: none; }
.recipe-list .ing { font-family: 'Noto Serif KR', serif; font-weight: 400; }
.recipe-list .amt {
  font-family: 'Cormorant Garamond', serif;
  color: var(--gold);
  font-weight: 500;
  font-size: 14px;
  letter-spacing: 0.05em;
  padding-left: 12px;
  white-space: nowrap;
}
.cocktail-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-bottom: 14px;
}
.cocktail-notes {
  padding-top: 14px;
  border-top: 1px solid var(--border-faint);
  font-style: italic;
}
.cocktail-tip {
  font-size: 12.5px;
  color: var(--text-faint);
  margin-top: 12px;
  line-height: 1.65;
}
.cocktail-tip::before { content: '✦ '; color: var(--gold); }
"""

GUEST_CSS = """
.cocktail { padding: 32px 32px 28px; }
.cocktail-head { margin-bottom: 18px; }
.cocktail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(460px, 1fr));
  gap: 32px;
}
.cocktail-notes {
  font-size: 14.5px;
  line-height: 1.8;
  color: var(--text-primary);
  margin-top: 16px;
}
.flavor-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-top: 18px;
  margin-bottom: 18px;
}
.flavor-tag {
  font-family: 'Noto Serif KR', serif;
  font-size: 12px;
  color: var(--gold);
  padding: 4px 12px;
  border: 1px solid var(--border);
  border-radius: 999px;
  background: rgba(200, 169, 106, 0.04);
  letter-spacing: 0.05em;
}
.cocktail-detail {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 8px 16px;
  padding-top: 16px;
  border-top: 1px solid var(--border-faint);
  font-size: 12.5px;
}
.cocktail-detail dt {
  font-family: 'Cormorant Garamond', serif;
  text-transform: uppercase;
  letter-spacing: 0.25em;
  color: var(--gold);
  font-size: 10.5px;
  align-self: center;
}
.cocktail-detail dd {
  font-family: 'Noto Serif KR', serif;
  color: var(--text-muted);
  align-self: center;
}

@media (max-width: 720px) {
  .flavor-tag { font-size: 11px; padding: 3px 10px; }
  .cocktail-detail { gap: 6px 12px; font-size: 12px; }
  .cocktail-detail dt { font-size: 10px; letter-spacing: 0.2em; }
}
"""

SCROLLSPY_JS = """
(function() {
  const navLinks = document.querySelectorAll('.cat-nav a');
  if (!navLinks.length) return;
  const sections = Array.from(navLinks).map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if (!sections.length) return;

  const navMap = new Map();
  navLinks.forEach(a => navMap.set(a.getAttribute('href').slice(1), a));

  let activeId = null;
  function setActive(id) {
    if (id === activeId) return;
    activeId = id;
    navLinks.forEach(a => a.classList.remove('active'));
    const link = navMap.get(id);
    if (link) {
      link.classList.add('active');
      // Auto-scroll nav to keep active link visible on mobile
      const nav = document.querySelector('.cat-nav');
      const linkLeft = link.offsetLeft;
      const linkWidth = link.offsetWidth;
      const navWidth = nav.clientWidth;
      nav.scrollTo({
        left: linkLeft - navWidth / 2 + linkWidth / 2,
        behavior: 'smooth'
      });
    }
  }

  const observer = new IntersectionObserver(entries => {
    // Find the topmost visible section
    const visible = entries
      .filter(e => e.isIntersecting)
      .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visible.length) setActive(visible[0].target.id);
  }, { rootMargin: '-15% 0px -70% 0px' });

  sections.forEach(s => observer.observe(s));
})();
"""

# ============================================================
# RENDER HELPERS
# ============================================================

def abv_class(abv):
    if abv == 0: return "zero"
    if abv >= 25: return "high"
    return ""

def abv_block(abv):
    klass = abv_class(abv)
    return (f'<div class="abv-badge {klass}"><span class="pct">{abv}</span>'
            f'<span class="label">% ABV</span></div>')

def ingredient_summary(recipe):
    ings = []
    for ing, amt in recipe:
        clean = ing.replace("(선택)", "").replace("(옵션)", "").strip()
        ings.append(clean)
    return " · ".join(ings)

def make_id(c):
    """Stable anchor ID for a cocktail (based on English name)."""
    import re
    en = c["en"].split("·")[0]  # Strip Japanese/extra parts
    s = re.sub(r"[^\w\s-]", "", en.lower())
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return f"c-{s}" if s else f"c-{c['kr']}"

def render_recipe_card(c):
    out = f'''
    <article class="cocktail" id="{make_id(c)}">
      <div class="cocktail-head">
        <div>
          <h3 class="cocktail-name">{c["kr"]}</h3>
          <div class="cocktail-name-en">{c["en"]}</div>
        </div>
        {abv_block(c["abv"])}
      </div>
      <div class="recipe-label">Recipe</div>
      <ul class="recipe-list">'''
    for ing, amt in c["recipe"]:
        out += f'<li><span class="ing">{ing}</span><span class="amt">{amt}</span></li>'
    out += '</ul>'
    out += '<div class="cocktail-meta">'
    out += f'<span class="meta-tag method">{c["method"]}</span>'
    out += f'<span class="meta-tag">{c["glass"]} Glass</span>'
    if c.get("garnish"):
        out += f'<span class="meta-tag">{c["garnish"]}</span>'
    out += '</div>'
    out += f'<div class="cocktail-notes">{c["notes"]}</div>'
    out += f'<div class="cocktail-taste">{c["taste"]}</div>'
    if c.get("tip"):
        out += f'<div class="cocktail-tip">{c["tip"]}</div>'
    out += '<a href="#quick-index" class="back-to-list">목록으로</a>'
    out += '</article>'
    return out

def render_guest_card(c):
    ings = ingredient_summary(c["recipe"])
    tags_html = "".join(f'<span class="flavor-tag">{t}</span>' for t in c.get("tags", []))
    garnish = c.get("garnish") or "—"
    return f'''
    <article class="cocktail" id="{make_id(c)}">
      <div class="cocktail-head">
        <div>
          <h3 class="cocktail-name">{c["kr"]}</h3>
          <div class="cocktail-name-en">{c["en"]}</div>
        </div>
        {abv_block(c["abv"])}
      </div>
      <p class="cocktail-notes">{c["notes"]}</p>
      <div class="cocktail-taste">{c["taste"]}</div>
      <div class="flavor-tags">{tags_html}</div>
      <dl class="cocktail-detail">
        <dt>Base</dt><dd>{ings}</dd>
        <dt>Glass</dt><dd>{c["glass"]}</dd>
        <dt>Garnish</dt><dd>{garnish}</dd>
      </dl>
      <a href="#quick-index" class="back-to-list">목록으로</a>
    </article>'''

def render_quick_index():
    """전체 칵테일 목록 — 클릭하면 해당 설명으로 점프"""
    by_cat = {}
    for c in COCKTAILS:
        by_cat.setdefault(c["cat"], []).append(c)
    blocks = []
    for cat_key, num, name_en, name_kr in SECTIONS:
        cocktails = by_cat.get(cat_key, [])
        if not cocktails:
            continue
        kr_short = name_kr.replace(" 베이스", "").strip()
        items = "".join(
            f'<li><a href="#{make_id(c)}">{c["kr"]}</a></li>' for c in cocktails
        )
        blocks.append(f'''
        <div class="qi-cat">
          <div class="qi-cat-name">{name_en}<span class="qi-cat-name-kr">{kr_short}</span></div>
          <ul class="qi-list">{items}</ul>
        </div>''')
    return f'''
    <nav class="quick-index" id="quick-index" aria-label="전체 칵테일 목록">
      <div class="quick-index-title">— Full List · 전체 목록 —</div>
      <div class="qi-grid">{"".join(blocks)}</div>
    </nav>'''

def render_nav():
    by_cat = {}
    for c in COCKTAILS:
        by_cat.setdefault(c["cat"], []).append(c)
    items = []
    for cat_key, num, name_en, name_kr in SECTIONS:
        if by_cat.get(cat_key):
            items.append(f'<a href="#{cat_key}">{name_en}</a>')
    return f'<nav class="cat-nav"><div class="cat-nav-inner">{"".join(items)}</div></nav>'

def render_sections(version):
    render = render_recipe_card if version == "recipe" else render_guest_card
    out = []
    for cat_key, num, name_en, name_kr in SECTIONS:
        cards = [render(c) for c in COCKTAILS if c["cat"] == cat_key]
        if not cards: continue
        out.append(f'''
        <section class="section" id="{cat_key}">
          <div class="section-header">
            <div class="section-number">{num}</div>
            <h2 class="section-title">{name_en}</h2>
            <div class="section-title-kr">{name_kr}</div>
          </div>
          <div class="cocktail-grid">{"".join(cards)}</div>
        </section>''')
    return "".join(out)

def render_page(version, page_url=""):
    is_recipe = version == "recipe"
    title = "나만의 칵테일 메뉴 · 레시피" if is_recipe else "나만의 칵테일 메뉴"
    edition = "Bartender Edition" if is_recipe else "Guest Menu"
    edition_label = "레시피 포함" if is_recipe else "손님용 메뉴"
    css_extra = RECIPE_CSS if is_recipe else GUEST_CSS
    og_desc = ("개인 칵테일 컬렉션 — 바텐더용 레시피 모음" if is_recipe
               else f"개인 칵테일 메뉴 — 총 {len(COCKTAILS)}종, 풍미·도수·재료 한눈에")

    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#15100c">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Cocktail Menu">
<meta name="format-detection" content="telephone=no">

<title>{title}</title>
<meta name="description" content="{og_desc}">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:locale" content="ko_KR">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{og_desc}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Italianno&family=Noto+Serif+KR:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<!-- Inline SVG favicon: golden cocktail glass -->
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2315100c'/%3E%3Cpath d='M6 8 L26 8 L18 18 L18 25 L22 25 L22 27 L10 27 L10 25 L14 25 L14 18 Z' fill='none' stroke='%23c8a96a' stroke-width='1.5' stroke-linejoin='round'/%3E%3Ccircle cx='20' cy='11' r='1' fill='%23e4c785'/%3E%3C/svg%3E">

<style>{BASE_CSS}{css_extra}</style>
</head>
<body>
{render_nav()}

<div class="container">
  <header class="cover">
    <div class="cover-ornament">✦</div>
    <div class="cover-eyebrow">Personal Cocktail Collection</div>
    <h1>나만의 <em>Cocktail</em> 메뉴</h1>
    <p class="cover-subtitle">— A Curated Selection of {len(COCKTAILS)} Recipes —</p>
    <div class="cover-meta">
      <span>{len(COCKTAILS)} Cocktails</span>
      <span>9 Categories</span>
      <span>찌니의 칵테일 비법</span>
    </div>
    <div class="cover-edition">{edition}<span class="label">{edition_label}</span></div>
  </header>

  {render_quick_index()}

  {render_sections(version)}

  <footer class="footer">
    <div class="footer-ornament">✦</div>
    <p>Drink responsibly &mdash; savor slowly.</p>
    <p class="small">— Personal Cocktail Collection · Based on 찌니의 칵테일 비법 —</p>
  </footer>
</div>

<script>{SCROLLSPY_JS}</script>
</body>
</html>'''


# ============================================================
# README for GitHub
# ============================================================

README = f"""# 🍸 나만의 칵테일 메뉴 (Personal Cocktail Menu)

찌니의 칵테일 비법 영상을 바탕으로 정리한 개인 칵테일 메뉴판입니다. 총 **{len(COCKTAILS)}종** · 9개 카테고리.

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
{{
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
}},
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
"""

# ============================================================
# WRITE FILES
# ============================================================

import os
out_dir = "/mnt/user-data/outputs"
os.makedirs(out_dir, exist_ok=True)

with open(f"{out_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(render_page("guest"))

with open(f"{out_dir}/recipes.html", "w", encoding="utf-8") as f:
    f.write(render_page("recipe"))

with open(f"{out_dir}/README.md", "w", encoding="utf-8") as f:
    f.write(README)

with open(f"{out_dir}/build_menu.py", "w", encoding="utf-8") as f:
    # Copy the build script itself
    with open(__file__, "r", encoding="utf-8") as src:
        f.write(src.read())

print(f"✓ Generated {len(COCKTAILS)} cocktails across {len(SECTIONS)} sections")
print()
print("Files written to /mnt/user-data/outputs/:")
print("  • index.html      ← 손님용 (GitHub Pages 기본 페이지)")
print("  • recipes.html    ← 바텐더용 (레시피 포함)")
print("  • README.md       ← GitHub 배포 가이드")
print("  • build_menu.py   ← 빌드 스크립트 (재생성용)")
