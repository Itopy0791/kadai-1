def special_number_sequence():
    for i in range(1, 40):
        if i % 3 == 0:
            # 3の倍数を漢数字にする
            print(to_kanji(i))
        elif i >= 10:
            # 10以上の数字を漢数字に変換
            print(to_kanji(i))
        else:
            # その他の数字はそのまま出力
            print(i)

def to_kanji(num):
    kanji_map = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七", 8: "八", 9: "九", 10: "十"}
    if num < 10:
        return kanji_map[num]
    elif num < 20:
        return "十" + kanji_map[num % 10] if num % 10 != 0 else "十"
    else:
        tens = kanji_map[num // 10]
        ones = kanji_map[num % 10] if num % 10 != 0 else ""
        return tens + "十" + ones
