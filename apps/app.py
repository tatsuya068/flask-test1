from flask import Flask


# create_app関数を作成する
def create_app():
    # Flaskインスタンス生成
    app = Flask(__name__)

    # crudパッケージからviewsをimportする
    from crud.view import crud as crud_views

    # register_blueprintを使いveiwsのcrudアプリへ登録する
    app.register_blueprint(crud_views, url_prefix="/crud")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
