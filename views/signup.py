import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from server import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash

layout = html.Div(
    children=[
        html.Div(
            className="container",
            children=[
                dcc.Location(id='url_signup', refresh=True),
                html.Div('''Please log in to continue Krishna:''', id='h1'),
                html.Div(
                    # method='Post',
                    children=[
                        dcc.Input(
                            placeholder='Enter your username',
                            type='text',
                            id='name-box'
                        ),
                        dcc.Input(
                            placeholder='Enter your email id',
                            type='text',
                            id='email-box'
                        ),
                        dcc.Input(
                            placeholder='Enter your password',
                            type='password',
                            id='password-box'
                        ),
                        html.Button(
                            children='signup',
                            n_clicks=0,
                            type='submit',
                            id='signup-button'
                        ),
                        html.Div(children='', id='output-state')
                    ]
                ),
            ]
        )
    ]
)


@app.callback(Output('url_signup', 'pathname'),
              [Input('signup-button', 'n_clicks')],
              [State('name-box', 'value'),
               State('email-box', 'value'),
               State('password-box', 'value')
               ])
def sucess(n_clicks, input1, input2):
    user = User.query.filter_by(username=input1).first()
    if user:
        if check_password_hash(user.password, input2):
            login_user(user)
            return '/success'
        else:
            pass
    else:
        pass


@app.callback(Output('output-state', 'children'),
              [Input('login-button', 'n_clicks')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        user = User.query.filter_by(username=input1).first()
        if user:
            if check_password_hash(user.password, input2):
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''
