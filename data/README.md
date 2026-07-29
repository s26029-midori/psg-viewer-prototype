# データについて

現時点でこのリポジトリに含まれる実データは **`data/sample/` のみ** です。
`data/psg_ipa_original/` と `data/perturbed/` は空フォルダで、実行時にローカルで
用意する想定になっています(`.gitignore`で除外、GitHubには含まれません)。

| フォルダ | GitHubに含まれるか | 内容 |
|---|---|---|
| `data/sample/` | 含まれる | PSG-IPAオリジナルデータから数エポックだけ切り出したサンプル |
| `data/psg_ipa_original/` | 含まれない(ローカルのみ) | オリジナルデータ全体を置く想定の場所 |
| `data/perturbed/` | 含まれない(ローカルのみ) | 人工的に迷いを注入したエポックを置く想定の場所(**データソースは未定**) |

## `data/sample/` の出典

`data/sample/` に含まれるサンプルは、以下のデータセットの一部をそのまま
(改変なしで)切り出したものです。

**PSG-IPA: A PolySomnoGraphic Inter-scorer Performance Assessment database**
(version 1.0.0), PhysioNet.

- 著者: Alvarez-Estevez, D.
- DOI: https://doi.org/10.13026/esx0-nw71
- ライセンス: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://physionet.org/content/psg-ipa/view-license/1.0.0/)
- 入手先: https://physionet.org/content/psg-ipa/1.0.0/

引用する場合は以下を使用してください。

```
Alvarez-Estevez, D. (2026). PSG-IPA: A PolySomnoGraphic Inter-scorer
Performance Assessment database (version 1.0.0). PhysioNet.
https://doi.org/10.13026/esx0-nw71
```

原著論文の引用:

```
Alvarez-Estevez, D., & Rijsman, R. M. (2022). Computer-assisted analysis
of polysomnographic recordings improves inter-scorer associated agreement
and scoring times. PLOS ONE, 17(9), e0275530.
```

サンプルは**エポックを切り出しただけ**で、波形自体への加工(アルファ波注入などの
改変)は行っていません。

## `data/psg_ipa_original/` と `data/perturbed/` について(未定事項)

この2つのフォルダは、動作確認用にローカルでオリジナルデータや人工迷いエポックを
置くための場所として`app.py`側に用意していますが、**実際にどのデータソースを
使うかはまだ確定していません**(引き続きPSG-IPAを使うか、別のデータセットに
するかを検討中)。

データソースが決まり次第、このREADMEにも出典情報を追記します。
`data/perturbed/`のデータについては、CC BY 4.0など改変を伴う場合に
求められる「改変を行った旨の明記」を、その時点で追加する必要があります。

## ライセンス遵守について

PSG-IPAはOpen Access(資格審査不要)でCC BY 4.0ライセンスのもと公開されており、
出典を明記すれば再配布が許可されています。本リポジトリでは、データ容量や
GitHubの実用上の理由から、フルの記録ファイルではなく`data/sample/`に
一部を切り出したサンプルのみを置いています。フルデータが必要な場合は、
上記入手先から直接ダウンロードしてください。
