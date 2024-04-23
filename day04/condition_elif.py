# elif
# num = int(input("점수 입력>>"))
#
# if num >= 90:
#    print("A등급")
# elif num >= 80:
#    print("B등급")
# elif num >= 70:
#    print("C등급")
# else:
#    print("과락입니다.(っ °Д °;)っ")

#국, 영, 수 점수 3개를 입력 받고,
#평균이 90점 이상 A 80 B 70 C 60 D 나머지 F 프로그램
kor = int(input("국어 점수>>"))
eng = int(input("영어 점수>>"))
math = int(input("수학 점수>>"))
ave = (kor+eng+math)/3

if ave >= 90:
    print("A학점")
elif ave >= 80:
    print("B학점")
elif ave >= 70:
    print("C학점")
elif ave >= 60:
    print("D학점")
else:
    print("F학점")

#nested condition
#if문은 2번까지만 중첩해서 쓰는 것을 지향
score = int(input("점수 입력>>"))

if score > 60:
    if score == 100:
        print("만점입니다.")
    else:
        print("합격입니다")
else:
    if score == 0:
        print("이건 좀...")
    else:
        print("불합격입니다.")