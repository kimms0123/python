from gtts import gTTS

text = "내일이면 공강이다 유후~ 시험공부하기 싫어 슈슈슈슉발"

a = gTTS(text, lang='ko')
a.save('result.mp3')