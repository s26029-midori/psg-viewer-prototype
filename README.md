# PSG波形ビューワー & 判定投票プロトタイプ

PSG(睡眠ポリグラフ検査)のEDFファイルを読み込み、エポック単位で波形を表示しながら
暫定判定(W/N1/N2/N3/R)を投票できる、ローカル動作の学習用プロトタイプです。

将来の「判定困難例を多施設で共有するプラットフォーム」の最小プロトタイプとして、
Streamlitの基本機能(ページ分割・ウィジェット)を練習する目的も兼ねています。

## フォルダ構成

```
psg-viewer-prototype/
├── app.py                    # メインページ:波形ビューワー+投票フォーム
├── pages/
│   └── 1_投票履歴.py           # 投票履歴ページ(Streamlitのマルチページ機能)
├── utils/
│   ├── data_loader.py         # MNEでEDF読み込み・エポック抽出
│   └── voting.py               # 投票結果のCSV保存・読み込み
├── data/
│   ├── README.md               # データの出典・ライセンス情報
│   └── sample/                 # GitHubに含まれる唯一の実データ(数エポック分のみ)
├── requirements.txt
└── .gitignore
```

## セットアップ

```powershell
# 仮想環境を作る場合
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## データの配置

このリポジトリには、`data/sample/`(PSG-IPAオリジナルデータから数エポックだけ
切り出したサンプル)以外のEDFファイルは含まれていません。出典・ライセンスの
詳細は`data/README.md`を参照してください。

オリジナルデータや、人工的に迷いを注入したエポックを使って動作確認したい場合は、
`app.py`冒頭の各パスを、実際のデータ保存場所に合わせて書き換えてください。

```python
ORIGINAL_DATA_DIR = Path("data/psg_ipa_original")   # ローカルのみ(.gitignoreで除外)
PERTURBED_DATA_DIR = Path("data/perturbed")          # ローカルのみ(.gitignoreで除外)
SAMPLE_DATA_DIR = Path("data/sample")                # GitHub公開用(同梱済み)
```

サイドバーの「データの種類」で、オリジナル・人工迷いエポック・サンプル(公開用)を
切り替えられます。クローンしただけの状態でまず動かしたい場合は「サンプル(公開用)」
を選んでください。

## 起動

```powershell
streamlit run app.py
```

ブラウザが自動で開きます。左サイドバーの「投票履歴」から、これまで記録した投票を確認できます。

## GitHubに公開する手順(練習用)

1. GitHub上で新しいリポジトリを作成する(Public、READMEなどは追加しない)
2. このフォルダで以下を実行:

```powershell
cd psg-viewer-prototype
git init
git add .
git commit -m "PSG波形ビューワー プロトタイプ 初回コミット"
git branch -M main
git remote add origin https://github.com/【ユーザー名】/【リポジトリ名】.git
git push -u origin main
```

3. GitHub上のリポジトリページを開き、ファイルが反映されていれば公開完了です。

`data/psg_ipa_original/`・`data/perturbed/`フォルダと`votes.csv`は`.gitignore`で
除外されているため、実データや投票結果はアップロードされません。
`data/sample/`と`data/README.md`のみ例外的に公開されます。
