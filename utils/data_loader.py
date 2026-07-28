"""EDFファイルの読み込みとエポック抽出(MNEを使うデータ処理担当)"""
from pathlib import Path

import mne


def list_edf_files(directory: Path) -> list[str]:
    """指定フォルダ内のEDFファイル名一覧を返す(フォルダが無ければ空リスト)"""
    if not directory.exists():
        return []
    return sorted(p.name for p in directory.glob("*.edf"))


def load_raw(filepath: str):
    """
    EDFを読み込む。

    呼吸/SpO2チャンネルのヘッダに由来するlowpass値(1.6Hz)が
    全チャンネルに誤って適用され、EEGが間引き表示される不具合があるため、
    ここで明示的に上書きしておく(前回の作業で判明した対策)。
    """
    raw = mne.io.read_raw_edf(filepath, preload=True, verbose=False)
    with raw.info._unlock():
        raw.info["lowpass"] = 40.0
    return raw


def get_epoch(raw, epoch_number: int, epoch_sec: int = 30):
    """指定エポック番号(1始まり)の区間データ(µV)と、0始まりの時刻(秒)を返す"""
    sfreq = raw.info["sfreq"]
    start = int((epoch_number - 1) * epoch_sec * sfreq)
    stop = int(epoch_number * epoch_sec * sfreq)
    data, times = raw.get_data(start=start, stop=stop, return_times=True)
    return data * 1e6, times - times[0]  # V→µV、時刻は0始まりに変換
