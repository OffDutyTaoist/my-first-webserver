import os
import shutil

def copy_dir_recursive(src: str, dst: str):
    """
    Recursively copy all files/dirs from src to dst.
    Assumes dst exists. Logs each operation.
    """
    for name in os.listdir(src):
        s_path = os.path.join(src, name)
        d_path = os.path.join(dst, name)
        if os.path.isdir(s_path):
            os.makedirs(d_path, exist_ok=True)
            print(f"[dir ] {d_path}")
            copy_dir_recursive(s_path, d_path)
        elif os.path.isfile(s_path):
            shutil.copy(s_path, d_path)
            print(f"[file] {s_path} -> {d_path}")
        else:
            # Skip symlinks or special files
            print(f"[skip] {s_path} (not a regular file/dir)")

def copy_static_to_public(static_dir: str = "static", public_dir: str = "public"):
    """
    Deletes the destination directory completely, then copies static_dir into it.
    Logs what it does.
    """
    # 1) clean public/
    if os.path.exists(public_dir):
        print(f"[wipe] removing {public_dir}")
        shutil.rmtree(public_dir)

    # 2) recreate public/
    os.makedirs(public_dir, exist_ok=True)
    print(f"[make] {public_dir}")

    # 3) sanity check for static/
    if not os.path.exists(static_dir):
        print(f"[warn] source '{static_dir}' does not exist — nothing to copy")
        return

    # 4) copy recursively
    copy_dir_recursive(static_dir, public_dir)
