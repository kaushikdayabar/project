from flask_wtf import Form
from wtforms import SelectField,IntegerField,SubmitField
from wtforms import validators,ValidationError

class cf(Form):
    freq=SelectField("frequency",choices=[("d","daily"),("m","monthly")])
    tech=SelectField("technique",choices=[("b","base_clp"),("p","base_yuan"),("a","sma"),("e","ses"),("e1","des"),("pslr","slr_peso"),("yslr","slr_yuan")])

    s=SubmitField("calculate")
    oos=IntegerField("oos")
    ins=IntegerField("ins")
    rmse=IntegerField("rmse")
