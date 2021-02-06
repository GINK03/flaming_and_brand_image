# 炎上とブランドイメージの定量化をbertで行う

## イントロダクション
近年のSNSでの炎上は企業にとって大きなリスクとして認識されています。炎上してしまうと、企業はその対応に追われ、多大な労力を払うことになります。また、企業のブランドイメージの既存があると一般的に認識されているようです。  
2020年は企業・国務に関連した多くの不祥事がありました。不祥事が起こるたびにその対策は行われてきましたが、炎上自体が引き起こす、ブランドイメージの低下等は定量化されていないようです。  
今回、twitterのデータと機械学習のbertと呼ばれるアルゴリズムを用いることで、炎上した企業・商品・公人がどのような影響を受けたかを定量化し、曖昧であった炎上のリスクを可視化したいと思います。  

## 類似した研究等
 - [クチコミによるネット炎上の定量化の試みとその検証](https://www.jstage.jst.go.jp/article/proceedingsissj/12/0/12_c22/_pdf/-char/ja)
 - [ネット炎上の実態と政策的対応の考察](https://www.soumu.go.jp/iicp/chousakenkyu/data/research/icp_review/11/11-4yamaguchi2015.pdf)

## どのように定量化したか
**データの取得**  
twitterのデータは[twint](https://github.com/twintproject/twint)と呼ばれるapi likeに使えるプログラムを用いて取得しました。  
全て取得すると非常に時間がかかるので、一日あたり1000件に限定して取得を行いました。  

**分析対象の選定**  
2019 ~ 2020年度の炎上のまとめサイトを見ながら、対象とするキーワードを選択しました。 

*選択したキーワード*  
 - セブンイレブン
 - くら寿司
 - 東京五輪
 - けものフレンズ
 - ドコモ口座
 - ドコモ
 - テラスハウス
 - ゆうちょ銀行
 - 自民党
 - 公明党
 - 立憲
 - 共産党
 - 国民民主
 - 山本太郎
 - 電通

**ブランドイメージを定量化する機械学習**  
twitterに出現するような表現に対して柔軟かつ精度良く、そのツイートが良い感情をもって表現されたかネガティブな感情をもって表現されたかを推論するアルゴリズムに、`bert`と呼ばれるアルゴリズムを用いました。  
`bert`の`pretrained model`にtweetを入力すると、`0.0 ~ 1.0`のスコアが得られます。`0.5以下`だと`ネガティブ`, `0.5以上`だと`ポジティブ`と認識されます。  
このスコアを利用して、あるキーワードに対する一日あたりの平均のスコアを算出することが可能になります。平均したスコアを28日(4週間)の移動平均をとり、乱雑さを軽減しました。  
`x軸`は`日付`, `y軸`は`平均スコア`が表示されることになり、炎上を経験した企業・商品・公人のイメージを追跡することが可能になります。  

実際にこのモデルにてプリキュアを分類した結果を確認すると以下のようになり、期待した動作が得られました。

<div align="center">
  <img width="300" alt="スクリーンショット 2021-02-06 12 40 17" src="https://user-images.githubusercontent.com/4949982/107108046-9af45480-6878-11eb-925b-77786212da95.png">
  <img float="left" width="300" alt="スクリーンショット 2021-02-06 12 40 34" src="https://user-images.githubusercontent.com/4949982/107108047-9def4500-6878-11eb-98c6-0f0ebcf1937a.png">
</div>

<p align="center"> 左: ポジティブな例, 右: ネガティブな例</p>


**統計を正確にするためのヒューリスティクス**  
twitterのデータを扱う際には気をつけるべきポイントが幾つかあります。ポイント等のインセンティブを狙った機械的な投稿や、偏執的に同一の話題に対して何度も発言する人などのバイアスを外す必要があります。

そこで以下のようなルールを入れました。  
 - ある人が一日に特定の話題について複数回話していても、採用するのは一つ
 - `http`等URLを記入した投稿は採用しない
 
## 結果

## 論点

## 結論
