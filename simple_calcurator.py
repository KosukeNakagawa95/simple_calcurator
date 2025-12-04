import  math

while True:
    try:
        time_per_unit = int(input("1個当たり何秒必要ですか？"))
        break

    except:ValueError #ValueErrorの場合のみexcept処理を行う
    print("半角数字を入力してください。")
    continue #tryに戻る

while True:
    try:
        quantity = int(input("何個作りますか？"))
        break

    except:ValueError
    print("半角数字を入力してください。")
    continue

#所要時間を秒で求めたのち、分に計算する
total_seconds = time_per_unit * quantity
total_minutes = math.ceil(total_seconds / 60)

#結果を表示する
print(f"1個当たり{time_per_unit}秒かかる工程を{quantity}個では、{total_minutes}分が必要になります。")