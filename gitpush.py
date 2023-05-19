import datetime
import subprocess
# 获取当前日期
current_date = datetime.date.today()

# 将日期转换为字符串格式
commit_message = f"Commit on {current_date}"

# 配置全局Git用户名和电子邮件
subprocess.run(["git", "config", "--global", "user.name", "zhangw"], shell=True)
subprocess.run(["git", "config", "--global", "user.email", "2713819970@qq.com"], shell=True)

# 执行 git add .
subprocess.run(["git", "add", "."], shell=True)

# 执行 git commit -m "Commit on {current_date}"
subprocess.run(["git", "commit", "-m", commit_message], shell=True)

# 执行 git push
subprocess.run(["git", "push"], shell=True)
