from pprint import pprint
from vultr.v1_server import VultrServer
from vultr.v1_regions import VultrRegions
from vultr.v1_plans import VultrPlans
from vultr.v1_os import VultrOS
from vultr.v1_startupscript import VultrStartupScript
from vultr.v1_sshkey import VultrSSHKey

api_key = "MYKEY"

# 区域列表-DCID,必选
regions = VultrRegions(api_key)
regions_list = regions.list()

# 套餐列表-VPSPLANID,必选
plans = VultrPlans(api_key)
plans_list = plans.list()
pprint(plans_list)

# 系统类型列表-OSID,必选
os_type = VultrOS(api_key)
os_type_list = os_type.list()

# 启动脚本列表
startup_script = VultrStartupScript(api_key)
startup_script_list = startup_script.list()

# ssh-key列表
ssh_key = VultrSSHKey(api_key)
ssh_key_list = ssh_key.list()

# 建立一台新加坡的主机
DCID = '40'  # 新加坡
VPSPLANID = '201'  # 202-$5,

vultr_server = VultrServer(api_key)
# vultr_server.create()
