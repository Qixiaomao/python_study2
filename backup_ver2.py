import os
import time

# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Windows 下：
# source = ['"C:\\My Documents"', 'C:\\Code']

source = [r'C:\Users\14864\Documents\计算机\workspace\pyStudy\day17\file_demo\demo']

# 2. 备份文件必须存储在一个
# 主备份目录中
# 例如在 Windows 下：
# target_dir = 'E:\\Backup'
target_dir = r'C:\Users\14864\Documents\计算机\workspace\pyStudy\day17\file_demo\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)#创建目录

# 3. 备份文件将打包压缩成 zip 文件。
# 4. 将当前日期作为主备份目录下的子目录名称

today = target_dir + os.sep + time.strftime('%Y%m%d')
#将当前时间作为zip文件的文件名

now = time.strftime('%H%M%S')

#zip文件名称格式

target = today + os.sep + now + '.zip'

#如果子目录上不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

#我们使用zip命令将文件打包成zip格式

zip_command = 'zip -qr {0}{1}'.format(target,' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
