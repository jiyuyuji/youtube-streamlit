import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()#空の要素を追加し、atest_iterationに代入する
bar = st.progress(0)

for i in range(100):#for文で100の範囲で数値が増え、同時にlatest_iterationにforの値を追加し、バーとして表示
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)#0.1秒止まって動作する

'Done!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander = st.expander('問い合わせ')#エキスパンダーを表示する　→　開くとその先の文章が見れるやつ
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く2')

#text = st.text_input('あなたの趣味を教えてください。')#｣を使うと、サイドバーに入力欄を表示できる
#'あなたの趣味:', text

#condition = st.slider('あなたの今の調子は？', 0, 100, 50)#スライダーインタラクティブなウィジェット)の表示　('質問内容',スタート値,最低値,最大値,初期値)
#'コンディション:',condition