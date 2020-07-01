#課題１
x = 11
y = 3

print("<実行結果>")
print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "×", y, "=", x * y)
print(x, "÷", y, "=", x // y, "余り", x % y)

#課題２
print("一つ目の値を入力してください")
num1 = int(input())
print("二つ目の値を入力してください")
num2 = int(input())

print("<実行結果>")
print("合計：", num1 + num2)
print("平均：", (num1 + num2) / 2)

#課題３
print("身長を入力してください")
height = float(input())
print("体重を入力してください")
weight = float(input())

bmi = weight / height**2

if bmi < 18.5:
    result = "やせ"
elif bmi >= 18.5 or bmi < 25:
    result = "標準"
elif bmi >= 25 or bmi < 30:
    result = "肥満"
else:
    result = "高度肥満"

print("<実行結果>")
print("あなたは「" , result, "」です。" )

#課題３
debt = 250000
y_interest_rate = 14.0
m_interest_rate = y_interest_rate / 12
amount_repaid = 30000

remaining_debt = debt * m_interest_rate - amount_repaid

print("<実行結果>")
print("ヶ月目：", "返済額＝", ",", remaining_debt)