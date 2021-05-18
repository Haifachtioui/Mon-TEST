from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired
class SignUpForm(FlaskForm):
    nom = StringField ('nom',
              validators=[DataRequired()
              ])
    prénom= StringField ('prénom',
              validators=[DataRequired(),
              ])
    email= StringField('email',
            validators=[DataRequired()
            ])

    submit = SubmitField ('suivant')

