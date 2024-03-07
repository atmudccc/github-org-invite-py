# README.md

## 项目介绍

这是一个使用Python和Flask框架构建的Web应用程序，主要功能是通过GitHub OAuth进行用户身份验证，并邀请他们加入指定的GitHub组织。项目使用了`python-dotenv`库来管理环境变量，`requests`库来发送HTTP请求，以及`gunicorn`作为WSGI HTTP服务器。

## 环境变量

- `CLIENT_ID`: GitHub OAuth应用的客户端ID。
- `CLIENT_SECRET`: GitHub OAuth应用的客户端密钥。
- `REDIRECT_URI`: GitHub OAuth应用的重定向URI。
- `ORGANIZATION_NAME`: 需要邀请用户加入的GitHub组织名称。
- `GITHUB_P_ACCESSTOKEN`: 用于邀请用户加入组织的GitHub个人访问令牌。

## 如何启动项目

1. 克隆项目到本地。
2. 在项目根目录下创建一个`.env`文件，并填写上述环境变量。
3. 安装项目依赖：`pip install -r requirements.txt`。
4. 启动项目：`python main.py`。

## 如何构建Docker镜像

在项目根目录下运行以下命令：

```shell
docker build -t github-org-invite-py .
```

## Docker启动示例命令

```shell
docker run \
--restart=always \
--name github-org-invite-py \
-e CLIENT_ID=your_client_id \
-e CLIENT_SECRET=your_client_secret \
-e REDIRECT_URI=your_redirect_uri \
-e ORGANIZATION_NAME=your_organization_name \
-e GITHUB_P_ACCESSTOKEN=your_github_p_accesstoken \
-p 18989:18989 \
-d github-org-invite-py
```

以上命令将会启动一个Docker容器，应用将在容器的18989端口上运行，并映射到宿主机的18989端口。

## 其他说明

- 项目使用了`Flask`框架，所有的路由定义都在`app/routes.py`文件中。
- `app/utils.py`文件包含了所有的辅助函数，如获取访问令牌、获取用户登录ID以及邀请用户加入组织等。
- `app/config.py`文件用于加载环境变量并存储在`Config`类中，以便在项目中使用。
- `Dockerfile`文件定义了如何在Docker容器中运行应用。
- `run.sh`是一个shell脚本，用于在Docker容器中启动应用。