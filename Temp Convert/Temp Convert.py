# 温度转换
InputTemp = input("请输入温度:")
if InputTemp[-1] in ["C", "c"]:
    F = eval(InputTemp[0:-1]) * 1.8 + 32
    print("转换后的温度是 {:.1f}F".format(F))
elif InputTemp[-1] in ["F", "f"]:
    C = (eval(InputTemp[0:-1]) - 32) / 1.8
    print("转换后的温度是 {:.1f}C".format(C))
else:
    print("格式错误")
