    #�����ֵ佫����ͨѶ¼�ı��ϲ�Ϊһ���ı�
    def main():
            ftele2=open('TeleAddressBook.txt','rb')
            ftele1=open('EmailAddressBook.txt','rb')
     
            ftele1.readline()#������һ��
            ftele2.readline()
            lines1 = ftele1.readlines()
            lines2 = ftele2.readlines()
     
            dic1 = {}   #�ֵ䷽ʽ����
            dic2 = {}
     
     
            for line in lines1:#��ȡ��һ�������е������͵绰��Ϣ
                    elements = line.split()
                    #���ı���������bytesת��Ϊstr����
                    dic1[elements[0]] = str(elements[1].decode('gbk'))
                     
            for line in lines2:#��ȡ�ڶ��������е������͵绰��Ϣ
                    elements = line.split()
                    dic2[elements[0]] = str(elements[1].decode('gbk'))
     
            ###��ʼ����###
            lines = []
            lines.append('����\t    �绰   \t  ����\n')
     
            for key in dic1:
                s= ''
                if key in dic2.keys():
                        s = '\t'.join([str(key.decode('gbk')), dic1[key], dic2[key]])
                        s += '\n'
                else:
                        s = '\t'.join([str(key.decode('gbk')), dic1[key], str('   -----   ')])
                        s += '\n'
                lines.append(s)
                 
            for key in dic2:
                s= ''
                if key not in dic1.keys():
                        s = '\t'.join([str(key.decode('gbk')), str('   -----   '), dic2[key]])
                        s += '\n'       
                lines.append(s)
     
            ftele3 = open('AddressBook.txt', 'w')
            ftele3.writelines(lines)
     
            ftele3.close()
            ftele1.close()
            ftele2.close()
            print("The addressBooks are merged!")
     
    if __name__ == "__main__":
            main()