from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    contents = TextAreaField(label='Content', validators=[DataRequired()])
    submit = SubmitField('Send Post')
