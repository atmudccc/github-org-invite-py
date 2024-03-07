from flask import redirect, request, render_template_string, render_template
from .utils import get_access_token, get_user_login_id, invite_user_to_organization
from .config import Config

def configure_routes(app):

    @app.route("/")
    def index():
        # HTML content moved to separate templates or rendered directly
        return render_template("index.html")

    @app.route("/refuse")
    def refuse():
        # HTML content moved to separate templates or rendered directly
        return render_template("refuse.html")

    @app.route('/invite')
    def invite():
        return redirect(f'https://github.com/login/oauth/authorize?client_id={Config.CLIENT_ID}&redirect_uri={Config.REDIRECT_URI}&scope=read:user')

    @app.route('/callback')
    def callback():
        # Function implementation remains the same, using Config for configuration
        code = request.args.get('code')
        access_token = get_access_token(code)
        user_login_id = get_user_login_id(access_token)
        response = invite_user_to_organization(user_login_id, Config.GITHUB_P_ACCESSTOKEN)
        if response.status_code == 201:
            return render_template("invites_success.html")
        else: 
            response_failReason = "{} : {}".format(response.status_code, response.json().get('failed_reason') or '未知错误')
            return render_template("invites_fail.html", fail_reason=response_failReason)