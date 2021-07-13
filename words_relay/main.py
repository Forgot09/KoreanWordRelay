#-*- coding: utf-8 -*- 
import sys

#####################################################
f=open('list.txt', 'rt', encoding='utf-8')
wordsList = f.readlines()
f.close()
f=open('wflist.txt', 'rt', encoding='utf-8')
canFirstWords = f.readlines()
f.close()
#####################################################
judgement = True
botWords = ''
bunli = ''
turnTimes = 1
beforeList = []
dum = {'녀':'여', '녁':'역', '녂':'엮', '녃': '엯', '년': '연', '녅': '엱', '녆':'엲', '녇':'엳', '녈':'열', '녉':'엵', '녊':'엶', '녋':'엷', '녌':'엸', '녍':'엹', '녎':'엺', '녏':'엻', '념':'염', '녑':'엽', '녒':'엾', '녓':'엿', '녔':'였', '녕':'영', '녖':'옂', '녗':'옃', '녘':'옄', '녙':'옅', '녚':'옆', '녛':'옇','뇨':'요', '뇩':'욕', '뇪':'욖', '뇫': '욗', '뇫': '욗', '뇭': '욙', '뇮':'욙', '뇯':'욛', '뇰':'욜', '뇱':'욝', '뇲':'욞', '뇳':'욟', '뇴':'욠', '뇵':'욡', '뇶':'욢', '뇷':'욣', '뇸':'욤', '뇹':'욥', '뇺':'욦', '뇻':'욧', '뇼':'욨', '뇽':'용', '뇾':'욪', '뇿':'욫', '눀':'욬', '눁':'욭', '눂':'욮', '눃':'욯', '뉴':'유', '뉵':'육', '뉶':'윢', '뉷': '윣', '뉸': '윤', '뉹': '뉹', '뉺':'윦', '뉻':'윧', '뉼':'율', '뉽':'윩', '뉾':'윪', '뉿':'윫', '늀':'윬', '늁':'윭', '늂':'윮', '늃':'윯', '늄':'윰', '늅':'윱', '늆':'윲', '늇':'윳', '늈':'윴', '늉':'융', '늊':'윶', '늋':'윷', '늌':'윸', '늍':'윹', '늎':'윺', '늏':'윻', '니':'이', '닉':'익', '닊':'읶', '닋': '읷', '닌': '인', '닍': '읹', '닎':'읺', '닏':'읻', '닐':'일', '닑':'읽', '닒':'읾', '닓':'읿', '닔':'잀', '닕':'잁', '닖':'잂', '닗':'잃', '님':'임', '닙':'입', '닚':'잆', '닛':'잇', '닜':'있', '닝':'잉', '닞':'잊', '닟':'잋', '닠':'잌', '닡':'잍', '닢':'잎', '닣':'잏','랴':'야', '략':'약', '랶':'앾', '랷':'앿', '랸':'얀', '랹':'얁', '랺':'얂', '랻':'얃', '랼':'얄', '랽':'얅', '랾':'얆', '랿':'얇', '럀':'얈', '럁':'얉', '럂':'얊', '럃':'얋', '럄':'얌', '럅':'얍', '럆':'얎', '럇':'얏', '럈':'얐', '량':'양', '럊':'얒', '럋':'럋', '럌':'얔', '럍':'얕', '럎':'얖', '럏':'얗', '려':'여', '력':'역', '렦':'엮', '렧':'엯', '련':'연', '렩':'엱', '렪':'렪', '렫':'엳', '렭':'엵', '렮':'엶', '렯':'엷', '렰':'엸', '렱':'엹', '엺':'엺', '렳':'엻', '렴':'염', '렵':'엽', '렶':'엾', '렷':'엿', '렸':'였', '령':'영', '렺':'옂', '렻':'옃', '렼':'옄', '렽':'옅', '렾':'옆', '렿':'옇', '례':'예', '롁':'옉', '롂':'옊', '롃':'옋', '롄':'옌', '롅':'옍', '롆':'옎', '롇':'옏', '롈':'옐', '롉':'옑', '롊':'옒', '렓':'옓', '롌':'옔', '롍':'옕', '롎':'옖', '롏':'옗', '롐':'옘', '롑':'옙', '롒':'옚', '롓':'옛', '렜':'옜', '롕':'옝', '롖':'옞', '롗':'옟', '롘':'옠', '롙':'옡', '롑':'옙', '롛':'옣', '료':'요', '룍':'욕', '룎':'욖', '룏':'욗', '룐':'욘', '룑':'욙', '룒':'욚', '룓':'욛', '룔':'욜', '룕':'욝', '룖':'욞', '룗':'욟', '룘':'욠', '룙':'욡', '룚':'욢', '룛':'욣', '룜':'욤', '룝':'욥', '룞':'욦', '룟':'욧', '룠':'욨', '룡':'용', '룢':'욪', '룣':'욫', '룤':'욬', '룥':'욭', '룦':'욮', '룧':'욯', '류':'유', '륙':'육', '륚':'윢', '륛':'윣', '륜':'윤', '륝':'윥', '륞':'윦', '륟':'윧', '륡':'윩', '륢':'윪', '륣':'윫', '륤':'윬', '륥':'윭', '륦':'윮', '륧':'윯', '륨':'윰', '륩':'윱', '륪':'윲', '륫':'윳', '륬':'윴', '륭':'융', '륮':'윶', '륯':'윷', '륰':'윸', '륱':'윹', '륲':'윺', '륳':'륳','리':'이', '릭':'익', '릮':'읶', '릯':'읷', '린':'인', '릱':'읹', '릲':'읺', '릳':'읻', '릴':'일', '릵':'읽', '릶':'읾', '릷':'읿', '릸':'잀', '릹':'잁', '릺':'잂', '릻':'잃', '림':'임', '립':'입', '릾':'잆', '릿':'잇', '맀':'있', '링':'잉', '맂':'잊', '맃':'잋', '맄':'잌', '맅':'잍', '맆':'잎', '맇':'잏'}
dum_etc = {'렬':'열', '률':'율'}
#####################################################
def jamo(a):
    a = list(a)
    chosung = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    jungsung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    jongsung = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', '#']

    bunli = []

    for i in a:
        charactorf = ord(i)-0xAC00
        chosung_i = (charactorf) // 21 //28
        if chosung_i == -75:
            bunli.append('space')
            continue
        else:
            bunli.append(chosung[chosung_i])


        jungsung_i = ((charactorf) - (chosung_i * 21 * 28)) //28
        bunli.append(jungsung[jungsung_i])


        jongsung_i = ((charactorf) - (chosung_i * 21 * 28) - ((jungsung_i) * 28) - 1)
        bunli.append(jongsung[jongsung_i])
    
    return bunli

def check(data):
    global judgement, beforeList, turnTimes, botWords
    if data == 'end' or data == '항복' or data == 'gg':
        print('[!] 봇의 승리 입니다. 아쉽군요, 다시 도전해보세요')
        print('[!] 프로그램이 종료 됩니다')
        exit()
    elif 1 == len(data):
        judgement = True
        turnTimes -= 1
        print('[!] 단어가 한 글자 입니다, 다시 입력해주세요')
    elif data in beforeList:
        judgement = True
        turnTimes-=1
        print('[!] 이 단어를 이미 사용했습니다, 다시 입력해주세요')
    elif data.upper() != data.lower():
        judgement = True
        turnTimes -= 1
        print('[!] 영어입니다, 다시 입력해주세요')

def bot_words(data):
    global wordsList, botWords, dum, bunli, dum_etc, canFirstWords
    turn = 0
    checkVar = True
    if data[-1]+'\n' in canFirstWords or dum[data[-1]]+'\n' in canFirstWords or bunli[1] == 'ㄴ' and dum_etc[data[-1]+'\n' in canFirstWords]:
        if not data[-1] in dum or not bunli[2] == 'ㄴ' and data[-1] in dum_etc:
            while checkVar:
                botWords = wordsList[turn]
                if data[-1] == botWords[0]:
                    botWords = botWords.rstrip('\n')
                    print(botWords)
                    wordsList.remove(botWords+'\n')
                    checkVar = False
                turn += 1
        elif data[-1] in dum:
            while checkVar:
                botWords = wordsList[turn]
                if dum[data[-1]] == botWords[0]:
                    botWords = botWords.rstrip('\n')
                    print(botWords)
                    wordsList.remove(botWords+'\n')
                    checkVar = False
                turn += 1
        elif bunli[2] == 'ㄴ' and data[-1] in dum_etc:
            while checkVar:
                if dum_etc[data[-1]] == botWords[0]:
                    botWords = botWords.rstrip('\n')
                    print(botWords)
                    wordsList.remove(botWords+'\n')
                    checkVar = False

    else:
        print('[!] 당신의 승리입니다. 축하드립니다 이 화면을 캡쳐하여 개발자 이메일로 전해주세요')
        print('[!] 개발자 이메일 >> forcoding4@gmail.com')
        sys.exit('[!] 끝말잇기가 종료 되었습니다')
#####################################################

###################   main   ########################
print('[!] 끝말잇기가 시작되었습니다')
print('='*50)
while judgement:
    if turnTimes == 1:
        inputData = input('[!] 단어를 입력해주세요 >> ')
        inputData = inputData.rstrip('\n')
        if inputData == '' or inputData == ' ':
            judgement = True
            turnTimes -= 1
            print('[!] 단어를 입력하지 않았습니다, 다시 입력해주세요')
        bunli = jamo(inputData)
        judgement = False
        check(inputData)
        if judgement:
            continue
        else:
            judgement = True
            
    else:
        inputData = input('[!] 단어를 입력해주세요 >> ')
        inputData = inputData.rstrip('\n')
        bunli = jamo(inputData)
        if inputData[0] != botWords[-1] and not inputData[0] in dum and not inputData[0] in dum_etc and not bunli[1] == 'ㄴ':
            print('[!] ', inputData[0], '(은)는', botWords[-1], '(으)로 시작하지 않습니다, 다시 입력해주세요')
            judgement = True
            if turnTimes > 2:
                turnTimes -= 1
            continue
        check(inputData)

        if not judgement:
            judgement = True
    try:
        bot_words(inputData) 
        turnTimes += 1
    except IndexError:
        print('[!] 당신의 승리입니다. 축하드립니다 이 화면을 캡쳐하여 개발자 이메일로 전해주세요')
        print('[!] 개발자 이메일 >> forcoding4@gmail.com')
        sys.exit('[!] 끝말잇기가 종료 되었습니다')
