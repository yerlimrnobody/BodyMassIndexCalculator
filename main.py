import tkinter

window = tkinter.Tk()
window.title("BMI CALCULATOR")
window.config(background="#581845")
window.config(pady=10)
window.minsize(400,250)
window.maxsize(400,250)

label_widget_top = tkinter.Label()
label_widget_top.config(text="Body Mass Index (BMI) Calculator")
label_widget_top.config(font="Bold")
label_widget_top.config(padx=30, pady=10)
label_widget_top.pack()

#label_widget_top.update()
#print(label_widget_top.winfo_height())
#print(label_widget_top.winfo_width())


label_widget_weight = tkinter.Label()
label_widget_weight.config(text="Please Enter Your Weight as (kg) : ")
label_widget_weight.config(pady=2)
label_widget_weight.place(x=35, y=50)

entry_widget_weight = tkinter.Entry()
entry_widget_weight.place(x=275, y=50, width=91)


label_widget_height = tkinter.Label()
label_widget_height.config(text="Please Enter Your Height as (cm) : ")
label_widget_height.config(padx=0)
label_widget_height.place(x=35, y=80)


entry_widget_height = tkinter.Entry()
entry_widget_height.place(x=275, y=80, width=91)

def user_inputs():
    try:
        kg = int(entry_widget_weight.get())
        boy = int(entry_widget_height.get())
        boy_float = boy/100
        bmi = kg/(boy_float*boy_float)

        if bmi < 18.5:

            label_widget_result = tkinter.Label()
            label_widget_result.config(text="YOU ARE UNDERWEIGHT",background="#DAF7A6")
            label_widget_result.place(x=35, y=180)

        elif 18.5 <= bmi <= 24.9:

            label_widget_result = tkinter.Label()
            label_widget_result.config(text="YOU ARE AT NORMAL WEIGHT", background="#F7DC6F")
            label_widget_result.place(x=35, y=180)

        elif 25 <= bmi <= 29.9:

            label_widget_result = tkinter.Label()
            label_widget_result.config(text="YOU ARE OVERWEIGHT", background="#FFC300")
            label_widget_result.place(x=35, y=180)

        elif 30 <= bmi <= 34.9:

            label_widget_result = tkinter.Label()
            label_widget_result.config(text="YOU ARE OBESITY CLASS 1", background="#FF5733")
            label_widget_result.place(x=35, y=180)

        elif 35 <= bmi <= 39.9:

            label_widget_result = tkinter.Label()
            label_widget_result.config(text="YOU ARE OBESITY CLASS 2", background="#FF5733")
            label_widget_result.place(x=35, y=180)

        elif bmi >= 40:

            label_widget_result = tkinter.Label()
            label_widget_result.config(text="YOU ARE OBESITY CLASS 3", background="#FF5733")
            label_widget_result.place(x=35, y=180)

        label_widget_bottom = tkinter.Label()
        label_widget_bottom.config(text=f"Your BMI : {bmi}")
        label_widget_bottom.place(x=35, y=150)

    except:

        label_attention = tkinter.Label()
        label_attention.config(text="PLEASE ENTER AN INTEGER")
        label_attention.place(x=35, y=150)




calculate_button = tkinter.Button()
calculate_button.config(text="CALCULATE", command=user_inputs)
calculate_button.config(width=34, pady=5)
calculate_button.place(x=35, y=110)




window.mainloop()


