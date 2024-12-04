def convert_to_kanji(numbers):
    kanji_digits = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
    kanji_numbers = []

    for num in numbers:
        if num < 10:
            # 10未満の数字はそのまま漢字に変換
            kanji_numbers.append(kanji_digits[num])
        else:
            # 10以上の数字
            digits = str(num)
            if len(digits) == 2:
                kanji = kanji_digits[int(digits[0])] + "十"
                if digits[1] != "0":  # 一の位が0でない場合
                    kanji += kanji_digits[int(digits[1])]
                kanji_numbers.append(kanji)
    return kanji_numbers

# 1から40までの数字を生成
numbers = list(range(1, 41))

# 変換したい数字を指定
numbers_to_convert = [3, 6, 9, 12, 13, 15, 18, 21, 23, 24, 27, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

# 変換したい数字を漢数字に変換
converted_numbers = convert_to_kanji(numbers_to_convert)

# 結果を表示
print("1から40までの数字:")
print(numbers)
print("\n指定された数字を漢数字に変換した結果:")
for num, converted in zip(numbers_to_convert, converted_numbers):
    print(f"{num} -> {converted}")

