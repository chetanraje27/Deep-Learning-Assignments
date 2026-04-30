import os
import shutil

src = r"C:\Users\Chetanraje\Downloads\DL_Assignmnet_5"
dst = r"C:\Users\Chetanraje\Downloads\temp_upload_repo2\Assignment_No_5_LSTM"

os.makedirs(dst, exist_ok=True)
files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f))]
print('files', len(files))
for f in files:
    shutil.copy2(os.path.join(src, f), dst)
