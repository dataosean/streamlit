# """
# # My first app
# Here's our first attempt at using data to create a table:
# """
# # (1) 표 그리기
# import streamlit as st
# import pandas as pd
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })
# df # st.write(df) 와 동일하게 작동함.

# # (2) 표와 제목 그리기, 동적 테이블, 정적 테이블
# import streamlit as st
# import pandas as pd

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# st.write("Here's our first attempt at using data to create a table:")
# st.dataframe(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# st.write("Here's our first attempt at using data to create a table:")
# st.table(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# # (3) Line chart
# import streamlit as st
# import numpy as np
# import pandas as pd

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# # (4) 지도 (샘플 데이터 생성 후 강남 지도 그리기)
# import streamlit as st
# import numpy as np
# import pandas as pd

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.514575, 127.0495556],
#     columns=['lat', 'lon'])

# st.map(map_data)

# # (5) 위젯: 사용자의 입력을 받을 경우 st.slider(), st.button(), st.selectbox() 같은 위젯 추가 가능.
# import streamlit as st
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# # (6) 체크박스: 그냥 쓸 수도 있지만 if문을 이용하면 checkbox에 check가 되어 있을 때는 조건문 실행, check가 해제되어 있을 때는 조건문 실행하지 않음.
# import streamlit as st
# import numpy as np
# import pandas as pd

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])
#     chart_data

# # (7) 선택박스
# import streamlit as st
# import pandas as pd

# option = st.selectbox(
#     '여러분이 궁금한 지역을 선택해주세요.',
#      ['종로구', '마포구', '서대문구', '동대문구', '강남구'])

# 'You selected: ', f'{option}의 유명한 빵집 이름은 A입니다.'

# # (8) Layout
# import streamlit as st

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# # (9) st.columns를 사용하면 위젯을 나란히 배치할 수 있음.
# import streamlit as st

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

# # (10) DB Connection
# # 기본 스크립트가 포함된 폴더에 `.streamlit` 폴더 생성 (폴더명 앞에 점을 꼭 붙여주세요!)
# # `.streamlit` 폴더에  `secrets.toml` 파일 생성하고 아래 코드를 변경하여 저장한다.
# # [connections.my_database]
# #     type="sql"
# #     dialect="mysql"
# #     username="root"
# #     password="0000"
# #     host="localhost" # IP or URL
# #     port=3306 # Port number
# #     database="my_test" # Database name

# # pip install mysqlclient 해야한다.
# import streamlit as st

# conn = st.connection("my_database")  # sqlalchemy 설치 필요.
# df = conn.query("SELECT * FROM ecommerce.list_of_python")
# st.dataframe(df)

# (11) 앱이 커지면 여러 페이지로 나누는 것이 유용하다.
# 1. `main.py`파일이 포함된 폴더에 새 `pages`폴더 생성
# 2. 앱에 더 많은 페이지를 추가하려면 `pages`폴더에 새로운 `.py` 파일 추가

import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")