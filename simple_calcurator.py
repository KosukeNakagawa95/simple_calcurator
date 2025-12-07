import  math

#関数get_vaild_numberを定義する
def get_vaild_number(message): #get_vaild_numberを実行するときに(message)を表示するようにしている
    while True: #while関数でtry exceptのループをする
        try: #値がTrue（このばあいは半角数字が入力された）の場合の挙動
            user_input = int(input(message)) #messageでinputされた文字列をintで整数に変換
            return user_input #user_inputをreturnし、whileループから抜ける

        except:ValueError #ValueError（半角数字以外が入力されてエラー）の挙動
        print("半角数字を入力してください。") #エラーメッセージをprintしtryに戻る        
    

time_per_unit = get_vaild_number("何個作りますか？") #time_per_unitを定義
quantity = get_vaild_number("1個当たり何秒必要ですか？") #quantityを定義

total_minutes = math.ceil((time_per_unit * quantity) / 60) #合計秒数を60で割って、計算結果の少数を切り上げ

print(f"1個当たり{time_per_unit}秒かかる工程を{quantity}個では、{total_minutes}分が必要になります。")