import os
import shutil

def organize_files(directory):
    # 디렉토리 내의 모든 파일 리스트 가져오기
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for file in files:
        # 파일 이름에서 폴더 이름 추출
        folder_name = file.split('_')[0]
        
        # 폴더가 없으면 생성
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # 파일을 해당 폴더로 이동
        current_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(folder_path, file)
        shutil.move(current_file_path, new_file_path)

if __name__ == "__main__":
    # 파일들이 있는 디렉토리 경로 지정
    directory_path = r"C:\Users\rlarb\Desktop\MAB"
    
    # 파일 정리 함수 호출
    organize_files(directory_path)
