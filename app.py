"""
PSG波形ビューワー(メインページ)

起動方法: streamlit run app.py

pages/ フォルダに追加ページを置くと、左サイドバーに自動でメニューが増える
(Streamlitのマルチページ機能)。このアプリでは pages/1_投票履歴.py がそれにあたる。
"""
from pathlib import Path

import plotly.graph_objects as go
import plotly.subplots as sp
import streamlit as st

from utils.data_loader import get_epoch, list_edf_files, load_raw
from utils.voting import REASON_OPTIONS, STAGE_OPTIONS, save_vote

# ここだけ書き換えれば動く3箇所(実際の保存場所に合わせて変更)
ORIGINAL_DATA_DIR = Path("data/psg_ipa_original")
PERTURBED_DATA_DIR = Path("data/perturbed")
SAMPLE_DATA_DIR = Path("data/sample")

st.set_page_config(page_title="PSG波形ビューワー", layout="wide")
st.title("PSG波形ビューワー")

# --- データ選択 ---
source = st.sidebar.radio("データの種類", ["オリジナル", "人工迷いエポック", "サンプル(公開用)"])
if source == "オリジナル":
    data_dir = ORIGINAL_DATA_DIR
elif source == "人工迷いエポック":
    data_dir = PERTURBED_DATA_DIR
else:
    data_dir = SAMPLE_DATA_DIR

edf_files = list_edf_files(data_dir)
if not edf_files:
    st.warning(f"`{data_dir}` にEDFファイルが見つかりません。パス設定を確認してください。")
    st.stop()

selected_file = st.sidebar.selectbox("EDFファイル", edf_files)
raw = load_raw(str(data_dir / selected_file))

n_epochs = max(int(raw.times[-1] // 30), 1)
epoch_number = st.sidebar.number_input("エポック番号", 1, n_epochs, 1)

# --- チャンネル選択(ユーザーが直接選ぶシンプルな方式) ---
channels = st.multiselect("表示チャンネル", raw.ch_names, default=raw.ch_names[:5])
if not channels:
    st.info("表示するチャンネルを選んでください。")
    st.stop()

# --- 波形表示(チャンネルごとに行を分けたシンプルなsubplot) ---
data, times = get_epoch(raw, epoch_number)
fig = sp.make_subplots(rows=len(channels), cols=1, shared_xaxes=True, vertical_spacing=0.02)
for i, ch in enumerate(channels, start=1):
    idx = raw.ch_names.index(ch)
    fig.add_trace(go.Scatter(x=times, y=data[idx], mode="lines", name=ch), row=i, col=1)
    fig.update_yaxes(title_text=ch, row=i, col=1)
fig.update_xaxes(title_text="時間 (秒)", row=len(channels), col=1)
fig.update_layout(height=150 * len(channels), showlegend=False, margin=dict(t=20))

st.subheader(f"{selected_file} — エポック #{epoch_number}")
st.plotly_chart(fig, use_container_width=True)

# --- 投票フォーム ---
st.subheader("判定投票")
stage = st.radio("暫定判定", STAGE_OPTIONS, horizontal=True)
reason = st.selectbox("迷った理由", REASON_OPTIONS)
note = st.text_area("一言メモ(任意)")

if st.button("投票を記録する"):
    save_vote(source, selected_file, epoch_number, stage, reason, note)
    st.success("記録しました。左メニューの「投票履歴」ページで確認できます。")
