"""投票結果の保存・読み込み(CSV担当)"""
from pathlib import Path
from datetime import datetime

import pandas as pd

VOTES_CSV = Path("votes.csv")

STAGE_OPTIONS = ["W", "N1", "N2", "N3", "R"]
REASON_OPTIONS = [
    "覚醒と睡眠の細切れ混在",
    "EMGの判断が困難",
    "前後エポックとの整合性の問題",
    "アーチファクトの混入",
    "N1/Rの鑑別困難",
    "その他",
]


def save_vote(source, filename, epoch_number, stage, reason, note):
    """投票結果を1行追記する(ファイルが無ければヘッダー付きで新規作成)"""
    row = pd.DataFrame([{
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "source": source,
        "filename": filename,
        "epoch_number": epoch_number,
        "stage": stage,
        "reason": reason,
        "note": note,
    }])
    row.to_csv(VOTES_CSV, mode="a", header=not VOTES_CSV.exists(), index=False)


def load_votes() -> pd.DataFrame:
    """これまでの投票結果を読み込む(無ければ空のDataFrame)"""
    if VOTES_CSV.exists():
        return pd.read_csv(VOTES_CSV)
    return pd.DataFrame()
