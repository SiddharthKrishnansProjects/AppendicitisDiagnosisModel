import appendicitisLogReg as alr
import tkinter as tk

app = tk.Tk()
app.title("Appendicitis Diagnosis Prediction")
app.geometry("300x600")

def onbuttonclick():
    predict_output.delete(1.0, tk.END)
    try:
        diagnosis = alr.prediction(ageentry.get(), bmientry.get(), heightentry.get(), weightentry.get(), btentry.get(), wbccentry.get(),
                       rbccentry.get(), hgentry.get(), tcentry.get())
        if diagnosis == 1:
            predict_output.insert(tk.INSERT, "Diagnosis: Appendicitis\n")
        else:
            predict_output.insert(tk.INSERT, "Diagnosis: No Appendicitis\n")

        predict_output.insert(tk.INSERT, "Model Accuracy: ~" + str(round(alr.score()*100, 2)) + "%")
    except:
        predict_output.insert(tk.INSERT, "Error. Please type valid \nnumerical values into \nevery field.")

agelabel = tk.Label(app, text="Patient Age:")
agelabel.place(x=20, y=0)
ageentry = tk.Entry(app)
ageentry.place(x=20, y=20)

bmilabel = tk.Label(app, text="Patient BMI:")
bmilabel.place(x=20, y=50)
bmientry = tk.Entry(app)
bmientry.place(x=20, y=70)

heightlabel = tk.Label(app, text="Patient Height (cms):")
heightlabel.place(x=20, y=100)
heightentry = tk.Entry(app)
heightentry.place(x=20, y=120)

weightlabel = tk.Label(app, text="Patient Weight (kgs):")
weightlabel.place(x=20, y=150)
weightentry = tk.Entry(app)
weightentry.place(x=20, y=170)

btlabel = tk.Label(app, text="Patient Body Temperature (Celsius):")
btlabel.place(x=20, y=200)
btentry = tk.Entry(app)
btentry.place(x=20, y=220)

wbcclabel = tk.Label(app, text="Patient WBC Count (*10^9/L):")
wbcclabel.place(x=20, y=250)
wbccentry = tk.Entry(app)
wbccentry.place(x=20, y=270)

rbcclabel = tk.Label(app, text="Patient RBC Count (*10^9/L):")
rbcclabel.place(x=20, y=300)
rbccentry = tk.Entry(app)
rbccentry.place(x=20, y=320)

hglabel = tk.Label(app, text="Patient Hemoglobin Count (*10^9/L):")
hglabel.place(x=20, y=350)
hgentry = tk.Entry(app)
hgentry.place(x=20, y=370)
#
tclabel = tk.Label(app, text="Patient Thrombocyte Count (*10^9/L):")
tclabel.place(x=20, y=400)
tcentry = tk.Entry(app)
tcentry.place(x=20, y=420)

predict_output = tk.Text(app, height=5, width=30)
predict_output.place(x=20, y=500)

predict = tk.Button(app, text="Predict", command=onbuttonclick)
predict.place(x=20, y=450)

app.mainloop()