"""
1.登陆jenkins 账号信息配置;
"""
accUrl="http://192.168.1.1:8080/jenkins"
username="admin"
password="admin"

"""
2.jenkins视图列表默认dev,test,ontest,prod 环境;
"""
viewList = ["Dev", "Test", "Ontest", "Prod"]


class MysqlConfig(object):
    DIALECT = "mysql"
    DRIVER = "pymysql"
    USERNAME = "root"
    PASSWORD = "123456"
    HOST = "192.168.11.101"
    PORT = "3306"
    DATABASE = "devops-cicd-api"
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                           PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

appMgHeader=[
    {"name":"group","alias":"小组名称"},
    {"name":"appname","alias":"应用名称"},{"name":"level","alias":"应用级别"},
    {"name":"apptype","alias":"应用类型"},{"name":"business","alias":"业务线"},
    {"name":"giturl","alias":"git地址"}, {"name":"owner","alias":"应用负责人"},
    {"name":"port","alias":"服务端口"},{"name":"used","alias":"用途"},
    {"name":"createtime","alias":"创建时间"},
]
#{"name":"id","alias":"唯一标识"},

instanceMgHeader=[
    {"name":"appname","alias":"应用名称"}, {"name":"instancename","alias":"实例名称"},
    {"name":"ip","alias":"实例ip地址"}, {"name":"env","alias":"环境"},
    {"name":"createtime","alias":"创建时间"},
]
#{"name":"id","alias":"唯一标识"},




###环境关系标识定义####
envListkey = ["dev","test","test2","pre","pro","devops"]
envListdisplay_name=["开发环境","测试环境","测试环境2","预发布环境","生产环境","运维环境"]

##发布版本分支关系定义#####
releaseListkey = ["Release","master","hostfix"]
releaseListDisplay_name=["release","master","hostfix"]

#支持发布语言
languageType = ["java","php","vue","python","go"]
languageTypedisplay_name=["Java","PHP","VUE","Python","Go"]

#查询软件包路径地址
searchPackPath="/xwkj/data/update"

##发布表头
cicdMgHeader=[
    {"name": "id", "alias": "唯一标识"},{"name": "env", "alias": "发布环境"},
    {"name": "appname", "alias": "应用名称"},{"name": "appversion", "alias": "发布版本"},
    {"name": "instance_ip", "alias": "发布实例"},{"name": "giturl", "alias": "GIT地址"},
    {"name": "language_type", "alias": "语言类型"},{"name": "release_reason", "alias": "发布原因"},
    {"name": "jenkins_callback", "alias": "Jenkins返回"},{"name": "releasetime", "alias": "发布时间"},
]
#ldap表头
ldapHeader=[
    #{"name": "id", "alias": "唯一标识"},
    {"name": "username", "alias": "登录用户"},
    {"name": "password", "alias": "用户密码"},{"name": "name", "alias": "用户全名"},
    {"name": "mail", "alias": "邮箱地址"},{"name": "createtime", "alias": "创建时间"},
]

