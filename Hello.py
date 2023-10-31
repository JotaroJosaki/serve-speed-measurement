import streamlit as st
from datetime import datetime

# Streamlitアプリの構造
st.title("テニスサーブ速度計測アプリ")

# エンドラインとネットの間の距離入力
distance = st.number_input("エンドラインからネットまでの距離（メートル）", min_value=0.0, value=11.887, step=0.01)

# サーブのタイミング計測
if 'start' not in st.session_state:
    st.session_state['start'] = None
if 'end' not in st.session_state:
    st.session_state['end'] = None

start_time = st.button("サーブ開始")
end_time = st.button("ネット通過")

if start_time:
    st.session_state['start'] = datetime.now()

if end_time:
    st.session_state['end'] = datetime.now()

# タイミングと速度の計算と表示
if st.session_state['start'] and st.session_state['end']:
    elapsed_time = (st.session_state['end'] - st.session_state['start']).total_seconds()
    st.write(f"経過時間: {elapsed_time:.3f} 秒")
    
    if elapsed_time > 0:
        speed = (distance / elapsed_time) * 3.6  # km/h
        st.write(f"サーブの速度: {speed:.2f} km/h")
