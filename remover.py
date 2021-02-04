import os, glob
import re


udalit_naher = []

#Список расширений файлов для удаления
formats_list = ['*.cer', '*.crl', '*.crt', '*.xml', '*.docx', '*.rtf', '*.txt', '*.rar', '*.png', '*.mp4', '*.jpg', '*.jpeg', '*.zip', '*.xlsx', '*.doc', '*.html', '*.pdf']

#Каталог, в котором будем искать фалы для удалени
DIR = r"C:\Users\{}\Downloads".format(os.environ.get("USERNAME"))


#Найти фалы для удаления по их расширению
def find_unnecessary_files(formats):
  files_for_removal = []

  for format in formats:
    for file in glob.glob(format):
      files_for_removal.append(file)

  return files_for_removal


#Найти дубликаты фалов для удаления по шаблону
def find_duplicate_files():
  file_list = os.listdir(DIR)
  files_for_removal = []

  for file in file_list:
    regex_duplicate = re.compile(r'\s[(]\d+[)]\.')
    if regex_duplicate.findall(file):
      files_for_removal.append(file)
      # print(file)
  # print(files_for_removal)
  return files_for_removal


def delete_unnecessary_files(file_list):
  for file in file_list:
    os.remove(DIR + r'\\' + file)



os.chdir(DIR)
udalit_naher = find_duplicate_files() + find_unnecessary_files(formats_list)
delete_unnecessary_files(udalit_naher)
