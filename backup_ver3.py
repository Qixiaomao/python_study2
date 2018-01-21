import os
import time

# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Windows 下：
source = [r'C:\Users\14864\Documents\计算机\workspace\pyStudy\day17\file_demo']

# 2. 备份文件必须存储在一个
# 主备份目录中
# 例如在 Windows 下：
# target_dir = 'E:\\Backup'
target_dir = r'C:\Users\14864\Documents\计算机\workspace\pyStudy\day17\file_demo\Backup'

# 3. 备份文件将打包压缩成 zip 文件。
# 4. 将当前日期作为主备份目录下的
# 子目录名称

today = target_dir + os.sep + time.strftime('%y%m%d')
now = time.strftime('%H%M%S')

# 添加一条来自用户的注释以创建
# zip 文件的文件名

comment = input('Enter a comment -->')
#检查是否有评论键入

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else :
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -qr {0}{1}'.format(target,' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Runnig:')
if os.system(zip_command) == 0:
    print('Successfully backup to',target)
else:
    print('Bacup FAILED')
