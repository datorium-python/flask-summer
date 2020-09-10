from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    text = TextAreaField('text', validators=[DataRequired(), Length(min=20, max=500)])
