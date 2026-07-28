"""投票履歴ページ(Streamlitのマルチページ機能の練習)"""
import streamlit as st

from utils.voting import load_votes

st.title("投票履歴")

votes = load_votes()
if votes.empty:
    st.info("まだ投票がありません。")
else:
    st.dataframe(votes, use_container_width=True)
