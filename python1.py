# 課題１
x = 11
y = 3

print("<実行結果>")
print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "×", y, "=", x * y)
print(x, "÷", y, "=", x // y, "余り", x % y)

# 課題２
print("一つ目の値を入力してください")
num1 = int(input())
print("二つ目の値を入力してください")
num2 = int(input())

print("<実行結果>")
print("合計：", num1 + num2)
print("平均：", (num1 + num2) / 2)

# 課題３
print("身長を入力してください")
height_m = float(input())
print("体重を入力してください")
weight = float(input())

bmi = weight / height_m**2

if bmi < 18.5:
    result = "やせ"
elif bmi >= 18.5 and bmi < 25:
    result = "標準"
elif bmi >= 25 and bmi < 30:
    result = "肥満"
else:
    result = "高度肥満"

print("<実行結果>")
print(f"あなたは「{result}」です。")

# 課題４
debt = 250000
interest_rate = 0.14
amount_repaid = 30000
month = 0

print("<実行結果>")
while debt >= 0:
    month += 1
    interest_debt = debt * (interest_rate / 12 + 1)
    debt = interest_debt - amount_repaid
    if interest_debt >= amount_repaid:
        print(f"{month}ヶ月目：返済額＝{amount_repaid}円,残り{debt}円")
    else:
        print(f"{month}ヶ月目：返済額＝{interest_debt}円,返済完了。")