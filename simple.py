# 환경 설정
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from collections import Counter
import folium
from streamlit_folium import st_folium

# 스트림릿 특: 버튼 누를 때마다 처음부터 시작한다.
text_file = pd.read_csv("streamlit_cluster(04.24).csv")
latlon = text_file.groupby('Store').first()[['Y', 'X']]
Review_text = text_file[['Store','Review_text','sentiment','cluster']]

# 페이지를 session_state에 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'home' # 페이지란 값이 없을테니 당연 home으로 이동. home은 home_page()이다.

# 세션은 영구저장을 도와준다.
# if 'tmp' not in st.session_state:
    # st.session_state.tmp = None

# 버튼 씹힘 문제 해결: page변수에 args가 들어가면 함수로 이동
def button_click(page):
    st.session_state.page = page

# 클러스터 저장하기: breadmap()처음에 발동
def cluster_name(name):
    st.session_state.cluster = name
    if st.session_state.cluster == 'cluster_0':
        st.session_state.num = 1
    elif st.session_state.cluster == 'cluster_1':
        st.session_state.num = 2
    elif st.session_state.cluster == 'cluster_2':
        st.session_state.num = 3
    elif st.session_state.cluster == 'cluster_3':
        st.session_state.num = 4
    elif st.session_state.cluster == 'cluster_4':
        st.session_state.num = 5
    elif st.session_state.cluster == 'cluster_5':
        st.session_state.num = 0
    print(st.session_state.num)

# 가게명 저장하기: 클러스터 누를 때 발동, 랜덤 9개 가게명 리스트를 일단 저장한다.
def store_name(name):
    st.session_state.store_name = [name.iloc[i] for i in range(9)] # 이건 맨 아래 함수에서 쓰인다.

def latlon_save(lat,lon):
    st.session_state.latlon = (lat,lon)

def new_friend_name1(name):
    st.session_state.name_list1 = name

def new_friend_name3(name):
    st.session_state.name_list3 = name

#######################################################################################################

# 메인인 홈페이지
def home_page():

    # 배경사진
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image:url("https://i.imgur.com/wtY58mv.png");
        background-attachment:fixed;
        background-size:cover
        
    }}
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Hi Bread!</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 25px; font-family: Noto Sans CJK KR, sans-serif;'>네게 맛집만 보여줄게, 좋아하는 🥖키워드를 눌러볼래?</h1>", unsafe_allow_html=True)

    # HTML을 사용하여 버튼의 스타일을 조정
    st.markdown("""
        <style>
            /* 버튼의 너비를 190px로 지정 */
            .stButton>button {
                width: 200px;
                height: 60px;
            }
        </style>
    """, unsafe_allow_html=True)

    # 버튼들을 중앙에 배치하기 위해 빈 칼럼, 버튼 칼럼, 빈 칼럼 순서로 생성합니다.
    left, mid, right = st.columns([0.1,2,0.1])

    # 버튼들을 중앙 칼럼에 배치합니다.
    with mid:
        b1, b2, b3 = st.columns(3)

        # 첫 번째 줄의 버튼들
        b1.button('내가 찾던 빵맛집👍', type="primary", on_click=button_click, args=("cluster_0",))
        b2.button('멋진 뷰와 분위기', type="primary", on_click=button_click, args=("cluster_1",))
        b3.button('기가 막히는 음료', type="primary", on_click=button_click, args=("cluster_2",))
        
        # 두 번째 줄의 버튼들
        b4, b5, b6 = st.columns(3)
        b4.button('넓고 쾌적한 매장', type="primary", on_click=button_click, args=("cluster_3",))
        b5.button('아름다운 인테리어', type="primary", on_click=button_click, args=("cluster_4",))
        b6.button('그외 빵집도 궁금해', type="primary", on_click=button_click, args=("cluster_5",))

#######################################################################################################

# 누가 궁금해? 페이지
def breadmap():

    # 배경사진
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image:url("https://i.imgur.com/wtY58mv.png");
        background-attachment:fixed;
        background-size:cover
        
    }}
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Click me!</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 25px; font-family: Noto Sans CJK KR, sans-serif;'>네게 리뷰를 모아서 보여줄게, 어떤 🥖맛집이 궁금해?</h1>", unsafe_allow_html=True)

    # HTML을 사용하여 버튼의 스타일을 조정
    st.markdown("""
        <style>
            /* 버튼의 너비를 350px로 지정 */
            .stButton>button {
                width: 200px;
                height: 60px;
            }
        </style>
    """, unsafe_allow_html=True)

    left, mid, right = st.columns([0.1,2,0.1])
    
    flag = True
    while flag:
        if st.session_state.cluster == 'cluster_0':
            random_store = text_file[text_file['cluster'] == 1]['Store'].sample(n=9) # 시리즈
            store_name(random_store) # 리스트
        elif st.session_state.cluster == 'cluster_1':
            random_store = text_file[text_file['cluster'] == 2]['Store'].sample(n=9)
            store_name(random_store)
        elif st.session_state.cluster == 'cluster_2':
            random_store = text_file[text_file['cluster'] == 3]['Store'].sample(n=9)
            store_name(random_store)
        elif st.session_state.cluster == 'cluster_3':
            random_store = text_file[text_file['cluster'] == 4]['Store'].sample(n=9)
            store_name(random_store)
        elif st.session_state.cluster == 'cluster_4':
            random_store = text_file[text_file['cluster'] == 5]['Store'].sample(n=9)
            store_name(random_store)
        elif st.session_state.cluster == 'cluster_5':
            random_store = text_file[text_file['cluster'] == 0]['Store'].sample(n=9)
            store_name(random_store)
        
        # 중복 가게 제거
        counter = Counter(random_store)
        counter_list = list(counter.values())
        if max(counter_list) == 1:
            flag=False
    
    with mid: # 버튼들을 중앙 칼럼에 배치합니다.
    # 첫 번째 줄의 버튼들
        b1, b2, b3 = st.columns(3)
        b1.button(f'{random_store.iloc[0]}',type="primary", on_click=button_click, args=("store_0",), key='store_0_button')
        b2.button(f'{random_store.iloc[1]}',type="primary", on_click=button_click, args=("store_1",), key='store_1_button')
        b3.button(f'{random_store.iloc[2]}',type="primary", on_click=button_click, args=("store_2",), key='store_2_button')
    
        # 두 번째 줄의 버튼들
        b4, b5, b6 = st.columns(3)
        b4.button(f'{random_store.iloc[3]}',type="primary", on_click=button_click, args=("store_3",), key='store_3_button')
        b5.button(f'{random_store.iloc[4]}',type="primary", on_click=button_click, args=("store_4",), key='store_4_button')
        b6.button(f'{random_store.iloc[5]}',type="primary", on_click=button_click, args=("store_5",), key='store_5_button')

        # 세 번째 줄의 버튼들
        b7, b8, b9 = st.columns(3)
        b7.button(f'{random_store.iloc[6]}',type="primary", on_click=button_click, args=("store_6",), key='store_6_button')
        b8.button(f'{random_store.iloc[7]}',type="primary", on_click=button_click, args=("store_7",), key='store_7_button')
        b9.button(f'{random_store.iloc[8]}',type="primary", on_click=button_click, args=("store_8",), key='store_8_button')

        # 처음으로 버튼
        c1, c2, c3 = st.columns(3)
        c1.button("처음으로 돌아가기", on_click=button_click, args=("home",))

#######################################################################################################

# 친구 소개하기
def friend():

    # Streamlit 페이지 설정
    # st.set_page_config(layout="wide")

    # 배경사진
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image:url("https://i.imgur.com/wtY58mv.png");
        background-attachment:fixed;
        background-size:cover
        
    }}
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Introduce myself!</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # with col1:
    #     # 위치 데이터 설정 (소공동의 위도 및 경도)
    #     cond = (latlon.index == f'{st.session_state.name}')

    #     map_data = pd.DataFrame({
    #         'lat': [latlon[cond].iloc[0].values[1]],
    #         'lon': [latlon[cond].iloc[0].values[0]]
    #     })

    #     st.map(map_data, size=80)

    with col1:
        # 가게 소개
        cond5 = (text_file['cluster']==st.session_state.num)
        information = text_file[cond5].groupby('Store').first()[['Review_score','Address','행정동명','cluster_labeling']]
        cond1 = (information.index == f'{st.session_state.name}')

        st.write("🍰Here's Bakery information")
        df_int = pd.DataFrame({
            '이름': [f'🥖 {st.session_state.name}'],
            '평점': f'⭐ {information[cond1].iloc[0].values[0]}',
            '특성': [information[cond1].iloc[0].values[3]],
            '행정동': [information[cond1].iloc[0].values[2]],
            '주소': [information[cond1].iloc[0].values[1]]
        }).T
        df_int.columns=['상세 정보']
        st.dataframe(df_int, use_container_width=True)

        # 사용자가 선택한 위치에 대한 조건
        cond = (latlon.index == f'{st.session_state.name}')

        st.write("🍩Here's Bakery Location")

        # PyDeck 사용할 때, 조건에 맞는 데이터로부터 지도 데이터 생성
        map_data = pd.DataFrame({
            'lat': [latlon[cond].iloc[0].values[0]],
            'lon': [latlon[cond].iloc[0].values[1]]
        })
        lat = latlon[cond].iloc[0].values[0]
        lon = latlon[cond].iloc[0].values[1]
        latlon_save(lat, lon)

        # PyDeck을 사용하여 지도 생성 -> 실패!
        # map = pdk.Deck(
        #     map_style='mapbox://styles/mapbox/light-v9',
        #     initial_view_state=pdk.ViewState(
        #         latitude=map_data['lat'].values[0],
        #         longitude=map_data['lon'].values[0],
        #         zoom=15,
        #         pitch=50,
        #     ),
        #     layers=[
        #         pdk.Layer(
        #             'ScatterplotLayer',
        #             data=map_data,
        #             get_position='[lon, lat]',
        #             get_color='[0, 68, 255, 160]',
        #             get_radius=20,
        #         ),
        #     ],
        #     # 지도의 너비와 높이 조절
        #     width='100%',
        #     height=500,
        # )
        
        # st.pydeck_chart(map)

        # 준성 튜터님의 폴리움을 이용한 지도 사이즈 조정 -> 힌트 얻음!
        # import folium
        # from streamlit_folium import st_folium

        # # Folium 지도 생성
        # map = folium.Map(location=[lat, lon], zoom_start=12)
        # # 마커표시
        # folium.Marker([lat, lon], popup=st.session_state.name).add_to(map)
        # # Streamlit에 지도 표시
        # st_folium(map, width=800, height=300)

        # 지도를 HTML파일로 저장한 후, 스트림릿에서 HTML컴포넌트로 직접 불러오는 방법
        import os

        # Folium 지도 생성
        m = folium.Map(location=[lat, lon], zoom_start=12)

        # 마커 생성: 여기서 다 만들고 저장시키는 구나?, 하이퍼파라미터 popup/tooltip
        marker = folium.Marker([lat, lon], popup='빵!', tooltip=st.session_state.name)
        marker.add_to(m)

        # Folium 지도를 HTML 파일로 저장
        map_file_path = 'map.html'
        m.save(map_file_path)

        # Streamlit에서 HTML 파일 불러와서 렌더링
        with open(map_file_path, 'r', encoding='utf8') as f:
            map_html = f.read()

        # Streamlit의 html 함수를 사용하여 렌더링
        st.components.v1.html(map_html, height=300, scrolling=False)

        # (선택사항) 사용 후 HTML 파일 삭제
        os.remove(map_file_path)

        # HTML을 사용하여 버튼의 스타일을 조정하여 뒤로가기 생성
        st.markdown("""
            <style>
                /* 버튼의 너비를 350px로 지정 */
                .stButton>button {
                    width: 345px;
                }
            </style>
        """, unsafe_allow_html=True)

        st.button("다른 친구 알아보기", type="primary", on_click=button_click, args=("breadmap",))

    with col2:
        # 불호 리뷰
        cond2 = (Review_text['Store'] == f'{st.session_state.name}')
        cond3 = (Review_text['sentiment'] == 1)
        cond4 = (Review_text['sentiment'] == 0)
        cond6 = (Review_text['cluster'] == st.session_state.num)

        st.write("👎Here's Bakery Negative reviews (부정리뷰)")
        st.dataframe(pd.DataFrame({
            '리뷰 더블클릭': Review_text[cond2&cond4&cond6]['Review_text']
        }).reset_index(drop=True), hide_index=True, use_container_width=True, height=212)

        # 극호 리뷰
        st.write("👍Here's Bakery Positive reviews (긍정리뷰)")
        try:
            st.dataframe(pd.DataFrame({
                '리뷰 더블클릭': Review_text[cond2&cond3&cond6]['Review_text']
            }).reset_index(drop=True), hide_index=True, use_container_width=True, height=300)
        except:
            st.write(pd.DataFrame({
                '리뷰 더블클릭': ['불호 리뷰가 없어요!'] # 안되네
            }).reset_index(drop=True))
        
        st.button("1 Km 이내 비슷한 빵집을 알려줄게", on_click=button_click, args=("new_friend1",))
        st.button("3 Km 이내 비슷한 빵집을 알려줄게", on_click=button_click, args=("new_friend3",))

        # HTML을 사용하여 버튼의 스타일을 조정
        # st.markdown("""
        #     <style>
        #         /* 버튼의 너비를 350px로 지정 */
        #         .stButton>button {
        #             width: 350px;
        #         }
        #     </style>
        # """, unsafe_allow_html=True)

        # if st.button('300m'):
        #     st.session_state.page = 'new_friend'
        # if st.button('500m'):
        #     st.session_state.page = 'new_friend'
        # if st.button('1km'):
        #     st.session_state.page = 'new_friend'
        # if st.button('2km'):
        #     st.session_state.page = 'new_friend'

#######################################################################################################

# 1km 이내의 새로운 친구보기
def new_friend1():

    # 배경사진
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image:url("https://i.imgur.com/wtY58mv.png");
        background-attachment:fixed;
        background-size:cover
        
    }}
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Introduce my friend!</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 25px; font-family: Noto Sans CJK KR, sans-serif;'>네게 1km이내 친구들을 보여줄게, 어떤 🥖맛집이 궁금해?</h1>", unsafe_allow_html=True)

    # HTML을 사용하여 버튼의 스타일을 조정
    st.markdown("""
        <style>
            /* 버튼의 너비를 350px로 지정 */
            .stButton>button {
                width: 200px;
                height: 60px;
            }
        </style>
    """, unsafe_allow_html=True)

    import math

    def haversine(lat1, lon1, lat2, lon2):
        # 위도와 경도를 라디안으로 변환
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # 위도와 경도 차이
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Haversine 공식
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))

        # 지구 반지름 (킬로미터)
        R = 6371.0

        # 결과 거리
        distance = R * c

        return distance
    
    latlon2 = text_file[text_file['cluster']==st.session_state.num].groupby('Store').first()[['Y', 'X']]
    dis1 = []
    dis3 = []
    for i in range(len(latlon2)):
        lat1, lon1 = (37.5604164, 126.9662337) # 사용자 위치 st.session_state.latlon
        lat2, lon2 = tuple(latlon2.iloc[i]) # 빵집 위치
        distance = haversine(lat1, lon1, lat2, lon2)
        if distance <= 1:
            dis1.append(latlon2.index[i])
        if distance <= 3: # elif말고 if로 중복허용
            dis3.append(latlon2.index[i])

    # 리스트의 순서를 무작위로 섞기
    import random
    random.shuffle(dis1)
    new_friend_name1(dis1)

    left, mid, right = st.columns([0.1,2,0.1])
    
    with mid: # 버튼들을 중앙 칼럼에 배치합니다.
    # 첫 번째 줄의 버튼들
        # b1, b2, b3 = st.columns(3)
        # b1.button(dis1[0],type="primary", on_click=button_click, args=("store_0",), key='store_0_button')
        # b2.button(dis1[1],type="primary", on_click=button_click, args=("store_1",), key='store_1_button')
        # b3.button(dis1[2],type="primary", on_click=button_click, args=("store_2",), key='store_2_button')
    
        # # 두 번째 줄의 버튼들
        # b4, b5, b6 = st.columns(3)
        # b4.button(dis1[3],type="primary", on_click=button_click, args=("store_3",), key='store_3_button')
        # b5.button(dis1[4],type="primary", on_click=button_click, args=("store_4",), key='store_4_button')
        # b6.button(dis1[5],type="primary", on_click=button_click, args=("store_5",), key='store_5_button')

        # # 세 번째 줄의 버튼들
        # b7, b8, b9 = st.columns(3)
        # b7.button(dis1[6],type="primary", on_click=button_click, args=("store_6",), key='store_6_button')
        # b8.button(dis1[7],type="primary", on_click=button_click, args=("store_7",), key='store_7_button')
        # b9.button(dis1[8],type="primary", on_click=button_click, args=("store_8",), key='store_8_button')

        # dis1 리스트의 길이에 따라 동적으로 버튼을 생성합니다.
        for i in range(0, 9, 3):  # 3개씩 끊어서 반복
            # 현재 줄에 대한 컬럼을 생성합니다.
            cols = st.columns(3)
            # 현재 줄에 버튼을 최대 3개까지 생성합니다.
            for j in range(3): # 0,1,2
                if i + j < len(dis1):  # dis1 리스트의 범위 내에 있을 때만 버튼 생성
                    cols[j].button(dis1[i+j], type="primary", on_click=button_click, args=(f"new1store_{i+j}",), key=f'new1store_{i+j}_button')

        # 처음으로 버튼
        # c1, c2, c3 = st.columns(3)
        # c1.button("처음으로 돌아가기", on_click=button_click, args=("home",))

# 3km 이내의 새로운 친구보기
def new_friend3():

    # 배경사진
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image:url("https://i.imgur.com/wtY58mv.png");
        background-attachment:fixed;
        background-size:cover
        
    }}
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Introduce my friend!</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 25px; font-family: Noto Sans CJK KR, sans-serif;'>네게 3km이내 친구들을 보여줄게, 어떤 🥖맛집이 궁금해?</h1>", unsafe_allow_html=True)

    # HTML을 사용하여 버튼의 스타일을 조정
    st.markdown("""
        <style>
            /* 버튼의 너비를 350px로 지정 */
            .stButton>button {
                width: 200px;
                height: 60px;
            }
        </style>
    """, unsafe_allow_html=True)

    import math

    def haversine(lat1, lon1, lat2, lon2):
        # 위도와 경도를 라디안으로 변환
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # 위도와 경도 차이
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Haversine 공식
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))

        # 지구 반지름 (킬로미터)
        R = 6371.0

        # 결과 거리
        distance = R * c

        return distance
    
    latlon2 = text_file[text_file['cluster']==st.session_state.num].groupby('Store').first()[['Y', 'X']]
    dis1 = []
    dis3 = []
    for i in range(len(latlon2)):
        lat1, lon1 = (37.5604164, 126.9662337) # 사용자 위치 st.session_state.latlon
        lat2, lon2 = tuple(latlon2.iloc[i]) # 빵집 위치
        distance = haversine(lat1, lon1, lat2, lon2)
        if distance <= 1:
            dis1.append(latlon2.index[i])
        if distance <= 3: # elif말고 if로 중복허용
            dis3.append(latlon2.index[i])

    # 리스트의 순서를 무작위로 섞기
    import random
    random.shuffle(dis3)
    new_friend_name3(dis3)

    left, mid, right = st.columns([0.1,2,0.1])
    
    with mid: # 버튼들을 중앙 칼럼에 배치합니다.
        # dis3 리스트의 길이에 따라 동적으로 버튼을 생성합니다.
        for i in range(0, 9, 3):  # 3개씩 끊어서 반복
            # 현재 줄에 대한 컬럼을 생성합니다.
            cols = st.columns(3)
            # 현재 줄에 버튼을 최대 3개까지 생성합니다.
            for j in range(3): # 0,1,2
                if i + j < len(dis3):  # dis3 리스트의 범위 내에 있을 때만 버튼 생성
                    cols[j].button(dis3[i+j], type="primary", on_click=button_click, args=(f"new3store_{i+j}",), key=f'new3store_{i+j}_button')

#######################################################################################################

# 페이지 렌더링
if st.session_state.page == "home":
    print(st.session_state.page)
    home_page()
elif st.session_state.page == "breadmap":
    print(st.session_state.page)
    st.session_state.page = st.session_state.cluster
    breadmap()
elif st.session_state.page == "cluster_0":
    print(st.session_state.page)
    cluster_name(st.session_state.page)
    breadmap()
elif st.session_state.page == "cluster_1":
    print(st.session_state.page)
    cluster_name(st.session_state.page)
    breadmap()
elif st.session_state.page == "cluster_2":
    print(st.session_state.page)
    cluster_name(st.session_state.page)
    breadmap()
elif st.session_state.page == "cluster_3":
    print(st.session_state.page)
    cluster_name(st.session_state.page)
    breadmap()
elif st.session_state.page == "cluster_4":
    print(st.session_state.page)
    cluster_name(st.session_state.page)
    breadmap()
elif st.session_state.page == "cluster_5":
    print(st.session_state.page)
    cluster_name(st.session_state.page)
    breadmap()
elif st.session_state.page == "store_0":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[0]
    friend()
elif st.session_state.page == "store_1":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[1]
    friend()
elif st.session_state.page == "store_2":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[2]
    friend()
elif st.session_state.page == "store_3":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[3]
    friend()
elif st.session_state.page == "store_4":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[4]
    friend()
elif st.session_state.page == "store_5":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[5]
    friend()
elif st.session_state.page == "store_6":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[6]
    friend()
elif st.session_state.page == "store_7":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[7]
    friend()
elif st.session_state.page == "store_8":
    print(st.session_state.page)
    st.session_state.name = st.session_state.store_name[8]
    friend()
elif st.session_state.page == "new_friend1":
    print(st.session_state.page)
    new_friend1()
elif st.session_state.page == "new_friend3":
    print(st.session_state.page)
    new_friend3()

for e in range(9):
    if st.session_state.page == f"new1store_{e}":
        print(st.session_state.page)
        st.session_state.name = st.session_state.name_list1[e]
        friend()
for e in range(9):
    if st.session_state.page == f"new3store_{e}":
        print(st.session_state.page)
        st.session_state.name = st.session_state.name_list3[e]
        friend()